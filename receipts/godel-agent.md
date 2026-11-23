---
title: 'Gödel Agent: rewriting the routine that rewrites'
question: 'How often does an agent that can edit its own improvement loop end up worse than it started?'
system: 'Gödel Agent'
year: 2024
changed: improver
verified: reported
transfer: untested
---

**Claim:** An agent that modifies its own running code, including the routine that performs the modification, reaches results "optimal or comparable" to Meta Agent Search and 11% higher on MGSM, for about USD 15 against USD 300 ([Yin et al.](https://arxiv.org/abs/2410.04444v4)).

**Change:** The agent's code in memory, patched at runtime. The main loop is a recursive function, so the improvement logic is itself editable.

**Controls:** A random-sampling control on MGSM (30 runs stay around 30%). The baseline numbers are taken from the ADAS paper, not rerun. GPT-4o drives the agent; the optimised policy is evaluated with GPT-3.5.

**Result:** Across 100 optimisation trials on MGSM, 4% terminated unexpectedly, 92% had a temporary drop along the way, and 14% ended below the starting policy. Terminations happened when the agent modified its own recursive improvement module. In an unconstrained variant, the large gains came from the agent deciding to call GPT-4o for help.

**Verified:** The authors' own runs. [Code](https://github.com/Arvid-pku/Godel_Agent) is public.

**Open:** No test of whether an optimised policy carries to another task or model. The comparison with ADAS uses numbers from another paper's setup. The authors present the experiments as a demonstration that the approach is feasible.

**Try it:** Count endings, not just the best run. Report the share of runs that finish below the start, and treat "the agent called a stronger model" as a different intervention.
