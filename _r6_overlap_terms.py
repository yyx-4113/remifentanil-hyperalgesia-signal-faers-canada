# -*- coding: utf-8 -*-
"""
Round-6: term x cohort-overlap counts, then the overlap-removed head-to-head table.
Writes 17_overlap_adjusted_rorr.csv (Table S8 source).
"""
import urllib.request, urllib.parse, json, time, os, csv, math, threading
from concurrent.futures import ThreadPoolExecutor
from collections import OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))
def P(*a): return os.path.join(HERE, *a)
BASE = 'https://api.fda.gov/drug/event.json'
CACHE = P('_r6_overlap_cache.json')
LOCK = threading.Lock()
cache = json.load(open(CACHE, encoding='utf-8')) if os.path.exists(CACHE) else {}

def q(s):
    with LOCK:
        if s in cache:
            return cache[s]
    u = BASE + '?' + urllib.parse.urlencode({'search': s, 'limit': '1'})
    for i in range(5):
        try:
            with urllib.request.urlopen(u, timeout=60) as r:
                t = json.load(r)['meta']['results']['total']
            with LOCK:
                cache[s] = t
                json.dump(cache, open(CACHE, 'w', encoding='utf-8'))
            return t
        except urllib.error.HTTPError as e:
            if e.code == 404:
                with LOCK:
                    cache[s] = 0
                return 0
            time.sleep(1.5 * (i + 1))
        except Exception:
            time.sleep(1.5 * (i + 1))
    return None

D = {'REMIFENTANIL': 'patient.drug.activesubstance.activesubstancename.exact:("REMIFENTANIL" "REMIFENTANIL HYDROCHLORIDE")',
     'FENTANYL':     'patient.drug.activesubstance.activesubstancename.exact:("FENTANYL")',
     'SUFENTANIL':   'patient.drug.activesubstance.activesubstancename.exact:("SUFENTANIL" "SUFENTANIL CITRATE")',
     'MORPHINE':     'patient.drug.activesubstance.activesubstancename.exact:("MORPHINE")'}
TERMS = ['HYPERAESTHESIA', 'ALLODYNIA', 'PROCEDURAL PAIN', 'DRUG WITHDRAWAL SYNDROME',
         'PAIN', 'DRUG INEFFECTIVE', 'NAUSEA', 'VOMITING', 'PRURITUS', 'CONSTIPATION',
         'DRUG TOLERANCE', 'HYPERPATHIA']
ptx = lambda t: 'patient.reaction.reactionmeddrapt.exact:"%s"' % t

base = json.load(open(P('_r6_cache.json'), encoding='utf-8'))
N_all = base['patient.reaction.reactionmeddrapt:[* TO *]']
COH = {d: base[e] for d, e in D.items()}
print('cohorts:', COH, 'N =', N_all, flush=True)

jobs = []
for t in TERMS:
    for d, e in D.items():
        jobs.append(('OVT|%s|%s' % (t, d), e + ' AND ' + ptx(t)))
pairs = [('REMIFENTANIL', 'FENTANYL'), ('REMIFENTANIL', 'SUFENTANIL'), ('REMIFENTANIL', 'MORPHINE')]
for t in TERMS:
    for a, b in pairs:
        jobs.append(('CO|%s|%s&%s' % (t, a, b), D[a] + ' AND ' + D[b] + ' AND ' + ptx(t)))

def work(j):
    k, s = j
    return k, q(s)

res = {}
with ThreadPoolExecutor(max_workers=6) as ex:
    for k, v in ex.map(work, jobs):
        res[k] = v
print('fetched %d counts' % len(res), flush=True)

pub = {r['PT']: r for r in csv.DictReader(open(P('01_faers_results.csv'), encoding='utf-8-sig'))}
# term totals from the earlier round
tot = {}
for t in TERMS:
    tot[t] = base.get(ptx(t))

def ror(a, n, T, N):
    """Conventional 2x2 as in the manuscript: c = term total minus this arm's a."""
    b = n - a
    c = T - a
    d = N - a - b - c
    if min(a, b, c, d) <= 0:
        return None
    r = (a*d)/(b*c)
    se = math.sqrt(1/a + 1/b + 1/c + 1/d)
    return (r, math.exp(math.log(r) - 1.96*se), math.exp(math.log(r) + 1.96*se))

def rorr_ci(e1, e2):
    if not e1 or not e2:
        return None
    r = e1[0]/e2[0]
    se = math.sqrt(sum(1/max(v, 1e-12) for v in (1,) * 0)) if False else None
    return r

rows = []
for t in TERMS:
    T = tot.get(t)
    if T is None:
        print('  no term total for', t, flush=True)
        continue
    o = OrderedDict()
    o['preferred_term'] = t
    o['term_total'] = T
    for d in D:
        o['a_%s' % d.lower()] = res.get('OVT|%s|%s' % (t, d))
        o['n_%s' % d.lower()] = COH[d]
    for b in ('FENTANYL', 'SUFENTANIL', 'MORPHINE'):
        co = res.get('CO|%s|REMIFENTANIL&%s' % (t, b))
        o['n_remi_and_%s' % b.lower()] = co
        n_r = COH['REMIFENTANIL'] - (res.get('CO|%s|REMIFENTANIL&%s' % (t, 'FENTANYL')) if b == 'FENTANYL' else co)
        # note: the remifentanil arm is always reduced by its overlap with THIS comparator
        a_r = res.get('OVT|%s|REMIFENTANIL' % t) - co
        a_c = res.get('OVT|%s|%s' % (t, b))
        n_c = COH[b]
        # published
        e_r0 = ror(res.get('OVT|%s|REMIFENTANIL' % t), COH['REMIFENTANIL'], T, N_all)
        e_c0 = ror(a_c, n_c, T, N_all)
        if b == 'FENTANYL':
            o['RORR_published'] = round(e_r0[0]/e_c0[0], 3) if (e_r0 and e_c0) else ''
        e_r = ror(a_r, n_r, T, N_all)
        e_c = ror(a_c, n_c, T, N_all)
        if e_r and e_c:
            o['RORR_excl_%s' % b.lower()] = round(e_r[0]/e_c[0], 3)
        else:
            o['RORR_excl_%s' % b.lower()] = ''
    rows.append(o)

with open(P('17_overlap_adjusted_rorr.csv'), 'w', newline='', encoding='utf-8-sig') as fh:
    w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
    w.writeheader(); w.writerows(rows)
print('wrote 17_overlap_adjusted_rorr.csv', flush=True)
for r in rows:
    print('  %-26s published_vs_FEN=%-8s excl_vs_FEN=%-8s excl_vs_SUF=%-8s excl_vs_MOR=%-8s' % (
        r['preferred_term'], r.get('RORR_published', ''), r['RORR_excl_fentanyl'],
        r['RORR_excl_sufentanil'], r['RORR_excl_morphine']), flush=True)
print('DONE', flush=True)
