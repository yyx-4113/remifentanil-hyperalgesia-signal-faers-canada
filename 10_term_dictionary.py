# -*- coding: utf-8 -*-
"""A2 核查产物：术语词典级核对（MedDRA 层级 / 双库可检索性）→ 10_term_dictionary.csv

背景（审稿意见 A2）：
  原稿把「HYPERALGESIA 等 5 个术语全库为 0」当作「结构性缺失」的证据。
  但若某串并非 MedDRA 首选语(PT)，`reactionmeddrapt.exact` 天然永远命不中，
  此时零是「词典事实」而不是「报告事实」。本脚本把这一层核对做成可复现产物。

三种核对手段（互相独立）：
  1) 全库精确检索：patient.reaction.reactionmeddrapt.exact:"TERM"
       - FAERS 侧 = 报告数；Canada 侧 = reactions.txt 中该 PT 的反应行数
       - 命中 >0 ⇒ 该串在两个语料的 MedDRA 中确实是 PT 且被使用（存证）
  2) 相邻词短语检索：patient.reaction.reactionmeddrapt:"TERM"
       - 分析字段按 token 切分；若某 PT 含相邻 token 序列即命中。
       - 返回 0 ⇒ 该串不作为 PT 出现在语料中（既不存在或从未被用）
  3) 词典级结论：HYPERALGESIA 非 PT，而是 PT HYPERAESTHESIA(MedDRA 10020568)
     下的低位语(LLT)。该结论此前只以「人工」标注、无产物支撑（Round-6 A1 Issue 4
     要求坐实而非断言），现由两条独立产物绑定：
       (i)  _r6_term_level_check.csv —— 加拿大 v.27.1 全库家族普查：家族内在用
            首选语 114 个，HYPERAESTHESIA 523 反应行，HYPERALGESIA 与
            HYPERESTHESIA 均为 0 行；
       (ii) _r6_term_dictionary_check.csv —— ADReCS v3.3（MedDRA 编码本体，15 317
            条目）中无任何条目名为 Hyperalgesia，该串作为 10020568 的同义词出现
            （另有 10050100 与 10053552 两个术语也以之为同义词，共 3 个不同术语）；
            该文件末尾另附 DECLARED_EXTERNAL_PROXIES 区块，逐条记录手工抄录的公开
            旁证及其 URL（Cochrane 给 Hyperalgesia 的 MedDRA 码 10020573、MeSH
            D006930 与 D006941 之分），供表 S4 注按值绑定。
     MedDRA 层次本身属订阅制资源，故上述均为旁证式核验、非一手词典抽取；披露见正文表 S4 注。

输出：10_term_dictionary.csv（表 S4 的数据源）
"""
import csv, io, json, os, time, urllib.error, urllib.parse, urllib.request
from _fda_auth import add_key

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = "https://api.fda.gov/drug/event.json"
CACHE = os.path.join(HERE, "_faers_cache.json")
CV_REAC = os.path.join(HERE, "cv", "cvponline_extract_20241130", "reactions.txt")
OUT = os.path.join(HERE, "10_term_dictionary.csv")

cache = json.load(open(CACHE, encoding="utf-8")) if os.path.exists(CACHE) else {}


def save():
    json.dump(cache, open(CACHE, "w", encoding="utf-8"))


def api_total(search):
    if cache.get(search) is not None:
        return cache[search]
    q = urllib.parse.urlencode(add_key({"search": search, "limit": "1"}))
    for i in range(6):
        try:
            with urllib.request.urlopen(f"{BASE}?{q}", timeout=30) as r:
                t = json.load(r).get("meta", {}).get("results", {}).get("total", 0)
            cache[search] = t
            save()
            time.sleep(0.55)
            return t
        except urllib.error.HTTPError as e:
            if e.code == 404:
                cache[search] = 0
                save()
                return 0
            if e.code in (403, 429):
                time.sleep(min(20, 2 ** i * 3))
                continue
            time.sleep(3)
        except Exception:
            time.sleep(3)
    return None


# (term, group, in_analysis, note)
TERMS = [
    ("HYPERALGESIA",             "narrow",  "yes", "not a MedDRA preferred term; lowest level term carried by the preferred term HYPERAESTHESIA (10020568); no preferred term of that name in v27.1, verified against a public MedDRA-coded ontology and against the release census"),
    ("ALLODYNIA",                "narrow",  "yes", "retrievable preferred term in both corpora"),
    ("PAIN",                     "surrogate", "yes", "retrievable preferred term in both corpora"),
    # Round-7 A3: a zero alone does not make a string a non-preferred term. Only
    # HYPERALGESIA was checked against a dictionary (ADReCS v3.3 census, _r6_* files);
    # for these four the preferred-term status is unverified, so the zero may equally be
    # disuse. The wording is deliberately two-tier.
    ("PAIN INCREASED",           "broad",   "yes", "zero in both corpora; preferred-term status not dictionary-verified, so artefact and disuse are not distinguished here"),
    ("POSTOPERATIVE PAIN",       "broad",   "yes", "zero in both corpora; preferred-term status not dictionary-verified, so artefact and disuse are not distinguished here"),
    ("CHRONIC PAIN",             "broad",   "yes", "zero in both corpora; preferred-term status not dictionary-verified, so artefact and disuse are not distinguished here"),
    ("OPIOID WITHDRAWAL SYNDROME", "broad", "yes", "zero in both corpora; preferred-term status not dictionary-verified, so artefact and disuse are not distinguished here"),
    ("DRUG TOLERANCE",           "broad",   "yes", "retrievable preferred term in both corpora"),
    ("DRUG INEFFECTIVE",         "probe",   "yes", "retrievable preferred term in both corpora"),
    ("NAUSEA",                   "negative control", "yes", "retrievable preferred term in both corpora"),
    ("VOMITING",                 "negative control", "yes", "retrievable preferred term in both corpora"),
    ("PRURITUS",                 "negative control", "yes", "retrievable preferred term in both corpora"),
    ("CONSTIPATION",             "negative control", "yes", "retrievable preferred term in both corpora"),
    # 词典代理：承载同一临床概念、且确实可检索的 PT
    # Round-7 A1/A3: HYPERAESTHESIA is where the free-text word hyperalgesia lands, but
    # it denotes sensitivity to any sensory stimulus, so it is a loose proxy, not an
    # opioid-induced-hyperalgesia term.
    ("HYPERAESTHESIA",           "dictionary proxy", "yes", "preferred term carrying it in both corpora (MedDRA 10020568); a generic term for increased sensitivity to sensory stimulation rather than a nociception-specific term, so a loose proxy for hyperalgesia"),
    ("HYPERPATHIA",              "dictionary proxy", "yes", "retrievable preferred term; painful-syndrome concept sibling explored as a sensitivity term, substituting for no planned string"),
    ("PROCEDURAL PAIN",          "dictionary proxy", "yes", "retrievable preferred term nearest to POSTOPERATIVE PAIN; expected nociceptive pain from the procedure, not hyperalgesia"),
    ("CHRONIC PAIN SYNDROME",    "dictionary proxy", "yes", "not a preferred term: the only occurrence is the free text 'chronic pain syndrome' in safetyreportid 9291134 (received 9 October 2012), which carries no reactionmeddraversionpt, whereas every coded term in that report carries v16.0"),
    ("DRUG WITHDRAWAL SYNDROME", "dictionary proxy", "yes", "retrievable preferred term nearest to OPIOID WITHDRAWAL SYNDROME; a discontinuation syndrome, not hyperalgesia"),
]

print("== 1) FAERS 全库精确检索 + 相邻词短语检索 ==")
faers_exact, faers_phrase = {}, {}
for t, *_ in TERMS:
    e = api_total(f'patient.reaction.reactionmeddrapt.exact:"{t}"')
    p = api_total(f'patient.reaction.reactionmeddrapt:"{t}"')
    faers_exact[t], faers_phrase[t] = e, p
    print(f"  {t:28s} exact={e!s:>9s}  phrase_reports={p}")

print("\n== 2) Canada Vigilance 全库 PT 精确匹配（MedDRA v27.1）==")
want = {t.upper() for t, *_ in TERMS}
cv_pt = {t: 0 for t in want}
cv_ver = {}
with io.open(CV_REAC, encoding="utf-8", errors="replace") as f:
    for i, line in enumerate(f):
        parts = [x.strip().strip('"') for x in line.rstrip("\n").split("$")]
        if len(parts) < 8:
            continue
        if len(parts) > 9:
            cv_ver[parts[9]] = cv_ver.get(parts[9], 0) + 1
        pt = parts[5].upper()
        if pt in cv_pt:
            cv_pt[pt] += 1
        if (i + 1) % 2000000 == 0:
            print(f"    reactions 行 {i+1}")
print("   MedDRA 版本分布:", cv_ver)
for t, *_ in TERMS:
    print(f"  {t:28s} canada_rows={cv_pt[t.upper()]}")

# 「计数 > 0 ⇒ 可作 PT 检索」只是一条启发式，存在一个已证反例：
#   CHRONIC PAIN SYNDROME 的 FAERS 唯一命中（safetyreportid 9291134，2012-10-09）
#   是该报告里的自由文本，不携带 reactionmeddraversionpt，而同一报告里所有已编码
#   术语都是 v16.0 —— 即它不是编码词典里的首选语。此前这一行只在 CSV 里手工改过、
#   脚本未同步，导致重新生成时把正确值冲回错误值。现在把例外写进源头，
#   使「脚本 → CSV → 表 S4」单向可复现。
RETRIEVABLE_OVERRIDE = {
    "CHRONIC PAIN SYNDROME": "no",
}

rows = []
for t, grp, inan, note in TERMS:
    e, p = faers_exact[t], faers_phrase[t]
    c = cv_pt[t.upper()]
    retrievable = RETRIEVABLE_OVERRIDE.get(t, "yes" if (e or c) else "no")
    rows.append({
        "Term": t,
        "Group": grp,
        "In_analysis": inan,
        "FAERS_reports_whole_corpus": "" if e is None else e,
        "FAERS_reports_adjacent_token_phrase": "" if p is None else p,
        "Canada_reaction_rows_whole_corpus": c,
        "Retrievable_as_preferred_term": retrievable,
        "MedDRA_level_note": note,
    })

with open(OUT, "w", newline="", encoding="utf-8-sig") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
    w.writeheader()
    w.writerows(rows)
print(f"\n写出: {OUT}")
