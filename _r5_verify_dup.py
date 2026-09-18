import json,urllib.request,urllib.parse,collections
BASE="https://api.fda.gov/drug/event.json"
def q(params):
    url=BASE+"?"+urllib.parse.urlencode(params)
    with urllib.request.urlopen(url,timeout=60) as r:
        return json.load(r)
# remifentanil + HYPERAESTHESIA, full records
res=q({"search":'patient.drug.activesubstance.activesubstancename.exact:"REMIFENTANIL" AND patient.reaction.reactionmeddrapt.exact:"HYPERAESTHESIA"',"limit":100})
print("total matched:",res["meta"]["results"]["total"])
recs=res["results"]
print("returned:",len(recs))
rows=[]
for x in recs:
    rows.append({
      "safetyreportid":x.get("safetyreportid"),
      "safetyreportversion":x.get("safetyreportversion"),
      "receivedate":x.get("receivedate"),
      "receiptdate":x.get("receiptdate"),
      "age":x.get("patient",{}).get("patientonsetage"),
      "sex":x.get("patient",{}).get("patientsex"),
      "reporter":x.get("primarysource",{}).get("reportercountry"),
      "occp":x.get("primarysource",{}).get("qualification"),
      "drugs":[ (d.get("medicinalproduct") or d.get("activesubstance",{}).get("activesubstancename"), d.get("drugcharacterization"), d.get("drugstartdate"), d.get("drugindication")) for d in x.get("patient",{}).get("drug",[])],
      "nreac":len(x.get("patient",{}).get("reaction",[])),
    })
for r in rows:
    print("---")
    for k,v in r.items():
        if k=="drugs":
            print("  drugs(%d):"%len(v))
            for d in v: print("     ",d)
        else:
            print("  %s: %s"%(k,v))
