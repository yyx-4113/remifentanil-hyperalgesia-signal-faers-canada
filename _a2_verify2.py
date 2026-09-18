import math
from scipy.stats import nchypergeom_fisher
N = 20_692_687

def exact_bounds(a,b,c,d):
    # find ROR lower: smallest ROR with P(X>=a) <= 0.025
    def sf(r): return nchypergeom_fisher(a+b, a+c, a+b+c+d, r).sf(a-1)
    def cdf(r): return nchypergeom_fisher(a+b, a+c, a+b+c+d, r).cdf(a)
    # bracket lower on log scale
    lo, hi = -25.0, 5.0
    for _ in range(100):
        m = (lo+hi)/2
        if sf(math.exp(m)) > 0.025: lo = m
        else: hi = m
    lb = math.exp(lo)
    lo, hi = -5.0, 25.0
    for _ in range(100):
        m = (lo+hi)/2
        if cdf(math.exp(m)) > 0.025: hi = m
        else: lo = m
    ub = math.exp(hi)
    return lb, ub

def midp_bounds(a,b,c,d):
    def sfmid(r):
        dd = nchypergeom_fisher(a+b, a+c, a+b+c+d, r)
        return dd.sf(a-1) - 0.5*dd.pmf(a)
    def cdfmid(r):
        dd = nchypergeom_fisher(a+b, a+c, a+b+c+d, r)
        return dd.cdf(a) + 0.5*dd.pmf(a)
    lo, hi = -25.0, 5.0
    for _ in range(100):
        m=(lo+hi)/2
        if sfmid(math.exp(m)) > 0.025: lo=m
        else: hi=m
    lb=math.exp(lo)
    lo,hi=-5.0,25.0
    for _ in range(100):
        m=(lo+hi)/2
        if cdfmid(math.exp(m)) > 0.025: hi=m
        else: lo=m
    ub=math.exp(hi)
    return lb,ub

# validation: ALLODYNIA remi a=1 (manuscript exact 0.088-19.387, midP 0.173-17.153)
a,b,c = 1, 5374, 1109
d = N-a-b-c
print(f"ALLODYNIA remi a=1: exact={exact_bounds(a,b,c,d)}  midP={midp_bounds(a,b,c,d)}  (manuscript: 0.088-19.387 / 0.173-17.153)")

# HYPERPATHIA (not in sparse audit)
for name,a,b,c in [("HYPERPATHIA sufentanil a=1",1,6512,42),("HYPERPATHIA fentanyl a=2",2,121817,41)]:
    d=N-a-b-c
    ror=a*d/(b*c)
    eb=exact_bounds(a,b,c,d); mb=midp_bounds(a,b,c,d)
    print(f"{name}: ROR={ror:.3f} exact={eb[0]:.4f}-{eb[1]:.1f} midP={mb[0]:.4f}-{mb[1]:.1f}  signal_if_lower>1? {eb[0]>1}")
