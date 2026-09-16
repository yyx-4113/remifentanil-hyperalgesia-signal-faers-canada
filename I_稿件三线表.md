# I 步稿件三线表 —— 已并入正文文件（本文件仅作指引）

> 状态：**已废止（superseded）**。此前本文件是 Tables 1–4 与图注的独立草稿；
> 现在它们**唯一权威地**保存在 `I_正文_IMRaD_en.md` 的 `## Tables` 与
> `## Figure legends` 两节（投稿时由 `_build_submission.py` 一并写入 `Manuscript.docx`）。
> 历史内容见 git 历史（最后一次实质版本为 commit `062c1f8`）。

## 为什么不保留第二份副本

1. **避免数字漂移**：同一份表存在两处副本时，改一处忘另一处就会产生互相矛盾的产物。
2. **门禁只认正文文件**：`_check_consistency.py` 逐格核对的是 `I_正文_IMRaD_en.md` 中的
   Table S1（两面板 54 行 × 8 列）与 Table S4（18 行 × 3 个计数列），以及
   Tables 2、3、4A、4B 中引用的每一个数字。副本不进门禁，因此不可信。

## 当前位置索引

| 内容 | 位置 |
|---|---|
| Table 1 队列规模 | `I_正文_IMRaD_en.md` → `### Table 1.` |
| Table 2 FAERS 主分析（含词典代理 PT 与 `†` 不可估计标注） | `I_正文_IMRaD_en.md` → `### Table 2.` |
| Table 3 跨库确认 | `I_正文_IMRaD_en.md` → `### Table 3.` |
| Table 4A / 4B 敏感性分析 | `I_正文_IMRaD_en.md` → `### Table 4A.` / `### Table 4B.` |
| Table S1 / S3 / S4（附件） | `I_正文_IMRaD_en.md` → `### Table S1.` / `S3.` / `S4.`；S2 为独立文件 `I_TableS2_READUS-PV_checklist.md` |
| Figure 1 / 2 图注 | `I_正文_IMRaD_en.md` → `## Figure legends` |
| 图的绘制脚本与取值来源 | `05_figures.py`（数值取自 `01_faers_results.csv`、`04_sensitivity_year_pain.csv`） |

## 2026-09-16 Amendment 1 对表的影响（摘要）

- **Table 2**：新增五个**词典代理 PT**（HYPERAESTHESIA、HYPERPATHIA、PROCEDURAL PAIN、
  CHRONIC PAIN SYNDROME、DRUG WITHDRAWAL SYNDROME）；ALLODYNIA 的两个 RORR 加 `†`
  标注 **not estimable（n = 1）**；脚注不再声称"所有可计算 RORR 均 <1"
  （PROCEDURAL PAIN vs 芬太尼 = 1.962，1.14–3.39）。
- **Table 3**：同步新增五个代理 PT 行；HYPERAESTHESIA 的跨库结论改为
  "FAERS 信号未在 Canada 复现"。
- **新增 Table S4**：18 个结局术语在两个语料中的可检索性核验（数据源
  `10_term_dictionary.csv`）。
- **Figure 1**：移出 ALLODYNIA（不可估计），增入三个可估计的代理 PT；
  词条按"承载概念的 PT / 代理 PAIN / 四个阴性对照 / 特异性探针"分组排列。
