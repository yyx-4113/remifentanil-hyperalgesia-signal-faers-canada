import urllib.request, urllib.parse, json, time, sys
def q(s, tries=5):
    u = 'https://api.fda.gov/drug/event.json?limit=1&search=' + urllib.parse.quote(s, safe='')
    for _ in range(tries):
        try:
            return json.load(urllib.request.urlopen(u, timeout=60))['meta']['results']['total']
        except urllib.error.HTTPError as e:
            if e.code == 404: return 0
            time.sleep(2)
        except Exception:
            time.sleep(2)
    return None
D = {'REMIFENTANIL': '("REMIFENTANIL" "REMIFENTANIL HYDROCHLORIDE")',
     'FENTANYL': '("FENTANYL")',
     'SUFENTANIL': '("SUFENTANIL" "SUFENTANIL CITRATE")',
     'MORPHINE': '("MORPHINE")'}
AGE = {'18-64': '[18 TO 64]', '>=65': '[65 TO 120]'}
res = {}
for age, rng in AGE.items():
    res[age] = {}
    for d, expr in D.items():
        base = f'patient.drug.activesubstance.activesubstancename.exact:{expr} AND patient.patientonsetage:{rng}'
        n = q(base); sys.stdout.write(f'  {age} {d} cohort={n}\n'); sys.stdout.flush()
        e = {'n': n}
        for pt in ('PAIN', 'DRUG INEFFECTIVE'):
            a = q(base + f' AND patient.reaction.reactionmeddrapt.exact:"{pt}"')
            e[pt] = a
            sys.stdout.write(f'      {pt} a={a}\n'); sys.stdout.flush()
        res[age][d] = e
# sex strata for PAIN
res['sex'] = {}
for sex, code in (('Female', '2'), ('Male', '1')):
    res['sex'][sex] = {}
    for d, expr in D.items():
        base = f'patient.drug.activesubstance.activesubstancename.exact:{expr} AND patient.patientsex:{code}'
        n = q(base)
        a = q(base + ' AND patient.reaction.reactionmeddrapt.exact:"PAIN"')
        di = q(base + ' AND patient.reaction.reactionmeddrapt.exact:"DRUG INEFFECTIVE"')
        res['sex'][sex][d] = {'n': n, 'PAIN': a, 'DRUG INEFFECTIVE': di}
        sys.stdout.write(f'  {sex} {d} n={n} PAIN={a} DI={di}\n'); sys.stdout.flush()
json.dump(res, open('_a5_faers_strata.json', 'w'), indent=1)
print('DONE')
