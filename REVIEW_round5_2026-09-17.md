# Round-5 独立审稿总报告

**稿件**：`I_正文_IMRaD_en.md`（v1.4.0，单作者，拟投 *Anaesthesia* Original Article）
**审稿日期**：2026-09-17
**面板构成**：7 位**全新**审稿人（A1–A7），与前四轮评审面板无重叠
**汇总人**：主编（本轮以"第一次收到该投稿"的立场独立复核了每条最严重发现）

---

## 0. 独立性声明（本轮的方法学前提）

本轮唯一不同于前四轮的地方是**强制独立性**。执行方式：

1. 新建共享简报 `_review_r5/_PANEL_BRIEF.md`，明列**禁止读取**的文件：`REVIEW_*.md`、`RESPONSE_*.md`、`REVISION_*.md`、`01_任务状态.md`、`00_项目总览与执行路线图.md`、`SUBMISSION_MANIFEST.md`、`GITHUB_DEPOSIT_SOP.md`、`author_verification_statement.md`，并禁止读取同目录下其他审稿人输出。
2. 简报中明确写入："不得假设任何'本稿已经很成熟/已通过多轮评审'的前提。**把稿件当作你第一次收到的投稿。**"
3. 7 位审稿人均在各自报告的 §6 中声明了未读前轮材料，且**均未**提及"已修过/已通过"类先验。

**结果**：本轮 7 份意见合计 3 170 行 / 约 460 KB，是四轮以来第一次出现"多位独立审稿人不约而同击中同一处数据级缺陷"的情况（见 §4）。这本身是独立性纪律生效的证据——若存在先验污染，审稿人会倾向于复述前轮已解决的问题。

### 面板构成与 Verdict

| 代号 | 角色 | Verdict | 独立核查的最低层级 |
|---|---|---|---|
| A1 | 临床麻醉学 / OIH 专家 | **Major Revision** | 原始报告字段 + 临床文献（含指定遗漏文献） |
| A2 | 药物警戒信号检测方法学家 | **Major Revision** | openFDA 逐页取个案记录 + 交互式查询 |
| A3 | 生物统计学家 | **Major Revision** | 自建 2×2 + 三种区间估计并行重算 |
| A4 | MedDRA 术语学与数据字典专家 | **Major Revision** | 逐条调阅原始报告 + 词典层级外部查证 |
| A5 | 药物流行病学 / 因果推断 | **Major Revision** | 加拿大原始适应证表 join + MH 分层 |
| A6 | 资深编委 + READUS-PV/格式规范 | **Major Revision** | 期刊指南逐条取证 + Crossref + GitHub API |
| A7 | 数据溯源与计算审计 | **Minor Revision** | 字节级流式解析 2.1 GB 原始 line-listing |

**Verdict 分布：6 Major + 1 Minor。无 Accept。**

**关于 A7 的 Minor（重要裁断）**：A7 在报告开头即自我限定"本轮只做一件事：独立重算与逐格比对。**我不评价写作风格。**"他给 Minor 是**正确且诚实的**——就"数字与源文件的吻合度"这一维度，稿件确实近乎无瑕（1 196 格中仅 2 格双重舍入、加拿大侧端到端 0 处不符）。但 A7 的 Minor **不覆盖设计级问题**，而设计级问题（§3 T0）恰是本轮的核心。因此**本报告以 A2–A6 的一致判定为准：Major Revision**；A7 的 Minor 应读作"算术层面干净"的独立认证，而不是"本轮可小修"的结论。

---

## 1. 一句话结论

稿件的方法学骨架（术语可检索性核验 + 跨库头对头负对照）是真实且有价值的，**但它的"修正后主发现"在数据层面站不住**：承载全文结论的 10 条瑞芬太尼 HYPERAESTHESIA 报告中，**9 条是同一个 76 岁男性病例的系列上报**；而稿件用来解释"2024 年抬升为四药共有"的证据，经复核**就是这同一簇被重复计入四个队列**。这不是措辞问题，是结论的方向问题。

**同时必须说清：这个缺陷不来自作者的疏忽，而来自公开聚合层的结构性特性**——openFDA 的 `count`/`search` 界面不暴露报告者身份、不便于跨药交叉核对，四个队列的重叠在聚合层是隐形的。作者已经主动做了四轮自检，并把最脆弱的数字（leave-2024-out）印在摘要里，说明作者没有藏问题。**缺陷是被发现的，不是被掩盖的**——这一点决定了本稿的正确出路是**重构论证 + 补做少数可执行的分析**，而非撤稿。

---

## 2. 交叉验证总表：稿件声称 vs 独立复核值

本表是本轮最有价值的部分。左列为稿件原文主张，右列为审稿人/主编**亲手算出**的值。

| # | 稿件位置 | 稿件声称 | 独立复核值 | 复核人 | 判定 |
|---|---|---|---|---|---|
| 1 | §3.3 / §4.1 / §5 | 瑞芬太尼 HYPERAESTHESIA a = 10，构成"10 例" | **a = 10 = REMIFENTANIL 7 + REMIFENTANIL HYDROCHLORIDE 3**；其中 **9 条为同一病例簇**（76 岁男性、US、同一围术期七药配伍、2024-10-07 → 2025-03-25），第 10 条为 2021-08-13 日本 45 岁女性（盐型） | A4 + **主编亲验** | **推翻** |
| 2 | §3.8 | "The 2024 elevation is shared by all four opioids … pointing to a 2024 coding or reporting shift rather than a remifentanil-specific event" | **SUFENTANIL 2024 年 HYPERAESTHESIA = 7，这 7 条 100% 落在瑞芬簇内（7/7）**；芬太尼 2024 年 17 例中仅 5 例在簇内 | A4 + **主编亲验** | **反转为：同一簇被计入四臂** |
| 3 | 全稿 | 四队列独立、头对头比较 | 瑞芬队列 **1 575/5 375 = 29.3%** 同时含芬太尼；HYPERAESTHESIA 10 例中 **6 例**同时含芬太尼、**8 例**同时含舒芬太尼 | A2 + **主编亲验** | **不成立** |
| 4 | §3.3 / §5 | "weakest of the four"、RORR 0.696 (0.37–1.31) | 剔除共同报告后 **0.393 (0.15–1.06)**；保留每例最新版本后 **0.979 (0.48–1.99)** | A2 | **不成立** |
| 5 | §3.8 / 摘要 | leave-2024-out → a = 1，ROR 0.70 (0.10–4.98)，signal 消失 | 该口径实为"**限定 2015–2023**"（丢弃 1 129 份 2015 年前报告）；真·全库剔 2024 为 **a = 2、0.943 (0.236–3.774)**；且 4.73 落在剔除后 CI (0.099–4.978) 内 | A3 + A6-P2-6 | **口径错 + 不具判别力** |
| 6 | §5 | "the four negative controls … could not be tested in Canada" | 加拿大 VOMITING **可算**：REMI 3 / FEN 124 / SUF 1 / MOR 508 → **RORR vs FEN = 1.066、vs MOR = 0.392**（方向与 FAERS 的 0.409 **相反**） | A7 + A5 + **主编亲验** | **与源数据矛盾** |
| 7 | §2.4 | "Both ratios share the same background reference, so comparator-specific terms cancel" | FAERS 侧**不抵消**：HYPERAESTHESIA 的 c_R = 8151 vs c_F = 7846（差 3.9%）；按稿件自己承诺的"计数直推"得 **0.719** 而非 0.696（差 3.3%） | A7 | **描述与实现不符** |
| 8 | §2.4 | "the ignored covariance is under 0.001% of the variance, so it is conservative" | 实为 **0.12%–0.25%**（差约 120–250 倍）；方向（保守）成立，量级错 | A7 + A3 | **量级错 100 倍** |
| 9 | §2.2 / §4.5 | "a role-restricted analysis was not possible, the case-level file … being inaccessible"；"The FDA case-level files could not be retrieved" | `patient.drug.drugcharacterization` 在 20 692 690/20 692 687 条上存在；`search` 直接返回嵌套 `patient.drug` 数组 | A2 | **声明不成立** |
| 10 | §2.3 | "the two a priori hyperalgesia outcomes (HYPERALGESIA, ALLODYNIA) produced no estimable result" | ALLODYNIA 在瑞芬 a = 1，2×2 无空格，OR 3.47 (0.49–24.67) **可估**（稿件自己在 Table 2 印了） | A7 | **"可估"≠"达阈值"混淆** |
| 11 | 全稿 | HYPERAESTHESIA 承载 hyperalgesia 概念 | 作者自己在 §4.4 承认其 "is not pain-specific"；换用 INADEQUATE ANALGESIA (8 465) 后**瑞芬 ROR 5.016 反超**舒芬 3.761、吗啡 3.576 | A1 + A4 | **代理关系不成立** |
| 12 | §3.7 SOC 级 | 加拿大免疫类"elevated ratios"（2.363；1.792 vs fentanyl） | n = 111 队列中 Immune 仅 **9 例**；加拿大全库功效 **0.19%**，80% 功效需 ROR ≈ 88 | A3 + A6 | **点估计不可解读** |
| 13 | §2.4 | "All computations used Python 3.13.14 and matplotlib 3.11.1" | 实测 `3.13.14 (main, Jun 11 2026)`、`matplotlib 3.11.1` | A6 + A7 | **属实（无问题）** |
| 14 | 首页 | "main text 4 000 words"、"Tables: 4" | 正文实测 **3 789–3 996**（四种口径）；表对象实为 **6**（1、2、3、4A、4B、4C） | A6 + A7 | **声明不实** |
| 15 | Table 4C 注 | "so the table holds nine rows" | 表体 **10 行**（2015–2024）；瑞芬列合计 9 | A7 + A6 | **与表体冲突** |
| 16 | §3.4 | "The same pattern held for every negative control across all three comparators" | 12 个可算比值中 **11 < 1、1 > 1**（PRURITUS vs sufentanil 1.310）；同句后半段自己否定了前半段 | A7 | **同句自相矛盾** |
| 17 | Table S3 | Morphine 18–64 岁 54.4%；Fentanyl Female 43.2% | **54.3%**（4171/7675 = 54.3453）；**43.1%**（2106/4881 = 43.1469）——双重舍入 | A7 | **两格错 0.1pp** |
| 18 | Table S3 | FENTANYL 与 MORPHINE 的 "Other health professional" 均为 2 056 | **真实巧合**。用原始 line-listing 独立重算确认；两列各自与队列精确闭合（4 881 / 7 675），其余六类互不相同 | A7 + A6（A6 列为待澄清） | **经查无误** |
| 19 | Table S2 题注 | READUS-PV 引为 [10, 11] | 本稿 [10] = Angst 2003、[11] = Yu 2016；READUS-PV 是 **[13, 14]** | A6 | **引用编号错** |
| 20 | refs 29、30 | 各列 7 位作者 | Crossref 核实**恰为 7 位**，本刊规则应为"前 3 位 + et al." | A6 | **格式违规** |
| 21 | Figure 1 图注 | "Terms are grouped from the top: … (HYPERAESTHESIA) … (DRUG INEFFECTIVE)" | 图内**自下而上**为 HYPERAESTHESIA → … → DRUG INEFFECTIVE，与图注**上下颠倒** | A6 + A7 | **方向写反** |
| 22 | §9 溯源表 | "每个数字都可溯源到源文件" | 10 处正文数字在 §9 找不到映射（11 882 968、5 270、15.4 系列、8、300/4 000…）；第 539 行少一个竖线致表格断裂 | A7 | **声明过强** |
| 23 | AI 声明 | "Every reported value is a direct read of the analysis output files by the archived scripts" | `05_figures.py:179–185` 中 Figure 2 的全部数值是**手写常量**（经核与源 CSV 一致，但非运行期读取） | A6 | **声明与实物不符** |
| 24 | 全稿 | "defined a priori"（**11 处**） | `ANALYSIS_PLAN.md:5`："This plan was written **post hoc**, once the data had been retrieved" | A6 + A3 | **可核查的不实陈述** |

**复核结论的可信度说明**：#1、#2、#3、#6 四条是主编**亲手验证**的（脚本 `_r5_editor_verify.py`、`_r5_editor_verify3.py`，原始输出 `_r5_editor_out.txt`、`_r5_editor_out3.txt`），不依赖任何审稿人的中间文件；#7、#8、#17、#18 由 A7 以原始 line-listing 端到端复现；#9、#16 由 A2/A7 以原始接口实测。

---

## 3. 分级问题清单（合并去重后）

### T0 — 结论级（不解决则结论不成立）

**T0-1｜"修正后主发现"实为单一来源病例簇（A4-M1；A1-M1；A2-M1/M2 从重叠与版本两个角度独立触及）**
- 10 条瑞芬 HYPERAESTHESIA 报告中 9 条为同一 76 岁男性病例的系列上报（同一美国报告者、同一七药围术期配伍、9 个月内 9 次），独立患者数 ≈ **2**。
- 去重后不构成信号，故 §3.3、§4.1、§5 的 "meets the signal criterion … remifentanil included" 需整体降级为 "term-level demonstration"。
- 连带失效：§3.8 的"2024 编码/上报迁移"解释（见 T0-2）。
- **必须动作**：新增报告级明细（`safetyreportid / receivedate / occurcountry / 年龄 / 性别 / primarysource.qualification / 并发用药`），明写"9 条同源、独立病例 2"；把"signal"改为"term-level demonstration"。

**T0-2｜"四药共有"是同一簇被重复计入四臂（A4-M1；主编亲验）**
- SUFENTANIL 2024 年 HYPERAESTHESIA = 7，其中 **7/7** 来自瑞芬簇；芬太尼 17 例中 5 例来自簇。
- 稿件的论证（"四药共有 → 是全库性年份位移，不是瑞芬特有"）因此**反转**：不是位移，是**同一病例在四臂被各计一次**。
- 这同时说明 **"头对头"在本数据上部分失效**——四臂共享报告。

**T0-3｜四队列非独立，RORR 的破坏可量化（A2-M1；A5-M5）**
- 瑞芬队列 29.3% 含芬太尼；剔除共同报告后 RORR 0.696 → 0.393 (0.15–1.06)，ROR 4.73 → 2.67 (1.00–7.12)。
- 全稿**唯一**显著 >1 的 PROCEDURAL PAIN vs fentanyl 1.962 (1.14–3.39) → 1.386 (0.65–2.96)，**不再显著**。
- **注**：A2 给 29.3%、A5 给 33.7%/37.7%，两者口径不同（是否含盐型/是否限定 role），需作者统一后澄清。

**T0-4｜语料是案例版本集合，版本构成在队列间不同（A2-M2）**
- 23.9% 报告带 version ≥ 2；各队列 27.7%–39.6%。
- 仅保留 version 1 后 RORR vs FEN 0.696 → **0.979 (0.48–1.99)**，"四者中最弱"不成立。

**T0-5｜leave-2024-out 的口径与判别力（A3-M2）**
- 现口径是"限定 2015–2023"（`_round4_leave2024.py:26–29` 只在年度行上求和），丢弃 1 129 份 2015 年前报告；真全库剔 2024 得 a = 2、0.943 (0.236–3.774)。
- 更关键：合并 ROR 4.73 **落在**剔除后 CI (0.099–4.978) **内**，故"signal 消失"混淆了"估计不稳定"与"效应不存在"。
- **必须动作**：改为"2015–2023 窗口"或补真口径；删去"signal 消失"措辞；Summary 与 §5 同步。

**T0-6｜术语选择决定结论方向，且代理关系被作者自认否定（A1-M1/M2；A4-M4）**
- HYPERAESTHESIA 被已自认非疼痛特异（§4.4 "is not pain-specific"）却仍"carrying the hyperalgesia concept"承载结论。
- 换 INADEQUATE ANALGESIA (8 465) 后**方向反转**：瑞芬 5.016 > 舒芬 3.761 > 吗啡 3.576。
- 两个"代理"（CHRONIC PAIN SYNDROME = 2012 遗留自由文本、HYPERPATHIA 仅 43 条全库）不成立。
- **注**：这条**削弱的是全文的"改正后主发现"，但也因此把稿件推回它真正的强项**——"术语决定答案"本身就是本文的卖点（§4.4），只是现在它需要从"我们发现概念存在"改为"我们发现检索路径决定结论"。

**T0-7｜完全缺失 SMQ / CMQ（A4-M3）**
- 全文未出现 "SMQ" 一词。对 OIH 这类"临床名 ≠ 编码名"的概念，药物警戒惯例是用官方 SMQ 或自定义 MQ（CMQ）；五个手工挑选、彼此不构成 term set 的 PT 无法替代。
- **这一条无法用文字修改弥补**，只能补做。

**T0-8｜适应证混杂可量化却从未量化（A5-M1；A2-P1-2）**
- 作者自己的 `cv/cvponline_extract_20241130/report_drug_indication.txt`（330 万行）含可归因到具体药品记录的适应证。
- 固定到"围术期麻醉"层后 PAIN RORR 0.235 → **0.399 (0.048–3.295)**（跨 1）；在"疼痛适应证"层**反转为 1.791**。
- §5 的 "large, stable and reproduced in Canada" 因此站不住。
- **注意**：这条既是"必须补做"，也是**作者最强的一次翻盘机会**——把低报归因到报告设置（setting）本来就有数字支撑，只是需要做出来。

### T1 — 必须补做的分析（数据都在作者手上，全部可执行）

| # | 补什么 | 数据/方法 | 预期产物 | 提出者 |
|---|---|---|---|---|
| T1-1 | 按 `safetyreportid` 保留每例最新版本 + 仅目标药自身 `drugcharacterization = 1` 的主分析重算 | openFDA 逐页取个案 | 与现稿并列的新 Table 1–4 | A2-#1 |
| T1-2 | 两库统一 RORR 估计量（(a_r·b_c)/(b_r·a_c)）并量化队列重叠 | 现有 CSV + 计数 | Table S6：18 术语的"剔共同报告"RORR + 4×4 重叠矩阵 | A2-#2、A5-#4、A7-M2 |
| T1-3 | 适应证分层头对头 | `report_drug_indication.txt` join `report_drug` | **Table 5**：`Stratum \| 四药 n \| a \| RORR vs FEN (95% CI) \| RORR vs MOR (95% CI)`；层：全样本/围术期麻醉/疼痛适应证/18–64/≥65/医师/其他 HCP/严重/非严重 | A2-#3、A5-#1 |
| T1-4 | 报告深度（每报告反应术语条数）控制 | `reactions.txt` 逐报告计数 + MH 分层 | **Table 6**：`PT \| terms per report(四药) \| 单条反应报告% \| crude RORR \| MH-adjusted RORR \| share-of-terms ratio` | A5-#2 |
| T1-5 | SMQ/CMQ 替换手工 PT | 官方层级式 SMQ 20000100（abuse/dependence/withdrawal）+ SMQ "Lack of efficacy" + 疼痛臂 CMQ | **Table S6**：`PT \| code \| HLT \| HLGT \| primary SOC \| narrow/broad \| rationale`；并说明"无 hyperalgesia 官方 SMQ" | A4-#2 |
| T1-6 | 稀疏格子改用精确条件 / mid-P / Haldane 区间 | 全稿 a < 5 的格子 | 三种区间并列；Table 2 的 ALLODYNIA 给精确 CI **0.09–19.39** | A3-#1 |
| T1-7 | 年份分析升级为计数模型 | Poisson/负二项 GLM：`log E[Y_dy] = log R_dy + μ + α_d + γ_y + δ_{d×y}` | 交互 LRT + 线性趋势 p；重写 Table 4B/4C 的"稳定"表述 | A3-#3 |
| T1-8 | `ratio_2024_to_pooled` 补区间或降级 | delta / bootstrap | 15.41 [6.01–39.49] 等；声明分子分母不独立 | A3-#4 |
| T1-9 | 报告级去重后的主分析 a | 与 T1-1 同源 | 瑞芬 HYPERAESTHESIA 的真实独立病例数与对应 ROR | A4-#1 |
| T1-10 | 检索与抽取日志 | 复述实际执行的 openFDA `search=` 表达式 | **Table S6（或 S8）**：`source, endpoint, exact_query, fields, date, returned_n, note` | A6-P1-3 |

### T2 — 必须改措辞（不需要新数据，但必须全部落实）

| # | 位置 | 现文 | 改为 | 提出者 |
|---|---|---|---|---|
| T2-1 | 全稿 **11 处** | "defined a priori in a dated analytical plan" | "specified in a dated analysis plan that was written **after** data extraction and before the results were interpreted; the plan is supplied as Supporting Information (Appendix S1). The analysis was **not** prospectively registered." 并在 §2.3 直陈五代理是"看到 0 之后"加的 | A6-M2 |
| T2-2 | `ANALYSIS_PLAN.md:36`、投稿信 `:20` | 同 T2-1 的旧表述 | 三处口径必须一致 | A6-M2 |
| T2-3 | §5 末段 | "the four negative controls … could not be tested in Canada, whose cohorts were too small" | "Of the four negative controls **only vomiting could be tested** in Canada — three remifentanil reports, ratio 1.07 versus fentanyl and 0.39 versus morphine — while nausea, pruritus and constipation could not be tested, the remifentanil cell being empty in each" | A7-M1、A5-P1-3 |
| T2-4 | §4.5 limitation | "too small for most ratios to be computed" | "of the four negative controls only vomiting had a non-zero remifentanil cell (3 reports); the remaining three were untestable" | A7-M1 |
| T2-5 | Table 3 | 增行 `VOMITING \| 64 \| 0.409 / 0.185 \| 3 \| 1.066 / 0.392 \| no (direction reversed versus fentanyl)` | A7-M1 |
| T2-6 | §3.4 首句 | "The same pattern held for **every** negative control across all three comparators" | "The same direction held for the negative controls against fentanyl and morphine, and for nausea, vomiting and constipation against sufentanil: **eleven of the twelve** computable ratios were below 1, the exception being pruritus versus sufentanil (1.310, 0.84–2.04)" | A7-P1-3 |
| T2-7 | §3.8、§4.1 | "all negative controls stayed below 1" | 与 Table 4A 的 PRURITUS vs FEN **1.087** 冲突；改为"11 of 12" | A5-P1-2 |
| T2-8 | §2.4 | "Both ratios share the same background reference, so comparator-specific terms cancel" | "Each ratio was computed in its own 2×2 table … so the two ratios do not share their event column exactly and **no term cancels algebraically**; the two d values differ by under 0.6% and the two c values by the term's own frequency in the cohort" | A7-M2、A2-P1-6 |
| T2-9 | Table S5 脚注 | "every ratio … can be recomputed from the counts alone" | 补入"the 2×2 convention in §2.4"作为前提 | A7-M2 |
| T2-10 | §2.4 | "the ignored covariance is under 0.001% of the variance" | "… on the order of 1/c reports, so the ignored covariance is of order 10⁻⁴ against a log-scale variance of 0.10, i.e. about **0.1%** of the variance" | A7-P1-1 |
| T2-11 | §2.3 | "the two a priori hyperalgesia outcomes … produced no estimable result" | "**neither met the signal criterion**: HYPERALGESIA returned no report in either corpus, and ALLODYNIA contributed a single remifentanil report, **so its estimate is uninterpretable**" | A7-P1-2 |
| T2-12 | Table 3 Confirmed 列 | "yes (zero in both)"（14 行覆盖两种截然不同情形） | "yes (remifentanil zero in both)"，并注明"exposure-side zero, not unretrievability"（依据：DRUG TOLERANCE 加拿大全库 **386** 份、HYPERAESTHESIA **521**、PROCEDURAL PAIN **1 510**、DRUG WITHDRAWAL SYNDROME **1 664**、ALLODYNIA **29**，而 HYPERPATHIA 为 **0**） | A7-P2-2、A4-P1-1 |
| T2-13 | Table 4C 注 | "so the table holds nine rows" | "Nine of the ten reports carry a receivedate in 2015–2024 …, **so the remifentanil column of this table sums to nine**" | A7-M3 |
| T2-14 | Figure 1 图注 | "Terms are grouped from the top" | "from the bottom"（或代码加 `ax.invert_yaxis()`） | A7-M5、A6-M4 |
| T2-15 | Table 4A Group 列 | `DRUG INEFFECTIVE \| OIH-wide`、`PAIN \| OIH-wide` | 统一用 `10_term_dictionary.csv` 的 Group（`probe` / `surrogate`） | A1-P2-1、A7-P2-3、A5-P2-4 |
| T2-16 | Table S3 | 54.4 / 43.2 | **54.3 / 43.1**，并加题注"Proportions are computed from the counts and the cohort size and then rounded to one decimal place, not rounded from a previously rounded value" | A7-M4 |
| T2-17 | §3.9 | 免疫类"灵敏度正对照" | 改写为**伪信号示例**（532/5 375 = 9.9% 过敏性休克 vs 芬太尼 0.28%）；§4.5 增补"该臂不承担灵敏度论证职能" | A1-M3、A5-P1-6 |
| T2-18 | §3.4 | "physician-only analysis (5.921 and 10.604)" | 实为"分子限定医师、分母用全队列"的混合量；**正确值 17.936 (5.15–62.48)**；补 CI 或删除 | A5-P1-1、A1-P2-2 |
| T2-19 | §3.5、§4.5、Table 3 列名、摘要 | "independent Canadian database"、"Cross-database **confirmation**"、"Confirmed"、"for confirmation" | "a second, methodologically cleaner but **non-independent** North American system"、"Cross-database **comparison**"；Table 3 删去不可算行的"yes" | A5-M6、A2-M5 |
| T2-20 | §2.2、§4.5 | "a role-restricted analysis was not possible"、"The FDA case-level files could not be retrieved" | 撤回；改为准确边界（`patient.reaction.reactiondate`/`onsetdate` 确不存在故 TTO 不可做；但 **role 可限定、个案可翻页获取**） | A2-M3 |
| T2-21 | §2.3、Table S4 脚注 | "a string returns a count only if it is a **preferred term**" | 改为"加拿大侧仅含 PT；openFDA 侧亦保留早期遗留字符串"；Table S4 增设 `Evidence of dictionary status` 列（CHRONIC PAIN SYNDROME 的"1"实为 2012 年 safetyreportid 9291134 的 v16.0 自由文本） | A4-P1-3 |
| T2-22 | Table 3 / Table 2 / Table 4A / S5 | 不可检索字符串印成 `0` | 统一改为 `NR`（not retrievable）并脚注定义；同步改 READUS-PV 清单第 9 条自述 | A4-P1-2 |
| T2-23 | §3.3、Table 4C 注 | 第 10 条报告 "undated" | 实为 **receivedate = 2025-03-25**；改为"received on 25 March 2025, outside the window"；同时披露 9/10 集中在 6 个月内 | A4-P1-6 |
| T2-24 | §4.5 | "起病时间无法分析"的绝对化表述 | 加拿大 `reactions.txt` 字段 3–5 实为反应时间字段（**185 926 行**非空，含 Hyperaesthesia 13、Procedural pain 57），补描述性 Table S7 | A4-P1-7 |
| T2-25 | §2.3 / §4.6 | "has not been examined"、"decisions … should rest on the prospective literature [7, 8]" | 收敛新颖性主张（引 Hirai 2023、Dai 2023）；§4.6 产生真实价值（见 T2-26） | A1-P1-3/P1-5 |
| T2-26 | §4.6 | 对临床医生近乎零信息 | 加"每 X 份报告 1 份"表述（瑞芬 **1/538**、芬 **1/387**、舒 **1/296**、吗 **1/216**；allodynia 瑞芬 1/5 375）+ 报告完备度量级句 | A1-P1-3 |
| T2-27 | §1、§2.3、§4.2 | 对 Fletcher 2014 的转述丢掉"significant"与"mainly remifentanil"；后 2016 年定量证据全缺 | 补 **Mauermann 2016 (Anesthesiology 124:453–63, DOI 10.1097/ALN.0000000000000976)**（痛评分下降 0.83、痛觉过敏面积上升 30.5%、**allodynia 不变 P = 0.682**）+ Higgins 2019 BJA、Adams 2023 BJA、Colvin 2019 Lancet、Huang 2024 BMC Anesthesiol、Koo 2017 BJA | A1-P1-1/P1-2 |
| T2-28 | §3.7 | "elevated ratios"（加拿大 n = 111，Immune 仅 9 例） | 补 CI（或标 `point estimate only`）；若下界远小于 1 则不得用 "elevated" | A6-P1-4、A3-P1-3 |
| T2-29 | 首页 | "main text 4 000 words"、"Tables: 4 (Table 4 in three panels)" | 实测值与口径；"Tables: 1–3 and 4A–4C (six table objects) plus 5 supplementary" | A6-P1-5、A7-P1-5/P2-1 |
| T2-30 | 摘要 | "(a = 1)"、"preferred term" | "(a single report)"；"the term stored in the coding dictionary for that reaction" | A6-P1-4 |

### T3 — 格式与规范（编辑办公室可先行拦截）

| # | 问题 | 依据 | 判定 |
|---|---|---|---|
| T3-1 | 两图均有**图内 legend box**（`05_figures.py:170`、`:221`） | 本刊："There should be no titles, plot frames, gridlines or **legend boxes** within the graphs" | **A6 判 FAIL；A7 判 PASS（分歧，见 §4）** |
| T3-2 | Table S1/S3/S4/S5 **全表内嵌正文文件**；仅 S2 独立 | 本刊："should be uploaded as separate documents and not included in the main document file"、"all supporting tables in one file" | **FAIL（硬）** |
| T3-3 | refs 29、30 各列 7 位作者 | 本刊："List all authors unless there are seven or more, in which case give the first three followed by 'et al.'" | **FAIL** |
| T3-4 | Table S2 题注 `[10, 11]` → `[13, 14]` | 参考文献编号规则 | **FAIL** |
| T3-5 | AI 声明缺**工具名与版本、使用日期、隐私与合规**三要素 | Wiley 模板 + 编辑立场声明 | **FAIL** |
| T3-6 | 数据可用性无版本锚点（§10 说 `v1.0.0`，仓库最新为 **v1.4.0**）；"permanently available" 过强 | 可复现性承诺 | **FAIL（轻度）** |
| T3-7 | READUS-PV 检查表 Part A 第 9 条声称"每个估计都有 95% CI"，实测 Table 3 加拿大列、Table S1 两面板、§3.7、§3.9 全为裸点估计 | 自查表真实性 | **FAIL** |
| T3-8 | READUS-PV 定位列抽查 6 条有 3 条指向不含该内容的章节（第 11 条 §4.5、第 12c 条 §4.6、第 7c 条 §2.4） | 同上 | **FAIL** |
| T3-9 | §9、§10、"Formatting note (not for submission)"、脚本名、仓库文件名残留在投稿文件里 | — | **DESK-REJECT 级**（§10 第 564 行含 "updated after **round 2**"、披露"本环境打不开 github 页面"、reviewer suggestions 的辩解口吻） |
| T3-10 | 投稿信题名（"…**with negative controls defined a priori**"）与稿件题名（"…**with a terminology caution**"）**完全不同** | triage 阶段必然发现 | **DESK-REJECT 级** |
| T3-11 | 投稿信称 "ten calendar years"（实为 8 个可估年份）、"four tables"（实为 6 张） | 同上 | FAIL |
| T3-12 | 题名 "with a terminology caution" 带结论倾向 | 本刊："Title should be non-declarative"、"should not state a conclusion" | **FAIL（轻度）** |
| T3-13 | 图件同时提供 `.png` | 本刊可接受格式：".pdf, .jpg, .tiff or .pptx" | 勿上传 PNG |
| T3-14 | §9 溯源表第 539 行少一个 `|`，表格断裂 | — | FAIL |
| T3-15 | §2.4 数值口径与 Table S1 Panel B 覆盖率未报告（94.3% / 96.9% / 93.7% / 96.8%，全局 98.8%，源 `03_soc_27.csv`） | 探索性分析的唯一已知偏倚来源 | 建议补 |
| T3-16 | Short title 标签用 "Running head"（本刊用词为 "Short title"） | 本刊用词 | 建议改 |

---

## 4. 审稿人之间的共识、互补与分歧

### 4.1 高度共识的核心发现（多路独立触及）

**"同一病例簇"这一发现是本轮最重要的结果，而它是被四条独立路径同时逼近的：**

| 路径 | 审稿人 | 切入方式 |
|---|---|---|
| 报告级身份核对 | **A4** | 逐条调阅原始报告，发现 9 条为同一 76 岁男性、同一报告者、同一配伍 |
| 队列重叠 | **A2** | 发现 29.3% 的瑞芬报告含芬太尼、10 例 HYPERAESTHESIA 中 6 例含芬太尼 |
| 案例版本 | **A2** | 发现 23.9% 报告带 version ≥ 2，去版本后 0.696 → 0.979 |
| 术语学语义 | **A4、A7** | Table 3 "zero in both" 在 14 行里混同两种情形 |
| 临床语义 | **A1** | HYPERAESTHESIA 非疼痛特异，代理关系不成立 |
| **报告级亲验** | **主编** | 独立查询确认 10 条构成、盐型归属、9 条同源，并用舒芬太尼 7/7 落在簇内锁定"四臂共享" |

**六位审稿人 + 主编在"稿件的核心结论不能按现文成立"上完全一致。**

### 4.2 互补关系（各自独有的贡献）

- **A1 独有**：临床文献证据（Mauermann 2016 的 allodynia 不变 P = 0.682 是**表型层面证伪"PAIN 可作代理"的直接人体证据**；这是任何数据审计都发现不了的）；"每 X 份报告 1 份"的可读化建议。
- **A2 独有**：**推翻两项最大自我设限**（role 可限定、个案可翻页获取）；EBGM 先验退化（α = 0.540、β = 1e-5 → EBGM ≡ (a + 0.540)/E，不是 MGPS 估计）。
- **A3 独有**：稀疏格子的三种区间并行对照（a = 1 时 Woolf 下界 0.488 vs 精确 0.088 vs Haldane 1.049 vs mid-P 0.173）；加拿大功效 **0.19%**（80% 功效需 ROR ≈ 88）。
- **A4 独有**：**SMQ/CMQ 的完全缺失**（这是最不可用文字弥补的缺陷）；`patient.reaction.reactionmeddraversionpt` **存在**（实测 17.0/24.0/27.1/28.1），故"openFDA exposes none"有误；且 HYPERAESTHESIA 全库年报告量 2015 年 646 → 2024 年 **337（十年最低）**，直接否证"2024 编码迁移"。
- **A5 独有**：**报告深度是结构性混杂**——每报告反应术语条数 1.694 / 3.899 / 4.111 / 6.502（差 2.3–3.8 倍），MH 分层后 PAIN vs MOR 0.146 → **0.978**、vs FEN 0.235 → **0.640**。这是"该术语低报"与"整体低报"的分界线。
- **A6 独有**：11 处 "a priori" 的**逐处定位**与 `ANALYSIS_PLAN.md:5` 的直接对撞；READUS-PV 自查表的**抽查式证伪**；280 词重写摘要；32 行格式对照表。
- **A7 独有**：**在算术层面为稿件背书**——1 196 格中仅 2 格不符；加拿大侧 2.1 GB 原始数据端到端 100% 复现。**这一背书对作者极其重要**：它说明问题不在实现，在设计。

### 4.3 真实分歧（必须在作者回复中显式处理）

**分歧 1｜Figure 的 legend box 是否违规**
- **A6**：判 FAIL。依据是本刊原文 "no titles, plot frames, gridlines or **legend boxes** within the graphs"，`frameon=False` 只去掉边框、没去掉图例本身，而图注已能完整解释符号，图例纯属冗余。
- **A7**：判 PASS。依据是"图例 `frameon=False` 无框"即满足"no legend boxes"。
- **主编裁断**：**采纳 A6 的读法。** "legend boxes" 的宾语是图例框这一整体，"frameon=False" 是作者视角的技术细节，不是编辑视角的判定标准；且删除图例零成本、零信息损失。**建议直接删除两图图例，符号说明全部移入图注。**

**分歧 2｜Verdict：Major Revision 还是 Minor Revision**
- **A7**：Minor。依据是 1 196 格仅 2 格错、加拿大端到端 0 处不符。
- **A1–A6**：Major。
- **主编裁断**：**Major Revision。** A7 的自我限定（"我不评价写作风格"）使他的核查看不到设计级问题；而 T0 的八条全部是设计级。A7 的 Minor 应读作"实现层干净"，不是"本轮可小修"。

**分歧 3｜统一 RORR 口径是否"数字不变"**
- A7 实测否定：若把加拿大侧也改为"各自 c、d"，**两格会变**——PAIN vs morphine **0.146 → 0.144**、DRUG INEFFECTIVE vs morphine **1.703 → 1.706**（另两格 0.235 / 1.277 不变）；共同因子 (d_R·c_C)/(d_C·c_R) 最大偏离 −1.18%，因加拿大队列仅 111 人。
- **主编裁断**：这一条**必须让作者明确二选一**——要么保留现状 + 题注明说两库口径不同，要么统一口径 + 同步改这两格。**绝不可只改文字不改数**。

**分歧 4｜队列重叠比例**
- A2 给 29.3%（瑞芬队列中含芬太尼）；A5 给 33.7% / 37.7%（口径不同，可能含盐型或限定 role）。
- **主编裁断**：需作者给出一张 4×4 重叠矩阵（T1-2），把口径一次讲清。

**分歧 5｜稿件类型是否可保留 Original Article**
- A6：可保留，但须满足 4 项硬条件（补一个正面、有数字的结论并配 Table 5；把 ANALYSIS_PLAN 作为正式 SI；把术语核查做成 5–10 行的"查询前必做"清单；正文字数留余量）；否则应改 Science Letter（本刊无 "Short Report" 栏目）。
- A1：若拒绝按清单重构论证框架，应 Reject 并转投药物警戒类期刊。
- **主编裁断**：**可保留 Original Article，但必须先完成 T0-1 与 T0-8**——即把"报告设置解释低报"这一**有数字、稳定、可复现的正面结论**推到前台，同时把术语发现降级为"检索路径决定结论"的方法学警示。这是本稿唯一站得住的 Original Article 形态。

---

## 5. 按优先级的必改清单（含阻塞标记）

### P0 — 阻塞投稿（不做则不应投稿）

| # | 动作 | 依据 | 后果 |
|---|---|---|---|
| **P0-1** | 删除 §9、§10、"Formatting note (not for submission)" 全节及脚本名/仓库文件名残留（`I_正文_IMRaD_en.md:15`、`:217`、`:528–566`） | A6-P2-1 | **DESK-REJECT**：§10 第 564 行含 "updated after round 2"，并披露内部流程与"本环境打不开 github 页面" |
| **P0-2** | 投稿信题名改为与稿件逐字一致；修正 "ten calendar years" → "the eight calendar years in which an estimate was possible"、"four tables" → "four main tables (Table 4 as panels 4A–4C)" | A6-M6 | **DESK-REJECT**：triage 必然发现 |
| **P0-3** | **报告病例簇事实并降级"signal"**：新增报告级明细（10 条 `safetyreportid/receivedate/country/年龄/性别/qualification/并发用药`），明写"9 条同源、独立患者 2"；§3.3、§4.1、§5 的 "signal" 改为 "term-level demonstration" | A4-M1 + 主编亲验 | 结论不成立 |
| **P0-4** | **撤回"2024 抬升为四药共有 → 编码位移"的解释**（舒芬 7/7 落在瑞芬簇内）；改为"同一病例簇被计入多臂" | A4-M1 + 主编亲验 | 论证反转 |
| **P0-5** | 全稿 11 处 "defined a priori" 统一改为如实表述 + 明写未前瞻注册；同步 `ANALYSIS_PLAN.md:36` 与投稿信 `:20` | A6-M2 + A3 | **诚信条款**；拒绝则升级 Reject |
| **P0-6** | §5 与 §4.5 的加拿大阴性对照表述按事实改写（VOMITING 可算，1.066 / 0.392） | A7-M1 + A5-P1-3 + 主编亲验 | 结论与源数据矛盾 |
| **P0-7** | leave-2024-out 口径明确为"2015–2023 窗口"，或补真全库剔 2024 的 a = 2 / 0.943；删去"signal 消失"措辞 | A3-M2 + A6-P2-6 | 结论不可复算 |
| **P0-8** | 删除两图图内 legend box；Figure 1 图注 "from the top" → "from the bottom" | A6-M4 + A7-M5 | 本刊明文 + 图注与图相反 |

### P1 — 必须补做（阻塞"结论级"问题）

| # | 动作 | 预期产物 |
|---|---|---|
| P1-1 | 去版本重复 + role 限定的主分析重算（T1-1） | 与现稿并列的新 Table 1–4 |
| P1-2 | 队列重叠矩阵 + 两库统一 RORR（T1-2） | Table S6 + 4×4 矩阵 |
| P1-3 | 适应证分层头对头（T1-3）——**这是作者最强的翻盘机会** | **Table 5** |
| P1-4 | 报告深度 MH 分层（T1-4） | **Table 6** |
| P1-5 | SMQ / CMQ 替换手工 PT（T1-5） | Table S6（术语集规格） |
| P1-6 | 稀疏格子精确区间（T1-6） | Table 2 的 ALLODYNIA 精确 CI 0.09–19.39 |
| P1-7 | 年份计数模型（T1-7） | 交互 LRT + 趋势 p |
| P1-8 | 检索与抽取日志（T1-10） | Table S6/S8 |

### P2 — 必须改措辞（T2 表格全 30 条，逐条落实）

### P3 — 格式与包装（T3 表格全 16 条）

### P4 — 建议改

- 正文压缩至 ~3 850 词以规避计数口径风险（A6 给出 5 处可删段落、合计约 150 词）。
- 题名去掉 "with a terminology caution"，改用含设计词的表述（如 "…: an observational head-to-head disproportionality analysis"），或保留术语主题则为 "…: an observational disproportionality analysis with negative controls"。
- 投稿只上传 `.tif` / `.pdf`，不上传 `.png`。
- 提供 `refs_verification.csv`，把"30 条按标识符核实"变成可抽验的文件。
- 把 Figure 2 改为运行期读取 `04_sensitivity_year_pain.csv`（消除 AI 声明与硬编码的矛盾）。
- Table S3 两列 "Other health professional" 均为 2 056 已确认为真巧合，加脚注说明即可，**不必改数**。

---

## 6. 稿件站得住的地方（共识，作者不应因评审而改动）

七位审稿人一致确认以下为"经核查无问题"，**其中若干是本稿真正的资产**：

1. **术语可检索性核验是真实、可复现的方法学贡献**（A1、A2、A4、A7 独立确认）。FAERS 缓存中 `HYPERALGESIA` 返回 0；加拿大 742 MB 反应表前 100 万行中 `Hyperalgesia` 出现 0 次而 `Hyperaesthesia` 166 次。**"临床用词检索必得 0"这件事被在两个国家级库上实证了一遍，这是本文唯一不可替代的增量。**
2. **表格数字的实现质量极高**（A7 认证）：1 196 格中仅 2 格不符（且为双重舍入，0.1pp）；ROR 独立重算最大相对误差 9.0×10⁻⁴；**加拿大侧 2.1 GB 原始 line-listing 端到端 100% 复现，逐格不一致 = 0**；170 处"破折号 = 不可估计"语义核对全部正确。
3. **作者主动拆解自己最好的数字**（A2、A6、A7 共同赞扬）：主动披露 10 例中 8 例在 2024 年、主动给出 leave-2024-out、主动给出四药 2024/pooled 比值。**这种自我拆解是这类研究最需要的诚实，也是本轮缺陷能被发现的原因。**
4. **探测失灵被如实报告**（A6、A7）：DRUG INEFFECTIVE 在两库方向相反（FAERS 0.568/0.470；加拿大 1.277/1.703），作者没藏，而是写 "it narrows rather than settles the interpretation"。**探针失灵被如实报告，比探针成功更让人相信作者没有挑选结果。**
5. **主动给自己的次优分析贴标签**（A6）：FAERS 侧 SOC 分析被明确降级为探索性并写明 "counting is event-level and the rules are not authoritative"。投稿中相当少见。
6. **跨库设计是真跨库**：加拿大侧用原生 `SOC_NAME_ENG` 与 `Suspect` 角色限制，而非照搬 FAERS 做法。
7. **多处"我原本怀疑但核查后无问题"**（A6、A7）：Python 3.13.14 / matplotlib 3.11.1 实测属实；两图 600 ppi、180 mm、体积合格、无标题/网格/四边框；Table S3 的 2 056 是真巧合（三路独立证据）；Bonferroni 下界 1.61 复算为 1.6132 正确；30 条文献抽验 3 条 DOI 全部解析正确；全稿无美式拼写；仓库经 GitHub API 确认为公开、MIT、含 v1.0.0–v1.4.0 五个带结果包的 release。
8. **READUS-PV 检查表的 not applicable / not performed 条目属实**（A6 抽查）。

---

## 7. 建议的处理路径

### 路径 A（推荐）：重构为"报告设置解释低报 + 术语警示"的双结论稿，保留 Original Article

1. 完成 P0 全部 8 条（去内部痕迹、修题名、报告病例簇、撤 2024 位移解释、改 a priori、改加拿大对照、改 leave-2024 口径、删图例）。
2. 完成 P1-1 至 P1-4（去版本 + role、统一 RORR、适应证分层、报告深度）——**这四项做完后，稿件的核心结论将从"瑞芬太尼的失衡信号"转变为"自发报告系统中的围术期低报结构"，后者有数字、稳定、跨库、且不受病例簇影响。**
3. 把 §4.4 的术语发现从"主发现"改写为"检索规范警示"，并做成 A6 建议的 5–10 行"查询前必做"清单（这才是标题里 "terminology caution" 应有的形态）。
4. 补 P1-5（SMQ/CMQ）与 P1-6（精确区间）。
5. 完成 P2 全部措辞修订 + P3 格式包装。
6. 按要求重跑三道门禁并回填字数声明。

**预期**：可保留 Original Article，且**比现稿更强**——因为现稿的"主发现"（瑞芬太尼信号）本来就是一个脆弱数字，换成一个稳定的结构性发现是升级而非降级。

### 路径 B（若作者不愿重构）：降格为 Science Letter 或方法学 Commentary

把内容压缩到"术语可检索性核验 + 一次头对头负对照示范"，字数与图表大幅收缩。**代价**：放弃已完成的跨库工作与 4 000 词体量。

### 路径 C（不建议）：维持现稿只做文字修补

**不可行**。T0 的八条中有六条是数据层事实（病例簇、队列重叠、版本、口径、适应证、报告深度），不是措辞能覆盖的。若只改文字投稿，审稿人（尤其统计与药物警戒背景）会独立发现同样的数字，届时"可核查"这一最强声明会反噬。

---

## 8. 七份意见的索引

| 文件 | 行数 | 大小 | Verdict | 核心贡献 |
|---|---|---|---|---|
| `_review_r5/_PANEL_BRIEF.md` | 78 | 5.7 KB | — | 独立性纪律与输出契约 |
| `_review_r5/A1_clinical_OIH.md` | 336 | 60.2 KB | Major | 临床语义、Mauermann 2016、可读化、"每 X 份 1 份" |
| `_review_r5/A2_PV_methods.md` | 372 | 56.1 KB | Major | 推翻两处"数据不可得"、队列重叠、案例版本、EBGM 先验退化 |
| `_review_r5/A3_biostat.md` | 324 | 37.5 KB | Major | 稀疏区间三法对照、leave-2024 口径、计数模型、功效 0.19% |
| `_review_r5/A4_meddra.md` | 481 | 71.3 KB | Major | **病例簇（本轮最重要）**、SMQ/CMQ 缺失、MedDRA 版本、换 PT 反转 |
| `_review_r5/A5_epi_causal.md` | 377 | 58.3 KB | Major | **适应证分层**、报告深度、negative control 合法性、混合估计量 |
| `_review_r5/A6_editor.md` | 637 | 90.3 KB | Major | 11 处 a priori、READUS-PV 证伪、280 词摘要、32 行格式表 |
| `_review_r5/A7_provenance.md` | 643 | 80.2 KB | **Minor** | 1 196 格逐格比对、加拿大端到端复现、RORR 两口径差异 |
| `_review_r5/A7_scratch/` | — | — | — | A7 的原始重算脚本与日志 |
| `_review_r5/_a3_*.py`、`_a3_*.txt` | — | — | — | A3 的区间重算脚本与输出 |

**主编独立复核产物**（不依赖任何审稿人）：
- `_r5_editor_verify.py` → `_r5_editor_out.txt`（报告级构成、队列重叠、逐年计数）
- `_r5_editor_verify3.py` → 2024 簇跨药归属、加拿大 VOMITING（`cv/cv_pt_summary.csv`）
- `_r5_editor_cache.json`（openFDA 原始返回缓存）

---

## 9. 给作者的一段话

这轮评审给你的不是"你错了"，而是"你的**最强的那个数字不可靠，而你第二强的那个发现被你自己埋掉了**"。

HYPERAESTHESIA 的 4.73 从被算出来的那天起就只有一个病例簇在支撑它——**这件事连你自己四轮自检都没发现，不是因为你不够仔细，而是因为聚合层不让你看见**。而你真正的发现（瑞芬太尼在自发报告里系统性地低报包括疼痛在内的一切，而这是**围术期监护环境**的产物，不是药物的安全性信号）被写成了 §3.6 的一句解释段，藏在 4 000 字里。

把这两件事对调，这篇稿子会从"一个不可靠的信号 + 一句方法学警示"变成"一个稳定的报告学发现 + 一套可复用的检索规范"。后者才是 *Anaesthesia* 会想要的 Original Article。

**另有两点程序设计上的提醒**（与本轮意见平行的观察）：

1. 前四轮有 440 + 68 条门禁全绿，却没有任何一条门禁能拦住"10 例中有 9 例同源"——因为门禁认证的是**算术与溯源**，不是**设计**。本轮 T0 的八条，每一条都落在门禁的盲区里。**建议把"设计级断言"也落成产物文件并以值绑定写进正文**：例如把 4×4 队列重叠矩阵、报告深度分布、适应证分层结果都写成 CSV 并在正文引用其数值，这样门禁才能覆盖设计层。
2. `_verify_docx.py` 与 `_check_consistency.py` 目前比对的都是"稿件 vs 已生成的 CSV"。本轮 M1 的病例簇之所以逃过,是因为**从未有人问过"这 10 条报告是不是同一件事"**——这类问题无法由"稿件 vs CSV"的比对发现，只能由**假设生成式的独立复核**发现。**这恰是独立审稿面板不可被门禁替代的原因。**
