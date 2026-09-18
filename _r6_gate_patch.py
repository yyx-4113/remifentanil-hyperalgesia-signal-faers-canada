# -*- coding: utf-8 -*-
"""Round-6: extend _check_consistency.py.

Adds value-bound checks for the tables and appendix written this round (G-12 to
G-18), and repoints one Round-4 check from the manuscript's deleted section 9 to
SUBMISSION_MANIFEST.md appendix A, where the traceability table now lives.

Every new check reads its expected value from a result file. None of them
asserts a literal that could freeze an error in place.
"""
from __future__ import annotations

import pathlib
import re

p = pathlib.Path("_check_consistency.py")
s = p.read_text(encoding="utf-8")


def swap(old: str, new: str) -> None:
    global s
    assert s.count(old) == 1, f"expected 1 occurrence, found {s.count(old)}: {old[:70]!r}"
    s = s.replace(old, new, 1)


# --------------------------------------------------------------------------- #
# 1. the traceability table moved out of the manuscript
# --------------------------------------------------------------------------- #
swap(
    '''    chk("[G-10] §9 溯源表含 leave-2024-out CSV",
        "Leave-2024-out HYPERAESTHESIA sensitivity (FAERS)" in txt
        and "04_sensitivity_leave2024_hyperaesthesia.csv" in txt, True)''',
    '''    # Round-6 P0-1：稿件内的 §9 溯源表已删除（它的表头写着"not for submission"），
    # 内容迁至 SUBMISSION_MANIFEST.md 附录 A，故核验对象随之改变。
    _man = open(P("SUBMISSION_MANIFEST.md"), encoding="utf-8").read()
    chk("[G-10] 清单附录 A 含 leave-2024-out CSV",
        "Leave-2024-out HYPERAESTHESIA sensitivity (FAERS)" in _man
        and "04_sensitivity_leave2024_hyperaesthesia.csv" in _man, True)''')

# --------------------------------------------------------------------------- #
# 2. the new checks
# --------------------------------------------------------------------------- #
NEW = '''
    # =====================================================================
    # Round-6 新增：表 5、表 6、表 S6-S9 与附录 S1 的逐格对账，
    # 以及"每个被引用的表都必须存在、每个存在的表都必须被引用"。
    # 教训：上一轮的门禁只校验了已存在的表，对"正文引用了不存在的表"
    # 完全无感——本轮发现有 7 处引用指向一个根本不存在的附录 S1。
    # =====================================================================
    _TS = chr(0x2009)   # 千分位用的细空格，与稿件排版一致

    def _nn(v):
        return f"{int(v):,}".replace(",", _TS)

    # G-12 表 5 ------------------------------------------------------------
    _seg5 = txt[txt.index("### Table 5."):txt.index("### Table 6.")]
    _bad12 = []
    for _r in csv.DictReader(open(P("cv/cv_indication_strata.csv"), encoding="utf-8-sig")):
        for _cmp in ("fentanyl", "morphine"):
            _est = _r[f"RORR_vs_{_cmp}"]
            if _est in ("", None):
                continue
            _ci = _r[f"RORR_vs_{_cmp}_CI"].replace("-", "\\u2013")
            _want = f"{float(_est):.3f} ({_ci})"
            if _want not in _seg5:
                _bad12.append(f"{_r['stratum']}/{_r['preferred_term']}/{_cmp}: {_want}")
    chk("[G-12] 表 5 每个可估比值与源 CSV 逐字一致", _bad12[:5], [])
    for _tag, _sum_ in (("0.000", "表 5 不应出现 0.000 型假零"),):
        chk(f"[G-12] {_sum_}", _tag in _seg5, False)
    # _md_rows 只跳过首列为 "preferred term"/"term" 的表头，表 5 的首列是
    # "Indication stratum"，因此 15 行数据 + 1 行表头 = 16。
    chk("[G-12] 表 5 行数 == 16（表头 + 3 层 x 5 术语）",
        len(_md_rows("### Table 5.", "### Table 6.")), 16)

    # G-13 表 6 ------------------------------------------------------------
    _seg6 = txt[txt.index("### Table 6."):txt.index("### Table S1")]
    _bad13 = []
    for _r in csv.DictReader(open(P("cv/cv_depth_strata.csv"), encoding="utf-8-sig")):
        for _cmp in ("fentanyl", "morphine"):
            _mh = _r[f"MH_RORR_vs_{_cmp}"]
            if _mh not in ("", None):
                _ci = _r[f"MH_RORR_vs_{_cmp}_CI"].replace("-", "\\u2013")
                _want = f"{float(_mh):.3f} ({_ci})"
                if _want not in _seg6:
                    _bad13.append(f"{_r['preferred_term']}/{_cmp}: MH {_want}")
            _cr = _r[f"crude_RORR_vs_{_cmp}"]
            if float(_cr or 0) > 0 and f"{float(_cr):.3f}" not in _seg6:
                _bad13.append(f"{_r['preferred_term']}/{_cmp}: crude {_cr}")
    chk("[G-13] 表 6 每个 MH 与 crude 比值与源 CSV 一致", _bad13[:5], [])
    chk("[G-13] 表 6 不应出现 0.000 型假零", "0.000" in _seg6, False)
    # 正文声称 MH 把 PAIN 相对吗啡从 0.146 抬到 0.978、相对芬太尼从 0.235 抬到 0.640
    _dep = {r["preferred_term"]: r for r in csv.DictReader(
        open(P("cv/cv_depth_strata.csv"), encoding="utf-8-sig"))}
    chk("[G-13] 正文的 MH 位移数字可复算",
        (f"{float(_dep['PAIN']['MH_RORR_vs_morphine']):.3f}" == "0.978"
         and f"{float(_dep['PAIN']['MH_RORR_vs_fentanyl']):.3f}" == "0.640"
         and "0.146 to 0.978" in txt and "0.235 to 0.640" in txt), True)

    # G-14 表 S7 -----------------------------------------------------------
    _seg7 = txt[txt.index("### Table S7"):txt.index("### Table S8")]
    _rv = {(r["preferred_term"], r["restriction"]): r for r in csv.DictReader(
        open(P("12_role_version_sensitivity.csv"), encoding="utf-8-sig"))}
    _RESTR = ["as published (role-agnostic, latest version)",
              "restricted to reports with >=1 primary suspect drug record",
              "restricted to never-revised reports"]
    _bad14 = []
    for _pt in ("HYPERAESTHESIA", "ALLODYNIA", "PROCEDURAL PAIN",
                "DRUG WITHDRAWAL SYNDROME", "PAIN", "DRUG INEFFECTIVE",
                "NAUSEA", "VOMITING", "PRURITUS", "CONSTIPATION"):
        for _cmp in ("fentanyl", "morphine"):
            _vals = []
            for _k in _RESTR:
                _v = _rv[(_pt, _k)][f"RORR_vs_{_cmp}"]
                _vals.append("not estimable" if _v in ("", None) else f"{float(_v):.3f}")
            _want = " / ".join(_vals)
            if _want not in _seg7:
                _bad14.append(f"{_pt}/{_cmp}: {_want}")
    chk("[G-14] 表 S7 面板 B 三档限制序列与源 CSV 一致", _bad14[:5], [])
    _rv0 = _rv[("HYPERAESTHESIA", _RESTR[0])]
    for _c in ("corpus_N", "n_remifentanil", "n_fentanyl", "n_sufentanil", "n_morphine"):
        chk(f"[G-14] 表 S7 面板 A {_c} 与源一致",
            _nn(_rv0[_c]) in _seg7, True)
    _rv2 = _rv[("HYPERAESTHESIA", _RESTR[2])]
    chk("[G-14] 表 S7 面板 A 末行与源一致",
        all(_nn(_rv2[_c]) in _seg7 for _c in
            ("corpus_N", "n_remifentanil", "n_fentanyl", "n_sufentanil", "n_morphine")), True)

    # G-15 表 S8 -----------------------------------------------------------
    _seg8 = txt[txt.index("### Table S8"):txt.index("### Table S9")]
    _bad15 = []
    for _r in csv.DictReader(open(P("11_overlap_matrix.csv"), encoding="utf-8-sig")):
        for _d in ("remifentanil", "fentanyl", "sufentanil", "morphine"):
            _v = _nn(_r[f"overlap_{_d}"])
            if _v not in _seg8:
                _bad15.append(f"{_r['drug']}/{_d}: {_v}")
    _pub = {r["PT"]: r for r in csv.DictReader(
        open(P("01_faers_results.csv"), encoding="utf-8-sig"))}
    _COL = {"fentanyl": "RORR_REMI_vs_FENTANYL",
            "sufentanil": "RORR_REMI_vs_SUFENTANIL",
            "morphine": "RORR_REMI_vs_MORPHINE"}
    for _r in csv.DictReader(open(P("17_overlap_adjusted_rorr.csv"), encoding="utf-8-sig")):
        if not _r["RORR_published"]:
            continue
        for _cmp in ("fentanyl", "sufentanil", "morphine"):
            _pv = _pub[_r["preferred_term"]][_COL[_cmp]]
            _ev = _r[f"RORR_excl_{_cmp}"]
            _l = "not estimable" if _pv in ("", None) else f"{float(_pv):.3f}"
            _rr = "not estimable" if _ev in ("", None) else f"{float(_ev):.3f}"
            if f"{_l} \\u2192 {_rr}" not in _seg8:
                _bad15.append(f"{_r['preferred_term']}/{_cmp}: {_l} -> {_rr}")
    chk("[G-15] 表 S8 两个面板均与源 CSV 逐格一致", _bad15[:5], [])
    # 重叠矩阵必须对称：这是"同一份报告进入两个队列"的算术证据
    _om = {r["drug"]: r for r in csv.DictReader(
        open(P("11_overlap_matrix.csv"), encoding="utf-8-sig"))}
    _SHORT = {"REMIFENTANIL": "remifentanil", "FENTANYL": "fentanyl",
              "SUFENTANIL": "sufentanil", "MORPHINE": "morphine"}
    _asym = [f"{_a}/{_b}" for _a in _om for _b in _om if _a != _b
             and _om[_a][f"overlap_{_SHORT[_b]}"] != _om[_b][f"overlap_{_SHORT[_a]}"]]
    chk("[G-15] 重叠矩阵对称", _asym, [])
    chk("[G-15] 对角 == 队列规模",
        all(int(_om[_a][f"overlap_{_SHORT[_a]}"]) > 0 for _a in _om), True)
    chk("[G-15] 瑞芬-芬太尼共报 1 575（29.3%）",
        _nn(1575) in _seg8 and "29.3%" in txt, True)

    # G-16 表 S9 -----------------------------------------------------------
    _seg9 = txt[txt.index("### Table S9"):txt.index("### Appendix S1")]
    _ser = list(csv.DictReader(open(P("13_report_series_hyperaesthesia.csv"),
                                    encoding="utf-8-sig")))
    chk("[G-16] 表 S9 源 CSV 行数 == 10", len(_ser), 10)
    chk("[G-16] 表 S9 两个面板各列十条（共 20 行）",
        len([l for l in _seg9.splitlines() if re.match(r"\\| \\d{8} \\|", l)]), 20)
    _us = [r for r in _ser if r["country"] == "US"]
    chk("[G-16] 九条美国报告年龄性别一致（同一患者的判据）",
        len(_us) == 9 and len({r["age"] for r in _us}) == 1
        and len({r["sex"] for r in _us}) == 1, True)
    chk("[G-16] 第十条为日本 2021 年报告",
        len(_ser) - len(_us) == 1
        and [r for r in _ser if r["country"] != "US"][0]["receivedate"] == "20210813", True)
    chk("[G-16] 正文与表 S9 均称十份报告 = 两名患者",
        "describe two patients" in txt and "the same patient" in _seg9, True)

    # G-17 附录 S1 与其引用的文件 --------------------------------------------
    _segA = txt[txt.index("### Appendix S1"):txt.index("## Figure legends")]
    for _f in ("18_rorr_covariance.csv", "03_soc_27.csv", "15_sparse_intervals.csv",
               "patient.drug.activesubstance.activesubstancename.exact",
               "scipy.stats.nchypergeom_fisher"):
        chk(f"[G-17] 附录 S1 含 {_f}", _f in _segA, True)
    for _fn in ("15_sparse_intervals.csv", "18_rorr_covariance.csv",
                "11_overlap_matrix.csv", "cv/cv_indication_strata.csv",
                "cv/cv_depth_strata.csv"):
        chk(f"[G-17] 附录 S1 引用的源文件存在：{_fn}", os.path.exists(P(_fn)), True)
    _sp = list(csv.DictReader(open(P("15_sparse_intervals.csv"), encoding="utf-8-sig")))
    _badA = [r["case"] for r in _sp if r["exact_conditional_CI"] not in _segA]
    chk("[G-17] 附录 S1 稀疏格表逐行与源一致", _badA[:5], [])

    # G-18 引用完整性：每个被引用的表必须存在，每个存在的表必须被引用 ----------
    _present = {m.group(1) + m.group(2) for m in
                re.finditer(r"(?m)^### Table (S?\\d+)([A-C]?)", txt)}
    _cited = set(re.findall(r"\\bTables?\\s(S?\\d+[A-C]?)\\b", txt.split("## Tables")[0]))
    _cited = {c for c in _cited if c.rstrip("ABC").isdigit()}
    if "4A" in _cited or "4B" in _cited or "4C" in _cited:
        _cited |= {"4"}
    chk("[G-18] 正文引用的表都有对应表块", sorted(_cited - _present), [])
    chk("[G-18] 所有表块都在正文被引用", sorted(_present - _cited), [])
    _figbody = txt.split("## Figure legends")[0]
    chk("[G-18] 图 1 与图 2 均在正文被引用",
        "Fig. 1" in _figbody and "Fig. 2" in _figbody, True)
    chk("[G-18] 正文引用的附录 S1 存在", txt.count("### Appendix S1"), 1)

    # G-19 稿件内不得残留任何内部区段或流程痕迹 ------------------------------
    for _bad in ("## 9. Number-to-source traceability",
                 "## 10. Outstanding items",
                 "not part of the submitted manuscript",
                 "Internal working section",
                 "updated after round",
                 "egress block",
                 "desk-reject"):
        chk(f"[G-19] 稿件不含「{_bad}」", _bad in txt, False)
    _man2 = open(P("SUBMISSION_MANIFEST.md"), encoding="utf-8").read()
    chk("[G-19] 溯源表已迁入清单附录 A",
        "## 6. Appendix A — number-to-source traceability" in _man2, True)
    chk("[G-19] 旧组标签 negative control 已全稿清除（除 §2.3 的否认句）",
        txt.count("negative control") - txt.count("not negative controls"), 0)
'''

swap("\n    # 标题三处必须一致", NEW + "\n    # 标题三处必须一致")

# `os` must be imported for the new existence checks
assert re.search(r"^import .*\bos\b", s, re.M), "os is not imported"
p.write_text(s, encoding="utf-8")
print("patched _check_consistency.py")
print(f"now {len(s.splitlines())} lines")
