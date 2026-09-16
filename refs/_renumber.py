"""把稿件正文引用从 [Rn] 重编号为 Anaesthesia 的 [n]（按首次出现顺序），
并用终稿参考文献表替换原“References”区块。
保留原文件备份 I_正文_IMRaD_en.md.bak_prerenumber
"""
import json, re, shutil, os

ROOT = "D:/2026.9/极速交付9月会员日优惠套路/06_FAERS单药物SOC分类安全性评估/瑞芬太尼"
MD = os.path.join(ROOT, "I_正文_IMRaD_en.md")
REFMD = os.path.join(ROOT, "refs", "references_anaesthesia.md")

m = json.load(open(os.path.join(ROOT, "refs", "renumber_map.json"), encoding="utf-8"))

txt = open(MD, encoding="utf-8").read()

# ---- 1. 备份 ----
bak = MD + ".bak_prerenumber"
if not os.path.exists(bak):
    shutil.copy2(MD, bak)
    print("已备份 ->", os.path.basename(bak))

# ---- 2. 切出正文（参考文献表之前）----
cut = txt.find("| R1 |")
body, tail = txt[:cut], txt[cut:]

# ---- 3. 重编号正文引用 ----
def repl(mo):
    nums = [m["R" + n] for n in re.findall(r"R(\d+)", mo.group(0))]
    return "[" + ", ".join(str(x) for x in nums) + "]"

new_body, n_rep = re.subn(r"\[R\d+(?:\s*,\s*R\d+)*\]", repl, body)
print(f"正文引用重编号处数: {n_rep}")

# ---- 4. 校验：正文里不应再有 R 前缀引用 ----
leftover = re.findall(r"\[R\d+[^\]]*\]", new_body)
print("残留 R 前缀引用:", leftover if leftover else "无 ✅")

# ---- 5. 用终稿参考文献表替换原 References 区块 ----
refmd = open(REFMD, encoding="utf-8").read()
# 取终稿中的条目行（去掉标题与说明引文）
ref_lines = [l for l in refmd.splitlines() if re.match(r"^\d+\. ", l)]
ref_block = ("## References\n\n"
             "References are numbered in order of first citation. Journal names are abbreviated "
             "and italicised; volume numbers are bold. Every journal reference carries a DOI, "
             "as required by *Anaesthesia*.\n\n"
             + "\n".join(ref_lines) + "\n")

# 定位原 References 区块：
#   body 中从 "## References" 到结尾 = 需要删除的部分
#   tail 中从表末的 "---" 起 = 需要保留的部分
start = new_body.find("## References")
assert start > 0, "未找到 ## References"
new_body = new_body[:start]

sep = tail.find("\n---\n")
assert sep > 0, "未在 tail 找到 References 区块结束标记"
tail = tail[sep:]

new_body = new_body + ref_block

# ---- 6. 写回 ----
open(MD, "w", encoding="utf-8").write(new_body + tail)
print("已写回", os.path.basename(MD))

# ---- 7. 报告新编号映射 ----
print("\n新编号对应关系（旧 -> 新）：")
inv = {v: k for k, v in m.items()}
for i in sorted(inv):
    print(f"  {i:>2}  <- {inv[i]}")
