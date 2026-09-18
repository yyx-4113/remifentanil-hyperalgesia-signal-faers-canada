import json,urllib.request,sys
BASE="https://api.fda.gov/drug/event.json"
def total(search):
    url=BASE+"?search="+search.replace(' ','%20')+"&limit=1"
    try:
        with urllib.request.urlopen(url,timeout=40) as r: return json.load(r)["meta"]["results"]["total"]
    except Exception as e:
        s=str(e); return "0" if "404" in s else "ERR"
PT='patient.reaction.reactionmeddrapt.exact:"HYPERAESTHESIA"'
def D(s): return 'patient.drug.activesubstance.activesubstancename.exact:"'+s+'"'
drugs=["REMIFENTANIL","REMIFENTANIL HYDROCHLORIDE","SUFENTANIL","SUFENTANIL CITRATE","MORPHINE","FENTANYL"]
periods=[("2024","20240101","20241231"),("2025","20250101","20251231"),("le2023","19000101","20231231")]
for lab,y0,y1 in periods:
    for dg in drugs:
        s=D(dg)+" AND "+PT+" AND receivedate:["+y0+"+TO+"+y1+"]"
        print("%-9s %-24s %s"%(lab,dg,total(s)))
    sys.stdout.flush()
