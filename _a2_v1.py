import urllib.request, urllib.parse, json, time, os, math
BASE='https://api.fda.gov/drug/event.json'
C='_a2_cache3.json'
cache=json.load(open(C,encoding='utf-8')) if os.path.exists(C) else {}
def q(s):
    if s in cache and cache[s] is not None: return cache[s]
    for i in range(6):
        try:
            u=BASE+'?'+urllib.parse.urlencode({'search':s,'limit':'1'})
            with urllib.request.urlopen(u,timeout=30) as r:
                t=json.load(r)['meta']['results']['total']
            cache[s]=t; json.dump(cache,open(C,'w',encoding='utf-8')); time.sleep(1.2); return t
        except urllib.error.HTTPError as e:
            if e.code==404:
                cache[s]=0; json.dump(cache,open(C,'w',encoding='utf-8')); return 0
            time.sleep(4*(i+1))
        except Exception:
            time.sleep(4*(i+1))
    return None
D={'REMIFENTANIL':'patient.drug.activesubstance.activesubstancename.exact:("REMIFENTANIL" "REMIFENTANIL HYDROCHLORIDE")',
   'FENTANYL':'patient.drug.activesubstance.activesubstancename.exact:("FENTANYL")',
   'SUFENTANIL':'patient.drug.activesubstance.activesubstancename.exact:("SUFENTANIL" "SUFENTANIL CITRATE")',
   'MORPHINE':'patient.drug.activesubstance.activesubstancename.exact:("MORPHINE")'}
pt=lambda t:'patient.reaction.reactionmeddrapt.exact:"%s"'%t
V='safetyreportversion:1'
out={}
for k,v in D.items():
    out[k]={'n1':q(v+' AND '+V),'n':q(v)}; print(k,'cohort v1',out[k]['n1'],flush=True)
for t in ['PAIN','PROCEDURAL PAIN','DRUG INEFFECTIVE','NAUSEA','VOMITING','PRURITUS','CONSTIPATION','DRUG WITHDRAWAL SYNDROME','ALLODYNIA','HYPERAESTHESIA']:
    out.setdefault('terms',{})[t]={'tot1':q(pt(t)+' AND '+V),'arms':{}}
    for k,v in D.items():
        a=q(v+' AND '+pt(t)+' AND '+V)
        out['terms'][t]['arms'][k]=a
    print(t,out['terms'][t],flush=True)
json.dump(out,open('_a2_v1_results.json','w',encoding='utf-8'),indent=1)
print('DONE')
