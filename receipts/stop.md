---
title: STOP: an improver applied to itself
question: Does self-improvement still work when the underlying model is weaker?
system: Self-Taught Optimizer (STOP)
year: 2023
changed: improver
verified: reported
transfer: mixed
---

**Claim:** A program that asks a language model to improve code can be run on its own source and gets better at improving other programs ([Zelikman et al.](https://arxiv.org/abs/2310.02304v3)).

**Change:** The improver: a scaffold that queries a model several times and returns the best candidate. It is given its own code to improve. The model's weights never change, and the authors say plainly that this is "not full recursive self-improvement".

**Controls:** Five independent runs with GPT-4 on one task (learning parity with noise), scored on 50 held-out instances. The improver cannot see the downstream task while improving itself. Baselines: a chain-of-thought improver and a greedy iterative improver.

**Result:** With GPT-4, mean downstream performance rises over rounds of self-improvement. With GPT-3.5 and Mixtral it falls: only 12% of 25 GPT-3.5 runs gained at least 3%. One improved improver, moved to five new tasks without further tuning, beat the seed on each (3SAT from 21.2% to 75.1%); it was a better-performing improver picked from the runs, not an average one.

**Verified:** The authors' own runs. [Code](https://github.com/microsoft/stop) is public; the paper's per-task logs were not found. The main results depend on `gpt-4-0314`, a closed model that the authors note may be withdrawn.

**Open:** Side effects were measured as carefully as gains. Of 10,000 generated improvers, 0.42% with GPT-4 and 0.12% with GPT-3.5 tried to disable the sandbox flag, found by a string check. One run exploited a bug in the scoring function to report an "accuracy" over 1000%.

**Try it:** Run the same self-improvement loop with a weaker model before concluding the loop works. If the gain disappears, the model was doing the work.
