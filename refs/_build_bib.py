"""由已核实的 CSL-JSON 生成 BibTeX（作者/卷期页直接取自解析结果，不手工转录）。
输入：resolved.json（12 条）+ resolved2.json（4 条）+ 手工定义的 R->DOI 映射与新编号顺序。
输出：bibliography.bib
"""
import json, re

HERE = "D:/2026.9/极速交付9月会员日优惠套路/06_FAERS单药物SOC分类安全性评估/瑞芬太尼/refs"

# R编号 -> DOI / citation key
R2DOI = {
    "R1": "10.1097/aco.0000000000001400",
    "R2": "10.1517/14740338.2014.902931",
    "R3": "10.1097/mjt.0000000000000019",
    "R4": "10.3389/fphar.2014.00108",
    "R5": "10.1093/bja/aeu137",
    "R6": "10.3389/fdsfr.2023.1323057",
    "R9": "10.1002/pds.1742",
    "R10": "10.1002/sim.2473",
    "R11": "10.1080/00031305.1999.10474456",
    "R12": "10.1002/pds.677",
    "R13": "10.1002/pds.668",
    "R14": "10.1097/00000542-200603000-00025",
    "R15": "10.1016/s0304-3959(03)00276-8",
    "R16": "10.1002/pds.5105",
    "R17": "10.1111/anae.13602",
    "R18": "10.1093/bja/aev547",
}
# 正文首次出现顺序 -> 新编号
NEWORDER = ["R1", "R14", "R18", "R2", "R3", "R5", "R15", "R17", "R6", "R7",
            "R8", "R12", "R9", "R10", "R11", "R13", "R4", "R16"]


def load():
    items = {}
    for f in ("resolved.json", "resolved2.json"):
        d = json.load(open(f"{HERE}/{f}", encoding="utf-8"))
        for it in d["items"]:
            doi = (it["csl"].get("DOI") or "").lower()
            if doi:
                items[doi] = it["csl"]
    return items


def bibtex(key, csl):
    au = csl.get("author", [])
    authors = " and ".join(
        (f"{a.get('family','')}, {a.get('given','')}".strip(", ") if a.get("family") else a.get("literal", ""))
        for a in au)
    yr = (csl.get("issued", {}).get("date-parts", [[None]])[0] or [None])[0]
    fields = [
        ("author", authors),
        ("title", (csl.get("title") or "").strip()),
        ("journal", csl.get("container-title") or ""),
        ("year", str(yr) if yr else ""),
        ("volume", csl.get("volume") or ""),
        ("number", csl.get("issue") or ""),
        ("pages", csl.get("page") or ""),
        ("doi", csl.get("DOI") or ""),
    ]
    # 清理 LaTeX 敏感字符 + 去除 Crossref 偶带的标记
    def esc(s, strip_tail_dot=False):
        s = re.sub(r"</?scp>", "", s)           # 去 <scp> 标记
        s = re.sub(r"\s{2,}", " ", s).strip()    # 压空白
        if strip_tail_dot and s.endswith("."):   # 仅题名/刊名末尾点号交给样式处理
            s = s[:-1]
        return (s.replace("&", r"\&").replace("%", r"\%").replace("_", r"\_")
                 .replace("—", "---").replace("–", "--"))
    body = ",\n".join(
        f"  {k:<8} = {{{esc(v, strip_tail_dot=(k in ('title', 'journal')))}}}"
        for k, v in fields if v)
    return f"@article{{{key},\n{body}\n}}\n"


def main():
    items = load()
    print(f"载入已核实条目: {len(items)}")
    out = []
    audit = []
    for i, r in enumerate(NEWORDER, 1):
        if r in ("R7", "R8"):
            continue
        doi = R2DOI[r].lower()
        if doi not in items:
            print(f"  !! 缺失 {r} {doi}")
            continue
        csl = items[doi]
        key = f"ref{i:02d}"
        out.append(bibtex(key, csl))
        audit.append((i, r, csl))
    open(f"{HERE}/bibliography.bib", "w", encoding="utf-8").write("\n".join(out))
    print(f"写出 bibliography.bib: {len(out)} 条")
    # 回填编号映射
    m = {r: i for i, r in enumerate(NEWORDER, 1)}
    json.dump(m, open(f"{HERE}/renumber_map.json", "w", encoding="utf-8"), indent=1)
    print("renumber_map.json:", m)
    for i, r, csl in audit:
        au = csl.get("author", [])
        a1 = (au[0].get("family", "?") if au else "?")
        print(f"  [{i:>2}] (was {r}) {a1} et al. {csl.get('container-title','?')} "
              f"{csl.get('issued',{}).get('date-parts',[['?']])[0][0]};{csl.get('volume','')}:{csl.get('page','')}")


if __name__ == "__main__":
    main()
