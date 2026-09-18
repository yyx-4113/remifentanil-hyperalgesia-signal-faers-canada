# -*- coding: utf-8 -*-
"""只取决定性单元格：PAIN / DRUG INEFFECTIVE / HYPERAESTHESIA 在
physician、other_hp、age_18_64 三层的 a 值（非 count 查询，读 meta.results.total）。"""
import json, os, time, math, urllib.request, urllib.parse
HERE=os.path.dirname(os.path.abspath(__file__)); C=os.path.join(HERE,"_a5_key_cache.json")
B="https://api.fda.gov/drug/event.json"
cache=json.load(open(C,encoding="utf-8")) if os.path.exists(C) else {}
def call(s):
    if s in cache: return cache[s]
    url=B+"?"+urllib.parse.urlencode({"search":s,"limit":1})
    for _ in range(6):
        try:
            with urllib.request.urlopen(url,timeout=45) as r:
                d=json.loads(r.read().decode())
            v=d["meta"]["results"]["total"]; cache[s]=v
            json.dump(cache,open(C,"w",encoding="utf-8"),ensure_ascii=False); time.sleep(0.5); return v
        except urllib.error.HTTPError as e:
            if e.code==404:
                cache[s]=0; json.dump(cache,open(C,"w",encoding="utf-8"),ensure_ascii=False); return 0
            time.sleep(3)
        except Exception: time.sleep(3)
    return None
DRUG={"REMIFENTANIL":'patient.drug.activesubstance.activesubstancename.exact:("REMIFENTANIL" "REMIFENTANIL HYDROCHLORIDE")',
      "FENTANYL":'patient.drug.activesubstance.activesubstancename.exact:("FENTANYL")',
      "SUFENTANIL":'patient.drug.activesubstance.activesubstancename.exact:("SUFENTANIL" "SUFENTANIL CITRATE")',
      "MORPHINE":'patient.drug.activesubstance.activesubstancename.exact:("MORPHINE")'}
STR={"physician":"primarysource.qualification:1","other_hp":"primarysource.qualification:3",
     "age_18_64":'patient.patientonsetage:[18 TO 64] AND patient.patientonsetageunit:801',"all":""}
PTS=["PAIN","DRUG INEFFECTIVE","HYPERAESTHESIA","NAUSEA"]
tot={}; A={}
for s,f in STR.items():
    tot[s]={}; A[s]={}
    for d,dq in DRUG.items():
        base=dq if not f else dq+" AND "+f
        tot[s][d]=call(base)
        A[s][d]={p:call(base+' AND patient.reaction.reactionmeddrapt.exact:"%s"'%p) for p in PTS}
        print("cell",s,d,tot[s][d],A[s][d],flush=True)
def rr(s,p,comp):
    ar,tr=A[s]["REMIFENTANIL"][p],tot[s]["REMIFENTANIL"]
    ac,tc=A[s][comp][p],tot[s][comp]
    if None in (ar,ac,tr,tc) or min(ar,ac,tr-ar,tc-ac)<=0: return None
    br,bc=tr-ar,tc-ac; lr=(ar*bc)/(br*ac); se=(1/ar+1/br+1/ac+1/bc)**.5
    return (round(lr,3),round(math.exp(math.log(lr)-1.96*se),3),round(math.exp(math.log(lr)+1.96*se),3))
print("\n=== 结论 ===")
for s in STR:
    for p in PTS:
        print("%-11s %-18s a_r=%-4s | FEN=%-22s SUF=%-22s MOR=%-22s"%(s,p,A[s]["REMIFENTANIL"][p],rr(s,p,"FENTANYL"),rr(s,p,"SUFENTANIL"),rr(s,p,"MORPHINE")))
json.dump({"tot":tot,"A":A},open(os.path.join(HERE,"_a5_key_results.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
