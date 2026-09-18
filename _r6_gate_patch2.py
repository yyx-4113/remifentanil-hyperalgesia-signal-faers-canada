#!/usr/bin/env python
"""Round-6 gate patch, phase 2.

The Round-6 rewrite changed the manuscript's wording, its reference count, its
table inventory and two of its 2024 findings. Every assertion that hard-coded the
old state now fails. This patch re-anchors them, and - where the old assertion
was a frozen literal - replaces it with a value read from the source CSV so that
the same class of drift cannot go quiet again (project rule: a fixed-string
assertion freezes the wrong value instead of catching it).

Run:  python _r6_gate_patch2.py         (dry run, prints unmatched anchors)
      python _r6_gate_patch2.py --apply
"""
import io
import os
import re
import sys

GATE = "_check_consistency.py"
APPLY = "--apply" in sys.argv

REPS: list[tuple[str, str]] = []

# --------------------------------------------------------------------------- #
# 1. Reference count: 30 was last round's measured value. The journal allows
#    30-40, so a hard-coded 30 turns a legitimate addition into a gate failure.
#    Check the limit, the numbering, and that no citation runs off the end.
# --------------------------------------------------------------------------- #
REPS.append((
    '''    chk("参考文献条目数 == 30", len(ref_nums), 30)
    chk("参考文献编号连续 1..30", sorted(ref_nums), list(range(1, 31)))''',
    '''    # 30 是上一轮的实测值，不是刊物上限（30-40）。硬编码实测值会把"合法增删文献"
    # 变成门禁失败，也会在删文献时静默放行——改为查上限 + 查编号连续。
    chk("参考文献条目数在期刊上限 30-40", 30 <= len(ref_nums) <= 40, True)
    chk("参考文献编号连续 1..n", sorted(ref_nums), list(range(1, len(ref_nums) + 1)))''',
))

REPS.append((
    '''    chk("正文引用编号最大 == 30", max(cited) if cited else 0, 30)
    chk("正文无越界引用编号", sorted(x for x in cited if x > 30), [])
    must_contain("AI 声明参考文献计数", "all 30 cited references verified by identifier")''',
    '''    chk("正文引用编号最大 == n", max(cited) if cited else 0, len(ref_nums))
    chk("正文无越界引用编号", sorted(x for x in cited if x > len(ref_nums)), [])
    must_contain("AI 声明参考文献计数",
                 f"all {len(ref_nums)} cited references verified by identifier")''',
))

REPS.append((
    '''        ("I_投稿信_cover_letter.md",
         ["all 30 cited references verified by identifier", "30 references",
          f"is {main_words:,}".replace(",", " "), f"Summary of {summ_words} words",
          "five supplementary tables"]),
        ("SUBMISSION_MANIFEST.md",
         ["30, Vancouver style with DOIs", f"{main_words:,}".replace(",", " "),
          "with a terminology caution", "5 (S1–S5)"]),''',
    '''        ("I_投稿信_cover_letter.md",
         [f"all {len(ref_nums)} cited references verified by identifier",
          f"{len(ref_nums)} references",
          f"is {main_words:,}".replace(",", " "), f"Summary of {summ_words} words",
          "nine supplementary tables"]),
        ("SUBMISSION_MANIFEST.md",
         [f"{len(ref_nums)}, Vancouver style with DOIs",
          f"{main_words:,}".replace(",", " "),
          # 题名已改为中性的描述式题名，"with a terminology caution" 不应再出现
          "observational head-to-head disproportionality analysis", "9 (S1–S9)"]),''',
))

# --------------------------------------------------------------------------- #
# 2. Table inventory: derive the counts from the actual blocks, then check the
#    title page declares those same numbers. (Was: the literal "plus 5
#    supplementary", which died the moment the inventory changed.)
# --------------------------------------------------------------------------- #
REPS.append((
    '''    must_contain("Supplied tables 计数为 4", "plus 5 supplementary")''',
    '''    # 主表/补充表个数改为从实际表块读出，再与题名页声明比对（不固化字面）
    _n_main = len({m.group(1) for m in re.finditer(r"(?m)^### Table (\\d+)", txt)})
    _n_supp = len({m.group(1) for m in re.finditer(r"(?m)^### Table (S\\d+)", txt)})
    chk(f"题名页声明主表数 == 实测 {_n_main}",
        re.search(rf"\\b{_n_main}\\b in the main file", txt) is not None, True)
    chk(f"题名页声明补充表数 == 实测 {_n_supp}",
        re.search(rf"and {_n_supp} supplementary", txt) is not None, True)''',
))

# --------------------------------------------------------------------------- #
# 3. G-6 CHRONIC PAIN: the sentence was reworded to "returned one hit".
# --------------------------------------------------------------------------- #
REPS.append((
    '''    chk("[G-6] 正文已承认该例外", "CHRONIC PAIN returned a single hit" in txt, True)''',
    '''    chk("[G-6] 正文已承认该例外",
        re.search(r"CHRONIC PAIN[^.]{0,80}one hit", txt) is not None, True)''',
))

# --------------------------------------------------------------------------- #
# 4. G-10 leave-2024-out. Round 5 showed the old file is NOT leave-2024-out: it
#    is the 2015-2023 window. The manuscript now discloses both restrictions and
#    the numbers behind each. Bind every disclosed number to 19_*.csv.
# --------------------------------------------------------------------------- #
REPS.append((
    '''    chk("[G-10] 正文披露 'disappears when 2024 is excluded (a = 1)'",
        "disappears when 2024 is excluded (a = 1)" in txt, True)
    chk("[G-10] 正文披露 'leave-2024-out'", "leave-2024-out" in txt, True)
    chk("[G-10] 正文披露 'shared by all four opioids'", "shared by all four opioids" in txt, True)''',
    '''    # 旧断言固化了 "a = 1"，而 a = 1 属于 2015-2023 窗口、不是 leave-2024-out；
    # 真·全库剔 2024 是 a = 2。改为从 19_*.csv 读两套口径的值，逐值与正文比对。
    _l19 = P("19_leave2024_hyperaesthesia.csv")
    chk("[G-10] 两种 leave-2024 口径 CSV 存在", os.path.exists(_l19), True)
    if os.path.exists(_l19):
        _rows19 = list(csv.DictReader(open(_l19, encoding="utf-8-sig")))
        chk("[G-10] 19_*.csv 同时收录两种口径", len(_rows19), 2)
        _bad10 = []

        def _appears(raw, where):
            """值是否以某种合法排版形式出现在指定窗口内（千分位数字 / 英文数词 / 两位小数）。

            稿件对小整数写英文单词（"two reports"、"one report"），对大数写千分位
            数字（"19 373 581"），对率写两位小数（"1.01"）。三种形式都要认，否则
            断言会因为排版而非因为数值错误而失败。
            """
            try:
                fv = float(raw)
            except (TypeError, ValueError):
                return True
            _NUMW = {0: "no", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
                     6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten"}
            cands = []
            if fv == int(fv):
                n = int(fv)
                cands += [f"{n:,}".replace(",", chr(0x2009)), str(n), _NUMW.get(n, "")]
            else:
                cands.append(f"{fv:.2f}")
            for c in cands:
                if c and re.search(rf"(?<![\\d.]){re.escape(c)}(?![\\d])", where):
                    return True
            return False

        for _r in _rows19:
            _w10 = txt[txt.index("Two restrictions of this table"):][:1400]
            for _k in ("a", "cohort_n", "corpus_N", "ROR", "ROR_CI_low",
                       "ROR_CI_high", "RORR_vs_fentanyl"):
                _v = _r[_k]
                try:
                    float(_v)
                except (TypeError, ValueError):
                    continue          # 该口径下不可估（"see row 2 ..."），正文也不应写
                if not _appears(_v, _w10):
                    _bad10.append(f"{_r['definition'][:24]}/{_k}={_v}")
        chk("[G-10] 两种口径的 a/队列/N/ROR/CI 均在正文中出现", _bad10[:6], [])
    # 措辞：正文必须明确"两种口径不是一回事"，且旧的错误标签已被点名
    chk("[G-10] 正文区分两种口径",
        re.search(r"Two restrictions of this table", txt) is not None, True)
    chk("[G-10] 正文点名旧的误标",
        re.search(r"mislabelled as leave[- ]2024[- ]out", txt, re.I) is not None, True)
    chk("[G-10] 正文使用 leave-2024-out 一词",
        re.search(r"leave[- ]2024[- ]out", txt, re.I) is not None, True)
    # 2024 升高"四药共享"的说法已被否证（吗啡 0/21 不在簇内），不得复辟
    chk("[G-10] 已清除 'shared by all four opioids'",
        "shared by all four opioids" in txt, False)
    chk("[G-10] 正文改为三队列表述", "in three of the four cohorts" in txt, True)
    chk("[G-10] 正文说明吗啡不在簇内",
        re.search(r"morphine[^.]{0,240}\\bnot\\b", txt, re.I) is not None, True)''',
))

REPS.append((
    '''    chk("[G-10] 摘要披露代理为事后添加",
        "added after those zeros" in summ_text, True)
    chk("[G-10] 摘要 Results 将所报 PT 标为 proxy",
        "proxy preferred term" in summ_text, True)''',
    '''    # 不固化动词：只要"after those zeros"这个时序限定还在，措辞怎么改都算披露
    chk("[G-10] 摘要披露代理为事后添加",
        re.search(r"after those zeros", summ_text) is not None, True)
    chk("[G-10] 摘要 Results 将所报 PT 标为 proxy",
        re.search(r"proxy (?:preferred )?term", summ_text) is not None, True)''',
))

# --------------------------------------------------------------------------- #
# 5. G-11 2024 cluster: the old assertion wanted the literal ratio sequence
#    "15.4, 4.3, 4.9 and 1.7", which was removed along with the (false) claim
#    that all four opioids shared the rise. Bind to 20_*.csv instead.
# --------------------------------------------------------------------------- #
REPS.append((
    '''        chk("[G-11] 正文披露 2024 簇四药比值序列",
            "15.4, 4.3, 4.9 and 1.7" in txt, True)''',
    '''        # 旧的"四药比值序列"连同"四药共享升高"的结论一起被否证：
        # 吗啡 2024 年的 21 例中 0 例在瑞芬簇内。改为绑定 20_*.csv 的成员数。
        _clu20 = P("20_2024cluster_membership.csv")
        chk("[G-11] 2024 簇成员核验 CSV 存在", os.path.exists(_clu20), True)
        if os.path.exists(_clu20):
            _c20 = {r["query"]: int(r["reports"]) for r in
                    csv.DictReader(open(_clu20, encoding="utf-8-sig"))}
            _W = {0: "no", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
                  6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten",
                  11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen",
                  15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen",
                  19: "nineteen", 20: "twenty", 21: "twenty-one"}
            _win = txt[txt.index("That series also explains"):]
            _win = _win[:700]
            # 舒芬：簇内 7 / 2024 共 7；芬太尼：簇内 5 / 2024 共 17
            _bad11 = []
            for _drug, _k_both, _k_all in (
                    ("sufentanil", "sufentanil_with_term_2024_also_remifentanil",
                     "sufentanil_with_term_2024"),
                    ("fentanyl", "fentanyl_with_term_2024_also_remifentanil",
                     "fentanyl_with_term_2024")):
                for _k in (_k_both, _k_all):
                    _word = _W[_c20[_k]]
                    if not re.search(rf"\\b{re.escape(_word)}\\b[^.]{{0,120}}{_drug}", _win):
                        _bad11.append(f"{_k}={_c20[_k]} ({_word}) 未在 §3.3 出现")
            chk("[G-11] §3.3 披露簇成员数与源 CSV 一致", _bad11, [])
            chk("[G-11] 吗啡 2024 报告不在簇内（源 CSV）",
                _c20["morphine_with_term_2024_also_remifentanil"], 0)''',
))

# --------------------------------------------------------------------------- #
# 6. G-12: _md_rows skips only "preferred term"/"term" headers; Table 5's first
#    column is "Indication stratum".
# --------------------------------------------------------------------------- #
REPS.append((
    '''            if c[0].lower() in ("preferred term", "term") or set(c[0]) <= set("- "):''',
    '''            if (c[0].lower() in ("preferred term", "term", "indication stratum",
                                  "stratum", "report depth")
                    or set(c[0]) <= set("- ")):''',
))

# --------------------------------------------------------------------------- #
# 7. G-18: the citation normaliser dropped every S-table because "S1" is not
#    .isdigit(), and it kept "4A" while the blocks are 4A/4B/4C. Normalise both
#    sides by stripping the panel letter, and keep the S prefix.
# --------------------------------------------------------------------------- #
REPS.append((
    '''    _present = {m.group(1) + m.group(2) for m in
                re.finditer(r"(?m)^### Table (S?\\d+)([A-C]?)", txt)}
    _cited = set(re.findall(r"\\bTables?\\s(S?\\d+[A-C]?)\\b", txt.split("## Tables")[0]))
    _cited = {c for c in _cited if c.rstrip("ABC").isdigit()}
    if "4A" in _cited or "4B" in _cited or "4C" in _cited:
        _cited |= {"4"}
    chk("[G-18] 正文引用的表都有对应表块", sorted(_cited - _present), [])
    chk("[G-18] 所有表块都在正文被引用", sorted(_present - _cited), [])''',
    '''    # 两侧都按"去掉分面字母"归一：4A/4B/4C -> 4，S1 保留（旧代码用 isdigit()
    # 把全部 S 表静默丢掉，于是"表块未被引"永远查不出来）。
    _present = {re.sub(r"[A-C]$", "", m.group(1) + m.group(2)) for m in
                re.finditer(r"(?m)^### Table (S?\\d+)([A-C]?)", txt)}
    _cited = {re.sub(r"[A-C]$", "", c) for c in
              re.findall(r"\\bTables?\\s(S?\\d+[A-C]?)\\b", txt.split("## Tables")[0])}
    chk("[G-18] 正文引用的表都有对应表块", sorted(_cited - _present), [])
    chk("[G-18] 所有表块都在正文被引用", sorted(_present - _cited), [])''',
))


def main() -> int:
    s = io.open(GATE, encoding="utf-8").read()
    bad = [(o, s.count(o)) for o, _ in REPS if s.count(o) != 1]
    if bad:
        for o, n in bad:
            print(f"!! {n} matches for anchor:\n{o[:200]}")
        return 1
    for o, n in REPS:
        s = s.replace(o, n, 1)
    if APPLY:
        io.open(GATE, "w", encoding="utf-8").write(s)
    print(f"{len(REPS)} replacements {'written' if APPLY else '(dry run)'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
