#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""A2: quantify report-level overlap between the four opioid cohorts (openFDA live)."""
import urllib.request, urllib.parse, json, time, math, os

BASE = 'https://api.fda.gov/drug/event.json'
CACHEF = '_a2_cache.json'
cache = json.load(open(CACHEF, encoding='utf-8')) if os.path.exists(CACHEF) else {}

def q(search):
    if search in cache and cache[search] is not None:
        return cache[search]
    u = BASE + '?' + urllib.parse.urlencode({'search': search, 'limit': '1'})
    for i in range(5):
        try:
            with urllib.request.urlopen(u, timeout=30) as r:
                t = json.load(r)['meta']['results']['total']
            cache[search] = t; json.dump(cache, open(CACHEF, 'w', encoding='utf-8')); time.sleep(0.4)
            return t
        except urllib.error.HTTPError as e:
            if e.code == 404:
                cache[search] = 0; json.dump(cache, open(CACHEF, 'w', encoding='utf-8')); return 0
            time.sleep(2 * (i + 1))
        except Exception:
            time.sleep(2 * (i + 1))
    return None

R = 'patient.drug.activesubstance.activesubstancename.exact:("REMIFENTANIL" "REMIFENTANIL HYDROCHLORIDE")'
F = 'patient.drug.activesubstance.activesubstancename.exact:("FENTANYL")'
S = 'patient.drug.activesubstance.activesubstancename.exact:("SUFENTANIL" "SUFENTANIL CITRATE")'
M = 'patient.drug.activesubstance.activesubstancename.exact:("MORPHINE")'
N = q('patient.reaction.reactionmeddrapt:[* TO *]')
cohort = {'R': q(R), 'F': q(F), 'S': q(S), 'M': q(M)}
U = q('(%s OR %s OR %s OR %s)' % (R, F, S, M))
print('N =', N)
print('cohorts:', cohort, 'sum =', sum(cohort.values()))
print('union = %d  (%.3f%% of N; %.3f%% of the naive sum)' % (U, 100*U/N, 100*U/sum(cohort.values())))

pairs = {('R','F'): q(R+' AND '+F), ('R','S'): q(R+' AND '+S), ('R','M'): q(R+' AND '+M),
         ('F','S'): q(F+' AND '+S), ('F','M'): q(F+' AND '+M), ('S','M'): q(S+' AND '+M)}
print('pairwise overlaps:', pairs)
for (x,y),v in pairs.items():
    print('  %s&%s = %d  (%.1f%% of %s, %.1f%% of %s)' % (x,y,v,100*v/cohort[x],x,100*v/cohort[y],y))

def pt(s): return 'patient.reaction.reactionmeddrapt.exact:"%s"' % s

TERMS = ['HYPERAESTHESIA','PAIN','ALLODYNIA','PROCEDURAL PAIN','DRUG WITHDRAWAL SYNDROME',
         'DRUG TOLERANCE','DRUG INEFFECTIVE','NAUSEA','VOMITING','PRURITUS','CONSTIPATION']
print('\n--- FAERS counts (live re-query) and the remifentanil a that is shared with each comparator ---')
print('%-28s %8s %8s %8s %8s %8s %8s %8s' % ('PT','pt_total','a_R','a_F','a_S','a_M','a_R&F','a_R&M'))
live = {}
for t in TERMS:
    row = (q(pt(t)), q(R+' AND '+pt(t)), q(F+' AND '+pt(t)), q(S+' AND '+pt(t)), q(M+' AND '+pt(t)),
           q(R+' AND '+F+' AND '+pt(t)), q(R+' AND '+M+' AND '+pt(t)))
    live[t] = row
    print('%-28s %8d %8d %8d %8d %8d %8d %8d' % ((t,)+row))

def ror(a, n, ptot, N):
    b = n - a; cc = ptot - a; dd = N - a - b - cc
    if min(a, b, cc, dd) <= 0: return None
    return ((a*dd)/(b*cc), math.sqrt(1/a+1/b+1/cc+1/dd))

def rorr_maker(m_a, r_a):
    if not (m_a and r_a): return None
    rr = m_a[0]/r_a[0]; se = math.sqrt(m_a[1]**2 + r_a[1]**2)
    ln = math.log(rr)
    return (rr, math.exp(ln-1.96*se), math.exp(ln+1.96*se))

print('\n--- RORR remifentanil vs fentanyl: as-published vs overlap-excluded remifentanil arm ---')
nRF = cohort['R'] - pairs[('R','F')]
print('remifentanil-only (no fentanyl on the report) cohort = %d of %d  (%.1f%%)' % (nRF, cohort['R'], 100.0*nRF/cohort['R']))
print('%-28s %-20s %-20s' % ('PT','RORR vs F published','RORR vs F excl. R&F reports'))
for t in TERMS:
    ptot, aR, aF, aS, aM, aRF, aRM = live[t]
    pub = rorr_maker(ror(aR, cohort['R'], ptot, N), ror(aF, cohort['F'], ptot, N))
    exc = rorr_maker(ror(aR-aRF, nRF, ptot, N), ror(aF, cohort['F'], ptot, N))
    f = lambda x: ('%.3f (%.2f-%.2f)' % x) if x else 'n/e'
    print('%-28s %-20s %-20s' % (t, f(pub), f(exc)))

print('\n--- RORR remifentanil vs morphine: as-published vs overlap-excluded ---')
nRM = cohort['R'] - pairs[('R','M')]
print('remifentanil-only (no morphine on the report) cohort = %d of %d' % (nRM, cohort['R']))
print('%-28s %-20s %-20s' % ('PT','RORR vs M published','RORR vs M excl. R&M reports'))
for t in TERMS:
    ptot, aR, aF, aS, aM, aRF, aRM = live[t]
    pub = rorr_maker(ror(aR, cohort['R'], ptot, N), ror(aM, cohort['M'], ptot, N))
    exc = rorr_maker(ror(aR-aRM, nRM, ptot, N), ror(aM, cohort['M'], ptot, N))
    f = lambda x: ('%.3f (%.2f-%.2f)' % x) if x else 'n/e'
    print('%-28s %-20s %-20s' % (t, f(pub), f(exc)))
