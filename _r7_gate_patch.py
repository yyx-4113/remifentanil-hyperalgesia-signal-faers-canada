# -*- coding: utf-8 -*-
"""Round-7 gate patch: retarget two assertions and add the G-23 block.

Retargeted
----------
1. `SUBMISSION_MANIFEST.md` carried the pre-Round-7 title fragment. It is a title-agreement
   check, so it now carries the current headline fragment.
2. `[G-21] 表 2 已说明零值语义` was keyed to one verbatim sentence. The *requirement* (the
   Table 2 footnote must say why a zero is not an observation, and must separate the
   dictionary-verified zero from the unverified ones) survived while its wording moved, and
   the gate failed anyway — the same trap as R6-19. Restated as co-occurrence checks inside
   the footnote itself.

Added (G-23)
------------
Checks the Round-7 panel showed the gate could not reach. Each is either value-bound to a
source file or prohibitive; none fixes a wording. Written at module level (indentation 0)
and executed before the tally, because an indented block placed after the `else:` branch is
parsed into that branch and silently never runs — which is how a first attempt at this patch
produced a green gate with the new checks dead.

  i.   HYPERPATHIA fentanyl (a=2) and sufentanil (a=1) must sit in `15_sparse_intervals.csv`
       with their exact lower bounds read from that file.
  ii.  `14_faers_pt_distribution.csv` must agree with `01_faers_results.csv` wherever both
       carry a preferred term (morphine DRUG TOLERANCE read 0 where the count is 79).
  iii. The openFDA access date must be stated the same way in Methods and Acknowledgements.
  iv.  Neither the Table 2 footnote nor the Figure 1 legend may assert that PAIN INCREASED,
       POSTOPERATIVE PAIN, CHRONIC PAIN or OPIOID WITHDRAWAL SYNDROME are not preferred terms.
  v.   READUS-PV item 9 may not cite a section the manuscript does not contain.
  vi.  The Canadian reaction-row count must be one number everywhere (4 474 923).
"""
import io
import os

HERE = os.path.dirname(os.path.abspath(__file__))
GATE = os.path.join(HERE, "_check_consistency.py")

OLD_MANIFEST = '          "observational head-to-head disproportionality analysis", "9 (S1–S9)"]),'
NEW_MANIFEST = ('          "how the chosen preferred term decides remifentanil hyperalgesia '
                'reporting",\n          "9 (S1–S9)"]),')

OLD_ZERO = '''    # T2-22：零值必须说明"不是观测到的计数"
    chk("[G-21] 表 2 已说明零值语义",
        "the column is numeric and cannot hold a marker for that" in txt, True)'''
NEW_ZERO = '''    # T2-22：零值必须说明"不是观测到的计数"。Round-7 起按语义而非逐字绑定：要求
    # ①数值列自身无法标注零值的成因 ②脚注区分"词典已核验"与"未经核验"。逐字断言会在
    # 正确的改写上报错（R6-19 已吃过一次），这里检查含义而不是句子。
    _fn2 = txt[txt.index("OR = reporting odds ratio"):][:3200]
    chk("[G-21] 表 2 脚注说明零值并非观测计数",
        all(k in _fn2 for k in ("numeric", "marker", "not dictionary-verified")), True)
    chk("[G-21] 表 2 脚注区分词典核验与未核验的零",
        ("dictionary-verified" in _fn2 and "disuse" in _fn2), True)'''

G23 = '''
# =========================================================================
# Round-7 补强：门禁查不到设计与框定，但下面这些是数据/溯源问题，可以也应当被钉死。
# 缩进 0、位于统计输出之前 —— 缩进的块若落在 else 分支里会静默不执行。
# =========================================================================
if os.path.exists(P(MS)):
    _t7 = open(P(MS), encoding="utf-8").read()
    _fn7 = _t7[_t7.index("OR = reporting odds ratio"):][:3200]
    _leg7 = _t7[_t7.index("**Figure 1.**"):][:1800]

    # i) HYPERPATHIA 两个稀疏格必须进表，精确下界取自该表
    _sp7 = P("15_sparse_intervals.csv")
    chk("[G-23] HYPERPATHIA 两个稀疏格已进入稀疏区间表",
        len([r for r in csv.DictReader(open(_sp7, encoding="utf-8-sig"))
             if r["case"].startswith("HYPERPATHIA")]), 2)
    _h7 = {r["case"]: r for r in csv.DictReader(open(_sp7, encoding="utf-8-sig"))}
    for _case, _want in [("HYPERPATHIA fentanyl, whole corpus (a=2)", "0.965"),
                         ("HYPERPATHIA sufentanil, whole corpus (a=1)", "1.871")]:
        if _case in _h7:
            _dg = "fentanyl" if "fentanyl" in _case else "sufentanil"
            chk(f"[G-23] HYPERPATHIA {_dg} 精确下界取自稀疏表",
                _h7[_case]["exact_lower"], _want)
            chk(f"[G-23] HYPERPATHIA {_dg} 区间出现在附录 A1.4",
                _h7[_case]["exact_conditional_CI"] in _t7, True)
    chk("[G-23] 附录 A1.4 声明六个格",
        "for the six cells that drive the sparse terms" in _t7, True)

    # ii) top-500 分布表服从权威结果表
    _a7 = {r["PT"]: r for r in
           csv.DictReader(open(P("01_faers_results.csv"), encoding="utf-8-sig"))}
    _d7 = {r["term"]: r for r in
           csv.DictReader(open(P("14_faers_pt_distribution.csv"), encoding="utf-8-sig"))}
    _bad7 = []
    for _pt, _r in _a7.items():
        if _pt not in _d7:
            continue
        for _dg in ("REMIFENTANIL", "FENTANYL", "SUFENTANIL", "MORPHINE"):
            _w = _r[f"{_dg}_a"] or "0"
            if _d7[_pt][_dg] != _w:
                _bad7.append(f"{_pt}/{_dg}: {_d7[_pt][_dg]} != {_w}")
    chk("[G-23] top-500 分布表服从权威结果表", _bad7, [])
    chk("[G-23] 吗啡 DRUG TOLERANCE 分布计数 == 79",
        _d7["DRUG TOLERANCE"]["MORPHINE"], "79")
    _m7 = sum(int(r["MORPHINE"]) for r in _d7.values())
    chk("[G-23] 吗啡术语合计与正文一致", f"{_m7:,}".replace(",", " ") in _t7, True)

    # iii) openFDA 访问日期同口径
    _mth7 = _t7[_t7.index("**FAERS (primary).**"):][:600]
    _ack7 = _t7[_t7.index("**Data availability.**"):][:1200]
    chk("[G-23] Methods 写明复核重查",
        "re-queried for verification on 18 September 2026" in _mth7, True)
    chk("[G-23] 致谢写同一口径",
        "re-queried for verification on 18 September 2026" in _ack7, True)
    chk("[G-23] 不再出现并列双访问日旧写法",
        "accessed 16 and 18 September 2026" in _t7, False)

    # iv) 禁止性：四个未核验串不得被断言为"非首选语"
    _pat7 = (r"(PAIN INCREASED|POSTOPERATIVE PAIN|CHRONIC PAIN|OPIOID WITHDRAWAL SYNDROME)"
             r"[^.]{0,200}?not (?:a )?preferred term")
    chk("[G-23] 表 2 脚注未断言四串为非首选语",
        re.search(_pat7, _fn7) is not None, False)
    chk("[G-23] 图 1 图例未断言四串为非首选语",
        re.search(_pat7, _leg7) is not None, False)
    chk("[G-23] 脚注保留词典核验与未核验的二分",
        "only HYPERALGESIA is dictionary-verified" in _fn7, True)

    # v) READUS-PV 不得引用不存在的章节 / 不得声称个案文件不可得
    _ck7 = open(P("I_TableS2_READUS-PV_checklist.md"), encoding="utf-8").read()
    chk("[G-23] READUS-PV 不引用 §3.8/§3.9 或 pseudo-signal",
        re.search(r"section 3\\.9|sections? 3\\.[89]|pseudo-signal", _ck7) is not None, False)
    chk("[G-23] READUS-PV 7d 不再声称个案文件不可得",
        "case-level FDA files" in _ck7, False)

    # vi) 加拿大反应行数全稿统一
    chk("[G-23] 反应行数统一为 4 474 923", "4 474 922 reaction rows" in _t7, False)
    chk("[G-23] 起病解析的 1 行跳过已披露",
        "422 rows and therefore skips one short row" in _t7, True)
    chk("[G-23] 表 S1 的 20 692 687 单位为 reports 而非 reactions",
        "20 692 687 reports in total" in _t7, True)

    # Round-7 内容自身的存在性（防回退）
    chk("[G-23] 题名已改为术语选择而非信号",
        _t7.splitlines()[0].startswith("# Term selection, not the drug"), True)
    chk("[G-23] HYPERAESTHESIA 已标注为泛感觉术语",
        re.search(r"HYPERAESTHESIA[^.]{0,240}sensitivity to any sensory stimulus",
                  _t7) is not None, True)
    chk("[G-23] 信号判据的下限适用于三条子句",
        "the *a* ≥ 3 floor applies to all three clauses" in _t7, True)
    chk("[G-23] 正文说明无首选语承载该综合征",
        "defining measurement is a change in pain sensitivity" in _t7, True)
    chk("[G-23] 协方差段承认一处区间翻转",
        "one interval does flip significance" in _t7, True)
    chk("[G-23] 代理组已分角色",
        "they are not interchangeable, playing four roles" in _t7, True)

'''

src = io.open(GATE, encoding="utf-8").read()
for old, new in [(OLD_MANIFEST, NEW_MANIFEST), (OLD_ZERO, NEW_ZERO)]:
    if src.count(old) != 1:
        raise SystemExit(f"ABORT: anchor found {src.count(old)}x:\n{old[:90]}")
    src = src.replace(old, new)

anchor = 'print(f"==== PASS {len(OK)} / FAIL {len(BAD)} ====")'
if src.count(anchor) != 1:
    raise SystemExit("ABORT: tail anchor not unique")
src = src.replace(anchor, G23 + anchor)
io.open(GATE, "w", encoding="utf-8", newline="").write(src)
print("gate patched: 2 retargeted + G-23 block inserted at module level")
