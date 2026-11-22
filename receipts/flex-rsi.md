# Flex-RSI: Editing the improver

**Decision:** Separate the effect of offering more editable components from the effect of improving the improver.

**Intervention:** In [Flex-RSI](https://arxiv.org/abs/2611.08946), the agent can revise its harness, including mechanisms used during improvement; final evaluation remains outside those edits.

**Observed:** The [authors' overview](https://flex-rsi.github.io/blog.html) reports a comparison between permitting and disallowing harness edits. A comparison that enables multiple changes at once cannot identify which component caused any measured gain.

**Evidence:** Author-reported comparison, not independently rerun here. No isolated estimate for an edited improver is claimed.

**Transfer check:** Hold the starting executor, evaluator and total budget fixed; compare whether the edited vs. original improver produces better next-round changes on fresh tasks.
