import json,urllib.request,urllib.parse
BASE="https://api.fda.gov/drug/event.json"
def total(search):
    url=BASE+"?"+urllib.parse.urlencode({"search":search,"limit":1})
    try:
        with urllib.request.urlopen(url,timeout=45) as r:
            j=json.load(r); return j["meta"]["results"]["total"]
    except Exception as e:
        s=str(e)
        if "404" in s: return 0
        return "ERR:"+s[:60]
PT='patient.reaction.reactionmeddrapt.exact:"HYPERAESTHESIA"'
D=lambda s:'patient.drug.activesubstance.activesubstancename.exact:"%s"'%s
tests=[
 ("REMI",              f'{D("REMIFENTANIL")} AND {PT}'),
 ("REMI_HCL",          f'{D("REMIFENTANIL HYDROCHLORIDE")} AND {PT}'),
 ("FENTANYL",          f'{D("FENTANYL")} AND {PT}'),
 ("SUFENTANIL",        f'{D("SUFENTANIL")} AND {PT}'),
 ("SUFENTANIL_CITRATE",f'{D("SUFENTANIL CITRATE")} AND {PT}'),
 ("MORPHINE",          f'{D("MORPHINE")} AND {PT}'),
 ("---- REMI by year ----",""),
 ("REMI 2024",         f'{D("REMIFENTANIL")} AND {PT} AND receivedate:[20240101+TO+20241231]'),
 ("REMI 2025",         f'{D("REMIFENTANIL")} AND {PT} AND receivedate:[20250101+TO+20251231]'),
 ("REMI <=2023",       f'{D("REMIFENTANIL")} AND {PT} AND receivedate:[19000101+TO+20231231]'),
 ("REMI version>=2",   f'{D("REMIFENTANIL")} AND {PT} AND safetyreportversion:[2+TO+99]'),
 ("---- REMI+eastern cluster drugs ----",""),
 ("REMI + SUFENTANIL", f'{D("REMIFENTANIL")} AND {D("SUFENTANIL")} AND {PT}'),
 ("REMI + FENTANYL",   f'{D("REMIFENTANIL")} AND {D("FENTANYL")} AND {PT}'),
 ("SUFENTANIL 2024",   f'{D("SUFENTANIL")} AND {PT} AND receivedate:[20240101+TO+20241231]'),
 ("MORPHINE 2024",     f'{D("MORPHINE")} AND {PT} AND receivedate:[20240101+TO+20241231]'),
 ("FENTANYL 2024",     f'{D("FENTANYL")} AND {PT} AND receivedate:[20240101+TO+20241231]'),
]
for name,s in tests:
    if not s: print(name); continue
    print("%-22s %s"%(name,total(s)))
