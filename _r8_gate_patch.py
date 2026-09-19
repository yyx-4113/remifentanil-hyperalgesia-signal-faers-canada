# -*- coding: utf-8 -*-
"""Round-8 gate additions -- items R6-03/05/06/09/12/14/15/18/20/21/22/23.

What the gates can pin here is provenance, not framing: the reference numbering
must stay consistent after two citations were inserted, every value the paper
quotes from the two new products must equal what those products contain, and the
phrasings the review forced out (the blanket "not preferred terms" claim, the
"200 to 500" range, ten reports equalling two patients, "no ratio rises") must
not come back in a later edit.  That last family is the Round-6 lesson applied:
a prohibitive assertion, not a fixed string that a rewrite can satisfy by rote.

Both gates are patched in place; anchors are asserted to occur once.
"""
from __future__ import annotations

import io

GATE = "_check_consistency.py"
DOCX = "_verify_docx.py"

APPLIED = []


def patch(path: str, tag: str, old: str, new: str) -> None:
    s = io.open(path, encoding="utf-8").read()
    if s.count(old) != 1:
        raise SystemExit("[%s] anchor occurs %d times in %s:\n%s"
                         % (tag, s.count(old), path, old[:160]))
    io.open(path, "w", encoding="utf-8", newline="\n").write(s.replace(old, new, 1))
    APPLIED.append("%s/%s" % (path, tag))


# ---------------------------------------------------------------------------
# _check_consistency.py
# ---------------------------------------------------------------------------

# 1. the two Round-6-19 references moved when the primary citations were inserted
patch(GATE, "r6-19-needles",
      '                   "[34]", "[35]", "proxy-verified"):',
      '                   "[36]", "[37]", "proxy-verified"):')

patch(GATE, "r6-19-cite",
      '    chk("[R6-19] 正文挂上新引证 [22, 34, 35]", "[22, 34, 35]" in main_body, True)',
      '    chk("[R6-19] 正文挂上新引证 [24, 36, 37]", "[24, 36, 37]" in main_body, True)')

# 2. the proxy-role assertion was pinned to a phrase the Round-8 trim shortened;
#    keep the requirement (roles are stated and the table is cited), drop the rote string
patch(GATE, "proxy-roles",
      '        "they are not interchangeable, playing four roles" in _t7, True)',
      '        "they are not interchangeable and play four roles" in _t7, True)')

# 3. the Round-8 block, appended inside the same scope as G-23 so that it runs
G24 = '''    # ============ G-24：Round-8（第六轮 P2/P3 遗留项） ============
    _refblk8 = _t7[_t7.index("## References"):_t7.index("## Tables")]
    _refnums8 = [int(n) for n in re.findall(r"(?m)^(\\d+)\\. ", _refblk8)]
    chk("[G-24] 参考文献编号 1..37 连续无缺", _refnums8, list(range(1, 38)))
    _cited8 = {int(x) for m in re.finditer(r"\\[(\\d+(?:\\s*,\\s*\\d+)*)\\]", _t7)
               for x in m.group(1).split(",")}
    chk("[G-24] 每个引用号都有条目", sorted(_cited8 - set(_refnums8)), [])
    chk("[G-24] 两条一手机制文献入表",
        all(s in _refblk8 for s in ("Dynorphin promotes abnormal pain",
                                    "Tonic descending facilitation from the rostral ventromedial medulla")),
        True)
    chk("[G-24] 两条新文献的 DOI 正确",
        all(s in _refblk8 for s in ("10.1523/JNEUROSCI.20-18-07074.2000",
                                    "10.1523/JNEUROSCI.21-01-00279.2001")), True)
    chk("[G-24] 机制句挂上一手证据", "[1, 2, 3, 4]" in _t7, True)
    _mb8 = _t7[_t7.index("## 1. Introduction"):_t7.index("## Acknowledgements")]
    chk("[G-24] 正文不再把十份报告写成两位患者",
        re.search(r"(?<!appear to )describe two patients", _mb8) is None, True)
    chk("[G-24] 患者数已改为 at most two patients",
        _mb8.count("appear to describe at most two patients"), 3)
    chk("[G-24] 11/12 已标注为描述性计数",
        "That count is descriptive, not a test" in _t7, True)
    chk("[G-24] 信号判据注明统计报告数",
        "The floor counts reports rather than patients" in _t7, True)
    chk("[G-24] 附录 A1.3 同步该口径",
        "The floor counts reports, not patients" in _t7, True)
    chk("[G-24] 结论随行发生率免责",
        "spontaneous reporting cannot address its incidence in either direction" in _t7, True)
    chk("[G-24] PAIN 已声明非 OIH 代理",
        "not a proxy for opioid-induced hyperalgesia" in _t7, True)
    chk("[G-24] 摘要同步该框定",
        "a reporting-burden probe, not a syndrome proxy" in _t7, True)
    chk("[G-24] 疼痛幅度按原文单位复述",
        "9.4 cm on a 100 cm visual analogue scale" in _t7, True)
    chk("[G-24] 禁止旧 mm 口径复辟", "9.4 mm on a 100 mm scale" in _t7, False)
    chk("[G-24] 稀有度范围改为 216 to 540",
        "roughly one report in 216 to 540" in _t7, True)
    chk("[G-24] 禁止旧 200 to 500 复辟", "one report in 200 to 500" in _t7, False)
    chk("[G-24] READUS-PV 说明按清单实际位置",
        all(s in _t7 for s in ("body items 7d and 10", "abstract item 2e", "body item 14d")), True)
    chk("[G-24] 禁止 two items not applicable 复辟",
        "note on the two items that are not applicable" in _t7, False)
    chk("[G-24] 超长作者串已截断",
        all(s not in _t7 for s in ("Mu\\u00f1oz MA.", "Wisniewski A.")), True)
    # R6-20 直接两药头对头：产物自证 + 正文值绑定
    _d8 = list(csv.DictReader(open(P("23_direct_headtohead.csv"), encoding="utf-8-sig")))
    chk("[G-24] 直接两药头对头 29 个可估计格",
        sum(1 for r in _d8 if r["direct_OR"]), 29)
    chk("[G-24] 直接估计与已发表估计无一格跨越 1",
        [f"{r['preferred_term']}/{r['comparator']}" for r in _d8
         if r["direct_OR"] and r["published_RORR"]
         and (float(r["direct_OR"]) > 1) != (float(r["published_RORR"]) > 1)], [])
    _h2h = {r["preferred_term"]: r for r in _d8 if r["comparator"] == "FENTANYL"}
    _f3d = lambda v: "not estimable" if v in ("", None) else "%.3f" % round(float(v), 3)
    for _t8 in ("PROCEDURAL PAIN", "HYPERAESTHESIA"):
        _v8 = _f3d(_h2h[_t8]["direct_OR"])
        chk(f"[G-24] A1.11 直接估值 {_t8} vs fentanyl == {_v8}", _v8 in _t7, True)
    chk("[G-24] A1.11 指向产物", "23_direct_headtohead.csv" in _t7, True)
    # R6-21 双臂对称去重叠：产物逐格绑定表 S8，且旧的不对称读法不得复辟
    _s8 = list(csv.DictReader(open(P("24_symmetric_overlap_rorr.csv"), encoding="utf-8-sig")))
    _segS8 = _t7[_t7.index("### Table S8"):_t7.index("### Table S9")]
    _bad24 = []
    for _r in _s8:
        if not _r["RORR_both_arms_removed"]:
            continue
        _tri = "%s \\u2192 %s \\u2192 %s" % (_f3d(_r["RORR_published"]),
                                            _f3d(_r["RORR_one_arm_removed"]),
                                            _f3d(_r["RORR_both_arms_removed"]))
        if _tri not in _segS8:
            _bad24.append("%s/%s: %s" % (_r["preferred_term"], _r["comparator"], _tri))
    chk("[G-24] 表 S8 三段值与 24_ 产物逐格一致", _bad24[:5], [])
    chk("[G-24] 表 S8 注明对称口径为读数口径",
        "The symmetric restriction is the one read below" in _segS8, True)
    chk("[G-24] 禁止\\u300cno ratio rises\\u300d复辟", "no ratio rises" in _t7, False)
    # 声明字数必须等于实测（此前无人查，属第二处出现盲区）
    _spec8 = importlib.util.spec_from_file_location("_wc8", P("_wordcount.py"))
    _wc8 = importlib.util.module_from_spec(_spec8)
    _spec8.loader.exec_module(_wc8)
    _m8 = _wc8.count(_wc8.slice_between(_t7, "## 1. Introduction", "## Acknowledgements"))
    _s8w = _wc8.count(_wc8.slice_between(_t7, "## Summary", "## 1. Introduction"))
    _decl8 = re.search(r"Summary ([\\d ]+) words; main text ([\\d ]+) words", _t7)
    chk("[G-24] 声明 Summary 字数 == 实测", _decl8.group(1).replace(" ", ""), str(_s8w))
    chk("[G-24] 声明正文字数 == 实测", _decl8.group(2).replace(" ", ""), str(_m8))

'''
patch(GATE, "g24",
      'print(f"==== PASS {len(OK)} / FAIL {len(BAD)} ====")',
      G24 + 'print(f"==== PASS {len(OK)} / FAIL {len(BAD)} ====")')

# csv/re are already imported; importlib is needed for the word-count import
if "import importlib.util" not in io.open(GATE, encoding="utf-8").read():
    s = io.open(GATE, encoding="utf-8").read()
    anchor = "import csv, json, os, re, sys\n"
    if s.count(anchor) < 1:
        raise SystemExit("cannot find the import block in " + GATE)
    io.open(GATE, "w", encoding="utf-8", newline="\n").write(
        s.replace(anchor, "import csv, json, os, re, sys\nimport importlib.util\n", 1))
    APPLIED.append("%s/import-importlib" % GATE)

# ---------------------------------------------------------------------------
# _verify_docx.py
# ---------------------------------------------------------------------------

patch(DOCX, "ref-count",
      '"all 35 cited references verified by identifier"]:',
      '"all 37 cited references verified by identifier"]:')

patch(DOCX, "r8-needles",
      '        chk(f"Manuscript 含 R6-19 证据「{needle}」", needle in ms_text)',
      '''        chk(f"Manuscript 含 R6-19 证据「{needle}」", needle in ms_text)
    # Round-8：新引证、新口径与新产物都要到投稿件里，而不是只留在 markdown
    for needle in ["all 37 cited references verified by identifier",
                   "Vanderah TW", "10.1523/JNEUROSCI.20-18-07074.2000",
                   "roughly one report in 216 to 540",
                   "appear to describe at most two patients",
                   "spontaneous reporting cannot address its incidence in either direction",
                   "That count is descriptive, not a test",
                   "a reporting-burden probe, not a syndrome proxy",
                   "The floor counts reports rather than patients",
                   "9.4 cm on a 100 cm visual analogue scale",
                   "not a proxy for opioid-induced hyperalgesia"]:
        chk(f"Manuscript 含 Round-8 证据「{needle}」", needle in ms_text)
    for needle in ["A1.11", "23_direct_headtohead.csv", "24_symmetric_overlap_rorr.csv",
                   "The floor counts reports, not patients",
                   "The symmetric restriction is the one read below",
                   "body items 7d and 10", "abstract item 2e", "body item 14d"]:
        chk(f"Supporting 含 Round-8 证据「{needle}」", needle in si_text)''')

patch(DOCX, "figure-alpha",
      '                chk(f"[{f}] <= 10 MB", os.path.getsize(p) <= 10 * 1024 * 1024)',
      '''                chk(f"[{f}] <= 10 MB", os.path.getsize(p) <= 10 * 1024 * 1024)
                # Round-6 A4 #3: opaque white line art, no alpha channel
                chk(f"[{f}] 无 alpha 通道（不透明）", im.mode, "RGB")''')

print("patched:")
for a in APPLIED:
    print("   ", a)
