import json,urllib.request,urllib.parse,collections
BASE="https://api.fda.gov/drug/event.json"
def q(params):
    url=BASE+"?"+urllib.parse.urlencode(params)
    try:
        with urllib.request.urlopen(url,timeout=90) as r: return json.load(r)
    except Exception as e:
        return {"error":str(e)}
LIM=500
def fetch(search):
    out=[];skip=0
    while True:
        r=q({"search":search,"limit":LIM,"skip":skip})
        if "error" in r: print("   ERR",r["error"][:100]); return out,None
        out+=r["results"]; t=r["meta"]["results"]["total"]
        skip+=len(r["results"])
        if skip>=t or not r["results"]: break
    return out,t
COHORTS={
 "REMIFENTANIL":['REMIFENTANIL','REMIFENTANIL HYDROCHLORIDE'],
 "FENTANYL":['FENTANYL'],
 "SUFENTANIL":['SUFENTANIL','SUFENTANIL CITRATE'],
 "MORPHINE":['MORPHINE'],
}
summary={}
for dg,salts in COHORTS.items():
    recs={}
    for s in salts:
        search='patient.drug.activesubstance.activesubstancename.exact:"%s" AND patient.reaction.reactionmeddrapt.exact:"HYPERAESTHESIA"'%s
        rs,t=fetch(search)
        print("%-13s salt=%-24s total=%s returned=%d"%(dg,s,t,len(rs)))
        for x in rs: recs[x.get("safetyreportid")]=x
    n=len(recs)
    vers=collections.Counter(int(x.get("safetyreportversion") or 1) for x in recs.values())
    dates=sorted(str(x.get("receivedate")) for x in recs.values())
    key=collections.Counter((x.get("patient",{}).get("patientonsetage"),x.get("patient",{}).get("patientsex")) for x in recs.values())
    top=key.most_common(1)[0]
    print("   unique safetyreportid=%d  version dist=%s"%(n,dict(sorted(vers.items()))))
    print("   top (age,sex)=%s  -> %d/%d = %.1f%%"%(top[0],top[1],n,100*top[1]/n))
    print("   receivedate span: %s .. %s ; 2024 n=%d ; 2025 n=%d ; pre-2024 n=%d"%(
        dates[0],dates[-1],sum(d.startswith('2024') for d in dates),sum(d.startswith('2025') for d in dates),
        sum(d<'2024' for d in dates)))
    if dg=="REMIFENTANIL": print("   REMI dates:",dates)
    print()
    summary[dg]={"unique_reportid":n,"version_dist":dict(sorted(vers.items())),
                 "top_agesex":str(top[0]),"top_share_pct":round(100*top[1]/n,1)}
print(json.dumps(summary,indent=1,ensure_ascii=False))
