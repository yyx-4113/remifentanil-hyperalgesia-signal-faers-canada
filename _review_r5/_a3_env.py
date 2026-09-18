import sys
print("python", sys.version.split()[0])
for mod in ("numpy", "scipy", "statsmodels"):
    try:
        m = __import__(mod)
        print(mod, getattr(m, "__version__", "?"))
    except Exception as e:
        print(mod, "MISSING", type(e).__name__)
try:
    from scipy.stats.contingency import odds_ratio
    print("scipy.stats.contingency.odds_ratio OK")
except Exception as e:
    print("odds_ratio MISSING", e)
