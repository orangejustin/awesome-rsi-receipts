# Contributing

A receipt earns its place by changing a decision: after reading it, a maintainer should do something differently, or stop believing something. Results that went the other way, and results that settle nothing, are as welcome as gains.

## Add or correct a receipt

1. Copy [the template](receipts/TEMPLATE.md) to `receipts/your-name.md` and fill in the fields and the seven sections. Keep `title`, `question` and `system` single-quoted in the YAML header (for example, `title: 'The agent''s result: a rerun'`). Leave the year and choice fields unquoted.
2. Cite the original source. arXiv links carry a version (`v2`); links into a repository are pinned to a commit, so the evidence cannot move under the reader.
3. Keep development, final and transfer results apart. Do not infer per-task outcomes from ranks or averages, and do not call a transcription of published numbers a replication.
4. Say what you did yourself. Reading a diff is not rerunning an experiment.
5. Write `unknown` where the source is silent. A missing control is information.
6. Run:

   ```sh
   python3 receipts.py lint          # fields, sections, pinned sources
   python3 receipts.py ledger        # rebuild the tables in README.md
   python3 -m unittest discover
   ```

The generator updates the English tables only. When changing a receipt or a source, update [简体中文](README.zh-CN.md) and [繁體中文](README.zh-TW.md) as well.

## Add a source

Add one line to the fitting section of the README: what it is, then where its evidence stops. If you cannot say where it stops, it is not ready to list. Popularity is not a reason to include something.

## Ground rules

Only include material you may publish. Never submit API keys, private traces or copyrighted datasets. Label synthetic examples as synthetic. Disclose any connection you have to work you add.
