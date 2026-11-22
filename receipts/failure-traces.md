---
title: Notes learned from failures, against the same search without them
question: How much of the gain comes from seeing the failures, and how much from simply trying and keeping what scores better?
system: Agent Self-Improvement with Frozen Weights
year: 2026
changed: harness
verified: reported
transfer: failed
---

**Claim:** An agent with frozen weights can improve by writing itself notes from its own failed attempts. [Mitra et al.](https://arxiv.org/abs/2611.11342v2) measure what the failures add.

**Change:** Notes placed in the agent's harness. The weights of the model do not change.

**Controls:** The same note-writing process run with the mistakes withheld, so the only difference is whether the writer sees the failure traces. A blind audit of the test items. One open 9B model with a larger teacher.

**Result:** From the abstract: notes based on the agent's mistakes "improved accuracy by 4.0 percentage points over notes from the same process with the mistakes withheld", and that process alone, "trying and keeping better-scoring notes, reached about 60% of the total improvement". In full customer-service conversations the same notes "showed no demonstrated improvement", and in an exploratory comparison a neutral note with no procedure scored higher than the learned lessons. The blind audit "judged 146 of 240 tool-use test items defective".

**Verified:** The authors' own experiments, read from the abstract only and not rerun here.

**Open:** One model and one teacher. The authors describe several lessons as still awaiting tests on new data. If most test items are defective, the size of every gain measured on them is uncertain.

**Try it:** Run your improvement loop twice with the same budget: once showing the editor the failures, once hiding them. The difference is what the feedback is worth. Then have someone who has not seen the results audit a sample of the test items.
