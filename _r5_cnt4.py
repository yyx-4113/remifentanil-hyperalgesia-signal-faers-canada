import json,urllib.request,sys
BASE="https://api.fda.gov/drug/event.json"
def get(search,limit=1):
    url=BASE+"?search="+search.replace(' ','%20')+"&limit="+str(limit)
    try:
        with urllib.request.urlopen(url,timeout=50) as r: return json.load(r)
    except Exception as e:
        return {"err":("0" if "404" in str(e) else str(e)[:60])}
PT='patient.reaction.reactionmeddrapt.exact:"HYPERAESTHESIA"'
def D(s): return 'patient.drug.activesubstance.activesubstancename.exact:"'+s+'"'
j=get(D("REMIFENTANIL HYDROCHLORIDE")+" AND "+PT,100)
print("== REMIFENTANIL HYDROCHLORIDE 明细 ==")
for x in j.get("results",[]):
    p=x.get("patient",{})
    print("id=%s v=%s recv=%s age=%s sex=%s ctry=%s ndrug=%d nreac=%d"%(x.get("safetyreportid"),x.get("safetyreportversion"),x.get("receivedate"),p.get("patientonsetage"),p.get("patientsex"),x.get("primarysource",{}).get("reportercountry"),len(p.get("drug",[])),len(p.get("reaction",[]))))
sys.stdout.flush()
for lab,y0,y1 in [("le2023","19000101","20231231"),("2021","20210101","20211231")]:
    for dg in ["REMIFENTANIL","REMIFENTANIL HYDROCHLORIDE"]:
        r=get(D(dg)+" AND "+PT+" AND receivedate:["+y0+"+TO+"+y1+"]",1)
        print(lab,dg,r.get("meta",{}).get("results",{}).get("total",r.get("err")))
    sys.stdout.flush()
