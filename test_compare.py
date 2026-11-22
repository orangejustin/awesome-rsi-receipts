import json
from pathlib import Path
import subprocess
import sys
import unittest

from compare import compare, sign_test

FIXTURE = Path(__file__).resolve().parent / "examples/library-search.json"


class TestCompare(unittest.TestCase):
    def test_equal_totals_can_hide_changes(self):
        rows = json.loads(FIXTURE.read_text(encoding="utf-8"))
        self.assertEqual(
            compare(rows),
            {
                "tasks": 4, "baseline_passes": 2, "candidate_passes": 2,
                "net": 0, "flips": 2, "sign_test_p": 1.0,
                "gained": ["punctuation-in-title"], "regressed": ["distinct-editions"],
                "both_pass": ["exact-title"], "both_fail": ["missing-in-catalog"],
            },
        )
        self.assertEqual(compare(rows), compare(list(reversed(rows))))

    def test_sign_test_matches_known_values(self):
        self.assertEqual(sign_test(0, 0), 1.0)
        self.assertEqual(sign_test(1, 1), 1.0)
        self.assertAlmostEqual(sign_test(5, 0), 0.0625)       # 2 * (1/2)**5
        self.assertAlmostEqual(sign_test(0, 5), 0.0625)       # direction does not matter
        self.assertAlmostEqual(sign_test(8, 2), 0.109375)     # 2 * (1 + 10 + 45) / 1024
        self.assertLess(sign_test(15, 3), 0.01)

    def test_a_three_point_gain_on_fifty_tasks_is_not_evidence(self):
        rows = [{"id": f"t{i}", "baseline": i < 30, "candidate": i < 30} for i in range(50)]
        for i in (30, 31, 32, 33, 34):
            rows[i]["candidate"] = True        # five gains
        for i in (0, 1):
            rows[i]["candidate"] = False       # two regressions
        out = compare(rows)
        self.assertEqual((out["baseline_passes"], out["candidate_passes"], out["net"], out["flips"]), (30, 33, 3, 7))
        self.assertGreater(out["sign_test_p"], 0.4)

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
