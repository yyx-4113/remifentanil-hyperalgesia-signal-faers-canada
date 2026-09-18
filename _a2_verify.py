import math, csv
try:
    from scipy.stats import nchypergeom_fisher
    HAVE_SCIPY = True
except Exception as e:
    HAVE_SCIPY = False
    print("scipy not available:", e)

N = 20_692_687

def woolf(a,b,c,d):
    ror = a*d/(b*c)
    se = math.sqrt(1/a+1/b+1/c+1/d)
    ln = math.log(ror)
    return ror, (math.exp(ln-1.96*se), math.exp(ln+1.96*se))

def exact_conditional(a,b,c,d):
    # non-central hypergeometric, both margins fixed; solve for ROR
    lo, hi = 1e-9, 1e9
    # Brent on ln ROR via nchypergeom_fisher sf/CDF
    def tail_at(ror):
        # P(X >= a) for lower? We want lower bound = smallest ROR with P(X>=a) <= 0.025
        dist = nchypergeom_fisher(a+b, a+c, a+b+c+d, ror)
        return dist.sf(a-1)  # P(X>=a)
    def tail_at_upper(ror):
        dist = nchypergeom_fisher(a+b, a+c, a+b+c+d, ror)
        return dist.cdf(a)    # P(X<=a)
    # lower bound
    lo, hi = 1e-9, 1e6
    for _ in range(80):
        mid = math.sqrt(lo*hi)
        if tail_at(mid) > 0.025:
            lo = mid
        else:
            hi = mid
    lb = lo
    lo, hi = 1e-9, 1e6
    for _ in range(80):
        mid = math.sqrt(lo*hi)
        if tail_at_upper(mid) > 0.025:
            hi = mid
        else:
            lo = mid
    ub = hi
    return lb, ub

def midp(a,b,c,d):
    ror = a*d/(b*c)
    dist = nchypergeom_fisher(a+b, a+c, a+b+c+d, ror)
    # approximate mid-P bounds by nudging ROR until sf(a-1)-0.5*P(X=a)=0.025 etc.
    def midp_lower_tail(r):
        dd = nchypergeom_fisher(a+b, a+c, a+b+c+d, r)
        return dd.sf(a-1) - 0.5*dd.pmf(a)
    def midp_upper_tail(r):
        dd = nchypergeom_fisher(a+b, a+c, a+b+c+d, r)
        return dd.cdf(a) + 0.5*dd.pmf(a)
    lo, hi = 1e-9, 1e6
    for _ in range(80):
        mid = math.sqrt(lo*hi)
        if midp_lower_tail(mid) > 0.025: lo = mid
        else: hi = mid
    lb = lo
    lo, hi = 1e-9, 1e6
    for _ in range(80):
        mid = math.sqrt(lo*hi)
        if midp_upper_tail(mid) > 0.025: hi = mid
        else: lo = mid
    ub = hi
    return lb, ub

print("=== HYPERPATHIA sparse signals (NOT in 15_sparse_intervals.csv) ===")
for name,a,b,c in [("HYPERPATHIA sufentanil a=1",1,6512,42),
                    ("HYPERPATHIA fentanyl a=2",2,121817,41)]:
    d = N-a-b-c
    ror,wc = woolf(a,b,c,d)
    print(f"{name}: ROR={ror:.3f}, Woolf={wc[0]:.3f}-{wc[1]:.3f}", end="")
    if HAVE_SCIPY:
        ec = exact_conditional(a,b,c,d)
        mp = midp(a,b,c,d)
        print(f", exact={ec[0]:.3f}-{ec[1]:.3f}, midP={mp[0]:.3f}-{mp[1]:.3f}", end="")
        exc1 = ec[0] > 1
        print(f"  -> exact lower>1? {exc1}  (Table2 marks *signal*)")
    else:
        print()

print()
print("=== HYPERAESTHESIA leave-2024 verification ===")
# correct spec: drop 2024 from whole corpus. 19_leave2024 row2: a=2, cohort=4927, term_total=7824, N=19373581
a,b,c = 2,4927-2,7824-2
d = 19373581-a-b-c
ror,wc = woolf(a,b,c,d)
print(f"drop-2024: a={a} cohort={4927} term_total={7824} N={19373581} ROR={ror:.4f} CI={wc[0]:.4f}-{wc[1]:.4f} (file: 1.0051, 0.2513-4.0209)")
# 2015-2023 window (mis-spec): 04 file a=1 cohort=3798 ROR=0.701
a,b,c = 1,3798-1,4658-1
d = 12401440-a-b-c
ror,wc = woolf(a,b,c,d)
print(f"2015-2023 window: a={a} cohort={3798} term_total={4658} N={12401440} ROR={ror:.4f} CI={wc[0]:.4f}-{wc[1]:.4f} (file 04: 0.701, 0.099-4.978)")
