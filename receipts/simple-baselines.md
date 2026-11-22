---
title: Code evolution against simple baselines
question: Is the search method doing the work, or the way the problem was set up?
system: Simple Baselines are Competitive with Code Evolution
year: 2026
changed: program
verified: reported
transfer: untested
---

**Claim:** Elaborate code-evolution pipelines in the style of AlphaEvolve are often presented as the reason a new result was found. [Gideoni et al.](https://arxiv.org/abs/2602.16805v2) test two simple baselines against them.

**Change:** No new system. The study holds the problem formulation fixed and swaps the search procedure.

**Controls:** The same search space and budget for simple and complex methods, across the domains the paper covers. The exact baseline definitions and per-domain budgets are in the paper body, which we have not read in full.

**Result:** From the abstract: "the baselines match or outperform existing methods across all domains". On mathematical bounds, "the search space matters far more than the exact search algorithm, with both simple and complex methods performing similarly given the same search space". For agent scaffolds, noisy evaluations led every automated search method to pick scaffolds worse than a simple majority vote.

**Verified:** The authors' own comparisons, read from the abstract only and not rerun here.

**Open:** This does not question the constructions that evolution systems produced, which can be checked directly (see [AlphaEvolve](alphaevolve.md)). It questions what deserves the credit. It is a critique across pipelines, not a replication of any single one.

**Try it:** Keep your problem formulation and evaluator, replace the search with the plainest loop you can write (sample, score, keep the best), and give it the same number of model calls.
