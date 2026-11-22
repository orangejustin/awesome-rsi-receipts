---
title: Harness evolution against extra attempts
question: Would the unchanged harness do as well if it got the same budget and feedback?
system: Rethinking the Evaluation of Harness Evolution for Agents
year: 2026
changed: harness
verified: reported
transfer: mixed
---

**Claim:** Automatic harness evolution is usually credited with gains that a fixed harness might reach with more attempts. [Wang et al.](https://arxiv.org/abs/2607.12227v4) test that directly.

**Change:** Nothing new is proposed. The study gives a fixed harness comparable feedback and extra attempts, and compares it with evolved harnesses on tasks kept apart from those used for selection.

**Controls:** Matched inference budget between evolution and simpler test-time scaling; runs with and without access to test cases.

**Result:** On Terminal-Bench 2.1, automatic harness evolution "fails to outperform simple test-time scaling methods both with and without test cases, and exhibits limited generalization". In long-horizon game settings the direction reverses under matched budgets: the authors report +80% over the search baseline on ARC-AGI-3 and +11% on EdgeBench.

**Verified:** The authors' own comparisons, not rerun here.

**Open:** The two settings support opposite conclusions, so the result does not rank evolution against scaling in general. Which property of a task predicts the direction is not established.

**Try it:** Before crediting a search, give the unchanged harness the same number of model calls as extra attempts with the same feedback, on the same split. Log search cost and execution cost separately.
