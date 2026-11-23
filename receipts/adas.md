---
title: 'ADAS: gains that shrank when others reran it'
question: 'Does the discovered agent still win with a different executor model and the same budget?'
system: 'Automated Design of Agentic Systems (Meta Agent Search)'
year: 2024
changed: harness
verified: rerun
transfer: mixed
---

**Claim:** A meta agent that writes new agents in code beats hand-designed agents, by 13.6 F1 on DROP and 14.4% accuracy on MGSM ([Hu et al.](https://arxiv.org/abs/2408.08435v2)).

**Change:** The `forward` function of the task agent, written by a fixed GPT-4 meta agent that reads a growing archive of earlier agents. The meta agent itself is never edited; the authors list that as future work.

**Controls:** On ARC, search used 20 validation questions and reported on 60 test questions, each evaluated five times. Baselines are hand-designed agents. A random-search control and the number of independent search runs: unknown.

**Result:** In the paper, agents found on MGSM carry to GSM8K (+25.9%) and GSM-Hard (+13.2%), and agents found with GPT-3.5 carry to other models on ARC. The transferred agents were the top three by test accuracy. One run cost about USD 300 to 500.

**Verified:** Rerun by others, with different models. The [AFlow authors](https://arxiv.org/abs/2410.10762v4), using Claude 3.5 Sonnet to optimise and GPT-4o-mini to execute for 30 rounds, report ADAS averaging 67.2 across six benchmarks against 74.7 for plain chain-of-thought. The [MASS authors](https://arxiv.org/abs/2502.02533v2) report that it "only brings subtle gains" with Gemini 1.5. Both groups were proposing a competing method.

**Open:** No neutral rerun in the original configuration was found. The reruns changed the models, so they show the result is sensitive to the executor, not that the original numbers were wrong. [Code](https://github.com/ShengranHu/ADAS) is public; the paper's per-task logs were not found.

**Try it:** Rerun the discovered agent with the executor you actually deploy, next to a plain chain-of-thought baseline given the same number of model calls.
