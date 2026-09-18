import math
from scipy.stats import nchypergeom_fisher
N = 20_692_687

def exact_bounds(a,b,c,d):
    M, n, succ = a+b+c+d, a+b, a+c
    def sf(r): return nchypergeom_fisher(M, n, succ, r).sf(a-1)
    def cdf(r): return nchypergeom_fisher(M, n, succ, r).cdf(a)
    lo, hi = -25.0, 8.0
    for _ in range(120):
        m=(lo+hi)/2
        if sf(math.exp(m)) > 0.025: lo=m
        else: hi=m
    lb=math.exp(lo)
    lo, hi = -8.0, 25.0
    for _ in range(120):
        m=(lo+hi)/2
        if cdf(math.exp(m)) > 0.025: hi=m
        else: lo=m
    ub=math.exp(hi)
    return lb, ub

def midp_bounds(a,b,c,d):
    M,n,succ = a+b+c+d, a+b, a+c
    def sfmid(r):
        dd=nchypergeom_fisher(M,n,succ,r); return dd.sf(a-1)-0.5*dd.pmf(a)
    def cdfmid(r):
        dd=nchypergeom_fisher(M,n,succ,r); return dd.cdf(a)+0.5*dd.pmf(a)
    lo,hi=-25.0,8.0
    for _ in range(120):
        m=(lo+hi)/2
        if sfmid(math.exp(m))>0.025: lo=m
        else: hi=m
    lb=math.exp(lo)
    lo,hi=-8.0,25.0
    for _ in range(120):
        m=(lo+hi)/2
        if cdfmid(math.exp(m))>0.025: hi=m
        else: lo=m
    ub=math.exp(hi)
    return lb,ub

val = exact_bounds(1,5374,1109,N-1-5374-1109)
print(f"VALIDATE ALLODYNIA remi a=1 exact={val[0]:.4f}-{val[1]:.3f}  (manuscript 0.088-19.387)")
vmid = midp_bounds(1,5374,1109,N-1-5374-1109)
print(f"  midP={vmid[0]:.4f}-{vmid[1]:.3f}  (manuscript 0.173-17.153)")

# HYPERAESTHESIA remi a=10 (manuscript exact 2.266-8.710)
eb=exact_bounds(10,5365,8151,N-10-5365-8151)
print(f"VALIDATE HYPERAESTHESIA remi a=10 exact={eb[0]:.3f}-{eb[1]:.3f}  (manuscript 2.266-8.710)")

for name,a,b,c in [("HYPERPATHIA sufentanil a=1",1,6512,42),("HYPERPATHIA fentanyl a=2",2,121817,41)]:
    d=N-a-b-c; ror=a*d/(b*c)
    eb=exact_bounds(a,b,c,d); mb=midp_bounds(a,b,c,d)
    print(f"{name}: ROR={ror:.3f} exact={eb[0]:.4f}-{eb[1]:.2f} midP={mb[0]:.4f}-{mb[1]:.2f}  lower>1? {eb[0]>1}")
