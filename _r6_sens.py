# -*- coding: utf-8 -*-
"""
Round-6 sensitivity products, rebuilt offline from _r6_cache.json (keyed by search
expression) using the same label -> expression map as _r6_fetch.py.

Two restrictions are reported, and they mean different things:
  role1     reports containing at least one drug record flagged drugcharacterization = 1
            (primary suspect). Report-level, because the search API ORs across the
            patient.drug array; it is an upper bound on a drug-entry-level restriction.
  v1        reports whose safetyreportversion is 1, i.e. never revised. openFDA keeps
            only the latest version of each safetyreportid (verified: a query on a single
            safetyreportid returns one record), so this is NOT de-duplication; it removes
            38.4% of the corpus, and revised reports are systematically different.
"""
import json, csv, os, math
from collections import OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))
def P(*a): return os.path.join(HERE, *a)

D = {'REMIFENTANIL': 'patient.drug.activesubstance.activesubstancename.exact:("REMIFENTANIL" "REMIFENTANIL HYDROCHLORIDE")',
     'FENTANYL':     'patient.drug.activesubstance.activesubstancename.exact:("FENTANYL")',
     'SUFENTANIL':   'patient.drug.activesubstance.activesubstancename.exact:("SUFENTANIL" "SUFENTANIL CITRATE")',
     'MORPHINE':     'patient.drug.activesubstance.activesubstancename.exact:("MORPHINE")'}
DRUGS = list(D)
SHORT = {'REMIFENTANIL': 'remifentanil', 'FENTANYL': 'fentanyl',
         'SUFENTANIL': 'sufentanil', 'MORPHINE': 'morphine'}
TERMS = ['HYPERAESTHESIA', 'ALLODYNIA', 'PROCEDURAL PAIN', 'DRUG WITHDRAWAL SYNDROME',
         'PAIN', 'DRUG INEFFECTIVE', 'NAUSEA', 'VOMITING', 'PRURITUS', 'CONSTIPATION',
         'DRUG TOLERANCE', 'HYPERPATHIA']
V1 = 'safetyreportversion:1'
ROLE1 = 'patient.drug.drugcharacterization:1'
ptx = lambda t: 'patient.reaction.reactionmeddrapt.exact:"%s"' % t

# ---- rebuild the label -> expression map -------------------------------------
L = {}
L['__N_all__'] = 'patient.reaction.reactionmeddrapt:[* TO *]'
L['__N_v1__'] = L['__N_all__'] + ' AND ' + V1
L['__N_role1__'] = L['__N_all__'] + ' AND ' + ROLE1
for d, e in D.items():
    L['%s|N' % d] = e
    L['%s|N_v1' % d] = e + ' AND ' + V1
    L['%s|N_role1' % d] = e + ' AND ' + ROLE1
for t in TERMS:
    L['T|%s|tot' % t] = ptx(t)
    L['T|%s|tot_v1' % t] = ptx(t) + ' AND ' + V1
    L['T|%s|tot_role1' % t] = ptx(t) + ' AND ' + ROLE1
    for d, e in D.items():
        L['A|%s|%s|role1' % (t, d)] = e + ' AND ' + ptx(t) + ' AND ' + ROLE1
        L['A|%s|%s|v1' % (t, d)] = e + ' AND ' + ptx(t) + ' AND ' + V1

cache = json.load(open(P('_r6_cache.json'), encoding='utf-8'))
MISS = []
def g(label):
    s = L.get(label)
    if s is None or s not in cache:
        MISS.append(label)
        return None
    return cache[s]

N_all, N_v1, N_r1 = g('__N_all__'), g('__N_v1__'), g('__N_role1__')
print('corpus  all=%s  never-revised=%s (%.1f%% kept, %d dropped)  >=1 primary suspect=%s (%.1f%%)' % (
    N_all, N_v1, 100*N_v1/N_all, N_all-N_v1, N_r1, 100*N_r1/N_all), flush=True)
for d in DRUGS:
    print('  %-14s n=%-7s never-revised=%-7s (%.1f%%)  >=1 primary suspect=%-7s (%.1f%%)' % (
        d, g('%s|N' % d), g('%s|N_v1' % d), 100*g('%s|N_v1' % d)/g('%s|N' % d),
        g('%s|N_role1' % d), 100*g('%s|N_role1' % d)/g('%s|N' % d)), flush=True)

# ---- published values, for the side-by-side -----------------------------------
pub = {r['PT']: r for r in csv.DictReader(open(P('01_faers_results.csv'), encoding='utf-8-sig'))}

def cells(a, n, tot, N):
    b = n - a
    c = tot - a
    d = N - a - b - c
    return [a, b, c, d]

def ror_ci(cl):
    a, b, c, d = cl
    if min(cl) <= 0:
        return None
    r = (a*d)/(b*c)
    se = math.sqrt(sum(1/v for v in cl))
    return (r, math.exp(math.log(r) - 1.96*se), math.exp(math.log(r) + 1.96*se), cl)

def rorr_ci(e1, e2):
    if e1 is None or e2 is None:
        return None
    r = e1[0]/e2[0]
    se = math.sqrt(sum(1/v for v in e1[3]) + sum(1/v for v in e2[3]))
    return (r, math.exp(math.log(r) - 1.96*se), math.exp(math.log(r) + 1.96*se))

rows = []
for t in TERMS:
    for suff, lab, N in (('', 'as published (role-agnostic, latest version)', N_all),
                         ('role1', 'restricted to reports with >=1 primary suspect drug record', N_r1),
                         ('v1', 'restricted to never-revised reports', N_v1)):
        tkey = 'T|%s|tot%s' % (t, {'': '', 'role1': '_role1', 'v1': '_v1'}[suff])
        tot = g(tkey)
        if tot is None:
            print('NO TERM TOTAL for %s [%s]: expr=%r  in_cache=%s' % (
                t, suff, L.get(tkey), L.get(tkey) in cache), flush=True)
            continue
        o = OrderedDict()
        o['preferred_term'] = t
        o['restriction'] = lab
        o['corpus_N'] = N
        o['term_total'] = tot
        est = {}
        for d in DRUGS:
            n = g('%s|N%s' % (d, {'': '', 'role1': '_role1', 'v1': '_v1'}[suff]))
            if suff == '':
                a = int(pub[t]['%s_a' % d]) if pub[t]['%s_a' % d] not in ('', None) else 0
            else:
                a = g('A|%s|%s|%s' % (t, d, suff))
            o['n_%s' % SHORT[d]] = n
            o['a_%s' % SHORT[d]] = a
            est[d] = ror_ci(cells(a, n, tot, N)) if a is not None else None
            if est[d]:
                o['ROR_%s' % SHORT[d]] = round(est[d][0], 3)
                o['ROR_CI_%s' % SHORT[d]] = '%.2f-%.2f' % (est[d][1], est[d][2])
            else:
                o['ROR_%s' % SHORT[d]] = ''
                o['ROR_CI_%s' % SHORT[d]] = ''
        for cmp_ in ('FENTANYL', 'MORPHINE'):
            rr = rorr_ci(est.get('REMIFENTANIL'), est.get(cmp_))
            if rr:
                o['RORR_vs_%s' % SHORT[cmp_]] = round(rr[0], 3)
                o['RORR_CI_vs_%s' % SHORT[cmp_]] = '%.2f-%.2f' % (rr[1], rr[2])
            else:
                o['RORR_vs_%s' % SHORT[cmp_]] = ''
                o['RORR_CI_vs_%s' % SHORT[cmp_]] = ''
        e = est.get('REMIFENTANIL')
        o['remifentanil_signal'] = 'yes' if (e and e[1] > 1) else ('no' if e else 'not estimable')
        rows.append(o)

with open(P('12_role_version_sensitivity.csv'), 'w', newline='', encoding='utf-8-sig') as fh:
    w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
    w.writeheader(); w.writerows(rows)
print('\nwrote 12_role_version_sensitivity.csv (%d rows); missing lookups: %d' % (len(rows), len(MISS)), flush=True)

lines = []
for t in ['HYPERAESTHESIA', 'PAIN', 'DRUG INEFFECTIVE', 'PROCEDURAL PAIN',
          'NAUSEA', 'VOMITING', 'PRURITUS', 'CONSTIPATION', 'DRUG WITHDRAWAL SYNDROME']:
    lines.append('%s' % t)
    for r in [x for x in rows if x['preferred_term'] == t]:
        lines.append('   %-62s a_REMI=%-5s ROR=%-7s (%-13s) RORR_FEN=%-7s (%-13s) signal=%s' % (
            r['restriction'][:62], r['a_remifentanil'], r['ROR_remifentanil'],
            r['ROR_CI_remifentanil'], r['RORR_vs_fentanyl'], r['RORR_CI_vs_fentanyl'],
            r['remifentanil_signal']))
    lines.append('')
open(P('12b_notes.txt'), 'w', encoding='utf-8').write('\n'.join(lines))
print('\n'.join(lines), flush=True)
print('DONE', flush=True)
