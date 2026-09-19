# -*- coding: utf-8 -*-
"""Round-8: retarget two Round-6 gate assertions that had gone stale.

Both were verbatim-string assertions, and both broke for the right reason --
the manuscript was deliberately changed underneath them:

  G-16 required the literal "describe two patients" in the body.  R6-15 made
  that claim an inference ("appear to describe at most two patients") and moved
  the reasoning into the Table S9 note.  Keeping the old string would have
  frozen the very over-claim R6-15 removed, so the assertion now binds the
  hedged wording in the body *and* the inference statement in the note.

  G-21 required "one report in 200 to 500", the range R6-03 corrected to
  216-540 (the true min and max of the per-drug estimate).  It now binds the
  corrected range.

This is 铁律① again: a fixed-string assertion satisfies itself by rote and
hardens whatever it happens to contain; a semantic binding to the source does
not.
"""
from __future__ import annotations

import io

GATE = "_check_consistency.py"
APPLIED = []


def patch(tag: str, old: str, new: str) -> None:
    s = io.open(GATE, encoding="utf-8").read()
    if s.count(old) != 1:
        raise SystemExit("[%s] anchor occurs %d times:\n%s" % (tag, s.count(old), old[:200]))
    io.open(GATE, "w", encoding="utf-8", newline="\n").write(s.replace(old, new, 1))
    APPLIED.append(tag)


patch("g16",
      '''    chk("[G-16] 正文与表 S9 均称十份报告 = 两名患者",
        "describe two patients" in txt and "the same patient" in _seg9, True)''',
      '''    # R6-15：患者数是内容推断，不是经验证的计数 —— 绑定改写后的措辞与表 S9 的
    # 推断声明，而不是绑定已被撤销的旧断言句（铁律①）。
    chk("[G-16] 正文把患者数写成内容推断、表 S9 说明该计数系推断",
        "appear to describe at most two patients" in txt
        and "an inference from report content rather than a verified count of patients" in _seg9,
        True)''')

patch("g21",
      '''    chk("[G-21] §4.6 给出量级", "one report in 200 to 500" in txt, True)''',
      '''    # R6-03：200-500 低估了实际区间（每药最小值 216、最大值 538），已改为 216-540
    _seg46 = txt[txt.index("4.6 Implications"):][:700]
    chk("[G-21] §4.6 给出量级", "roughly one report in 216 to 540" in _seg46, True)''')

print("retargeted:")
for a in APPLIED:
    print("   ", a)
