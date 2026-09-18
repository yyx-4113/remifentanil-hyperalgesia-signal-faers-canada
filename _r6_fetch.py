# -*- coding: utf-8 -*-
"""
Round-6 fetch: gather every count needed for the revision, with an on-disk cache.
Concurrency is kept low enough to stay inside the openFDA no-key ceiling.
"""
import urllib.request, urllib.parse, json, time, os, threading, sys
from concurrent.futures import ThreadPoolExecutor

BASE = 'https://api.fda.gov/drug/event.json'
CACHE = '_r6_cache.json'
LOCK = threading.Lock()
cache = json.load(open(CACHE, encoding='utf-8')) if os.path.exists(CACHE) else {}
NEW = [0]

def q(search):
    with LOCK:
        if search in cache:
            return cache[search]
    u = BASE + '?' + urllib.parse.urlencode({'search': search, 'limit': '1'})
    for i in range(5):
        try:
            with urllib.request.urlopen(u, timeout=60) as r:
                t = json.load(r)['meta']['results']['total']
            with LOCK:
                cache[search] = t
                NEW[0] += 1
                if NEW[0] % 10 == 0:
                    json.dump(cache, open(CACHE, 'w', encoding='utf-8'))
            return t
        except urllib.error.HTTPError as e:
            if e.code == 404:
                with LOCK:
                    cache[search] = 0
                return 0
            time.sleep(1.5 * (i + 1))
        except Exception:
            time.sleep(1.5 * (i + 1))
    return None

D = {'REMIFENTANIL': 'patient.drug.activesubstance.activesubstancename.exact:("REMIFENTANIL" "REMIFENTANIL HYDROCHLORIDE")',
     'FENTANYL':     'patient.drug.activesubstance.activesubstancename.exact:("FENTANYL")',
     'SUFENTANIL':   'patient.drug.activesubstance.activesubstancename.exact:("SUFENTANIL" "SUFENTANIL CITRATE")',
     'MORPHINE':     'patient.drug.activesubstance.activesubstancename.exact:("MORPHINE")'}

# The 12 outcome terms that can actually be estimated for at least one arm.
TERMS = ['HYPERAESTHESIA', 'ALLODYNIA', 'PROCEDURAL PAIN', 'DRUG WITHDRAWAL SYNDROME',
         'PAIN', 'DRUG INEFFECTIVE', 'NAUSEA', 'VOMITING', 'PRURITUS', 'CONSTIPATION',
         'DRUG TOLERANCE', 'HYPERPATHIA']

V1 = 'safetyreportversion:1'
ROLE1 = 'patient.drug.drugcharacterization:1'

jobs = []
# corpus denominators
jobs.append(('__N_all__',  'patient.reaction.reactionmeddrapt:[* TO *]'))
jobs.append(('__N_v1__',   'patient.reaction.reactionmeddrapt:[* TO *] AND ' + V1))
jobs.append(('__N_role1__', 'patient.reaction.reactionmeddrapt:[* TO *] AND ' + ROLE1))
# cohort denominators + their v1 / role1 variants
for d, expr in D.items():
    jobs.append(('%s|N' % d, expr))
    jobs.append(('%s|N_v1' % d, expr + ' AND ' + V1))
    jobs.append(('%s|N_role1' % d, expr + ' AND ' + ROLE1))
    jobs.append(('%s|N_role1_v1' % d, expr + ' AND ' + ROLE1 + ' AND ' + V1))
# term x drug x {v1, role1}
for t in TERMS:
    pt = 'patient.reaction.reactionmeddrapt.exact:"%s"' % t
    jobs.append(('T|%s|tot' % t, pt))
    jobs.append(('T|%s|tot_v1' % t, pt + ' AND ' + V1))
    jobs.append(('T|%s|tot_role1' % t, pt + ' AND ' + ROLE1))
    for d, expr in D.items():
        jobs.append(('A|%s|%s|role1' % (t, d), expr + ' AND ' + pt + ' AND ' + ROLE1))
        jobs.append(('A|%s|%s|v1' % (t, d), expr + ' AND ' + pt + ' AND ' + V1))
        jobs.append(('A|%s|%s|role1_v1' % (t, d), expr + ' AND ' + pt + ' AND ' + ROLE1 + ' AND ' + V1))

# 4x4 overlap matrix (report level)
import itertools
keys = list(D)
for a, b in itertools.combinations(keys, 2):
    jobs.append(('OV|%s&%s' % (a, b), D[a] + ' AND ' + D[b]))
for combo in itertools.combinations(keys, 3):
    jobs.append(('OV3|%s' % '&'.join(combo), ' AND '.join(D[x] for x in combo)))
jobs.append(('OV4|all', ' AND '.join(D[x] for x in keys)))

print('jobs total: %d | cached already: %d' % (len(jobs), sum(1 for k, _ in jobs if _ in cache)), flush=True)
out, t0 = {}, time.time()

def work(job):
    key, s = job
    v = q(s)
    with LOCK:
        out[key] = v
    return key, v

with ThreadPoolExecutor(max_workers=6) as ex:
    for i, (key, v) in enumerate(ex.map(work, jobs), 1):
        if i % 20 == 0 or i == len(jobs):
            print('[%6.1fs] %d/%d done (new requests: %d)' % (time.time() - t0, i, len(jobs), NEW[0]), flush=True)

with LOCK:
    json.dump(cache, open(CACHE, 'w', encoding='utf-8'))
json.dump(out, open('_r6_counts.json', 'w', encoding='utf-8'), indent=1)
print('saved _r6_counts.json, %d entries, cache size %d' % (len(out), len(cache)), flush=True)
print('DONE', flush=True)
