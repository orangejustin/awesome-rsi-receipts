---
title: 'Huxley-Gödel Machine: a high score is a poor guide to good descendants'
question: 'Is the agent you would pick by benchmark score the one that leads to better agents?'
system: 'Huxley-Gödel Machine'
year: 2025
changed: harness
verified: reported
transfer: mixed
---

**Claim:** In self-improving coding agents, an agent's own benchmark score is a weak predictor of how good its descendants become, and selecting on estimated descendant quality does better ([Wang et al.](https://arxiv.org/abs/2510.21614v3)).

**Change:** The rule that chooses which agent to modify next. The agents still edit their own code; the selection rule is written by people.

**Controls:** All three methods start from the same agent (40% on a 60-task subset of SWE-bench Verified) with the same 800 evaluations. SWE-bench Lite results are given both with and without the 93 tasks that overlap SWE-bench Verified. Repeated runs for the 60-task comparison: none found.

**Result:** The selection scores used by earlier methods correlate 0.285 (DGM) and 0.444 (SICA) with measured descendant quality. After 800 evaluations: SICA 50.0, DGM 53.3, this method 56.7, using 517 allocated CPU-hours against DGM's 1,231. On the full 500 tasks an adjusted starting agent went from 53.2% to 61.4% over 8,000 evaluations.

Moved to SWE-bench Lite with GPT-5-mini, the agent improves on its starting point (34.8% to 40.1% on the non-overlapping tasks). With GPT-5 it scores 47.8% on those tasks against 48.3% for SWE-agent, and 57% against 56.7% with the overlap included.

**Verified:** The authors' own runs, including their runs of the two baselines with models the original papers did not use. [Code](https://github.com/metauto-ai/HGM) is public.

**Open:** On a 60-task subset one task is 1.67 points, so the 3.4-point lead over DGM is two tasks from a single run. On the tasks it had not seen, the transferred agent is level with a hand-built one, not ahead. A [later paper](https://arxiv.org/abs/2511.13646v3) reports 65.0% on the same subset from an agent that does not self-improve offline, quoting these baseline numbers.

**Try it:** Log the parent of every candidate. After a search, check whether your highest-scoring agents were also the ones whose children scored highest.
