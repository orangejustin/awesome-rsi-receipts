---
title: 'Darwin Gödel Machine: 20% to 50% on a subset'
question: 'How much of the gain survives on the full benchmark, another model or another benchmark?'
system: 'Darwin Gödel Machine'
year: 2025
changed: harness
verified: reported
transfer: mixed
---

**Claim:** A coding agent that rewrites its own code improves from 20.0% to 50.0% on SWE-bench and from 14.2% to 30.7% on Polyglot ([Zhang et al.](https://arxiv.org/abs/2505.22954v3)).

**Change:** The agent's own code repository: tools, prompts and workflow. The foundation models are frozen, and the outer loop that keeps an archive and picks parents is fixed and written by people.

**Controls:** Two ablations: a fixed meta agent that never improves itself, and no archive. The paper says gains "taper off quickly" in the first and that both end below the full method; their final scores appear only in figures. Run-to-run spread is reported for Polyglot only (three runs).

**Result:** The 50.0% is on a staged subset of SWE-bench Verified (10, then 60, then 200 tasks), not all 500. On Polyglot the in-loop subset of 50 tasks went from 14.0% to 38.0%, and the full benchmark from 14.2% to 30.7%. One SWE-bench run took 80 iterations, about two weeks and about USD 22,000.

Carrying the discovered agent elsewhere: on SWE-bench it lifts o3-mini from 23.0% to 33.0% and Claude 3.7 Sonnet from 19.0% to 59.5%. On Polyglot the lift from swapping models is small (32.0% to 33.3%, 35.6% to 36.8%). The SWE-bench-evolved agent scores 28.9% on Polyglot against a 14.2% start.

**Verified:** The authors' own runs. The [repository](https://github.com/jennyzzt/dgm) links the foundation-model output logs, which is what made the [later reanalysis](failure-feedback.md) possible. The [Huxley-Gödel Machine authors](https://arxiv.org/abs/2510.21614v3) reran the method with different models and a different budget, so their 53.3% is not a replication of this number.

**Open:** The number of independent SWE-bench runs is not stated. The paper also documents the agent gaming its objective: in a test of a hallucination detector, one agent removed the logging markers the detector relied on instead of fixing the behaviour.

**Try it:** If you report a search result on a subset, rerun the selected agent once on the full set and on a second model before quoting it.
