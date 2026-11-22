import re
import tempfile
import unittest
from pathlib import Path

import receipts

GOOD = """---
title: A result
question: Does it hold elsewhere?
system: Some system
year: 2026
changed: harness
verified: reported
transfer: untested
---

**Claim:** X, per [the paper](https://arxiv.org/abs/2601.00001v2).

**Change:** Y.

**Controls:** unknown.

**Result:** Z.

**Verified:** The authors.

**Open:** Everything else.

**Try it:** Run it.
"""


def problems(text):
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "r.md"
        path.write_text(text, encoding="utf-8")
        return receipts.problems(path)


class Lint(unittest.TestCase):
    def test_a_complete_receipt_passes(self):
        self.assertEqual(problems(GOOD), [])

    def test_every_receipt_in_the_repository_passes(self):
        for path in sorted(receipts.RECEIPTS.glob("*.md")):
            if path.name != "TEMPLATE.md":
                self.assertEqual(receipts.problems(path), [], path.name)

    def test_the_template_has_the_required_shape(self):
        fields, body = receipts.parse(receipts.RECEIPTS / "TEMPLATE.md")
        self.assertEqual(tuple(fields), receipts.FIELDS)
        self.assertEqual(re.findall(r"^\*\*([^*:]+):\*\*", body, re.M), list(receipts.SECTIONS))

    def test_missing_field_unknown_value_and_bad_question(self):
        self.assertTrue(any("missing field transfer" in p for p in problems(GOOD.replace("transfer: untested\n", ""))))
        self.assertTrue(any("changed must be one of" in p for p in problems(GOOD.replace("changed: harness", "changed: vibes"))))
        self.assertTrue(any("question" in p for p in problems(GOOD.replace("elsewhere?", "elsewhere."))))

    def test_sections_must_all_be_present_in_order(self):
        self.assertTrue(any("sections must be" in p for p in problems(GOOD.replace("**Open:** Everything else.\n\n", ""))))

    def test_sources_must_be_pinned(self):
        unversioned = GOOD.replace("2601.00001v2", "2601.00001")
        self.assertTrue(any("without a version" in p for p in problems(unversioned)))
        floating = GOOD.replace("**Change:** Y.", "**Change:** [file](https://github.com/o/r/blob/main/a.py).")
        self.assertTrue(any("not pinned" in p for p in problems(floating)))
        pinned = GOOD.replace("**Change:** Y.", f"**Change:** [file](https://github.com/o/r/blob/{'a' * 40}/a.py).")
        self.assertEqual(problems(pinned), [])


class Ledger(unittest.TestCase):
    def test_readme_tables_are_current(self):
        readme = (receipts.ROOT / "README.md").read_text(encoding="utf-8")
        self.assertEqual(receipts.build_readme(readme, receipts.load()), readme)

    def test_every_receipt_is_in_the_ledger_and_the_grid_adds_up(self):
        rows = receipts.load()
        table = receipts.ledger(rows)
        for r in rows:
            self.assertIn(f"]({r['path']})", table)
        counts = [int(n) for n in re.findall(r"\| (\d+) ", receipts.grid(rows) + " ")]
        self.assertEqual(sum(counts), len(rows))

    def test_readme_links_to_files_that_exist(self):
        readme = (receipts.ROOT / "README.md").read_text(encoding="utf-8")
        for target in re.findall(r"\]\((?!https?:|#)([^)#]+)", readme):
            self.assertTrue((receipts.ROOT / target).exists(), target)

    def test_readme_contents_match_its_headings(self):
        readme = (receipts.ROOT / "README.md").read_text(encoding="utf-8")
        slugs = {re.sub(r"[^\w\- ]", "", h.lower()).replace(" ", "-") for h in re.findall(r"^#{2,3} (.+)$", readme, re.M)}
        for anchor in re.findall(r"\]\(#([^)]+)\)", readme):
            self.assertIn(anchor, slugs)


class Links(unittest.TestCase):
    def test_status_classes(self):
        self.assertEqual([receipts.classify(s) for s in (200, 301, 404, 410, 403, 429, 503, None)],
                         ["ok", "ok", "dead", "dead", "unverifiable", "unverifiable", "unverifiable", "unverifiable"])

    def test_pinned_and_repository_links_are_recognised(self):
        m = receipts.GH_FILE.match(f"https://github.com/o/r/blob/{'b' * 40}/docs/x.md#L3")
        self.assertEqual((m.group(1), m.group(3)), ("o/r", "docs/x.md"))
        self.assertTrue(receipts.GH_REPO.match("https://github.com/o/r"))
        self.assertFalse(receipts.GH_REPO.match("https://github.com/o/r/issues/1"))


if __name__ == "__main__":
    unittest.main()
