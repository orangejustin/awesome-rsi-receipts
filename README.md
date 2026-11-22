# Awesome RSI Receipts [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

[![Verify](https://github.com/orangejustin/awesome-rsi-receipts/actions/workflows/verify.yml/badge.svg)](https://github.com/orangejustin/awesome-rsi-receipts/actions/workflows/verify.yml)
[![Links](https://github.com/orangejustin/awesome-rsi-receipts/actions/workflows/links.yml/badge.svg)](https://github.com/orangejustin/awesome-rsi-receipts/actions/workflows/links.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

> What changed, who checked it, and what broke, for systems said to improve themselves.

[One tuned harness](receipts/flashrsi-gepa.md) gained **12.34 points** on its home test and **10.83** on one transfer set, then lost **14.00** on another. [One self-improving agent](receipts/darwin-godel-machine.md) went from 20% to 50%, on 200 of 500 tasks. [One improver](receipts/stop.md) got better at improving with a strong model and worse with a weak one. Each of these is a real result. None of them means what the headline alone suggests.

This list collects the evidence behind claims of recursive self-improvement (RSI) in AI agents and reads each claim the same way. It is not a leaderboard, and it does not run any agent.

**Try it offline** (Python 3.9+, no setup, no API key):

```sh
python3 compare.py examples/library-search.json
```

Both versions pass 2 of 4 synthetic tasks, yet one task improves and one regresses. Run it on your own before-and-after results to see which tasks flipped and whether the flips could be chance.

## Contents

- [Start here](#start-here)
- [Receipts](#receipts)
- [Sources](#sources)
  - [Would a simpler baseline do as well?](#would-a-simpler-baseline-do-as-well)
  - [Is the benchmark measuring what you think?](#is-the-benchmark-measuring-what-you-think)
  - [Is the difference bigger than the noise?](#is-the-difference-bigger-than-the-noise)
  - [Does the gain carry over and keep going?](#does-the-gain-carry-over-and-keep-going)
  - [Agents that edit themselves](#agents-that-edit-themselves)
  - [Search and feedback](#search-and-feedback)
  - [Harness design](#harness-design)
  - [Results anyone can check](#results-anyone-can-check)
  - [Can AI do AI research?](#can-ai-do-ai-research)
  - [Weights](#weights)
  - [Risk and governance](#risk-and-governance)
  - [Related lists](#related-lists)
- [Make your own receipt](#make-your-own-receipt)
- [Contributing](#contributing)

## Start here

| If you want to… | Start with |
| --- | --- |
| **Judge** a result you just read | [Receipts](#receipts): the same seven questions asked of each claim, with what did not hold. |
| **Learn** how self-improving agents are built and tested | [Sources](#sources): papers, audits, benchmarks and tools, grouped by the question they help answer. |
| **Test** a prompt, tool or memory change on your own tasks | [Make your own receipt](#make-your-own-receipt): one change, the same task IDs, a decision rule set in advance. |

## Receipts

Two things decide how much a self-improvement result tells you. The first is **what changed**: one answer, a program, a reusable harness, model weights, or the thing that does the improving. The second is **who checked**: the authors, someone recalculating from released outcomes, an independent rerun, or an artifact anyone can verify. Where the receipts sit today:

<!-- grid -->
| | Authors report it | Recalculated from released outcomes | Independently rerun | Anyone can check the artifact |
| --- | :---: | :---: | :---: | :---: |
| **One answer** | · | · | 1 | · |
| **A program or proof** | 1 | · | · | 1 |
| **A reusable harness** | 6 | 1 | 1 | · |
| **Model weights** | 1 | · | · | · |
| **The improver itself** | 3 | · | · | · |
<!-- /grid -->

Most of the evidence sits in the first column. The bottom row, where the thing that improved is the improver itself, is what the word "recursive" depends on, and none of it has been checked by anyone but its authors.

<!-- ledger -->
| Receipt | Before you rely on it, ask | What changed | Who checked | Elsewhere |
| --- | --- | --- | --- | --- |
| [The AI Scientist: what an outside evaluation found](receipts/ai-scientist.md) · 2025 | What did independent evaluators find when they ran the system themselves? | One answer | Independently rerun | Not tested |
| [AlphaEvolve: results you can check yourself](receipts/alphaevolve.md) · 2025 | Which of the reported results can be confirmed without trusting the authors? | A program or proof | Anyone can check the artifact | Not tested |
| [Code evolution against simple baselines](receipts/simple-baselines.md) · 2026 | Is the search method doing the work, or the way the problem was set up? | A program or proof | Authors report it | Not tested |
| [ADAS: gains that shrank when others reran it](receipts/adas.md) · 2024 | Does the discovered agent still win with a different executor model and the same budget? | A reusable harness | Independently rerun | Mixed |
| [Darwin Gödel Machine: 20% to 50% on a subset](receipts/darwin-godel-machine.md) · 2025 | How much of the gain survives on the full benchmark, another model or another benchmark? | A reusable harness | Authors report it | Mixed |
| [Huxley-Gödel Machine: a high score is a poor guide to good descendants](receipts/huxley-godel-machine.md) · 2025 | Is the agent you would pick by benchmark score the one that leads to better agents? | A reusable harness | Authors report it | Mixed |
| [SICA: one run, fifty tasks](receipts/sica.md) · 2025 | How much of a 36-point gain on 50 tasks is the agent getting smarter? | A reusable harness | Authors report it | Not tested |
| [Did failure feedback fix the failure?](receipts/failure-feedback.md) · 2026 | When an edit was prompted by one failing task, did it repair that task? | A reusable harness | Recalculated from released outcomes | Did not hold |
| [FlashRSI: one harness, three outcomes](receipts/flashrsi-gepa.md) · 2026 | Would this tuned harness still help on a task family it was not tuned on? | A reusable harness | Authors report it | Mixed |
| [Harness evolution against extra attempts](receipts/matched-budget.md) · 2026 | Would the unchanged harness do as well if it got the same budget and feedback? | A reusable harness | Authors report it | Mixed |
| [Notes learned from failures, against the same search without them](receipts/failure-traces.md) · 2026 | How much of the gain comes from seeing the failures, and how much from simply trying and keeping what scores better? | A reusable harness | Authors report it | Did not hold |
| [SEAL: a model that writes its own training data](receipts/seal.md) · 2025 | What happens to earlier knowledge as self-generated updates accumulate? | Model weights | Authors report it | Not tested |
| [STOP: an improver applied to itself](receipts/stop.md) · 2023 | Does self-improvement still work when the underlying model is weaker? | The improver itself | Authors report it | Mixed |
| [Gödel Agent: rewriting the routine that rewrites](receipts/godel-agent.md) · 2024 | How often does an agent that can edit its own improvement loop end up worse than it started? | The improver itself | Authors report it | Not tested |
| [Flex-RSI: letting the improver edit itself](receipts/flex-rsi.md) · 2026 | Did the improver get better, or did the harness just get more attempts at being edited? | The improver itself | Authors report it | Not tested |
<!-- /ledger -->

**Elsewhere** records whether the gain showed up beyond the tasks it was selected on: another benchmark, another model, or a held-out task family.

## Sources

Each entry says what it is and where its evidence stops. Unless an entry says otherwise, results are the authors' own and were not rerun for this list. Entries marked 🧾 have a receipt.

### Would a simpler baseline do as well?

- [Rethinking the Evaluation of Harness Evolution for Agents](https://arxiv.org/abs/2607.12227v4) - Gives a fixed harness comparable feedback and extra attempts before crediting evolution. Evolution loses to plain test-time scaling on Terminal-Bench 2.1 and wins in long-horizon games, so the answer depends on the task. 🧾 [receipt](receipts/matched-budget.md)
- [Simple Baselines are Competitive with Code Evolution](https://arxiv.org/abs/2602.16805v2) - Two simple baselines match or beat elaborate code-evolution pipelines given the same search space. Credits the problem formulation more than the search algorithm. 🧾 [receipt](receipts/simple-baselines.md)
- [Agent Self-Improvement with Frozen Weights](https://arxiv.org/abs/2611.11342v2) - Compares notes learned from failures with the same search run blind. Seeing the failures adds 4.0 points; about 60% of the gain comes from trying and keeping what scores better. One model. 🧾 [receipt](receipts/failure-traces.md)
- [Does Failure Feedback Direct Agent Self-Modification?](https://arxiv.org/abs/2610.14662v1) - Recalculates, from public logs, whether an edit prompted by one failure repairs that failure. It did not do so more often than for other failures. Says nothing against aggregate gains from selection. 🧾 [receipt](receipts/failure-feedback.md)
- [BOXBOX](https://arxiv.org/abs/2611.09218v3) - Matches elapsed time when testing online harness revision against frozen, offline-evolved and scaled baselines. Adaptation inside one long software task is not compounding across tasks.
- [AI Research Agents for Machine Learning: Search, Exploration, and Generalization in MLE-bench](https://arxiv.org/abs/2507.02554v2) - Separates the search strategy from the set of edit operators and shows the pairing matters (Kaggle medal rate 39.6% to 47.7% on MLE-bench lite). A known benchmark, so contamination is not ruled out.
- [Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity](https://arxiv.org/abs/2507.09089v2) - A randomised trial: developers forecast a 24% speedup from AI tools and were 19% slower. Not about self-improvement, but the clearest example of a measured effect contradicting everyone's expectation.

### Is the benchmark measuring what you think?

- [Establishing Best Practices for Building Rigorous Agentic Benchmarks](https://arxiv.org/abs/2507.02825v5) - Audits widely used agent benchmarks and finds task and grading flaws that can misstate performance by up to 100% in relative terms. Comes with a checklist; it is guidance, not a tool.
- [The SWE-Bench Illusion](https://arxiv.org/abs/2506.12286v4) - Models name the buggy file from the issue text alone 76% of the time on SWE-bench Verified and 53% on repositories outside it. Indirect evidence of memorisation, not proof for any one model.
- [The More You Automate, the Less You See](https://arxiv.org/abs/2509.08713v2) - Isolates four failure modes in automated research pipelines (benchmark choice, data leakage, metric misuse, selection after the fact) and shows they are caught from logs and code, not from the final paper. Two systems studied.
- [Auditing Harness Tampering in Self-Improving Agents](https://arxiv.org/abs/2609.00069v1) - Finds self-edits that raise the score without raising capability in real runs, often in the lineage of the winning agent. The audit methods are benchmarked by the same authors.
- [PostTrainBench](https://arxiv.org/abs/2603.08640v2) - Agents get ten GPU-hours to post-train a model; the best reaches 23.2% against 51.1% for official instruction-tuned models. Some trained on the test set or used API keys they found.
- [The Meta-Agent Challenge](https://arxiv.org/abs/2606.04455v1) - A meta-agent must build an agent that does well on held-out tasks. Few match human-built baselines, and optimisation pressure produced attempts to extract the ground truth.
- [Holistic Agent Leaderboard](https://arxiv.org/abs/2510.11977v1) - 21,730 rollouts across 9 models and 9 benchmarks with all logs released. Reading the logs surfaced agents searching for the benchmark online instead of solving the task.
- Anthropic · [Demystifying evals for AI agents](https://www.anthropic.com/research/demystifying-evals-for-ai-agents) and [Quantifying infrastructure noise](https://www.anthropic.com/research/infrastructure-noise) - Grade the outcome, not the agent's claim of success; pin the environment and time limits. Resource settings alone moved a coding benchmark by several points.

### Is the difference bigger than the noise?

- [Adding Error Bars to Evals](https://arxiv.org/abs/2411.00640v1) - Formulas for error bars, paired comparisons and planning how many questions an evaluation needs. Relies on large-sample approximations.
- [Don't Use the CLT in LLM Evals With Fewer Than a Few Hundred Datapoints](https://arxiv.org/abs/2503.01747v3) - Shows those approximations give error bars that are too small on small benchmarks, with a [library](https://github.com/sambowyer/bayes_evals) of alternatives. A position paper.
- [Measuring all the noises of LLM Evals](https://arxiv.org/abs/2512.21326v3) - Separates noise from the model's answers and noise from the choice of questions, and finds the first usually larger in paired comparisons, so averaging repeated runs buys power.
- [SAGE: A Statistical Acceptance Gate for Self-Evolving Agents](https://arxiv.org/abs/2609.36043v1) - Replaces "keep any edit that raises the average" with a paired per-item test, because the best score on a small noisy set is biased upward. Regressions fell in 19 of 20 settings.
- [Trustworthy Recursive Self-Improvement with Statistical Guarantees](https://arxiv.org/abs/2611.10787v1) - An acceptance gate that bounds the share of accepted edits that are actually worse; a greedy gate accepted 45.59% inferior updates against 2.78%. The guarantee holds under stated assumptions.
- [GUARD](https://arxiv.org/abs/2611.23476v1) - Tracks newly broken behaviour separately from failures that were never fixed. Its non-regression guarantee covers the gated buffer, not unseen tasks.
- [On The Statistical Limits of Self-Improving Agents](https://arxiv.org/abs/2510.04399v3) - Theory: if self-modification can grow the agent's capacity without bound, a task that was learnable can become unlearnable. Not tested empirically.

### Does the gain carry over and keep going?

- [FlashRSI](https://github.com/RUC-NLPIR/FlashRSI/blob/560f02dfaa415be808647ae4c70d149423879cba/README.md#overall-results) - Moves selected harnesses to other task families without retuning. The same harness helps on one and hurts on another. 🧾 [receipt](receipts/flashrsi-gepa.md)
- [RRSI](https://arxiv.org/abs/2609.24972v3) ([code](https://github.com/google-research/rrsi)) - Screens out benchmark-specific edits during selection. Coverage on development tasks is not paired final correctness.
- [Self-Improvement Memory](https://arxiv.org/abs/2611.18856v1) - When switching task or model, passes down the reasons for past edits and what was expected against what happened, not only the harness. Tested on compatible switches, not across domains.
- [RSIBench-Data](https://arxiv.org/abs/2607.25886v1) - Fixed stack and budgets for agents improving training data. In 58.33% of settings agents improved on their first valid attempt; of searches that continued past their best score, 78.26% ended lower.
- [SelfImprove-Bench](https://arxiv.org/abs/2611.02797v1) - A ladder of five generalisation levels to separate capability from fitting the scenario. Gains from existing methods were inconsistent across the levels. Built on games.
- [Continual Learning Exam](https://arxiv.org/abs/2610.33956v1) - 600 levels measuring improvement from experience with retention. Feedback and revision added a median 5.3 points; the best system cleared 47.7% of levels. Graded by a model.
- [Evo-Bench](https://arxiv.org/abs/2608.09096v2) and [HarnessOpt-Bench](https://arxiv.org/abs/2608.06301v1) - Benchmarks that try to separate skill at improving a harness from the strength of the base model, the second with a sealed test partition. Gains vary a lot by task and seed.
- [AI4AI at Test-Time](https://arxiv.org/abs/2608.12307v1) - A stronger model writes a harness for a weaker one and nearly doubles its score. The authors attribute the gain to deterministic code, benchmark-specific routing and answer formatting, not better reasoning.

### Agents that edit themselves

- [Darwin Gödel Machine](https://arxiv.org/abs/2505.22954v3) ([code](https://github.com/jennyzzt/dgm)) - A coding agent rewrites its own code and keeps an archive of variants. The headline numbers are on subsets, and transfer is strong on one benchmark and small on the other. 🧾 [receipt](receipts/darwin-godel-machine.md)
- [Huxley-Gödel Machine](https://arxiv.org/abs/2510.21614v3) ([code](https://github.com/metauto-ai/HGM)) - Shows an agent's own score predicts its descendants' quality poorly and selects on the descendants instead. Its lead over earlier methods is two tasks in one run. 🧾 [receipt](receipts/huxley-godel-machine.md)
- [SICA](https://arxiv.org/abs/2504.15228v2) ([code](https://github.com/MaximeRobeyns/self_improving_coding_agent)) - No separate meta agent: the best agent so far writes the next. One run on 50 tasks, with much of the early gain from speed and cost. 🧾 [receipt](receipts/sica.md)
- [Gödel Agent](https://arxiv.org/abs/2410.04444v4) ([code](https://github.com/Arvid-pku/Godel_Agent)) - Patches its own running code, including the improvement routine. 14% of 100 trials ended below where they started. 🧾 [receipt](receipts/godel-agent.md)
- [STOP](https://arxiv.org/abs/2310.02304v3) ([code](https://github.com/microsoft/stop)) - An improver program applied to its own source. Works with GPT-4, degrades with weaker models, and measures how often generated code tried to leave the sandbox. 🧾 [receipt](receipts/stop.md)
- [ADAS](https://arxiv.org/abs/2408.08435v2) ([code](https://github.com/ShengranHu/ADAS)) - A fixed meta agent writes new agents in code. Two later groups reran it with other models and found small or negative gains. 🧾 [receipt](receipts/adas.md)
- [Flex-RSI](https://arxiv.org/abs/2611.08946v1) - A benchmark where the improver may edit the executor and itself. Shows editing beats not editing; does not isolate whether the improver improved. 🧾 [receipt](receipts/flex-rsi.md)
- [Hyperagents](https://arxiv.org/abs/2603.19461v2) - Makes the procedure that modifies the agent editable too, and reports that improvements at that level transfer across domains. "Self-accelerating" is stated as a possibility, not a measurement.
- [Recursive self-improvement of AI research agents](https://arxiv.org/abs/2609.26457v1) - A research agent edits its own code over an eight-day run and finds seven successive improvements that hold on four held-out benchmarks. One run; the comparison with a production agent is on the authors' own suite.
- [Evaluation-Free Recursive Self-Improvement for Coding Agents](https://arxiv.org/abs/2611.21056v1) - Evolves a coding agent using only validity checks, with no task evaluation inside the loop: 60.0% to 85.6%, against 86.7% and 88.3% for two methods that do evaluate.
- [Mendel Gödel Machine](https://arxiv.org/abs/2608.07645v1) and [Red Queen Gödel Machine](https://arxiv.org/abs/2606.26294v3) - Edit agents using several trajectories or another lineage at once, and co-evolve the evaluators with the agents. A moving evaluator makes comparison with other papers harder.
- [HELIX](https://arxiv.org/abs/2608.13951v1) - Evolves harnesses for a fixed model and keeps matched trajectories as training data for the next model. One round, code repair only, a 4.0% gain for the single best harness.

### Search and feedback

- [GEPA](https://arxiv.org/abs/2507.19457v2) ([code](https://github.com/gepa-ai/gepa)) - Revises prompts from failure traces instead of scores alone. Evidence for prompt optimisation under its protocols, not a ranking of harness or weight updates.
- [Meta-Harness](https://arxiv.org/abs/2603.28052v1) ([code](https://github.com/stanford-iris-lab/meta-harness)) - Gives the proposer prior harness diffs and full traces. Searching over harness code does not show the proposer itself improved.
- [Agentic Context Engineering](https://arxiv.org/abs/2510.04618v3) - Treats the context as the thing that evolves and names "context collapse", where repeated rewriting erodes detail. No weights change.
- OpenAI · [Build an agent improvement loop with traces, evals, and Codex](https://developers.openai.com/cookbook/examples/agents_sdk/agent_improvement_loop) - Turn a repeated trace failure into a regression case, make one reviewed edit, rerun. A worked example on synthetic tasks, not a controlled benchmark.

### Harness design

- OpenAI · [Harness engineering](https://openai.com/index/harness-engineering/) - Turn a recurring failure into a lint rule or test the agent can run, with a specific remediation message. A first-party case study, not an isolated estimate of what the harness contributed.
- Anthropic · [Effective harnesses for long-running agents](https://www.anthropic.com/research/effective-harnesses-for-long-running-agents) - Resume from a progress log and a clean commit instead of a plain restart. Persistence across sessions is not evidence that an improver gets better.
- Anthropic · [The components of agent memory](https://www.anthropic.com/research/components-of-agent-memory) - What changes when the agent gets a searchable transcript, distilled notes, or notes prepared between sessions. Better recall is not better edits.
- [WalkingLabs](https://github.com/walkinglabs/learn-harness-engineering), [LangChain's harness anatomy](https://www.langchain.com/blog/the-anatomy-of-an-agent-harness) and [Mitchell Hashimoto's adoption notes](https://mitchellh.com/writing/my-ai-adoption-journey) - Where to add tools, context or checks when building a small harness. Tutorials and practitioner notes.

### Results anyone can check

- [AlphaEvolve](https://arxiv.org/abs/2506.13131v1) ([results](https://github.com/google-deepmind/alphaevolve_results)) - Evolves programs against an automatic evaluator. The mathematical constructions are published with verification code; the infrastructure numbers are internal. 🧾 [receipt](receipts/alphaevolve.md)
- [Mathematical exploration and discovery at scale](https://arxiv.org/abs/2511.02864v3) - AlphaEvolve on 67 mathematics problems: best known solutions rediscovered in most, improved in several. The constructions are checkable; the search is closed.
- [Reinforced Generation of Combinatorial Structures](https://arxiv.org/abs/2509.18057v7) - New inapproximability bounds from structures the system found, with correctness resting on the authors' proofs. The system also made its own verification procedure up to 10,000 times faster.
- [ShinkaEvolve](https://arxiv.org/abs/2509.19349v1), [ThetaEvolve](https://arxiv.org/abs/2511.23473v1) and [TTT-Discover](https://arxiv.org/abs/2601.16175v2) - Open systems in the same family; the last two reach reported best-known bounds with small open models and public code. Best-known claims are per problem and await outside confirmation.
- [OpenEvolve](https://github.com/algorithmicsuperintelligence/openevolve) - An open implementation of the AlphaEvolve design. Its results are stated in the repository without a paper or an outside audit.
- [Self-Modifying Lean Proof Agents](https://arxiv.org/abs/2607.17352v1) and [Growing an Agent/Prover Interface](https://arxiv.org/abs/2609.39544v3) - Self-improvement where success only counts if a proof checker accepts the output. In the first, the benchmark co-evolves with the agent, which complicates comparison.

### Can AI do AI research?

- [RE-Bench](https://arxiv.org/abs/2411.15114v2) - Seven research-engineering tasks with 71 human expert attempts. Agents score higher than people at a two-hour budget and lower at 32 hours. Best-of-many agent attempts are compared with single human attempts.
- [Measuring AI Ability to Complete Long Tasks](https://arxiv.org/abs/2503.14499v4) - The length of task agents complete half the time has doubled about every seven months. The authors flag that how far this carries outside their task suite is open.
- [PaperBench](https://arxiv.org/abs/2504.01848v3) and [CORE-Bench](https://arxiv.org/abs/2409.11363v2) - Replicating published research from scratch (best agent 21.0%) and reproducing results from provided code (21% on the hardest tier). Scores are for the models available when each was written.
- [The Automated LLM Speedrunning Benchmark](https://arxiv.org/abs/2506.22419v2) - Agents struggle to reimplement known training speedups even when given detailed hints.
- [MLS-Bench](https://arxiv.org/abs/2605.08678v3) and [AutoLab](https://arxiv.org/abs/2606.05080v1) - Whether agents can invent methods that generalise, and sustain long optimisation runs. Tuning is easier for them than invention, and most stop early or run out of budget.
- [Towards Execution-Grounded Automated AI Research](https://arxiv.org/abs/2601.14525v1) - Runs model-proposed research ideas on real GPUs. Evolutionary search found methods that beat two baselines; training the idea generator on execution reward collapsed to a few ideas.
- [The AI Scientist](https://arxiv.org/abs/2408.06292v3) and [Evaluating Sakana's AI Scientist](https://arxiv.org/abs/2502.14297v3) - An end-to-end paper generator and an independent evaluation of it, in which 42% of experiments failed to run. 🧾 [receipt](receipts/ai-scientist.md)

### Weights

- [SEAL: Self-Adapting Language Models](https://arxiv.org/abs/2506.10943v2) ([code](https://github.com/Continual-Intelligence/SEAL)) - A model generates its own fine-tuning data and keeps the updates. Gains on small tasks, with forgetting as edits accumulate. 🧾 [receipt](receipts/seal.md)
- [Escaping Model Collapse via Synthetic Data Verification](https://arxiv.org/abs/2510.16657v3) - Retraining on self-generated data filtered by a verifier helps at first, then plateaus at what the verifier knows and can reverse. Theory in a linear setting plus one small experiment.
- [Frontis-MA1 / OpenMLE](https://arxiv.org/abs/2607.28568v1) - Trains a model to perform program-evolution steps and separates the model's contribution from the framework's. That training data was kept apart from the evaluation benchmarks is the authors' statement.

### Risk and governance

- [Your Agent May Misevolve](https://arxiv.org/abs/2509.26354v2) - Studies what goes wrong as agents evolve their memory, tools and workflows: safety behaviour degrades and new vulnerabilities appear. Covers the pathways the authors chose.
- Anthropic · [When AI Builds Itself](https://www.anthropic.com/institute/recursive-self-improvement) - A lab's own account of how much of its development is done by its models, with the statement that recursive self-improvement "is not inevitable". Internal, unaudited numbers; the page calls lines of code an imperfect measure.
- Google DeepMind · [Frontier Safety Framework update](https://deepmind.google/blog/strengthening-our-frontier-safety-framework/) - Adds capability levels for models that could accelerate AI research and development. No numeric thresholds are published.

### Related lists

- [LobeHub Awesome RSI](https://github.com/lobehub/awesome-rsi) - The broad map of the field: model-level, harness-level, multi-agent, embodied, safety and tools.
- [Harness RSI Atlas](https://github.com/LucasXinYu/harness-rsi) - Compares harness-level mechanisms with a traceable evidence dataset.

## Make your own receipt

[Test one change on your own data](docs/your-first-receipt.md) walks through it: decide what would make you keep the change before you look, record the same task IDs for both versions, and run

```sh
python3 compare.py my-holdout.json
```

The output lists the tasks that were gained and regressed, and `sign_test_p`: how often flips this one-sided would happen if the change made no difference. Seven flips split five to two is not evidence of anything.

## Contributing

Corrections and new receipts are welcome, and so are negative and inconclusive results. Start from the [receipt template](receipts/TEMPLATE.md) and the [contribution guide](CONTRIBUTING.md), then run:

```sh
python3 receipts.py lint && python3 receipts.py ledger && python3 -m unittest discover
```

## License

Original files here are [MIT-licensed](LICENSE). Linked work keeps its own terms.
