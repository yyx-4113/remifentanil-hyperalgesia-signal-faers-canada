import urllib.request, json, time, itertools, sys
BASE='https://api.fda.gov/drug/event.json?search='
def q(expr, tries=5):
    url = BASE + expr + '&limit=1'
    for k in range(tries):
        try:
            d = json.load(urllib.request.urlopen(url, timeout=60))
            return d['meta']['results']['total']
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return 0
            time.sleep(3)
        except Exception as e:
            time.sleep(3)
    return None
G = {'REMI': '(%22REMIFENTANIL%22+%22REMIFENTANIL+HYDROCHLORIDE%22)',
     'FEN': '(%22FENTANYL%22)', 'SUF': '(%22SUFENTANIL%22+%22SUFENTANIL+CITRATE%22)',
     'MOR': '(%22MORPHINE%22)'}
F = 'patient.drug.activesubstance.activesubstancename.exact:'
res = {}
for k, v in G.items():
    res[k] = q(F + v); print('single', k, res[k], flush=True)
for a, b in itertools.combinations(G, 2):
    res[a + '&' + b] = q(F + G[a] + '+AND+' + F + G[b]); print('pair', a, b, res[a+'&'+b], flush=True)
for combo in itertools.combinations(G, 3):
    res['&'.join(combo)] = q('+AND+'.join(F + G[x] for x in combo)); print('tri', combo, flush=True)
res['ALL4'] = q('+AND+'.join(F + G[x] for x in G)); print('all4', res['ALL4'], flush=True)
json.dump(res, open('_a5_overlap_faers.json', 'w'), indent=1)
print('DONE', flush=True)
