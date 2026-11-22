import json
from pathlib import Path
import subprocess
import sys
import unittest

from compare import compare

FIXTURE = Path(__file__).resolve().parent / "examples/library-search.json"


class TestCompare(unittest.TestCase):
    def test_equal_totals_can_hide_changes(self):
        rows = json.loads(FIXTURE.read_text(encoding="utf-8"))
        self.assertEqual(
            compare(rows),
            {
                "tasks": 4, "baseline_passes": 2, "candidate_passes": 2,
                "gained": ["punctuation-in-title"], "regressed": ["distinct-editions"],
                "both_pass": ["exact-title"], "both_fail": ["missing-in-catalog"],
            },
        )
        self.assertEqual(compare(rows), compare(list(reversed(rows))))

    def test_requires_unique_tasks(self):
        row = {"id": "same", "baseline": True, "candidate": False}
        with self.assertRaisesRegex(ValueError, "unique"):
            compare([row, row])

    def test_rejects_non_binary_value_and_missing_pair(self):
        for row in (
            {"id": "x", "baseline": 1, "candidate": False},
            {"id": "x", "baseline": True},
        ):
            with self.subTest(row=row), self.assertRaises(ValueError):
                compare([row])

    def test_rejects_empty(self):
        with self.assertRaisesRegex(ValueError, "non-empty"):
            compare([])

    def test_cli(self):
        result = subprocess.run(
            [sys.executable, str(FIXTURE.parents[1] / "compare.py"), str(FIXTURE)],
            check=True, capture_output=True, text=True,
        )
        self.assertEqual(json.loads(result.stdout)["tasks"], 4)


if __name__ == "__main__":
    unittest.main()
