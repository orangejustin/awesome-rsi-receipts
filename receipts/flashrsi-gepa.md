---
title: 'FlashRSI: one harness, three outcomes'
question: 'Would this tuned harness still help on a task family it was not tuned on?'
system: 'FlashRSI (GEPA search over a Claude Code harness)'
year: 2026
changed: harness
verified: reported
transfer: mixed
---

**Claim:** A GEPA-selected Claude Code harness raises HotpotQA test accuracy from 55.33 to 67.67 in the project's [overall results](https://github.com/RUC-NLPIR/FlashRSI/blob/560f02dfaa415be808647ae4c70d149423879cba/README.md#overall-results).

**Change:** The pinned explorer's [initial and selected snapshots](https://github.com/RUC-NLPIR/FlashRSI/blob/560f02dfaa415be808647ae4c70d149423879cba/docs/public/experiment-data/hotpotqa/resources/gepa-claude_code.json) differ only in `CLAUDE.md`. The selected version keeps the existing skill call and adds rules for short answers, source wording and formal entity names. These are the two ends of a lineage four edits long, not one edit. Claude Code is the harness, not the model: the [protocol](https://github.com/RUC-NLPIR/FlashRSI/blob/560f02dfaa415be808647ae4c70d149423879cba/docs/experiments/protocol.md) maps the serving alias to DeepSeek-V4.1-Flash and says an alias does not pin model weights.

**Controls:** Selection used 300 development items per record; the final and transfer sets are separate. A matched-budget baseline for this row: unknown. Number of independent search runs: unknown.

**Result:**

| Evaluation | Initial | Selected | Change (pp) |
| --- | ---: | ---: | ---: |
| HotpotQA development | 77.67 | 84.00 | +6.33 |
| HotpotQA test | 55.33 | 67.67 | +12.34 |
| MuSiQue transfer | 67.50 | 78.33 | +10.83 |
| DeepSearchQA transfer (F1) | 66.00 | 52.00 | -14.00 |

**Verified:** We read the source diff at the pinned commit. The scores are the authors' own and were not rerun. The [exporter](https://github.com/RUC-NLPIR/FlashRSI/blob/560f02dfaa415be808647ae4c70d149423879cba/scripts/_artifact_explorer.py#L249-L264) defines `coverage` as matching the best candidate score per development task, which counts a task as covered even when every candidate fails it; it is not paired final correctness.

**Open:** No paired per-task final outcomes were found, so which tasks flipped is unknown. The formatting rules are visible in the diff, but their role in the DeepSearchQA drop was not isolated.

**Try it:** Move your selected harness, unchanged, to a second task family and run [`compare.py`](../compare.py) on each set separately.
