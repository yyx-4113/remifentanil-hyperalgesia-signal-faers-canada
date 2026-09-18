"""Round-7 (R-3): add the two HYPERPATHIA sparse cells to 15_sparse_intervals.csv.

Why these two cells: Table 2 originally marked HYPERPATHIA fentanyl (a=2) and sufentanil
(a=1) with a signal star, yet neither appeared in the sparse-interval audit, and the
a>=3 floor applied only to the ROR clause of the criterion. With the floor applied to every
clause both lose their star, but their intervals still have to be on the record so the
reader can see what they do at those counts.

2x2 cells derived from 01_faers_results.csv (HYPERPATHIA PT_total = 43), the Table 1 cohort
totals and the grand total N = 20 692 687.

SELF-CHECK: the same routines are run against the existing ALLODYNIA row before anything is
written; if they do not reproduce 0.088-19.387 (exact) and 0.173-17.153 (mid-P) the script
aborts. That guards the lower/upper root mapping, which is easy to invert.
"""
import csv
import math
from scipy.stats import nchypergeom_fisher

N = 20_692_687
PATH = "15_sparse_intervals.csv"


def woolf(a, b, c, d):
    ror = a * d / (b * c)
    se = math.sqrt(1 / a + 1 / b + 1 / c + 1 / d)
    return ror, math.exp(math.log(ror) - 1.96 * se), math.exp(math.log(ror) + 1.96 * se)


def haldane(a, b, c, d):
    return woolf(a + 0.5, b + 0.5, c + 0.5, d + 0.5)[1:]


def _bisect(f, xa, xb, tol=1e-10, maxiter=400):
    """Root of a monotone f between xa and xb; f(xa) and f(xb) must straddle zero."""
    fa = f(xa)
    fb = f(xb)
    if fa * fb > 0:
        raise RuntimeError(f"no sign change on [{xa}, {xb}]: f({xa})={fa}, f({xb})={fb}")
    for _ in range(maxiter):
        xc = 0.5 * (xa + xb)
        fc = f(xc)
        if abs(fc) < tol or (xb - xa) < tol:
            return xc
        if fa * fc <= 0:
            xb, fb = xc, fc
        else:
            xa, fa = xc, fc
    return 0.5 * (xa + xb)


def _tails(a, b, c, d, odds):
    """P(X >= a) and P(X <= a) under the non-central hypergeometric law."""
    dist = nchypergeom_fisher(a + b + c + d, a + c, a + b, odds)
    return dist.sf(a - 1), dist.cdf(a)


def exact_ci(a, b, c, d):
    # X shifts RIGHT as odds rise, so P(X >= a) is increasing in odds -> its 0.025 root
    # is the LOWER bound and P(X <= a)'s 0.025 root is the UPPER bound. Getting this
    # backwards silently swaps the interval (it happened once already).
    lo = _bisect(lambda o: _tails(a, b, c, d, o)[0] - 0.025, 1e-9, 1e6)
    hi = _bisect(lambda o: _tails(a, b, c, d, o)[1] - 0.025, 1e-9, 1e9)
    return lo, hi


def midP_ci(a, b, c, d):
    def upper(odds):
        dist = nchypergeom_fisher(a + b + c + d, a + c, a + b, odds)
        return dist.sf(a - 1) - 0.5 * dist.pmf(a) - 0.025

    def lower(odds):
        dist = nchypergeom_fisher(a + b + c + d, a + c, a + b, odds)
        return dist.cdf(a) - 0.5 * dist.pmf(a) - 0.025

    return _bisect(upper, 1e-9, 1e6), _bisect(lower, 1e-9, 1e9)


def make_row(label, a, b, c, d):
    ror, wlo, whi = woolf(a, b, c, d)
    elo, ehi = exact_ci(a, b, c, d)
    mlo, mhi = midP_ci(a, b, c, d)
    hlo, hhi = haldane(a, b, c, d)
    return {
        "case": label,
        "a": a, "b": b, "c": c, "d": d,
        "ROR": f"{ror:.4f}",
        "woolf_CI": f"{wlo:.3f}-{whi:.3f}",
        "exact_conditional_CI": f"{elo:.3f}-{ehi:.3f}",
        "midP_CI": f"{mlo:.3f}-{mhi:.3f}",
        "haldane_CI": f"{hlo:.3f}-{hhi:.3f}",
        "woolf_lower": f"{wlo:.3f}",
        "exact_lower": f"{elo:.3f}",
        "haldane_lower": f"{hlo:.3f}",
        "woolf_declares_signal": "yes" if wlo > 1 else "no",
        "exact_declares_signal": "yes" if elo > 1 else "no",
    }


# --- self-check: reproduce the published ALLODYNIA row -------------------------
_chk = make_row("ALLODYNIA check", 1, 5374, 1109, 20_686_203)
if _chk["exact_conditional_CI"] != "0.088-19.387" or _chk["midP_CI"] != "0.173-17.153":
    raise SystemExit(
        f"self-check failed: exact={_chk['exact_conditional_CI']} "
        f"(expected 0.088-19.387), midP={_chk['midP_CI']} (expected 0.173-17.153)"
    )
print("self-check OK: ALLODYNIA reproduced ->", _chk["exact_conditional_CI"], _chk["midP_CI"])

# --- the two new cells --------------------------------------------------------
new_rows = [
    make_row("HYPERPATHIA fentanyl, whole corpus (a=2)", 2, 121_819 - 2, 43 - 2,
             N - 121_819 - 43 + 2),
    make_row("HYPERPATHIA sufentanil, whole corpus (a=1)", 1, 6_513 - 1, 43 - 1,
             N - 6_513 - 43 + 1),
]
for r in new_rows:
    assert r["a"] + r["b"] + r["c"] + r["d"] == N, r
    print(f"{r['case']:>46}  ROR {r['ROR']:>9}  woolf {r['woolf_CI']:>14}  "
          f"exact {r['exact_conditional_CI']:>16}  midP {r['midP_CI']:>16}  "
          f"haldane {r['haldane_CI']:>16}")

# --- rewrite the CSV, keeping every existing row and its order ----------------
with open(PATH, encoding="utf-8-sig", newline="") as f:
    raw_fields = next(csv.reader(f))
    rows = list(csv.reader(f))
fieldnames = [k for k in raw_fields if k]  # a stray trailing comma leaves an empty key
index = {name: i for i, name in enumerate(raw_fields) if name}
dict_rows = [{k: r[index[k]] for k in fieldnames} for r in rows if r]
kept = [r for r in dict_rows if "HYPERPATHIA" not in r["case"]]
# the two signalled HYPERPATHIA cells sit above the other terms, matching the order
# in which they are discussed (Table 2 footnote -> Appendix A1.4)
out = new_rows + kept

with open(PATH, "w", encoding="utf-8-sig", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_MINIMAL,
                       lineterminator="\n")
    w.writeheader()
    for r in out:
        w.writerow({k: r.get(k, "") for k in fieldnames})

print(f"\nwrote {len(out)} rows to {PATH}: "
      f"{', '.join(r['case'] for r in out)}")
