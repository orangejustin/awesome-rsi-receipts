---
title: AlphaEvolve: results you can check yourself
question: Which of the reported results can be confirmed without trusting the authors?
system: AlphaEvolve
year: 2025
changed: program
verified: checkable
transfer: untested
---

**Claim:** An evolutionary coding agent finds a way to multiply 4×4 complex matrices with 48 scalar multiplications, matches the best known result on about 75% of over 50 open mathematics problems and improves on about 20% ([Novikov et al.](https://arxiv.org/abs/2506.13131v1)).

**Change:** A program. The system proposes edits to code and keeps what a human-written evaluator scores higher. The language models (Gemini 2.0 Flash and Pro) are fixed and are not updated by the loop.

**Controls:** Ablations on two tasks, including a version without evolution that resubmits the same initial program. A scheduling heuristic was compared with the production one in a simulator before rollout.

**Result:** The matrix result is for fields of characteristic 0, and the paper's own footnote notes that algorithms using fewer than 49 multiplications already existed in forms that are not tensor decompositions. Inside Google the paper reports 0.7% of fleet-wide compute recovered by the scheduling heuristic, a 23% faster kernel that cut Gemini training time by 1%, and a 32% speedup of a FlashAttention kernel.

**Verified:** Two different levels in one paper. The mathematical constructions are published with verification code in a [notebook](https://github.com/google-deepmind/alphaevolve_results/blob/4226acbf237ff9ad10ba7673a2af127a2d8a5971/mathematical_results.ipynb), so anyone can check them. The infrastructure numbers are internal, with no public artifact. The repository holds improved instances only and says it does not contain the code to run the system.

**Open:** Whether the system improves itself. It sped up training of the model family it runs on, but the authors write that "the gains are moderate and the feedback loops for improving the next version of AlphaEvolve are on the order of months". The method needs a problem whose solutions can be scored automatically.

**Try it:** When a result can be stated as an object (a construction, a proof, a faster function), publish the object and a checker. That moves a claim from "reported" to "checkable" at almost no cost.
