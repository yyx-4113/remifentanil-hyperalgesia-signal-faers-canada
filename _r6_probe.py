# -*- coding: utf-8 -*-
"""Round-6: probe openFDA case-level pagination feasibility (limit ceiling, payload, latency)."""
import urllib.request, urllib.parse, json, time, sys

BASE = 'https://api.fda.gov/drug/event.json'
R = 'patient.drug.activesubstance.activesubstancename.exact:("REMIFENTANIL" "REMIFENTANIL HYDROCHLORIDE")'

def try_limit(n):
    u = BASE + '?' + urllib.parse.urlencode({'search': R, 'limit': str(n)})
    t0 = time.time()
    try:
        with urllib.request.urlopen(u, timeout=60) as r:
            raw = r.read()
        dt = time.time() - t0
        d = json.loads(raw)
        got = len(d.get('results', []))
        tot = d['meta']['results']['total']
        print('limit=%-5s -> HTTP 200, %d bytes, %d results, total=%d, %.2fs' % (n, len(raw), got, tot, dt))
        if got:
            rec = d['results'][0]
            print('    record keys:', sorted(rec.keys())[:14])
            pd_ = rec.get('patient', {}).get('drug', [])
            print('    patient.drug entries:', len(pd_))
            if pd_:
                print('    drug[0] keys:', sorted(pd_[0].keys()))
                print('    drug[0] characterization:', pd_[0].get('drugcharacterization'),
                      '| indication:', str(pd_[0].get('drugindication'))[:60])
            pr = rec.get('patient', {}).get('reaction', [])
            print('    reaction entries:', len(pr), '| first pt:', pr[0].get('reactionmeddrapt') if pr else None)
            print('    version:', rec.get('safetyreportversion'), '| receivedate:', rec.get('receivedate'))
        return True
    except urllib.error.HTTPError as e:
        print('limit=%-5s -> HTTP %s %s (%.2fs)' % (n, e.code, e.reason, time.time() - t0))
        return False
    except Exception as e:
        print('limit=%-5s -> ERR %r (%.2fs)' % (n, e, time.time() - t0))
        return False

print('=== probing limit ceiling for search= ===', flush=True)
for n in (1000, 500, 300, 100):
    if try_limit(n):
        break
    time.sleep(2)
print('DONE', flush=True)
