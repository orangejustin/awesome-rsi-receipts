import re
import tempfile
import unittest
from pathlib import Path

import receipts

GOOD = """---
title: 'A result'
question: 'Does it hold elsewhere?'
system: 'Some system'
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

    def test_quoted_text_preserves_yaml_punctuation_in_ledger(self):
        text = (GOOD.replace("'A result'", "'The agent''s result: #1'")
                .replace("'Does it hold elsewhere?'", "'Transfer: does it hold elsewhere?'")
                .replace("'Some system'", "'[Some system]'"))
        self.assertEqual(problems(text), [])
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "r.md"
            path.write_text(text, encoding="utf-8")
            fields, _ = receipts.parse(path)
        self.assertEqual(fields["system"], "[Some system]")
        table = receipts.ledger([{**fields, "path": "receipts/r.md"}])
        self.assertIn("[The agent's result: #1](receipts/r.md)", table)
        self.assertIn("Transfer: does it hold elsewhere?", table)

    def test_unquoted_and_malformed_yaml_text_is_rejected(self):
        for value in ("The AI Scientist: what an outside evaluation found",
                      "A result # misleading comment", "'The agent's result'"):
            with self.subTest(value=value):
                self.assertTrue(any("title must be single-quoted" in p
                                    for p in problems(GOOD.replace("'A result'", value))))

    def test_duplicate_fields_are_rejected(self):
        self.assertIn("duplicate field title",
                      problems(GOOD.replace("title: 'A result'", "title: 'First'\ntitle: 'Second'")))

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

    def test_language_navigation_and_localized_tables(self):
        names = ("README.md", "README.zh-CN.md", "README.zh-TW.md")
        docs = {name: (receipts.ROOT / name).read_text(encoding="utf-8") for name in names}
        english = docs["README.md"]

        def block(text, key):
            return text.split(f"<!-- {key} -->", 1)[1].split(f"<!-- /{key} -->", 1)[0]

        def cells(text):
            return [line.split("|")[2:-1] for line in block(text, "grid").splitlines()
                    if line.startswith("| **")]

        def entries(text):
            return re.findall(r"\]\((receipts/[^)]+)\) · (\d{4})", block(text, "ledger"))

        for name, readme in docs.items():
            with self.subTest(name=name):
                self.assertCountEqual(re.findall(r'<a href="(README[^"]*\.md)">', readme),
                                      [other for other in names if other != name])
                self.assertEqual(entries(readme), entries(english))
                self.assertEqual(cells(readme), cells(english))
                if name != "README.md":
                    targets = set(re.findall(r'<a name="([^"]+)"></a>', readme))
                    self.assertTrue(set(re.findall(r"\]\(#([^)]+)\)", readme)) <= targets)
                    # Localized annotations should point to the same primary sources.
                    pattern = r"\]\((https?://[^)]+)\)"
                    self.assertCountEqual(re.findall(pattern, readme), re.findall(pattern, english))

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
