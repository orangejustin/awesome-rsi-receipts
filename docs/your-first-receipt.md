# Test one harness change on your own data

Use your own already-recorded pass/fail judgments, or collect them with your evaluator. This repo only compares the paired records; it does not run a model or grade outputs.

## 1. Decide what would make you keep it

Copy [the receipt template](../receipts/TEMPLATE.md) in your fork. Before looking at final results, write down:

- **Change:** e.g., put a catalog lookup before the answer instead of changing both search and response formatting. Record the before/after revisions.
- **Controls:** use the same task inputs, model/revision, grader, environment, and limits apart from the intended change. Keep development tasks separate from a final set the editor and selector haven't seen. Pick the pass rule in advance; for noisy systems, repeat both arms and predefine how trials become one judgment per task.
- **Budget:** name the matching unit (e.g., model calls, tokens, dollars, or elapsed time). Log search and execution costs separately. If you searched for a harness, compare the winner with an unchanged harness using extra attempts under a comparable budget and with comparable feedback. Record any mismatches.
- **Decision rule:** e.g., keep only if held-out accuracy improves, none of the critical tasks regress, and a separate task family stays flat or improves. If you change the edit based on the final results, use a fresh final set for the next decision.

## 2. Record and compare the same tasks

From your checkout:

```sh
cp examples/library-search.json my-holdout.json
```

Replace **all** synthetic rows with your own matched judgments before using the result. For example, a single row looks like this (assumed outcomes, not measurements):

```json
{"id":"catalog-017","baseline":false,"candidate":true}
```

Each file is a JSON list of these rows: one unique, non-blank string ID per task, with two JSON booleans. Don't turn missing scores into failures or silently drop them; report missing pairs and why. Once your judgments are in the file:

```sh
python3 compare.py my-holdout.json
```

Run the command separately for the final and transfer sets, and again against the extra-attempts baseline if applicable.

## 3. Keep the before/after record

Record the totals and inspect `gained` and `regressed` against your decision rule. An aggregate tie can hide a costly regression.

Then read `sign_test_p`. Only the tasks that flipped say anything about the change, and the value is how often a split at least this one-sided would turn up if every flip were a coin toss. Five gains and two regressions give 0.45: no evidence either way. Fifteen and three give 0.008. The test treats each task as one independent judgment, so settle how repeated trials become one judgment per task before you run it, and do not read a small value as proof that the gain will hold on other tasks. A pass on your holdout is not evidence of transfer unless you also checked a different task family. If the only evidence is a published aggregate, keep it in prose; don't invent paired rows.

Keep private data local or in a private checkout. Only share task IDs, judgments, traces, or excerpts you are allowed to publish. To check the comparison tool itself, run `python3 -m unittest discover -v`.
