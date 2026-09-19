# -*- coding: utf-8 -*-
"""Round-8, item R6-20: the head-to-head ratio recomputed as a direct two-drug
comparison.

The published RORR divides remifentanil's marginal reporting odds ratio by the
comparator's, each computed in its own 2x2 table against the whole-corpus
remainder (section 2.4).  That estimator is inflated when the two cohorts
overlap, because a report naming both opioids enters both *a* cells while the
shared remainder is counted twice conceptually.  The alternative asked for by
the design reviewer is the direct two-drug odds ratio on a single 2x2 table
whose two rows are the two cohorts:

        OR = [ a_r / (n_r - a_r) ] / [ a_c / (n_c - a_c) ]

with the Woolf interval on the log scale.  It uses the same cell counts that
are already published, so it is a re-expression of the same data rather than a
new query.  Both are written out side by side so the reader can see how much of
the published ratio is an artefact of the shared remainder.

Source: 01_faers_results.csv (authoritative per-term counts) and the diagonal of
11_overlap_matrix.csv (cohort sizes).  Writes 23_direct_headtohead.csv.
"""
from __future__ import annotations

import csv
import io
import math
import os

HERE = os.path.dirname(os.path.abspath(__file__))
P = lambda *a: os.path.join(HERE, *a)

CSV_IN = P("01_faers_results.csv")
MATRIX = P("11_overlap_matrix.csv")
CSV_OUT = P("23_direct_headtohead.csv")

COMPARATORS = ["FENTANYL", "SUFENTANIL", "MORPHINE"]


def read_cohorts() -> dict[str, int]:
    """Cohort sizes from the diagonal (cohort_n) column of the overlap matrix."""
    rows = list(csv.DictReader(io.open(MATRIX, encoding="utf-8-sig")))
    out = {r["drug"].strip(): int(r["cohort_n"]) for r in rows}
    missing = [d for d in ("REMIFENTANIL",) + tuple(COMPARATORS) if d not in out]
    if missing:
        raise SystemExit("cohort sizes not found in %s: %s" % (MATRIX, missing))
    return out


def direct_or(a_r: int, n_r: int, a_c: int, n_c: int):
    """Direct two-drug odds ratio, Woolf interval. None if a cell is empty."""
    b_r, b_c = n_r - a_r, n_c - a_c
    if min(a_r, b_r, a_c, b_c) <= 0:
        return None
    orv = (a_r * b_c) / (b_r * a_c)
    se = math.sqrt(1 / a_r + 1 / b_r + 1 / a_c + 1 / b_c)
    lo = math.exp(math.log(orv) - 1.96 * se)
    hi = math.exp(math.log(orv) + 1.96 * se)
    return orv, lo, hi


def num(v: str):
    v = (v or "").strip()
    return int(float(v)) if v else None


def main() -> int:
    cohorts = read_cohorts()
    n_r = cohorts["REMIFENTANIL"]

    src = list(csv.DictReader(io.open(CSV_IN, encoding="utf-8-sig")))
    rows, moved = [], []
    for rec in src:
        a_r = num(rec["REMIFENTANIL_a"]) or 0
        for comp in COMPARATORS:
            a_c = num(rec[comp + "_a"]) or 0
            n_c = cohorts[comp]
            published = (rec.get("RORR_REMI_vs_" + comp) or "").strip()
            est = direct_or(a_r, n_r, a_c, n_c)
            row = {
                "preferred_term": rec["PT"],
                "comparator": comp,
                "a_remifentanil": a_r,
                "n_remifentanil": n_r,
                "a_comparator": a_c,
                "n_comparator": n_c,
                "direct_OR": "" if est is None else round(est[0], 4),
                "direct_CI": "" if est is None else "%.2f-%.2f" % (est[1], est[2]),
                "published_RORR": published,
                "direct_minus_published_ratio": (
                    "" if (est is None or not published)
                    else round(est[0] / float(published), 4)
                ),
            }
            rows.append(row)
            if est is not None and published:
                moved.append((rec["PT"], comp, est[0], float(published)))

    with io.open(CSV_OUT, "w", encoding="utf-8-sig", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)

    print("wrote", os.path.basename(CSV_OUT), "--", len(rows), "cells")
    print("%-26s %-11s %10s %10s %8s" % ("term", "comparator", "direct", "published", "d/p"))
    for pt, comp, d, pub in moved:
        print("%-26s %-11s %10.4f %10.4f %8.3f" % (pt, comp, d, pub, d / pub))

    # Which published ratios sit above one and what the direct estimator says.
    above = [(pt, comp, d, pub) for pt, comp, d, pub in moved if pub > 1]
    print("\npublished ratios above one: %d" % len(above))
    for pt, comp, d, pub in above:
        print("   %-26s vs %-10s published %.3f -> direct %.3f" % (pt, comp, pub, d))

    # Direction agreement: does the direct estimator preserve every sign?
    flip = [(pt, comp, d, pub) for pt, comp, d, pub in moved
            if (d > 1) != (pub > 1)]
    print("\ncells where the two estimators disagree about being above one: %d" % len(flip))
    for pt, comp, d, pub in flip:
        print("   %-26s vs %-10s published %.3f, direct %.3f" % (pt, comp, pub, d))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
