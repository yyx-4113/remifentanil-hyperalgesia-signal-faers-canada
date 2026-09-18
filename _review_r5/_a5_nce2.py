# -*- coding: utf-8 -*-
"""负对照暴露（含盐形式）：remifentanil vs 同场景非阿片药 的 PAIN RORR。"""
import json,os,time,math,urllib.request,urllib.parse
HERE=os.path.dirname(os.path.abspath(__file__)); C=os.path.join(HERE,"_a5_nce2.json")
B="https://api.fda.gov/drug/event.json"
cache=json.load(open(C,encoding="utf-8")) if os.path.exists(C) else {}
def call(s):
    if s in cache: return cache[s]
    url=B+"?"+urllib.parse.urlencode({"search":s,"limit":1})
    for _ in range(6):
        try:
            with urllib.request.urlopen(url,timeout=45) as r: d=json.loads(r.read().decode())
            v=d["meta"]["results"]["total"]; cache[s]=v
            json.dump(cache,open(C,"w",encoding="utf-8"),ensure_ascii=False); time.sleep(0.4); return v
        except urllib.error.HTTPError as e:
            if e.code==404:
                cache[s]=0; json.dump(cache,open(C,"w",encoding="utf-8"),ensure_ascii=False); return 0
            time.sleep(3)
        except Exception: time.sleep(3)
    return None
def D(*n): return "patient.drug.activesubstance.activesubstancename.exact:("+" ".join('"%s"'%x for x in n)+")"
G={
 "REMIFENTANIL":D("REMIFENTANIL","REMIFENTANIL HYDROCHLORIDE"),
 "FENTANYL":D("FENTANYL","FENTANYL CITRATE"),
 "SUFENTANIL":D("SUFENTANIL","SUFENTANIL CITRATE"),
 "MORPHINE":D("MORPHINE","MORPHINE SULFATE"),
 "PROPOFOL":D("PROPOFOL"),
 "MIDAZOLAM":D("MIDAZOLAM","MIDAZOLAM HYDROCHLORIDE"),
 "KETAMINE":D("KETAMINE","KETAMINE HYDROCHLORIDE"),
 "ROCURONIUM":D("ROCURONIUM BROMIDE"),
 "SEVOFLURANE":D("SEVOFLURANE"),
 "DEXMEDETOMIDINE":D("DEXMEDETOMIDINE","DEXMEDETOMIDINE HYDROCHLORIDE"),
}
T={};P={}
for k,s in G.items():
    T[k]=call(s); P[k]=call(s+' AND patient.reaction.reactionmeddrapt.exact:"PAIN"')
    print("%-16s total=%-8s PAIN=%-6s (%.3f%%)"%(k,T[k],P[k],100.0*P[k]/T[k] if T[k] else float('nan')),flush=True)
print("\n=== remifentanil 对各药 PAIN 的 RORR ===")
for k in G:
    if k=="REMIFENTANIL": continue
    ar,tr,ac,tc=P["REMIFENTANIL"],T["REMIFENTANIL"],P[k],T[k]
    if None in (ar,ac,tr,tc) or min(ar,ac,tr-ar,tc-ac)<=0:
        print("  vs %-16s 不可算 (a_r=%s a_c=%s)"%(k,ar,ac)); continue
    br,bc=tr-ar,tc-ac; lr=(ar*bc)/(br*ac); se=(1/ar+1/br+1/ac+1/bc)**.5
    print("  vs %-16s %.3f (95%%CI %.3f-%.3f)  a_r=%d a_c=%d"%(k,lr,math.exp(math.log(lr)-1.96*se),math.exp(math.log(lr)+1.96*se),ar,ac))
