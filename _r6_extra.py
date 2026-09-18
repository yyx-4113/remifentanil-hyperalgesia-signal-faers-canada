# -*- coding: utf-8 -*-
"""
Round-6 extra fetches (few requests only):
  13_report_series_hyperaesthesia.csv   every remifentanil HYPERAESTHESIA report, one row each
  14_faers_pt_distribution.csv          top-500 reaction terms per cohort (for CMQ + depth)
"""
import urllib.request, urllib.parse, json, time, os, csv, math
from collections import OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))
def P(*a): return os.path.join(HERE, *a)
BASE = 'https://api.fda.gov/drug/event.json'

def get(params, tries=5):
    u = BASE + '?' + urllib.parse.urlencode(params)
    for i in range(tries):
        try:
            with urllib.request.urlopen(u, timeout=90) as r:
                return json.load(r)
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return {'results': []}
            time.sleep(2 * (i + 1))
        except Exception:
            time.sleep(2 * (i + 1))
    return None

D = {'REMIFENTANIL': 'patient.drug.activesubstance.activesubstancename.exact:("REMIFENTANIL" "REMIFENTANIL HYDROCHLORIDE")',
     'FENTANYL':     'patient.drug.activesubstance.activesubstancename.exact:("FENTANYL")',
     'SUFENTANIL':   'patient.drug.activesubstance.activesubstancename.exact:("SUFENTANIL" "SUFENTANIL CITRATE")',
     'MORPHINE':     'patient.drug.activesubstance.activesubstancename.exact:("MORPHINE")'}
R = D['REMIFENTANIL']

# ---------------------------------------------------------------- 1. case series
print('fetching remifentanil HYPERAESTHESIA reports ...', flush=True)
d = get({'search': R + ' AND patient.reaction.reactionmeddrapt.exact:"HYPERAESTHESIA"', 'limit': '100'})
recs = d.get('results', []) if d else []
print('  returned %d records' % len(recs), flush=True)

rows = []
for r in recs:
    pat = r.get('patient', {})
    drugs = pat.get('drug', [])
    reacs = pat.get('reaction', [])
    # which of the report's drug entries are the target substance, and in what role
    tgt = [(str(x.get('medicinalproduct') or ''),
            x.get('drugcharacterization'),
            (x.get('openfda', {}) or {}).get('route'))
           for x in drugs
           if 'REMIFENTANIL' in str(x.get('activesubstance', {}).get('activesubstancename', '')).upper()
           or 'REMIFENTANIL' in str(x.get('medicinalproduct', '')).upper()]
    rows.append(OrderedDict([
        ('safetyreportid', r.get('safetyreportid')),
        ('version', r.get('safetyreportversion')),
        ('receivedate', r.get('receivedate')),
        ('country', (r.get('occurcountry') or r.get('primarysource', {}).get('reportercountry'))),
        ('age', pat.get('patientonsetage')),
        ('age_unit', pat.get('patientonsetageunit')),
        ('sex', pat.get('patientsex')),
        ('reporter_qualification', (r.get('primarysource', {}) or {}).get('qualification')),
        ('n_drug_entries', len(drugs)),
        ('n_reaction_terms', len(reacs)),
        ('remifentanil_entries', '; '.join('%s/char=%s' % (a, b) for a, b, _c in tgt)),
        ('all_medicinal_products', ', '.join(sorted({str(x.get('medicinalproduct') or '') for x in drugs}))),
        ('all_reaction_terms', ', '.join(sorted({str(x.get('reactionmeddrapt') or '') for x in reacs}))),
        ('serious', r.get('serious')),
    ]))
with open(P('13_report_series_hyperaesthesia.csv'), 'w', newline='', encoding='utf-8-sig') as fh:
    w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
    w.writeheader(); w.writerows(rows)
print('wrote 13_report_series_hyperaesthesia.csv (%d rows)' % len(rows), flush=True)
for r in rows:
    print('  %-9s v%-2s %s %-2s age=%-4s n_drug=%-3s : %s' % (
        r['safetyreportid'], r['version'], r['receivedate'], r['country'],
        r['age'], r['n_drug_entries'], r['all_medicinal_products'][:78]), flush=True)

# ------------------------------------------------- 2. top-500 PT per cohort
print('\nfetching top-500 reaction terms per cohort ...', flush=True)
dist = {}
for dname, expr in D.items():
    time.sleep(1)
    res = get({'search': expr, 'count': 'patient.reaction.reactionmeddrapt.exact', 'limit': '500'})
    lst = res.get('results', []) if res else []
    dist[dname] = lst
    tot = sum(x['count'] for x in lst)
    n = 0
    print('  %-14s terms=%d  terms counted=%d' % (dname, len(lst), tot), flush=True)
rows2 = []
allT = sorted({x['term'] for v in dist.values() for x in v})
for t in allT:
    row = OrderedDict([('term', t)])
    for dname in D:
        m = {x['term']: x['count'] for x in dist[dname]}
        row[dname] = m.get(t, 0)
    rows2.append(row)
with open(P('14_faers_pt_distribution.csv'), 'w', newline='', encoding='utf-8-sig') as fh:
    w = csv.DictWriter(fh, fieldnames=list(rows2[0].keys()))
    w.writeheader(); w.writerows(rows2)
print('wrote 14_faers_pt_distribution.csv (%d terms)' % len(rows2), flush=True)
json.dump({k: v for k, v in dist.items()}, open(P('_r6_ptdist.json'), 'w', encoding='utf-8'), indent=1)
print('DONE', flush=True)
