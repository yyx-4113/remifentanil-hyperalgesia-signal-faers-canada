# -*- coding: utf-8 -*-
"""
Round-6 offline products: build the result files that need no further network access.
Writes:
  11_overlap_matrix.csv              FAERS 4x4 report-level overlap (from _a5_overlap_faers.json)
  cv/cv_indication_strata.csv        Table 5 source: Canada indication-stratified head-to-head
  cv/cv_depth_strata.csv             Table 6 source: Canada reporting-depth MH stratification
  15_sparse_intervals.csv            Sparse-cell interval comparison (Woolf / exact / Haldane / mid-P)
  16_year_trend.csv                  Year-wise counts + Poisson-style trend test
"""
import json, csv, os, math
from collections import OrderedDict
import numpy as np
from scipy import stats

HERE = os.path.dirname(os.path.abspath(__file__))
def P(*a): return os.path.join(HERE, *a)
def load(f): return json.load(open(P(f), encoding='utf-8'))

DRUGS = ['REMIFENTANIL', 'FENTANYL', 'SUFENTANIL', 'MORPHINE']
SHORT = {'REMIFENTANIL': 'remifentanil', 'FENTANYL': 'fentanyl',
         'SUFENTANIL': 'sufentanil', 'MORPHINE': 'morphine'}

# ---------------------------------------------------------------- 1. overlap matrix
ov = load('_a5_overlap_faers.json')
KEYS = {'REMI': 'REMIFENTANIL', 'FEN': 'FENTANYL', 'SUF': 'SUFENTANIL', 'MOR': 'MORPHINE'}
n = {'REMIFENTANIL': ov['REMI'], 'FENTANYL': ov['FEN'], 'SUFENTANIL': ov['SUF'], 'MORPHINE': ov['MOR']}
rows = []
for a in DRUGS:
    ka = [k for k, v in KEYS.items() if v == a][0]
    r = OrderedDict()
    r['drug'] = a
    r['cohort_n'] = n[a]
    for b in DRUGS:
        kb = [k for k, v in KEYS.items() if v == b][0]
        if a == b:
            r['overlap_%s' % SHORT[b]] = n[a]
        else:
            pair = '&'.join(sorted([ka, kb], key=lambda x: ['REMI', 'FEN', 'SUF', 'MOR'].index(x)))
            r['overlap_%s' % SHORT[b]] = ov[pair]
    rows.append(r)
with open(P('11_overlap_matrix.csv'), 'w', newline='', encoding='utf-8-sig') as fh:
    w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
    w.writeheader(); w.writerows(rows)
print('[11] overlap matrix written', flush=True)
print('    union of the four cohorts = %d' % 0 if False else '', flush=True)
for k in ('REMI&FEN', 'REMI&SUF', 'REMI&MOR', 'FEN&SUF', 'FEN&MOR', 'SUF&MOR',
          'REMI&FEN&SUF', 'REMI&FEN&MOR', 'REMI&SUF&MOR', 'FEN&SUF&MOR', 'ALL4'):
    if k in ov:
        print('    %-12s = %d' % (k, ov[k]), flush=True)
print('    remifentanil reports also naming fentanyl: %.1f%%' % (100 * ov['REMI&FEN'] / ov['REMI']), flush=True)

# ------------------------------------------- 2. Canada indication strata  (Table 5)
ind = load('_a5_cv_indication_strata.json')
STRATA = [('ALL', 'All reports'), ('ANAESTHESIA_ANY', 'Perioperative anaesthesia indication'),
          ('PAIN_INDICATION', 'Pain indication')]
PTS = ['PAIN', 'DRUG INEFFECTIVE', 'VOMITING', 'NAUSEA', 'HYPERAESTHESIA']
out = []
for skey, slabel in STRATA:
    blk = ind['strata'][skey]
    for pt in PTS:
        e = blk.get(pt)
        if e is None:
            continue
        row = OrderedDict()
        row['stratum'] = slabel
        row['stratum_key'] = skey
        row['preferred_term'] = pt
        for d in DRUGS:
            row['n_%s' % SHORT[d]] = blk['n'][d]
            row['a_%s' % SHORT[d]] = e['a'][d]
        for cmp_, lab in (('FEN', 'fentanyl'), ('MOR', 'morphine')):
            v, ci = e.get('vs_%s' % cmp_), e.get('vs_%s_CI' % cmp_)
            row['RORR_vs_%s' % lab] = '' if v is None else round(v, 3)
            row['RORR_vs_%s_CI' % lab] = '' if ci is None else '%.3f-%.3f' % (ci[0], ci[1])
        out.append(row)
with open(P('cv', 'cv_indication_strata.csv'), 'w', newline='', encoding='utf-8-sig') as fh:
    w = csv.DictWriter(fh, fieldnames=list(out[0].keys()))
    w.writeheader(); w.writerows(out)
print('[cv] cv_indication_strata.csv written (%d rows)' % len(out), flush=True)

# --------------------------------------------- 3. depth strata (Table 6 source)
dep = load('_a5_depth_strata.json')
tpc = dep['terms_per_cohort']
mh = dep['mh']
norm = dep['normalised']
rrp = load('_a5_reactions_per_report.json')['reactions_per_report']
rows = []
for pt in ['PAIN', 'DRUG INEFFECTIVE', 'VOMITING', 'NAUSEA', 'HYPERAESTHESIA']:
    r = OrderedDict()
    r['preferred_term'] = pt
    for d in DRUGS:
        r['terms_per_report_%s' % SHORT[d]] = tpc[d]['terms_per_report']
        r['pct_single_term_%s' % SHORT[d]] = rrp[d]['pct_reports_with_1']
    for cmp_, lab in (('FENTANYL', 'fentanyl'), ('MORPHINE', 'morphine')):
        m = mh.get('%s|%s' % (pt, cmp_))
        if m and m.get('mh_RORR') is not None:
            r['MH_RORR_vs_%s' % lab] = m['mh_RORR']
            r['MH_RORR_vs_%s_CI' % lab] = '%.3f-%.3f' % (m['ci'][0], m['ci'][1])
        else:
            r['MH_RORR_vs_%s' % lab] = ''
            r['MH_RORR_vs_%s_CI' % lab] = ''
    nx = norm.get(pt)
    if nx:
        r['crude_RORR_vs_fentanyl'] = nx['author_RORR_vs_FEN']
        r['crude_RORR_vs_morphine'] = nx['author_RORR_vs_MOR']
        r['term_share_ratio_vs_fentanyl'] = nx['share_ratio_vs_FEN']
        r['term_share_ratio_vs_morphine'] = nx['share_ratio_vs_MOR']
        for d in DRUGS:
            r['share_pct_%s' % SHORT[d]] = nx['share_pct'][d]
    rows.append(r)
with open(P('cv', 'cv_depth_strata.csv'), 'w', newline='', encoding='utf-8-sig') as fh:
    w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
    w.writeheader(); w.writerows(rows)
print('[cv] cv_depth_strata.csv written (%d rows)' % len(rows), flush=True)

# ------------------------------------------- 4. sparse-cell interval comparison
def ror(a, b, c, d): return (a*d)/(b*c)

def woolf(a, b, c, d):
    if min(a, b, c, d) == 0: return (float('nan'), float('nan'))
    se = math.sqrt(1/a + 1/b + 1/c + 1/d)
    return (math.exp(math.log(ror(a, b, c, d)) - 1.96*se), math.exp(math.log(ror(a, b, c, d)) + 1.96*se))

def haldane(a, b, c, d):
    a2, b2, c2, d2 = a+.5, b+.5, c+.5, d+.5
    se = math.sqrt(1/a2 + 1/b2 + 1/c2 + 1/d2)
    return (math.exp(math.log(ror(a2, b2, c2, d2)) - 1.96*se), math.exp(math.log(ror(a2, b2, c2, d2)) + 1.96*se))

def _bisect(f, lo, hi):
    flo, fhi = f(lo), f(hi)
    if flo * fhi > 0:
        raise ValueError('no bracket for %r' % f)
    for _ in range(300):
        m = math.sqrt(lo*hi)
        fm = f(m)
        if flo * fm <= 0:
            hi, fhi = m, fm
        else:
            lo, flo = m, fm
    return math.sqrt(lo*hi)

def cond_ci(a, b, c, d, midp=False, alpha=0.05):
    """Exact conditional (non-central hypergeometric) interval; mid-P if asked.
    The lower bound is fixed by the right tail P(X >= a), the upper by the left tail P(X <= a)."""
    from scipy.stats import nchypergeom_fisher as nh
    M, nrow, ncol = a+b+c+d, a+b, a+c
    def left(orv):        # P(X <= a), decreasing in OR
        v = nh.cdf(a, M, nrow, ncol, orv)
        if midp: v -= 0.5*nh.pmf(a, M, nrow, ncol, orv)
        return v
    def right(orv):       # P(X >= a), increasing in OR
        v = nh.sf(a-1, M, nrow, ncol, orv) if a > 0 else 1.0
        if midp: v -= 0.5*nh.pmf(a, M, nrow, ncol, orv)
        return v
    from scipy.optimize import brentq
    # lower bound: an OR this small would put the observed a in the upper 2.5% tail
    lo = brentq(lambda o: right(o) - alpha/2, 1e-8, 1e9)
    # upper bound: an OR this large would put the observed a in the lower 2.5% tail
    hi = brentq(lambda o: left(o) - alpha/2, 1e-8, 1e9)
    return (lo, hi)

cases = [
    ('HYPERAESTHESIA remifentanil, whole corpus (a=10)', 10, 5365, 8151, 20684061),
    ('ALLODYNIA remifentanil, whole corpus (a=1)', 1, 5374, 1109, 20686203),
    ('HYPERAESTHESIA remifentanil, 2024 only (a=8)', 8, 440, 329, 1318329),
    ('PAIN remifentanil, whole corpus (a=23)', 23, 5352, 607153, 20085559),
]
rows = []
for label, a, b, c, d in cases:
    real = ror(a, b, c, d)
    wv = woolf(a, b, c, d); hv = haldane(a, b, c, d)
    ex = cond_ci(a, b, c, d); mp = cond_ci(a, b, c, d, midp=True)
    rows.append(OrderedDict([
        ('case', label), ('a', a), ('b', b), ('c', c), ('d', d),
        ('ROR', round(real, 4)),
        ('woolf_CI', '%.3f-%.3f' % wv),
        ('exact_conditional_CI', '%.3f-%.3f' % ex),
        ('midP_CI', '%.3f-%.3f' % mp),
        ('haldane_CI', '%.3f-%.3f' % hv),
        ('woolf_lower', round(wv[0], 3)), ('exact_lower', round(ex[0], 3)), ('haldane_lower', round(hv[0], 3)),
        ('woolf_declares_signal', 'yes' if wv[0] > 1 else 'no'),
        ('exact_declares_signal', 'yes' if ex[0] > 1 else 'no'),
    ]))
with open(P('15_sparse_intervals.csv'), 'w', newline='', encoding='utf-8-sig') as fh:
    w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
    w.writeheader(); w.writerows(rows)
print('[15] sparse interval comparison written', flush=True)
for r in rows:
    print('    %-48s ROR=%-9s woolf=%-17s exact=%-17s midP=%-17s haldane=%-17s' % (
        r['case'], r['ROR'], r['woolf_CI'], r['exact_conditional_CI'], r['midP_CI'], r['haldane_CI']), flush=True)

# ------------------------------------------------ 5. year trend (Poisson-style)
def poisson_trend(years, y, offset):
    """Fit log E[Y] = log(offset) + mu + beta*(year - min) by ML; LR test for beta."""
    y = np.asarray(y, float); off = np.asarray(offset, float)
    t = np.asarray(years, float) - min(years)
    X = np.column_stack([np.ones_like(t), t])
    def fit(Xm):
        beta = np.zeros(Xm.shape[1])
        for _ in range(200):
            eta = Xm @ beta
            mu = off * np.exp(eta)
            W = mu
            z = eta - 0 + (y - mu) / np.maximum(mu, 1e-12)
            A = Xm.T @ (Xm * W[:, None])
            bb = Xm.T @ (W * z)
            beta_new = np.linalg.solve(A, bb)
            if np.max(np.abs(beta_new - beta)) < 1e-10:
                beta = beta_new; break
            beta = beta_new
        eta = Xm @ beta
        mu = off * np.exp(eta)
        ll = np.sum(y * np.log(np.maximum(mu, 1e-12)) - mu - np.array([math.lgamma(v + 1) for v in y]))
        return beta, ll
    b_full, ll_full = fit(X)
    b_null, ll_null = fit(X[:, :1])
    lr = 2 * (ll_full - ll_null)
    p = stats.chi2.sf(lr, 1) if lr > 0 else 1.0
    return b_full[1], math.exp(b_full[1]), lr, p

rows = []
for fname, pt in (('04_sensitivity_year_hyperaesthesia.csv', 'HYPERAESTHESIA'),
                  ('04_sensitivity_year_pain.csv', 'PAIN')):
    with open(P(fname), encoding='utf-8-sig') as fh:
        recs = list(csv.DictReader(fh))
    for d, pre in (('REMIFENTANIL', 'REMIFENTANIL'), ('FENTANYL', 'FENTANYL'),
                   ('SUFENTANIL', 'SUFENTANIL'), ('MORPHINE', 'MORPHINE')):
        yrs = [int(r['Year']) for r in recs]
        ys = [int(r['%s_a' % pre]) for r in recs]
        off = [int(r['%s_reports' % pre]) for r in recs]
        if sum(ys) == 0:
            rows.append(OrderedDict([('term', pt), ('drug', d), ('total_a', 0),
                                     ('beta_per_year', ''), ('rate_ratio_per_year', ''),
                                     ('LR_chi2', ''), ('p_trend', ''), ('note', 'no events')]))
            continue
        beta, rr, lr, p = poisson_trend(yrs, ys, off)
        rows.append(OrderedDict([('term', pt), ('drug', d), ('total_a', sum(ys)),
                                 ('beta_per_year', round(beta, 4)), ('rate_ratio_per_year', round(rr, 4)),
                                 ('LR_chi2', round(lr, 3)), ('p_trend', round(p, 5)), ('note', '')]))
with open(P('16_year_trend.csv'), 'w', newline='', encoding='utf-8-sig') as fh:
    w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
    w.writeheader(); w.writerows(rows)
print('[16] year trend written', flush=True)
for r in rows:
    print('    %-16s %-14s a=%-5s RR/yr=%-8s p=%-9s %s' % (
        r['term'], r['drug'], r['total_a'], r['rate_ratio_per_year'], r['p_trend'], r['note']), flush=True)
print('DONE', flush=True)
