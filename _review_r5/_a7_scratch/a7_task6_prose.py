# -*- coding: utf-8 -*-
"""A7 任务6：正文（非表格）数字全扫描 —— 抽取 Summary/§1-§5/表题注/图注中每个数字及其上下文。"""
import os, re
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
lines = open(os.path.join(ROOT, "I_正文_IMRaD_en.md"), encoding="utf-8").read().splitlines()
# 只取正文主体：从 "## Summary" 到 "## 9. Number-to-source traceability"
start = next(i for i, l in enumerate(lines) if l.startswith("## Summary"))
end = next(i for i, l in enumerate(lines) if l.startswith("## 9. Number-to-source"))
num_re = re.compile(r"(?<![\w.])(\d[\d\s\u2009\u00a0,]*\.?\d*)\s*(%|times|x\b|events?|reports?|words?)?")
rows = []
for i in range(start, end):
    l = lines[i]
    if l.strip().startswith("|"): continue        # 表格行单列
    if not l.strip(): continue
    if l.strip().startswith(("#", ">", "**Word count")): continue
    for m in num_re.finditer(l):
        tok = re.sub(r"[\s\u2009\u00a0,]", "", m.group(1))
        if tok in ("", "."): continue
        ctx = l[max(0, m.start()-55):m.end()+35].replace("\n", " ")
        rows.append((i + 1, tok, m.group(2) or "", ctx))
print("正文数字 token 总数 =", len(rows))
seen = set()
out = []
for ln, tok, unit, ctx in rows:
    key = (ln, tok)
    if key in seen: continue
    seen.add(key)
    out.append("L%-5d %-12s %-8s %s" % (ln, tok, unit, ctx))
open(os.path.join(HERE, "a7_prose_numbers.txt"), "w", encoding="utf-8").write("\n".join(out))
print("去重后 =", len(out))
print("\n".join(out))
