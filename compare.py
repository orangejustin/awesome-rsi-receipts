"""Summarize paired pass/fail judgments for a baseline and a candidate on the same tasks.

Reports which tasks flipped and how likely that many one-sided flips would be if the
change made no difference. Does not run an agent, grade outputs or infer outcomes.
"""

import argparse
import json
from math import comb
from pathlib import Path


def sign_test(gained, regressed):
    """Exact two-sided p-value for "the flips are a coin toss" (McNemar's exact test).

    Only tasks whose judgment changed carry information about the change. Under the
    hypothesis that the candidate is no better or worse, each flip is equally likely
    to be a gain or a regression, so the count of gains is Binomial(flips, 1/2).
    """
    flips = gained + regressed
    if flips == 0:
        return 1.0
    tail = sum(comb(flips, k) for k in range(min(gained, regressed) + 1))
    return min(1.0, 2 * tail / 2 ** flips)


def compare(rows):
    if not isinstance(rows, list) or not rows:
        raise ValueError("expected a non-empty JSON list")
    groups = {label: [] for label in ("gained", "regressed", "both_pass", "both_fail")}
    cases = {
        (False, True): "gained",
        (True, False): "regressed",
        (True, True): "both_pass",
        (False, False): "both_fail",
    }
    seen = set()
    for row in rows:
        if not isinstance(row, dict) or set(row) != {"id", "baseline", "candidate"}:
            raise ValueError("each row needs exactly id, baseline and candidate")
        key = row["id"]
        if not isinstance(key, str) or not key.strip() or key in seen:
            raise ValueError("expected unique non-blank string IDs")
        seen.add(key)
        pair = row["baseline"], row["candidate"]
        if any(type(v) is not bool for v in pair):
            raise ValueError(f"{key}: judgments must be booleans")
        groups[cases[pair]].append(key)
    for group in groups.values():
        group.sort()
    return {
        "tasks": len(rows),
        "baseline_passes": len(groups["both_pass"]) + len(groups["regressed"]),
        "candidate_passes": len(groups["both_pass"]) + len(groups["gained"]),
        "net": len(groups["gained"]) - len(groups["regressed"]),
        "flips": len(groups["gained"]) + len(groups["regressed"]),
        "sign_test_p": round(sign_test(len(groups["gained"]), len(groups["regressed"])), 4),
        **groups,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("fixture", type=Path)
    args = parser.parse_args()
    try:
        result = compare(json.loads(args.fixture.read_text(encoding="utf-8")))
    except (OSError, ValueError) as exc:
        parser.error(str(exc))
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
