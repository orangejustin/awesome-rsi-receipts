---
title: SICA: one run, fifty tasks
question: How much of a 36-point gain on 50 tasks is the agent getting smarter?
system: SICA, a Self-Improving Coding Agent
year: 2025
changed: harness
verified: reported
transfer: untested
---

**Claim:** A coding agent that edits its own codebase improves from 17% to 53% on a random subset of SWE-bench Verified ([Robeyns et al.](https://arxiv.org/abs/2504.15228v2)).

**Change:** The agent's own code. There is no separate meta agent: the best agent in the archive is used to write the next one.

**Controls:** A fixed random subset of 50 tasks. One run of 15 iterations, costing about USD 7,000. An arm without self-improvement, repeated runs and a transfer test: none found in the paper.

**Result:** The per-iteration scores are not monotonic: 0.17, 0.14, 0.17, 0.22, 0.38, 0.30, 0.37, 0.33, 0.27, 0.47, 0.46, 0.44, 0.44, 0.27, 0.53, 0.51. The score that is optimised mixes accuracy with cost and time, under a 300-second timeout. The authors say the timeout depresses the starting score and that much of the early gain comes from faster file editing and lower cost. On reasoning tasks the scaffold averaged 76%, below o3-mini alone at 87% (AIME) and 79% (GPQA Diamond).

**Verified:** The authors' own single run. [Code](https://github.com/MaximeRobeyns/self_improving_coding_agent) is public. When the [Huxley-Gödel Machine authors](https://arxiv.org/abs/2510.21614v3) ran it with other models it stopped self-modifying after 360 evaluations because of context-window errors.

**Open:** With one run on 50 tasks, one task is two points, and a drop from 0.44 to 0.27 between adjacent iterations shows how large the noise is. How much of the gain would appear with a longer timeout from the start is not known.

**Try it:** Rerun your starting agent with the final timeout and cost limits before measuring improvement, so the baseline is not penalised for being slow.
