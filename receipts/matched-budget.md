# Harness evolution vs. extra attempts

**Decision:** Give the unchanged harness comparable feedback and inference budget before attributing a gain to evolution.

**Intervention:** The [authors' revised study](https://arxiv.org/abs/2607.12227v4) contrasts evolved harnesses with simpler task-level search and separates evaluation tasks from those used for selection.

**Observed:** In the authors' Terminal-Bench 2.1 setting, automated evolution did not outperform simpler test-time scaling and showed limited generalization. Certain long-horizon game settings favored task-specific evolution instead.

**Evidence:** Author-reported comparisons, not independently rerun here. These differences do not support one conclusion across all benchmarks.

**Transfer check:** Reuse the same evaluator and task split for the proposed change and the unchanged baseline with extra attempts. Track search cost and execution cost separately.
