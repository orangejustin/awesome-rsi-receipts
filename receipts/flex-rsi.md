---
title: 'Flex-RSI: letting the improver edit itself'
question: 'Did the improver get better, or did the harness just get more attempts at being edited?'
system: 'Flex-RSI benchmark'
year: 2026
changed: improver
verified: reported
transfer: untested
---

**Claim:** In [Flex-RSI](https://arxiv.org/abs/2611.08946v1), self-improvement raised the validation score in 150 of 177 runs (85%), with a median gain of 10.4 points, across 18 models and 24 vision and robotics tasks.

**Change:** After each round an improver revises the harness, "including the executor and itself". Every run starts from the same general-purpose harness and the final solution is scored on hidden test data.

**Controls:** Seven pairs of runs are identical in task version, budget, protocol and seed except that one keeps the harness frozen. With the frozen harness the improver does not run.

**Result:** The self-improving run scored higher on test in six of the seven pairs, by +2.0 to +40.0 points. The [authors' overview](https://flex-rsi.github.io/blog.html) gives examples.

**Verified:** The authors' own runs, not rerun here.

**Open:** The pairs show that editing the harness helps compared with not editing it. They do not show that the improver itself became better at improving, because the executor and the improver change together and there is no arm where only one of them is edited. Seven pairs is a small sample, and whether an edited improver carries over to a fresh task was not tested.

**Try it:** Freeze the executor, budget and evaluator. Give the original improver and the edited improver the same starting harness on fresh tasks, and compare the changes each one produces in the next round.
