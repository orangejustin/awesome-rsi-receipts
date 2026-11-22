# Awesome RSI Receipts

*What changed, what held up, and what broke in self-improving agents.*

[One FlashRSI harness](receipts/flashrsi-gepa.md) gained **12.34 percentage points** on its home test and **10.83 points** on one transfer set, but lost **14.00 F1 points** on another. Same selected harness, different tests. We inspected the change; the scores are author-reported, not rerun here.

**Try it offline** (Python 3.9+, no setup or API key):
```sh
python3 compare.py examples/library-search.json
```
Both versions pass 2 of 4 synthetic tasks, yet one task improves and one regresses. **Fork to see which of your own tasks flip**, not just whether the average goes up.

## Start here

| If you want to… | Start with |
| --- | --- |
| **Learn** how agent harnesses are designed and improved | [Read the source map](docs/source-map.md): papers and engineering reports organized by what you want to change or test. |
| **Decide** whether a result supports a change | [Read the receipts](#read-the-receipts): inspect the change, compare the controls, and see what did not transfer. |
| **Test** a prompt, tool, or memory change on your own data | [Fork and run a paired check](docs/your-first-receipt.md): one change, the same task IDs, and a decision rule set in advance. |

## Read the receipts

| Receipt | Decision | Evidence |
| --- | --- | --- |
| [FlashRSI: one change, three outcomes](receipts/flashrsi-gepa.md) | Check transfer before adopting a tuned harness | Inspected diff; author-reported aggregates |
| [Harness evolution vs. extra attempts](receipts/matched-budget.md) | Pay for search or spend the same budget on a simpler baseline? | Author-reported experiments |
| [Flex-RSI: editing the improver](receipts/flex-rsi.md) | What would establish that the improver itself got better? | Author-reported comparison; attribution unresolved |
| [Did failure feedback fix the failure?](receipts/failure-feedback.md) | Measure target repair separately from held-out improvement | Published reanalysis of DGM logs; not recalculated here |

Two labels matter: **what changed** (an answer, a reusable harness, or an improver actually used again) and **what was verified** (a published result, a calculation from recorded outcomes, or an independent rerun). Inspecting the code change is separate from checking the score. This is not a leaderboard or an agent runtime.

## Contribute

Start with the [receipt template](receipts/TEMPLATE.md) and [contribution guide](CONTRIBUTING.md). Run `python3 -m unittest discover -v` before submitting. Negative and inconclusive results are welcome. Original files here are MIT-licensed; linked third-party work retains its own terms.
