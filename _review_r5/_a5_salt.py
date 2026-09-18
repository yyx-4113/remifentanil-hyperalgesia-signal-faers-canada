# -*- coding: utf-8 -*-
"""A5：核对四个队列的盐形式是否一致纳入（作者对瑞芬/舒芬取了盐，对芬太尼/吗啡未取）。"""
import json,os,time,math,urllib.request,urllib.parse
HERE=os.path.dirname(os.path.abspath(__file__)); C=os.path.join(HERE,"_a5_salt_cache.json")
B="https://api.fda.gov/drug/event.json"
cache=json.load(open(C,encoding="utf-8")) if os.path.exists(C) else {}
def call(s,cnt=None):
    k=s+("||C" if cnt else "")
    if k in cache: return cache[k]
    p={"search":s,"limit":1}
    if cnt: p["count"]=cnt
    url=B+"?"+urllib.parse.urlencode(p)
    for _ in range(5):
        try:
            with urllib.request.urlopen(url,timeout=45) as r: d=json.loads(r.read().decode())
            v=({x["term"]:x["count"] for x in d.get("results",[])} if cnt else d["meta"]["results"]["total"])
            cache[k]=v; json.dump(cache,open(C,"w",encoding="utf-8"),ensure_ascii=False); time.sleep(0.4); return v
        except urllib.error.HTTPError as e:
            if e.code==404:
                cache[k]={} if cnt else 0; json.dump(cache,open(C,"w",encoding="utf-8"),ensure_ascii=False); return cache[k]
            time.sleep(3)
        except Exception: time.sleep(3)
    return None
def D(*names):
    return "patient.drug.activesubstance.activesubstancename.exact:("+" ".join('"%s"'%n for n in names)+")"
TESTS=[
 ("FENTANYL 作者的队列", D("FENTANYL")),
 ("+FENTANYL CITRATE",   D("FENTANYL","FENTANYL CITRATE")),
 ("FENTANYL CITRATE 单独", D("FENTANYL CITRATE")),
 ("MORPHINE 作者的队列", D("MORPHINE")),
 ("+MORPHINE SULFATE",   D("MORPHINE","MORPHINE SULFATE")),
 ("MORPHINE SULFATE 单独", D("MORPHINE SULFATE")),
 ("REMIFENTANIL 仅碱基", D("REMIFENTANIL")),
 ("REMIFENTANIL 作者口径", D("REMIFENTANIL","REMIFENTANIL HYDROCHLORIDE")),
 ("SUFENTANIL 仅碱基", D("SUFENTANIL")),
 ("SUFENTANIL 作者口径", D("SUFENTANIL","SUFENTANIL CITRATE")),
]
for lab,s in TESTS:
    tot=call(s); pain=call(s+' AND patient.reaction.reactionmeddrapt.exact:"PAIN"')
    pa=call(s,cnt="patient.reaction.reactionmeddrapt.exact") or {}
    pain=pa.get("PAIN",0) if isinstance(pa,dict) else pain
    print("%-26s total=%-8s PAIN=%-7s (%.2f%%)"%(lab,tot,pain,100.0*pain/tot if tot else float('nan')),flush=True)
