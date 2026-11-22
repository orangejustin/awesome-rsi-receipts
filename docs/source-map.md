# RSI source map

Pick the question you're trying to answer. The “try” column is a suggested experiment, not a claim that the result transfers. Papers report their own protocols and scores; engineering reports give patterns to adapt. None of the linked experiments were rerun for this map.

[Harness design](#harness-design) · [Search and feedback](#search-and-feedback) · [Evaluation and controls](#evaluation-and-controls) · [Transfer and continued improvement](#transfer-and-continued-improvement)

## Harness design

| Source | Try this | What it doesn't establish |
| --- | --- | --- |
| OpenAI · [Harness engineering](https://openai.com/index/harness-engineering/) · Engineering report | Turn a recurring failure into a lint rule or test the agent can run, with a specific remediation message. Keep repo guidance easy to find. | A first-party case study is not an isolated estimate of what the harness contributed. |
| Anthropic · [Effective harnesses for long-running agents](https://www.anthropic.com/research/effective-harnesses-for-long-running-agents) · Engineering report | Compare a plain restart with a restart from a progress log and a clean commit. Check whether the next session resumes the right task. | Resuming across sessions is persistence, not evidence that an improver gets better. |
| Anthropic · [The components of agent memory](https://www.anthropic.com/research/components-of-agent-memory) · Engineering experiments | Test what changes when the agent gets a searchable transcript, distilled notes, or notes prepared between sessions. | Better recall between sessions does not establish better harness edits. |

## Search and feedback

| Source | Try this | What it doesn't establish |
| --- | --- | --- |
| [GEPA](https://arxiv.org/abs/2507.19457v2) · Paper + [code](https://github.com/gepa-ai/gepa) | Compare prompt revisions based on failure traces with revisions that see scores alone. Reserve a final split. | Evidence for prompt optimization under the tested protocols is not a general ranking of harness or weight updates. |
| [Meta-Harness](https://arxiv.org/abs/2603.28052v1) · Paper + [code](https://github.com/stanford-iris-lab/meta-harness) | Give a proposer access to prior harness diffs and full traces. Compare with a proposer that gets the same candidates' scores only. | Searching over harness code does not show that the proposer itself improved. |
| OpenAI · [Build an agent improvement loop with traces, evals, and Codex](https://developers.openai.com/cookbook/examples/agents_sdk/agent_improvement_loop) · Cookbook | Convert a repeated trace failure into a regression case, then make a small, reviewed harness edit and rerun. | A worked example with synthetic tasks is not a controlled benchmark. |
| [Darwin Gödel Machine](https://arxiv.org/abs/2505.22954v3) and [Does Failure Feedback Direct Agent Self-Modification?](https://arxiv.org/abs/2610.14662v1) · Papers | When a patch was prompted by one failure, check whether it repaired that case, similar cases, and fresh cases separately. | A better selected agent does not prove the feedback drove that repair. The reanalysis doesn't refute DGM's aggregate gains. See the [receipt](../receipts/failure-feedback.md). |

## Evaluation and controls

| Source | Try this | What it doesn't establish |
| --- | --- | --- |
| Anthropic · [Demystifying evals for AI agents](https://www.anthropic.com/research/demystifying-evals-for-ai-agents) and [Quantifying infrastructure noise](https://www.anthropic.com/research/infrastructure-noise) · Guides and experiments | Grade the actual outcome, not the agent's claim of success. Pin environment and timeout rules, log infrastructure failures, and repeat noisy runs. | Different graders or resource limits can make small score gaps incomparable. |
| [Rethinking the Evaluation of Harness Evolution for Agents](https://arxiv.org/abs/2607.12227v4) · Paper | Give a fixed harness comparable feedback and extra attempts before attributing a win to evolution. | Its Terminal-Bench and game settings support different conclusions. See the [matched-budget receipt](../receipts/matched-budget.md). |
| [BOXBOX](https://arxiv.org/abs/2611.09218v3) · Paper | Match elapsed time when testing online harness revision against frozen, offline-evolved, and scaled baselines. | Adaptation within a long software optimization task does not establish compounding across tasks. |
| [GUARD](https://arxiv.org/abs/2611.23476v1) · Preprint | Track newly broken behavior separately from still-unfixed failures. Test your promotion rule on a fresh set. | The reported non-regression guarantee covers its gated buffer, not unseen tasks. |

## Transfer and continued improvement

| Source | Try this | What it doesn't establish |
| --- | --- | --- |
| [FlashRSI](https://github.com/RUC-NLPIR/FlashRSI/blob/560f02dfaa415be808647ae4c70d149423879cba/README.md#overall-results) and [RRSI](https://arxiv.org/abs/2609.24972v3) ([code](https://github.com/google-research/rrsi)) · Research artifacts and paper | Move the same selected harness to a different task family without retuning; compare that with screening out benchmark-specific edits during selection. | Transfer depends on the task family and protocol. Development-selection coverage is not paired final correctness. See the [FlashRSI receipt](../receipts/flashrsi-gepa.md). |
| [Self-Improvement Memory](https://arxiv.org/abs/2611.18856v1) · Preprint | When switching tasks or models, compare passing down only the harness with also passing edit rationale and expected vs. observed results. | The paper studies compatible benchmark or model switches; it doesn't establish general cross-domain compounding. |
| [Flex-RSI](https://arxiv.org/abs/2611.08946v1) · Preprint | Freeze the executor, budget, and evaluator; compare the original versus edited improver on the next round. | Permission to edit the whole harness doesn't isolate the effect of the improver. See the [Flex-RSI receipt](../receipts/flex-rsi.md). |

## Further reading

- **Broader maps:** [LobeHub Awesome RSI](https://github.com/lobehub/awesome-rsi) and [Harness RSI Atlas](https://github.com/LucasXinYu/harness-rsi) are starting points for finding adjacent methods, not substitutes for their original protocols.
- **Build a small harness:** [WalkingLabs](https://github.com/walkinglabs/learn-harness-engineering), [LangChain's harness anatomy](https://www.langchain.com/blog/the-anatomy-of-an-agent-harness), and [Mitchell Hashimoto's adoption notes](https://mitchellh.com/writing/my-ai-adoption-journey) help identify where to add tools, context, or checks. Tutorials and practitioner notes aren't evidence of recursive improvement.
