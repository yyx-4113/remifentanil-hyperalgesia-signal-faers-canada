# -*- coding: utf-8 -*-
"""Probe: what is the real limit ceiling for the search endpoint without a key?"""
import urllib.request, urllib.parse, json, time, socket

BASE = 'https://api.fda.gov/drug/event.json'
R = 'patient.drug.activesubstance.activesubstancename.exact:("REMIFENTANIL" "REMIFENTANIL HYDROCHLORIDE")'

for n in ('1000', '500', '100'):
    u = BASE + '?' + urllib.parse.urlencode({'search': R, 'limit': n})
    t0 = time.time()
    try:
        with urllib.request.urlopen(u, timeout=45) as r:
            raw = r.read()
        d = json.loads(raw)
        print('limit=%-5s  HTTP 200  bytes=%-9d n=%-5d total=%d  %.1fs' % (
            n, len(raw), len(d.get('results', [])), d['meta']['results']['total'], time.time() - t0), flush=True)
        rec = d['results'][0]
        drugs = rec.get('patient', {}).get('drug', [])
        reacs = rec.get('patient', {}).get('reaction', [])
        print('    version=%s receivedate=%s | drug entries=%d | reaction entries=%d' % (
            rec.get('safetyreportversion'), rec.get('receivedate'), len(drugs), len(reacs)), flush=True)
        for dr in drugs[:3]:
            print('      - %-28s char=%s route=%s' % (
                str(dr.get('medicinalproduct'))[:28], dr.get('drugcharacterization'),
                dr.get('openfda', {}).get('route')), flush=True)
        print('    reaction PTs:', [x.get('reactionmeddrapt') for x in reacs][:6], flush=True)
        break
    except urllib.error.HTTPError as e:
        body = e.read()[:200]
        print('limit=%-5s  HTTP %s %s  %.1fs  body=%s' % (n, e.code, e.reason, time.time() - t0, body), flush=True)
    except Exception as e:
        print('limit=%-5s  ERR %r  %.1fs' % (n, e, time.time() - t0), flush=True)
    time.sleep(1)

# also: is skip usable, and does drugcharacterization filter work at report level?
print('--- filter probes ---', flush=True)
for lab, s in [
    ('R alone', R),
    ('R AND char1', R + ' AND patient.drug.drugcharacterization:1'),
    ('R AND char2', R + ' AND patient.drug.drugcharacterization:2'),
    ('R AND version1', R + ' AND safetyreportversion:1'),
]:
    u = BASE + '?' + urllib.parse.urlencode({'search': s, 'limit': '1'})
    t0 = time.time()
    try:
        d = json.load(urllib.request.urlopen(u, timeout=45))
        print('  %-16s total=%-8d  %.1fs' % (lab, d['meta']['results']['total'], time.time() - t0), flush=True)
    except Exception as e:
        print('  %-16s ERR %r' % (lab, e), flush=True)
    time.sleep(1)
print('DONE', flush=True)
