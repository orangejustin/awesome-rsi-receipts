---
title: 'The AI Scientist: what an outside evaluation found'
question: 'What did independent evaluators find when they ran the system themselves?'
system: 'The AI Scientist, v1 and v2'
year: 2025
changed: answer
verified: rerun
transfer: untested
---

**Claim:** A system produces complete machine-learning papers for less than USD 15 each, and an automated reviewer judges some above a conference acceptance threshold ([Lu et al.](https://arxiv.org/abs/2408.06292v3)). A second version had one of three manuscripts pass peer review at an ICLR 2025 workshop ([Yamada et al.](https://arxiv.org/abs/2504.08066v1)).

**Change:** One output at a time: a paper. The system does not change itself between papers; the authors name a closed loop as a future aim.

**Controls:** The automated reviewer was compared with human decisions on ICLR 2022 data (65% against 66% balanced accuracy). For the second version, reviewers were told some submissions might be machine-generated but not which.

**Result:** [Beel et al.](https://arxiv.org/abs/2502.14297v3) ran the first version themselves. Five of twelve proposed experiments (42%) failed because of coding errors. The novelty check classed established ideas as new. Papers had a median of five citations, and only five of 34 were from 2020 or later. Several manuscripts contained hallucinated numbers. They confirmed the cost, at USD 6 to 15 per paper, plus 3.5 hours of human involvement.

For the second version the authors' own caveats are substantial: people chose the three ideas from about forty and picked the best manuscript for each; workshops accept roughly 60 to 80% of submissions; the paper was withdrawn after review by prior agreement; and the authors found citation errors and a figure that contradicts the text.

**Verified:** Independently rerun, for the first version. The second version's result is a single reviewed submission reported by its authors.

**Open:** Neither version is evidence of self-improvement. The first version did try to change its own conditions: it issued a system call to relaunch itself and edited its code to extend the time limit.

**Try it:** Count every attempt, including the ones that failed to run, and report how many outputs a person filtered before the one you show.
