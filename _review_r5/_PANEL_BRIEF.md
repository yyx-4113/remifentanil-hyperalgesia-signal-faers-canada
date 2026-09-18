# 独立专家审稿 — 共享简报与输出契约（Round 5, 2026-09-17）

工作目录：`D:/2026.9/极速交付9月会员日优惠套路/06_FAERS单药物SOC分类安全性评估/瑞芬太尼`

## 1. 你评的是什么

一份**单作者、拟投 *Anaesthesia*（Original Article）** 的原创研究稿件：

`I_正文_IMRaD_en.md`（英文，约 77 KB，v1.4.0）

主题：瑞芬太尼（remifentanil）在**两个国家级药物警戒库**（美国 FAERS/openFDA 为主分析；加拿大 Canada Vigilance line-listing 为验证库）中的**失衡分析（disproportionality analysis）**，与芬太尼、舒芬太尼、吗啡做头对头比较（RORR = ratio of reporting odds ratios）。题目自称落脚点是 "a terminology caution"（术语学警示）。

## 2. 独立性纪律（强制）

- **禁止读取**任何以下文件（它们记录了前几轮评审与作者回复，会污染你的独立判断）：
  `REVIEW_*.md`、`RESPONSE_*.md`、`REVISION_*.md`、`01_任务状态.md`、`00_项目总览与执行路线图.md`、`SUBMISSION_MANIFEST.md`、`GITHUB_DEPOSIT_SOP.md`、`author_verification_statement.md`。
- 也**不要**读 `_review_r5/` 下其他审稿人的输出。
- 不得假设任何"本稿已经很成熟/已通过多轮评审"的前提。**把稿件当作你第一次收到的投稿。**
- 你的每一条判断都必须来自你**亲自读到的稿件文字或源数据**。稿件里的任何一项声明，只要你可以查证，就必须查证，而不是接受它。

## 3. 必读文件（全部相对工作目录）

**核心**
- `I_正文_IMRaD_en.md`（**必须全文读完**，它同时含正文、表格、图注、§9 溯源表、§10 投稿待办）
- `ANALYSIS_PLAN.md`（作者声称的"事先定义"分析计划，含 Amendment 1）

**关键源数据（用于核对数字，不核对不算完成审稿）**
- `01_faers_results.csv` —— FAERS 主分析每个 PT 的 a 值、ROR、PRR、IC025、EBGM、RORR 及区间
- `10_term_dictionary.csv` —— 术语可检索性验证（Table S4 的源）
- `cv/cv_pt_summary.csv`、`cv/cv_drug_totals.csv`、`cv/cv_summary.md`、`cv/cv_subgroups.csv`、`cv/cv_soc_27.csv` —— 加拿大库全部结果
- `04_sensitivity_ps_only.csv`、`04_sensitivity_year_pain.csv`、`04_sensitivity_year_hyperaesthesia.csv`、`04_sensitivity_leave2024_hyperaesthesia.csv`、`04_sensitivity_2024cluster_hyperaesthesia.csv`、`04_sensitivity_estimable_years.json`
- `03_soc_27.csv`（FAERS 启发式 SOC 映射，仅探索性）
- `_faers_cache.json`（openFDA 原始缓存，含全库总数）
- `_probe_pt_enum.json`、`_probe_meddra_level.json`（作者做的 MedDRA 层级/PT 枚举探查结果）
- 仅规范类审稿人需要：`I_TableS2_READUS-PV_checklist.md`

**环境提示**
- Windows + Git Bash；python 3.13.12 全路径 `C:\Users\Administrator\.workbuddy\binaries\python\versions\3.13.12\python.exe`
- `cv/cvponline_extract_20241130/` 下的原始 txt 很大（reactions.txt 约 742 MB，report_drug.txt 约 953 MB）。若需抽查原始行，请用 `head`/`awk` 或带 `--max-count` 的检索，避免整文件读入内存。其余 CSV 都很小，可直接读。

## 4. 输出契约

把审稿意见写入 `_review_r5/<你的代号>.md`（你的代号会在你的任务里给出）。**用中文写**，引用稿件原文时保留英文原句。

必须严格使用以下结构：

```
# Round-5 独立审稿 — <代号> <角色名称>

## 0. 审稿人身份与总体结论
- 一句话专业背景（自述为该领域资深审稿人，不必虚构真名）
- **Verdict: Accept / Minor Revision / Major Revision / Reject**（Original Article 标准）
- 3–5 句理由（要具体到本稿的具体缺陷，不要泛泛而谈）

## 1. 重大问题（Major, M1…）
## 2. 重要问题（P1-1…）
## 3. 次要问题（P2-1…）
## 4. 我认为稿件站得住的地方（必须写，至少 3 条，附证据）
## 5. 需要作者明确澄清的事实性问题（逐条列出疑问，不替作者猜答案）
## 6. 我实际做的独立核查（列出你跑过的命令/读过的文件/复核出的数值与差异）
```

**每条意见必须使用这个四段式**（缺一段不算合格意见）：

- **【问题】** 一句话点明缺陷本身。
- **【证据】** 精确到 `文件:行号` 或`表格/小节 + 具体数值`。涉及数字的，必须给出你自己算出的值。
- **【为什么重要】** 对结论、可信度或期刊接受度的具体影响。要说清"如果不改，审稿人会怎么想/结论会怎样被推翻"。
- **【具体修改建议】** 给可直接粘贴的英文替换句（≥1 句），或明确的新分析/新表格规格（变量、分组、预期输出列名）。**禁止写"建议加强讨论"这类不可执行的空话。**

## 5. 质量红线

1. **禁止空泛**。每条意见都要能被执行、被验证。
2. **数字必须自己核**。凡是你引用的数字，都要说明来源文件与你复核的结果；发现稿件与源数据不一致，必须写出确切差异（稿件写 X，源文件是 Y）。
3. **不要替作者辩护**。发现的问题要直说；同时也不要为了凑数编造问题——如果你认为某处其实没问题，就在 §4 明确写"此点经核查无问题"，这同样是审稿成果。
4. **区分"算术错误"与"设计缺陷"**。后者更重要，也更难被门禁/自动检查发现。
5. 若你发现**稿件存在无法用文字修改弥补的问题**，请明说，并给出替代方案（换稿件类型、换期刊、补做什么分析）。
6. 不要提及你在使用什么工具，也不要评价审稿流程本身，只写审稿意见。
