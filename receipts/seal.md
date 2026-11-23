---
title: 'SEAL: a model that writes its own training data'
question: 'What happens to earlier knowledge as self-generated updates accumulate?'
system: 'Self-Adapting Language Models (SEAL)'
year: 2025
changed: weights
verified: reported
transfer: untested
---

**Claim:** A model that generates its own fine-tuning data and update instructions can make lasting improvements to its weights ([Zweiger et al.](https://arxiv.org/html/2506.10943v2)).

**Change:** The model's weights. A reinforcement-learning loop rewards the self-generated edits whose resulting update performs better.

**Controls:** Self-edits from the trained policy against self-edits without that training. Tasks are small in scale: question answering without the passage, and a subset of ARC.

**Result:** Incorporating new knowledge without the passage rose "from 33.5% to 47.0%". On the ARC subset the trained self-edits reached 72.5% against 20% without that training. As edits accumulate, "performance on earlier tasks gradually declines", which the authors read as the method being "still susceptible to catastrophic forgetting".

**Verified:** The authors' own experiments, not rerun here. [Code](https://github.com/Continual-Intelligence/SEAL) is public.

**Open:** Whether the gains survive at larger scale, and whether repeated rounds add up or wash out. The reported forgetting points to the second.

**Try it:** After each self-generated update, re-score every earlier task, not only the new one. Plot both lines.
