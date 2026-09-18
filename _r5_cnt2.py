import json,urllib.request
BASE="https://api.fda.gov/drug/event.json"
def get(search,limit=1):
    url=BASE+"?search="+search.replace(' ','%20')+"&limit=%d"%limit
    try:
        with urllib.request.urlopen(url,timeout=60) as r: return json.load(r)
    except Exception as e:
        s=str(e)
        return {"err":("0" if "404" in s else s[:70])}
def total(search):
    j=get(search,1)
    if "err" in j: return j["err"]
    return j["meta"]["results"]["total"]
PT='patient.reaction.reactionmeddrapt.exact:"HYPERAESTHESIA"'
D=lambda s:'patient.drug.activesubstance.activesubstancename.exact:"%s"'%s
print("== 年份分布（literal +）==")
for y0,y1,lab in [("20240101","20241231","2024"),("20250101","20251231","2025"),
                  ("19000101","20231231","<=2023"),("20150101","20231231","2015-2023")]:
    for dg in ["REMIFENTANIL","REMIFENTANIL HYDROCHLORIDE","SUFENTANIL","SUFENTANIL CITRATE","MORPHINE","FENTANYL"]:
        print("  %-24s %-9s %s"%(dg,lab,total(f'{D(dg)} AND {PT} AND receivedate:[{y0}+TO+{y1}]')))
print("== version / drugcharacterization ==")
for lab,s in [("REMI v>=2",f'{D("REMIFENTANIL")} AND {PT} AND safetyreportversion:[2+TO+99]'),
              ("REMIBOTH v>=2",f'({D("REMIFENTANIL")} OR {D("REMIFENTANIL HYDROCHLORIDE")}) AND {PT} AND safetyreportversion:[2+TO+99]')]:
    print("  %-16s %s"%(lab,total(s)))
print("== REMIFENTANIL HYDROCHLORIDE 3 条记录明细 ==")
j=get(f'{D("REMIFENTANIL HYDROCHLORIDE")} AND {PT}',100)
if "err" in j: print("  ERR",j["err"])
else:
    for x in j["results"]:
        p=x.get("patient",{})
        print("  id=%s v=%s recv=%s age=%s sex=%s country=%s ndrug=%d nreac=%d"%(
          x.get("safetyreportid"),x.get("safetyreportversion"),x.get("receivedate"),
          p.get("patientonsetage"),p.get("patientsex"),
          x.get("primarysource",{}).get("reportercountry"),len(p.get("drug",[])),len(p.get("reaction",[]))))
        print("     drugs:",sorted(set((d.get("activesubstance",{}) or {}).get("activesubstancename") or d.get("medicinalproduct") for d in p.get("drug",[]))))
