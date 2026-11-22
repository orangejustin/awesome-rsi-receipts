# Awesome RSI Receipts

*What changed, what held up, and what broke in self-improving agents.*

**Would you merge a change that gained 12.34 percentage points on its home benchmark, gained 10.83 on one transfer benchmark, and lost 14.00 on another?** That is what [FlashRSI's authors report for one GEPA-selected harness](receipts/flashrsi-gepa.md). The source change is inspectable. The aggregate scores are author-reported, not independently reproduced here.

This collection turns research claims and local experiments into evidence you can inspect before adopting a change. It is not a leaderboard or an autonomous agent runtime.

## Try a receipt offline

Requires Python 3.9+. No installation, API key or network.

```sh
python3 compare.py examples/library-search.json
python3 -m unittest discover -v
```

The library example uses synthetic search judgments, not research data. The report distinguishes tasks that improved, regressed, or stayed the same even when the aggregate score ties. To adapt it, copy the fixture, put the judgments for the **same** task IDs into the two columns, and keep your evaluation conditions fixed.

## Read the evidence

| Receipt | Decision | Evidence |
| --- | --- | --- |
| [FlashRSI: one change, three outcomes](receipts/flashrsi-gepa.md) | Check transfer before adopting a tuned harness | Inspected diff; author-reported aggregates |
| [Harness evolution vs. extra attempts](receipts/matched-budget.md) | Pay for search or spend the same budget on a simpler baseline? | Author-reported experiments |
| [Flex-RSI: editing the improver](receipts/flex-rsi.md) | What would establish that the improver itself got better? | Author-reported comparison; attribution unresolved |

A receipt separates what changed (answer, persistent harness, or an improver actually used next round) from what was verified (author report, recalculated recorded judgments, or independent run). None implies another. Paired judgments can show which tasks flipped; aggregate scores alone cannot.

## Go deeper

| Start here | Why |
| --- | --- |
| [LobeHub Awesome RSI](https://github.com/lobehub/awesome-rsi) and [Harness RSI Atlas](https://github.com/LucasXinYu/harness-rsi) | Broader research maps rather than another long index here. |
| [Darwin Gödel Machine](https://github.com/jennyzzt/dgm), [GEPA](https://github.com/gepa-ai/gepa), [Meta-Harness](https://github.com/stanford-iris-lab/meta-harness), [RRSI](https://github.com/google-research/rrsi) | Self-modification lineages, feedback-driven optimization, search over harness changes, and tests of transfer. |
| [FlashRSI](https://github.com/RUC-NLPIR/FlashRSI), [Flex-RSI](https://arxiv.org/abs/2611.08946) | Evaluation frameworks and protocols, not interchangeable scores. |
| [WalkingLabs](https://github.com/walkinglabs/learn-harness-engineering), [OpenAI](https://openai.com/index/harness-engineering/), [LangChain](https://www.langchain.com/blog/the-anatomy-of-an-agent-harness#memory-and-search-for-continual-learning), [Mitchell Hashimoto](https://mitchellh.com/writing/my-ai-adoption-journey) | Harness engineering context and practice, not evidence of RSI. |

## Contribute

Start with [the receipt template](receipts/TEMPLATE.md) and [contribution guide](CONTRIBUTING.md). Negative and inconclusive results are welcome. Original files in this repository are MIT-licensed; linked third-party work retains its own terms.
