# 01 核心失衡分析摘要：瑞芬太尼 OIH 信号 FAERS 头对头

> 数据层：openFDA 聚合层（全历史 N = 20,692,687，与氯胺酮管线版本一致）
> 方法：四算法 ROR / PRR / IC(BCPNN) / EBGM(MGPS) + 头对头 RORR（瑞芬 vs 芬太尼 / 舒芬 / 吗啡）
> 药物字段：`patient.drug.activesubstance.activesubstancename.exact`（与氯胺酮管线一致，单一字段避免盐型/商品名重复计数）
> 生成：2026-09-16 ｜ 脚本：`01_核心FAERS失衡分析.py`

> ### ⚠️ 更正（Amendment 1，2026-09-16，同日晚于本文件初稿）
>
> 本文件 §2、§5.4、§6 原先断言「OIH 相关术语在 FAERS 中**结构性缺失**」，并把 HYPERALGESIA 等五个字符串当作**MedDRA preferred term（PT）**。**该断言错误。**
>
> 经术语层级核验：两库的 reaction 字段存的是 **PT**，而 **HYPERALGESIA 是 MedDRA 的 lowest level term（LLT）**，其父 PT 为 **HYPERAESTHESIA（MedDRA 10020568）**。因此用临床用词检索**必然得 0**，这是词典假象，不是报告缺失。改用正确的 PT 后，两库均有报告，且四个阿片（含瑞芬太尼）均达信号标准（见 §8）。
>
> 由此新增五个**词典代理 PT**（HYPERAESTHESIA、HYPERPATHIA、PROCEDURAL PAIN、CHRONIC PAIN SYNDROME、DRUG WITHDRAWAL SYNDROME）并按同一口径分析；术语可检索性逐条记录于 `10_term_dictionary.csv`（稿件 Table S4）。**下文的"结构性缺失"表述一律以 §8 为准。**

---

## 1. 队列规模（权威计数，any-role 分母）

| 药物 | 报告数 | 说明 |
|---|---|---|
| **REMIFENTANIL**（瑞芬太尼） | **5,375** | 注：方案二 2026-09-12 记 3,739，系更早/更窄口径估计；**全文以本次分析字段权威计数 5,375 为准**（写入即诚信） |
| **FENTANYL**（芬太尼） | 121,819 | 主对照（含透皮贴，适应症混杂风险最高，C1 步途径分层处理） |
| **SUFENTANIL**（舒芬太尼） | 6,513 | 第二对照 |
| **MORPHINE**（吗啡） | 56,501 | 第三对照 |

---

## 2. 关键发现一：五个临床用词不是 preferred term，全库计数为 0（**原表述"结构性缺失"已更正，见 §8**）

下列五个字符串经独立复核（原始 404 `No matches found`）**全库计数为 0**：

| 字符串 | 全库计数 | 复核 | 层级（Amendment 1 核定） |
|---|---|---|---|
| HYPERALGESIA（痛觉过敏，窄定义核心） | 0 | 404 确认 | **LLT**，父 PT 为 HYPERAESTHESIA（10020568）→ 检索必得 0 |
| PAIN INCREASED（疼痛加重，宽定义） | 0 | 404 确认 | 未能确认为现行 PT |
| POSTOPERATIVE PAIN（术后痛，宽定义） | 0 | 404 确认 | 未能确认为现行 PT |
| CHRONIC PAIN（慢性痛，宽定义） | 0 | 404 确认 | 未能确认为现行 PT |
| OPIOID WITHDRAWAL SYNDROME（阿片撤药，宽定义） | 0 | 404 确认 | 概念由 PT **DRUG WITHDRAWAL SYNDROME** 承载 |

对照（查询机制正常）：PAIN = 607,176、ABDOMINAL PAIN = 229,433、BACK PAIN = 229,419、PAIN 子串 = 2,213,093。

**结论（更正版）**：这五个零**不是**"事件从未被报告"，而是**字符串与词典不匹配**。其中 HYPERALGESIA 已被证为 LLT；改用承载同一概念的 PT（HYPERAESTHESIA 等）后，两个库都有报告。因此正确的结论是：**零必须报为"不可检索"，不能报为"缺失"**；方法学要点是检索前须先做术语可检索性核验。详见 §8。

---

## 3. 关键发现二：唯一可分析的 OIH 邻域 PT —— ALLODYNIA（异常疼痛）

| 药物 | a | ROR (95%CI) | signal |
|---|---|---|---|
| REMIFENTANIL | 1 | 3.47 (0.49–24.67) | 否（a<3，不稳定） |
| FENTANYL | 48 | 7.64 (5.72–10.20) | **是** |
| SUFENTANIL | 0 | — | 否 |
| MORPHINE | 30 | 10.15 (7.06–14.59) | **是** |

头对头 RORR（瑞芬 vs 对照）：vs 芬太尼 **0.455 (0.06–3.30)**、vs 吗啡 **0.342 (0.05–2.51)**。

**该比值不可估计（not estimable）**：瑞芬太尼仅 1 例报告（a=1），CI 宽到 0.06–3.30，任何方向性解读都不成立。可以说的只有"未见信号"；**不能说瑞芬太尼的方向与芬太尼 / 吗啡相反**（原稿此处的方向性解读已在 Amendment 1 中删除）。稿件 Table 2 以 `†` 标注 not estimable，Figure 1 不再绘入该术语。

---

## 4. 关键发现三：瑞芬太尼对所有疼痛 / 常见 AE 均呈"低报"

| PT | 瑞芬 ROR | 芬太尼 ROR | 舒芬 ROR | 吗啡 ROR | RORR 瑞芬vs芬 | RORR 瑞芬vs舒 | RORR 瑞芬vs吗 |
|---|---|---|---|---|---|---|---|
| PAIN | 0.14 (0.09–0.21) | 2.14 (2.09–2.19) | 0.51 (0.41–0.62) | 3.08 (2.99–3.18) | **0.066 (0.04–0.10)** | **0.281 (0.18–0.44)** | **0.046 (0.03–0.07)** |
| DRUG INEFFECTIVE | 0.60 (0.52–0.69) | 1.06 (1.03–1.08) | 0.77 (0.68–0.86) | 1.28 (1.24–1.32) | 0.568 (0.49–0.65) | 0.784 (0.66–0.94) | 0.47 (0.41–0.54) |
| NAUSEA † | 0.245 | 1.079 | 0.435 | 2.235 | 0.227 | 0.563 | 0.11 |
| VOMITING † | 0.527 | 1.289 | 0.544 | 2.841 | 0.409 | 0.969 | 0.185 |
| PRURITUS † | 0.419 | 0.503 | 0.320 | 1.275 | 0.833 | 1.31 | 0.328 |
| CONSTIPATION † | 0.197 | 1.616 | 0.937 | 3.148 | 0.122 | 0.21 | 0.062 |

† 阴性对照。瑞芬太尼对全部阴性对照亦呈 ROR<1（显著低于芬太尼 / 吗啡）。

---

## 5. 解读（诚实、不夸大、不越过数据）

1. **无证据支持 RIH 作为可报告的安全信号（待更正版复核）**：见 §8——用正确的 PT 复核后，四个阿片（含瑞芬太尼）在 HYPERAESTHESIA 上**均达信号标准**，只是瑞芬太尼最弱（ROR 4.73）且未在 Canada 复现。故正确表述不是"无信号"，而是"瑞芬太尼的信号最弱、依赖数据库"。
2. **"全面低报"主要是报告构成 / 适应症混杂效应，而非保护效应**：瑞芬太尼报告富集于操作 / 麻醉事件，稀释了疼痛与 AE 占比；尤其 **PAIN 的瑞芬 vs 芬太尼 RORR 极低（0.066）主要由芬太尼的疼痛富集适应症（含透皮癌痛 / 慢性痛）驱动**，属方案二已预警的"适应症混杂"，**不能解读为瑞芬太尼镇痛更好**。
3. **阴性对照设计的价值在此反转但结论稳健**：若瑞芬太尼在 OIH 上"高报"而在阴性对照上"低报"，方能支持特异性 OIH 信号；实际是阴性对照对芬太尼 / 吗啡"全部低报"，故**无法分离出任何 OIH 特异性信号**。唯一定量例外是 **PROCEDURAL PAIN vs 芬太尼 = 1.962 (1.14–3.39)**，为全局唯一显著 >1 的头对头比值（另有两个 >1 但不显著：PROCEDURAL PAIN vs 舒芬 2.124、PRURITUS vs 舒芬 1.31）。
4. **自发报告不适合检测 OIH（更正版）**：问题不在"特定 PT 缺失"，而在**临床用词与编码用词不一致**——HYPERALGESIA 是 LLT 而非 PT，检索临床用词必得 0。即便改用正确的 PT，OIH 定义的是**痛敏的定量变化**，而自发报告记录的是**离散事件**，故该数据源只能记录"识别与编码"，不能测发生率。这一点本身是重要的药物警戒方法学结论，应在讨论中前置。

---

## 6. 论文走向决策（对应方案二表 7，**Amendment 1 后已调整为"术语学警示"**）

初稿采用表 7 第 3 行路径的**强化版**（证伪 / 阴性结果）：

> *（已废弃）* No disproportionate real-world reporting of hyperalgesia with remifentanil versus other intraoperative opioids: a FAERS signal study challenging remifentanil-induced hyperalgesia
>
> **当前题名：** *Remifentanil and hyperalgesia reporting in two national pharmacovigilance databases: a head-to-head disproportionality study with negative controls defined a priori*

**Amendment 1 后定稿走向**：论证重心从"阴性（无信号）"改为**"术语学警示"**——阳性信号确实存在，但在临床用词上根本查不到；而瑞芬太尼的信号最弱、且未跨库复现。

> *Remifentanil and hyperalgesia reporting in two national pharmacovigilance databases: a head-to-head disproportionality study with negative controls defined a priori*

- 头对头 + 阴性对照 + 术语层级核验，足以支撑 **Anaesthesia / BJA / J Clin Anesth / Regional Anesthesia & Pain Medicine / Therapeutic Advances in Drug Safety** 等级投稿。
- 与方案 5-2 机制研究"呼应"价值仍在：真实世界报告层不支持"瑞芬太尼特异性的强信号"，机制层面可继续独立探讨。
- 后续若个案层（27 SOC / TTO）再发现瑞芬太尼在某一 SOC 特异富集，可微调结论；当前聚合层结论已稳定。

---

## 7. 局限与下一步（持续步骤）

- **EBGM 先验**：因 openFDA `count` 端点限流未拟合经验先验，暂用保守弱先验（α=0.5, β=1.0）；个案层 ASCII 阶段用全库 PT 边际重估。
- **药物计数差异**：瑞芬 5,375 vs 方案二 3,739 已记录（口径差异，以本次为准）。
- 后续 C–J 步严格按 `00_项目总览与执行路线图.md` 推进；本回合完成 **A（聚合层）+ B**。
- 所有数字可溯源至 `01_faers_results.csv`（已 utf-8-sig 落盘）。

---

## 8. Amendment 1（2026-09-16）：术语层级核验与更正后的结果

### 8.1 逐术语可检索性（对应 `10_term_dictionary.csv` / 稿件 Table S4）

| 术语 | 组 | FAERS 全库 | FAERS 邻接短语 | Canada 反应行 | 可作 PT 检索 |
|---|---|---:|---:|---:|---|
| HYPERALGESIA | narrow | 0 | 0 | 0 | **no**（LLT → 父 PT HYPERAESTHESIA 10020568） |
| ALLODYNIA | narrow | 1,110 | 1,110 | 29 | yes |
| PAIN | surrogate | 607,176 | 2,213,093 | 49,260 | yes |
| PAIN INCREASED | broad | 0 | 0 | 0 | no |
| POSTOPERATIVE PAIN | broad | 0 | 0 | 0 | no |
| CHRONIC PAIN | broad | 0 | 1 | 0 | no |
| OPIOID WITHDRAWAL SYNDROME | broad | 0 | 0 | 0 | no（概念由 PT DRUG WITHDRAWAL SYNDROME 承载） |
| DRUG TOLERANCE | broad | 5,013 | 8,416 | 387 | yes |
| DRUG INEFFECTIVE | probe | 1,299,278 | 1,350,940 | 208,365 | yes |
| NAUSEA | negctrl | 778,546 | 779,387 | 64,611 | yes |
| VOMITING | negctrl | 462,663 | 467,932 | 39,131 | yes |
| PRURITUS | negctrl | 372,941 | 526,363 | 46,769 | yes |
| CONSTIPATION | negctrl | 213,536 | 213,678 | 13,579 | yes |
| HYPERAESTHESIA | **dictionary proxy** | 8,161 | 9,773 | 523 | yes |
| HYPERPATHIA | **dictionary proxy** | 43 | 43 | 0 | yes |
| PROCEDURAL PAIN | **dictionary proxy** | 27,300 | 27,488 | 1,527 | yes |
| CHRONIC PAIN SYNDROME | **dictionary proxy** | 1 | 1 | 0 | yes |
| DRUG WITHDRAWAL SYNDROME | **dictionary proxy** | 87,541 | 102,179 | 1,667 | yes |

Canada 抽取包 reactions.txt 共 4,474,923 行，其中 4,474,767 行标注 MedDRA 版本（全部 v.27.1），156 行该字段为空。openFDA 不暴露逐记录版本，且 FAERS 语料跨越 2004 年起的多个季度版本，故可检索性以**两个库的实测计数**为准，而非词典查表。

### 8.2 更正后的核心结果

| 术语（PT） | 瑞芬 a | 瑞芬 ROR (95%CI) | 芬太尼 a / ROR | 舒芬 a / ROR | 吗啡 a / ROR | RORR vs 芬 | RORR vs 吗 |
|---|---:|---|---|---|---|---|---|
| **HYPERAESTHESIA** | 10 | **4.73 (2.54–8.80)** | 315 / 6.80 | 22 / 8.61 | 262 / 12.17 | 0.696 (0.37–1.31) | 0.389 (0.21–0.73) |
| HYPERPATHIA | 0 | — | — | — | — | — | — |
| PROCEDURAL PAIN | 14 | 1.98 (1.17–3.34) | 1.01 | 0.93 | 2.25 | **1.962 (1.14–3.39)** | 0.878 (0.51–1.52) |
| CHRONIC PAIN SYNDROME | 0 | — | — | — | — | — | — |
| DRUG WITHDRAWAL SYNDROME | 7 | 0.31 (0.15–0.64) | 6.71 | 1.53 | 3.69 | 0.046 (0.02–0.10) | 0.083 (0.04–0.18) |

Canada（suspect-role，报告级）：HYPERAESTHESIA 瑞芬 **0** / 芬太尼 18 / 舒芬 0 / 吗啡 30；PROCEDURAL PAIN 瑞芬 0 / 14 / 0 / 42；DRUG WITHDRAWAL SYNDROME 瑞芬 0 / 139 / 1 / 195。

**结论**：① 承载 hyperalgesia 概念的 PT 在两个库都存在，且四个阿片**均达信号标准**——原先"无术语可用"的论断被推翻；② 瑞芬太尼的信号是四者中**最弱**，且**未在 Canada 复现**（瑞芬 0 / 111，样本量不足以检验）；③ 全局唯一显著 >1 的头对头比值是 PROCEDURAL PAIN vs 芬太尼（1.962），且同样未在 Canada 复现；④ 论文定位相应从"阴性研究"改为"术语学警示"。

### 8.3 下游同步

- 稿件：§2.3 新增 Term-level verification / MedDRA releases 两段与五个词典代理；§3.2 重写为"The clinical term is not a preferred term"；新增 §3.3；Tables 2、3 增列；**新增 Table S4**；Figure 1 重绘（增入三个可估计的代理 PT，ALLODYNIA 以 not estimable 移出）。
- 输出文件：`01_faers_results.csv`、`cv/cv_pt_summary.csv`、`10_term_dictionary.csv`、`ANALYSIS_PLAN.md`（Amendment 1）、`_check_consistency.py`（385 条断言）。
