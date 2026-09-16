"""通过 NCBI E-utilities 用 DOI 反查 PMID，再取 PubMed 官方题录，与 Crossref 侧逐项比对。
只读查询；输出 pubmed_verify.json 供人工复核，不改动任何稿件。
"""
import urllib.request, urllib.parse, json, time, re

EMAIL = "960856791@qq.com"
EUTILS = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"

DOIS = [
    "10.1097/ACO.0000000000001400",
    "10.1517/14740338.2014.902931",
    "10.1097/MJT.0000000000000019",
    "10.3389/fphar.2014.00108",
    "10.1093/bja/aeu137",
    "10.3389/fdsfr.2023.1323057",
    "10.1002/pds.1742",
    "10.1002/sim.2473",
    "10.1080/00031305.1999.10474456",
    "10.1002/pds.677",
    "10.1002/pds.668",
    "10.1097/00000542-200603000-00025",
    "10.1016/S0304-3959(03)00276-8",
    "10.1002/pds.5105",
    "10.1111/anae.13602",
    "10.1093/bja/aev547",
]


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": f"ref-check/1.0 (mailto:{EMAIL})"})
    with urllib.request.urlopen(req, timeout=45) as r:
        return r.read().decode("utf-8", "ignore")


def esearch_pmid(doi):
    u = f"{EUTILS}/esearch.fcgi?" + urllib.parse.urlencode(
        {"db": "pubmed", "term": f'"{doi}"[DOI]', "retmode": "json", "email": EMAIL})
    try:
        j = json.loads(fetch(u))
        ids = j.get("esearchresult", {}).get("idlist", [])
        return ids[0] if ids else None
    except Exception as e:
        return f"ERR:{type(e).__name__}"


def esummary(pmids):
    if not pmids:
        return {}
    u = f"{EUTILS}/esummary.fcgi?" + urllib.parse.urlencode(
        {"db": "pubmed", "id": ",".join(pmids), "retmode": "json", "email": EMAIL})
    j = json.loads(fetch(u))
    return j.get("result", {})


def main():
    mapping = {}
    for doi in DOIS:
        pmid = esearch_pmid(doi)
        mapping[doi] = pmid
        print(f"{doi:<40} -> {pmid}")
        time.sleep(0.4)
    good = [p for p in mapping.values() if p and not str(p).startswith("ERR")]
    summ = esummary(good)
    out = []
    for doi, pmid in mapping.items():
        rec = summ.get(str(pmid), {}) if pmid else {}
        au = [a.get("name", "") for a in rec.get("authors", [])]
        item = {
            "doi": doi,
            "pmid": pmid,
            "title": rec.get("title", ""),
            "journal": rec.get("fulljournalname", ""),
            "source": rec.get("source", ""),
            "volume": rec.get("volume", ""),
            "issue": rec.get("issue", ""),
            "pages": rec.get("pages", ""),
            "pubdate": rec.get("pubdate", ""),
            "authors": au,
        }
        out.append(item)
        print("-" * 80)
        print(f"DOI  {doi}")
        print(f"PMID {pmid or '未检索到'}")
        print(f"题名 {(item['title'] or '')[:100]}")
        print(f"期刊 {item['journal']} ({item['source']}) {item['pubdate']}; {item['volume']}({item['issue']}): {item['pages']}")
        print(f"作者 {'; '.join(au)}")
    json.dump(out, open("pubmed_verify.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("\n写出 pubmed_verify.json")


if __name__ == "__main__":
    main()
