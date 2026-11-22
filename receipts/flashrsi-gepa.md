# FlashRSI: GEPA-selected Claude Code harness

**Decision:** Treat the gains as benchmark-specific until transfer has been checked against your own tasks.

**Intervention:** The pinned explorer's [initial and selected snapshots](https://github.com/RUC-NLPIR/FlashRSI/blob/560f02dfaa415be808647ae4c70d149423879cba/docs/public/experiment-data/hotpotqa/resources/gepa-claude_code.json) differ only in `CLAUDE.md`. The selected version retains the existing skill call and adds short-answer formatting, source wording and formal entity-name rules. This compares the endpoints of a lineage, not a single parent-to-child edit. Claude Code is the harness, not the model. The [protocol](https://github.com/RUC-NLPIR/FlashRSI/blob/560f02dfaa415be808647ae4c70d149423879cba/docs/experiments/protocol.md) maps the serving alias to DeepSeek-V4.1-Flash, not a pinned weights revision.

| Evaluation | Initial | Selected | Change (pp) |
| --- | ---: | ---: | ---: |
| HotpotQA development (300 items per record) | 77.67 | 84.00 | +6.33 |
| HotpotQA test | 55.33 | 67.67 | +12.34 |
| MuSiQue transfer | 67.50 | 78.33 | +10.83 |
| DeepSearchQA transfer (F1) | 66.00 | 52.00 | -14.00 |

**Evidence:** Inspected source diff; development and [final matrix](https://github.com/RUC-NLPIR/FlashRSI/blob/560f02dfaa415be808647ae4c70d149423879cba/README.md#overall-results) aggregates are author-reported. Development selection and final results are separate. The [exporter](https://github.com/RUC-NLPIR/FlashRSI/blob/560f02dfaa415be808647ae4c70d149423879cba/scripts/_artifact_explorer.py#L249-L264) defines `coverage` as matching the best observed candidate score per development task, even when all candidates fail. It is not final paired correctness data.

**Unknown:** We did not find paired final outcomes, independently rerun the experiment, or establish an equal-budget comparison for this row. The formatting specialization is visible; its causal role in the transfer decline was not isolated.
