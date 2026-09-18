# Round-5 独立审稿 — A4_meddra MedDRA 术语学与药物警戒数据字典专家

## 0. 审稿人身份与总体结论

本人长期从事 MedDRA 术语维护与监管数据库编码字段工作，日常处理 LLT/PT/HLT/HLGT/SOC 五级层次、SMQ 与自定义 MedDRA 查询（CMQ）的构建与审计，熟悉 FAERS/openFDA 与各国 line-listing 的字段语义与版本迁移问题。

**Verdict: Major Revision**（Original Article 标准；若 M1 无法解决，则应改投/改稿型为纯方法学短文）

理由（具体到本稿缺陷）：

1. 本稿的"修正后主发现"——HYPERAESTHESIA 在瑞芬太尼中达到信号标准（a = 10，ROR 4.73）——经我逐条调阅原始报告后确认，**10 条中有 9 条疑似同一病例的重复/系列上报**（9 条全部为 76 岁男性、同一家美国报告者、同一组七药围术期配伍，2024-10-07 至 2025-03-25 之间），去重后仅余 2 条独立病例、无法构成信号。这直接推翻 §3.3、§4.1、§5 的核心表述，并使 §3.8"2024 年抬升为四药共有、提示 2024 编码/上报迁移"的解释失效（该"四药共有"实为同一病例簇被同时计入四个队列：舒芬太尼 2024 年 a = 7，与这 9 条中带舒芬太尼的 7 条完全重合）。
2. 本稿以术语学警诫为立论，却**通篇未出现 SMQ 一词**（我逐词检索确认），也未使用 MedDRA 层次（HLT/HLGT）做任何检索设计。对于 OIH 这样"临床名 ≠ 编码名"的概念，药物警戒惯例是 SMQ 或自定义 MQ；本稿用了五个手工挑选、彼此不构成术语集（term set）的 PT。这是最可能被 *Anaesthesia* 审稿人击中、且最不可用文字修补绕过的设计缺陷。
3. 版本漂移一节存在**可被当场查证的事实错误**：作者称"openFDA exposes none"（不暴露每条记录的 MedDRA 版本），而 openFDA 的 `patient.reaction.reactionmeddraversionpt` 字段就随每条记录返回；我实测同一次检索返回了 24.0、27.1、28.1 三个版本。作者本可做一个决定性检验而未做，而该检验的结论（HYPERAESTHESIA 全库年报告量 2015 年 646 条 → 2024 年 337 条，为十年最低）恰好排除"2024 编码迁移"这一作者自己给出的解释。
4. 稿件**内部自相矛盾**：READUS-PV 清单（Table S2，条目 9）声称不可估之术语"shown as not estimable rather than as zero"（以不可估而非零呈现），但 Table 2、Table 3、Table 4A、Table S5 恰恰把五个词典不可检索的字符串放在计数列里印成 **a = 0**。这与本稿"零的语义必须区分"的论旨直接冲突，且极易被读者读成"事件不存在"。
5. 作者最稳的次要结论（瑞芬太尼对所有疼痛类术语均报告更少）**同样是术语选择的产物**：换成频次充足、且更贴合"镇痛不足/疼痛加重"这一临床终点的 PT INADEQUATE ANALGESIA（全库 8 465 条）后，瑞芬太尼 ROR 5.02 高于舒芬太尼 3.76、吗啡 3.58，方向反转。这恰恰证明了本稿自己的论旨，却从未对自己的主结论做同样的压力测试。

---

## 1. 重大问题（Major）

### M1. "修正后的信号"实为单一来源病例簇，去重后不成立；"2024 年编码迁移"解释亦被否证

**【问题】** 全稿的"修正后主发现"（HYPERAESTHESIA 达信号标准，a = 10、ROR 4.73）在病例层面站不住：10 条瑞芬太尼 HYPERAESTHESIA 报告中 9 条特征几乎完全相同，疑为同一病例的重复/系列上报，且该簇同时构成本稿全部"四药共有"证据。

**【证据】**
我通过 openFDA drug/event 接口取回全部 10 条记录（`search=patient.drug.activesubstance.activesubstancename.exact:("REMIFENTANIL" "REMIFENTANIL HYDROCHLORIDE") AND patient.reaction.reactionmeddrapt.exact:"HYPERAESTHESIA"`，`total = 10`，与稿件的 a = 10 完全一致），逐条结果如下（safetyreportid / receivedate / 国家 / 年龄单位801=岁 / 性别1=男 / 报告者资质 / 反应）：

| # | safetyreportid | receivedate | 国家 | 年龄 | 性别 | qual | 反应 |
|---|---|---|---|---|---|---|---|
| 1 | 19700005 | 2021-08-13 | JP | 45 | 女 | 5 | Femur fracture; Internal fixation; Hypertension; **Hyperaesthesia**; Drug resistance |
| 2 | 24402565 | 2024-10-07 | US | 76 | 男 | 2 | **Hyperaesthesia** |
| 3 | 24641950 | 2024-11-20 | US | 76 | 男 | 3 | **Hyperaesthesia** |
| 4 | 24675457 | 2024-11-28 | US | 76 | 男 | 3 | **Hyperaesthesia**; Postoperative delirium; Psychotic disorder |
| 5 | 24690033 | 2024-12-03 | US | 76 | 男 | 3 | Delirium; **Hyperaesthesia**; Psychotic disorder |
| 6 | 24715261 | 2024-12-10 | US | 76 | 男 | 3 | **Hyperaesthesia** |
| 7 | 24716978 | 2024-12-10 | US | 76 | 男 | 3 | **Hyperaesthesia** |
| 8 | 24726643 | 2024-12-12 | US | 76 | 男 | 3 | **Hyperaesthesia** |
| 9 | 24727039 | 2024-12-12 | US | 76 | 男 | 3 | **Hyperaesthesia** |
| 10 | 25115900 | **2025-03-25** | US | 76 | 男 | 3 | **Hyperaesthesia** |

9 条美国报告（#2–#10）的患者年龄、性别、发生国、报告者国别与资质完全相同，用药清单为同一组围术期配伍（remifentanil、sufentanil、fentanyl、hydromorphone、oxycodone、ketamine、propofol，仅排列与少量项目变动；其中含舒芬太尼者 8/9、含芬太尼者 6/9），且 HYPERAESTHESIA 是其中 6 条的唯一反应。9 条集中在 2024-10-07 至 2025-03-25 的 5 个月内。这不可能是 9 例独立患者的巧合，而是**同一病例重复上报或单中心系列上报**。

关键推论：这 9 条中，2024 年内携带舒芬太尼的恰好是 **7 条**（#3、#4、#5、#6、#7、#8、#9），而 `04_sensitivity_year_hyperaesthesia.csv` 中舒芬太尼 2024 年的 `SUFENTANIL_a` 正是 **7**。也就是说，本稿 §3.8 用来论证"2024 年抬升为四药共有、指向编码/上报迁移"的证据，**完全由同一个病例簇被同时计入瑞芬太尼、舒芬太尼、芬太尼、吗啡四个队列而产生**，不是四药各自独立的现象。

此外，稿件 §3.3 称第十条报告"one undated"，Table 4C 脚注称"one has no usable receivedate"；该报告实际 `receivedate = 20250325`，是可用的日期，只是落在表格声明的 2015–2024 窗口之外。这使"9/10 落在 6 个月内"的事实被表述掩盖。

**【为什么重要】** 本稿把该信号作为"术语修正后概念其实存在"的唯一实证支点（§3.3、§4.1、§4.2、§4.4、§5 均依赖它）。若按 FDA 的病例级去重逻辑处理，瑞芬太尼 HYPERAESTHESIA 仅剩 2 条独立病例（1 例日本 2021、1 例美国 2024），ROR 不再可估或远离信号标准。这同时也使 Limitations 中"openFDA 未去重，会使**每个**队列等量膨胀，因此不会产生所观察到的方向"这一自我辩护失效——本簇的重复是集中在瑞芬太尼（5 375 条）与舒芬太尼（6 513 条）这两个小队列上的，方向恰恰由它产生。任何一位 *Anaesthesia* 审稿人只要点开这 10 条记录，就会得出同一结论。

**【具体修改建议】**
1. 新增一节 **§3.x Case-level inspection of the corrected signal**，报告：10 条报告的 receivedate、occurcountry、`primarysource.qualification`、患者年龄/性别、并发用药数，并明确"how many distinct patients the 10 reports represent"。
2. 在 §3.3 与 Summary 中把该信号改述为可辩护的版本，例如：
   > "After the corrected preferred term was used, remifentanil contributed ten HYPERAESTHESIA reports (reporting odds ratio 4.73, 95% CI 2.54–8.80). Nine of the ten, however, are a single US case series received between October 2024 and March 2025 with an identical 76-year-old male profile and an identical perioperative drug list, so the number of distinct patients is two; the estimate is therefore not interpretable as a drug-level signal and is reported only to document the term-level effect."
3. 删除或改写 §3.8 的"shared by all four opioids … pointing to a 2024 coding or reporting shift"，替换为：
   > "The 2024 cluster is not shared independently by the four cohorts: the same nine-case series supplies seven of sufentanil's eight HYPERAESTHESIA reports and six of fentanyl's 2024 reports, so the four 2024 estimates are not independent."
4. 在 §4.5 把"de-duplication … would not generate the observed direction"替换为：
   > "De-duplication would not be symmetric across cohorts: the duplicate cluster lies in the two smallest cohorts (remifentanil, sufentanil), so it does generate the observed direction for HYPERAESTHESIA; the direction of the PAIN finding, by contrast, is too extreme to be explained by duplication."
5. 若作者无法解决重复问题，最稳妥的处置是把全文重心从"信号"移到"术语/编码学"（见 M3），把 HYPERAESTHESIA 一节降为术语演示，而不是研究结论。

---

### M2. MedDRA 版本漂移：既存在事实错误，又未做那个能一锤定音的检验；而该检验的结论否定作者自己的解释

**【问题】** §2.3 与 Table S4 称 openFDA 不暴露逐条记录的 MedDRA 版本，据此推断加拿大库"单一版本"、FAERS"跨多版本"，并仅以一句"版本可能迁移"收尾；实际上该字段是公开可查的，作者本可量化，而未量化。

**【证据】**
- 稿件 §2.3（第 69 行）："The Canadian extract states the release used for every reaction row (v27.1) [18]; **openFDA exposes none**, and the FAERS corpus spans quarterly releases from 2004, so no single release applies to it."；Table S4 脚注（第 487 行）："**The openFDA interface exposes no per-record release**"。
- 实测：openFDA 的 `patient.reaction.reactionmeddraversionpt` 逐条返回。我取回瑞芬太尼 HYPERAESTHESIA 的 10 条记录，其 reaction 版本分别为 **24.0、27.1、28.1**（例：safetyreportid 24690033 三条反应均为 27.1；24675457 为 28.1；19700005 为 24.0）；随机取 1 条 2014 年 HYPERAESTHESIA 记录（receivedate 20140313）其 `reactionmeddraversionpt = "17.0"`。
- 也就是说，**同一条 PT 在 v17.0、v24.0、v27.1、v28.1 下都出现**；openFDA 并不把全库统一重编码，而是保留逐报告版本。
- 我进一步做了作者未做的检验——HYPERAESTHESIA 的**全库年度分布**（`search=patient.reaction.reactionmeddrapt.exact:"HYPERAESTHESIA" AND receivedate:[YYYY0101 TO YYYY1231]`）：

  | 年 | 2004 | 2005 | 2006 | 2007 | 2008 | 2009 | 2010 | 2011 | 2012 | 2013 | 2014 |
  |---|---|---|---|---|---|---|---|---|---|---|---|
  | 条 | 98 | 106 | 140 | 154 | 157 | 190 | 260 | 333 | 390 | 471 | 483 |

  | 年 | 2015 | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
  |---|---|---|---|---|---|---|---|---|---|---|---|---|
  | 条 | 646 | 568 | 587 | 573 | 438 | 477 | 484 | 486 | 399 | **337** | 267 | 116 |

  这与 `04_sensitivity_year_hyperaesthesia.csv` 的 `HYPERAESTHESIA_year_total` 列逐格完全一致（我逐格复核无误），说明作者手上就有这份数据，却没有把它用于版本/编码迁移的判断。

- 另一方面，Health Canada 官方术语表明确写着：每次 MedDRA 新版发布后，加拿大库会**回头重编已入库的历史报告**——"Following each new version release of MedDRA, the adverse reaction data is reviewed and updated in order to reflect any changes that may have occurred to the terminology. Therefore, some MedDRA terms have changed in some adverse reaction reports previously contained in this online database."（Health Canada, Glossary of Fields in the Canada Vigilance Adverse Reaction Online Database）。因此"加拿大库每一行都是 v27.1"是**统一重编的结果，而非时间上同质的证据**；作者把"加拿大=单版本 / FAERS=多版本"当作方法学对比，方向恰好相反：真正经历术语迁移的是加拿大库，而 FAERS 保留了原始逐报告版本。

**【为什么重要】** §3.8 把 2024 年的抬升归因为"a 2024 coding or reporting shift"。但：(i) HYPERAESTHESIA 自 2004 年起持续存在（v17.0 即有），不存在"2024 年新增/升格 PT"的可能；(ii) 全库 HYPERAESTHESIA 报告量在 2024 年降至十年最低（337 条 vs 2015 年 646 条），不支持任何"向 HYPERAESTHESIA 的编码迁移"；(iii) 真正的原因是 M1 的单来源病例簇。三点合并后，作者给出的解释不仅未被证实，而且已被可查数据否证。这一段现在是全文最容易被推翻的解释性文字。

**【具体修改建议】**
1. 把 §2.3 关于版本的句子替换为（可直接粘贴）：
   > "openFDA returns the release applied to each reaction through `patient.reaction.reactionmeddraversionpt`, so the release is recoverable per report rather than per corpus; in our extraction the term used here appeared under releases 17.0, 24.0 and 27.1–28.1, and no single release is common to the corpus. The Canadian extract instead carries one release label (v27.1) because Health Canada re-codes its whole database at each MedDRA release, so a single label does not imply that the Canadian data are free of term migration."
2. 新增一个可执行的检验，并写入正文或 Supporting Information：报告 HYPERAESTHESIA 报告的**版本构成**。注意 `reactionmeddraversionpt` 是 text 字段，openFDA 的 `count=` 聚合在其上不可用（会返回 `SERVER_ERROR: Text fields are not optimised for ... aggregations`），因此须以**抽样读取记录**的方式取得（如对 HYPERAESTHESIA 检索按 `skip` 分页抽取 n 条，逐条记录其 `reactionmeddraversionpt`），或直接使用 FDA 的季度 FAERS ASCII 文件（`REAC` 表中的版本列）按年统计。同时报告瑞芬太尼那 10 条报告各自的版本；预期结论为"该 PT 跨 17.0–28.1 稳定存在"，可作为排除版本漂移的正式证据。
3. 删除 §3.8 的"pointing to a 2024 coding or reporting shift"，改为：
   > "Because HYPERAESTHESIA was retrievable under every release represented in the corpus (17.0 onwards) and its corpus-wide reporting fell to a ten-year low in 2024 (337 reports), the 2024 cluster cannot be attributed to a coding shift; it is attributable to a single-source case series (see §3.x)."

---

### M3. 完全缺失 SMQ / 自定义 MedDRA 查询（CMQ）：这是本次审稿最重大的方法学缺陷

**【问题】** 稿件全文（含 §2.3、§2.5、§4.4、Table S4 与 READUS-PV 清单）从未出现 "SMQ"、也未使用任何 MedDRA 层次作为检索单元；对 OIH 这样一个"临床名称不是编码名称"的概念，仅靠五个孤立的 PT，既不符合药物警戒惯例，也使结论随术语选择而漂移（见 M4）。

**【证据】**
- 我在稿件中逐词检索 `SMQ|Standardised MedDRA|MedDRA Query|HLT|HLGT|hierarch`，**唯一命中**是第 177 行的 "…used keyword rules rather than the MedDRA hierarchy…"，即作者承认自己**没有**用层次。Table S2 READUS-PV 清单同样无 SMQ 条目。
- 官方 SMQ 全表（SMQ 入门指南 v28.0）中**不存在**任何"pain"/"hyperalgesia"SMQ——所以"没有现成疼痛 SMQ"这一点上作者不算错；但**存在**与本文第二、第三类结果直接对应的官方 SMQ：
  - **SMQ "Drug abuse, dependence and withdrawal"（SMQ code 20000100）**，为层级式 SMQ（narrow + broad），其检索词含 `Drug withdrawal syndrome`、`Drug withdrawal syndrome neonatal`、`Withdrawal syndrome`、`Drug tolerance`、`Dependence`、`Drug dependence`、`Drug withdrawal convulsions`、`Drug withdrawal headache`、`Neonatal complications of substance abuse` 等（我核对了 v26.1 的 PT 清单与 v28.0 入门指南第 2.26 节）。也就是说，本稿"阿片戒断"这一臂的正规做法是直接调用该 SMQ，而不是把 87 541 条记录的 `DRUG WITHDRAWAL SYNDROME` 当作 OPIOID WITHDRAWAL SYNDROME 的"最近代理"。附带确认：`OPIOID WITHDRAWAL SYNDROME`、`OPIATE WITHDRAWAL SYNDROME`、`NEONATAL WITHDRAWAL SYNDROME`、`NEONATAL ABSTINENCE SYNDROME` 在 FAERS 精确检索均为 0，而 `DRUG WITHDRAWAL SYNDROME NEONATAL` 有 14 763 条——术语学上正确的组合是 SMQ，不是单 PT。
  - **SMQ "Lack of efficacy/effect"** 覆盖 `Drug ineffective`，因此本文的"特异性探针"其实是一个官方 SMQ 成员，本可据此写成规范表述而非手选探针。
- 层次证据：MedDRA 的疼痛类 PT 并不挂在"疼痛"这一 HLT 之下便于整体调用——我已核实 `Chest pain`（10008479）的父级包含 HLA **"Pain and discomfort NEC"**，`Allodynia`（10053552）与 `Hyperpathia`（10065952）位于 HLT **"Sensory abnormalities NEC"**（10040021，UMLS C0852417），而 `Hyperaesthesia`（10020568）位于 HLT **"Paraesthesias and dysaesthesias"**，同属 HLGT "Neurological disorders NEC"、SOC "Nervous system disorders"。三者并非同一 HLT，因此"数几个 PT"与"按层次检索"会给出不同结果——这正是需要 CMQ 的理由。

**【为什么重要】** 本稿的卖点是"术语学警诫"。但当前的术语学只做到三层中最浅的一层（单个 PT 的字面可检索性），完全没做到药物警戒领域公认的第二、第三层（SMQ / 自定义 MQ、层次化检索）。审稿人会问：既然作者知道概念可能不落在临床名称上，为什么不采用行业标准做法直接调用 SMQ 或定义 CMQ？只要这一问被提出，本文"术语学警示"的原创性就会被显著削弱；反之，补上 SMQ/CMQ 后，本文的术语学论点会从"我们发现了一个词表坑"升级为"我们示范了应该怎么做"，这是**能救活全文的一次升级**。

**【具体修改建议】**
1. 新增 **§2.3.1 Standardised and customised MedDRA queries**，明确写出：
   > "No Standardised MedDRA Query (SMQ) exists for pain or for hyperalgesia, so for the pain-related arm we defined a customised MedDRA query (CMQ) rather than relying on single preferred terms. For the withdrawal arm we used the published hierarchical SMQ *Drug abuse, dependence and withdrawal* (SMQ 20000100) in its narrow and broad forms, which already includes Drug withdrawal syndrome, Drug withdrawal syndrome neonatal, Withdrawal syndrome and Drug tolerance. For the specificity probe we used the SMQ *Lack of efficacy/effect*, which contains Drug ineffective."
2. 新增 **Table S6. Customised MedDRA query for hyperalgesia and abnormal pain perception**，列为：`PT | MedDRA code | HLT | HLGT | SOC (primary) | rationale for inclusion | narrow/broad scope`。建议的术语集（我已核实各自在 FAERS 的可用性）：
   - narrow：`HYPERAESTHESIA`（10020568，含 LLT Hyperalgesia 10020573）、`ALLODYNIA`（10053552）、`HYPERPATHIA`（10065952）
   - broad：加上 `PROCEDURAL PAIN`、`INADEQUATE ANALGESIA`（全库 8 465）、`COMPLEX REGIONAL PAIN SYNDROME`（全库 1 468）、`SENSORY DISTURBANCE`（全库 15 917）、`FIBROMYALGIA`、`NEUROPATHY PERIPHERAL`
   - 说明：`HYPERALGESIA` 作为 LLT 无法在只发布 PT 的两个库中检索，须在术语表中以"PT that carries the LLT"的形式登记，而不是列为独立检索词。
3. 在 §2.3 与 §4.4 各加一句，说明 CMQ 的 PT 集合、检索范围（narrow/broad）与选择理由，并把结果按 narrow/broad 分别报告（这与作者已有的"narrow/broad"分组完全兼容，只需把分组从"手选字符串"改成"术语集"）。

---

### M4. 作者最稳的结论（瑞芬太尼对所有疼痛类术语均报告更少）同样是术语选择的产物，换 PT 后方向反转

**【问题】** 稿件反复强调（§3.4、§4.1、§4.3、§5）"remifentanil under-reported PAIN and every other pain-related term"、"every computable head-to-head ratio was below 1"，并把这一方向当作"large, stable and reproduced"的稳健结论。但该结论建立在单一 PT `PAIN`（及若干同源 PT）之上；换用频次充足、且更贴近"疼痛加重/镇痛不足"这一临床终点的 PT 后，方向对两个比较药反转。

**【证据】** 我用作者的同一套口径（同一 cohort 定义、同一全库分母 20 692 687、同一 ROR 与 Woolf 区间算法）独立计算了若干替代 PT：

| PT | 全库 | 瑞芬太尼 a (ROR) | 芬太尼 a (ROR) | 舒芬太尼 a (ROR) | 吗啡 a (ROR) | RORR vs 舒芬太尼 | RORR vs 吗啡 |
|---|---|---|---|---|---|---|---|
| PAIN（稿件所用） | 607 176 | 23 (0.142) | 7 349 (2.138) | 98 (0.505) | 4 794 (3.083) | 0.281 | 0.046 |
| **INADEQUATE ANALGESIA** | 8 465 | **11 (5.016)** | 313 (6.498) | 10 (3.761) | 82 (3.576) | **1.333** | **1.402** |
| COMPLEX REGIONAL PAIN SYNDROME | 1 468 | 0 (—) | 41 (4.853) | 0 (—) | 36 (9.187) | — | — |
| SENSORY DISTURBANCE | 15 917 | 2 (0.483) | 109 (1.165) | 2 (0.399) | 62 (1.429) | 1.208 | 0.338 |

即：在 `INADEQUATE ANALGESIA` 上，瑞芬太尼（ROR 5.02）**高于**舒芬太尼（3.76）与吗啡（3.58），仅低于芬太尼；两个 RORR 的点估计均 > 1（区间为 0.57–3.14 与 0.75–2.63，含 1，故不构成统计显著，但方向与稿件相反）。`INADEQUATE ANALGESIA` 在语义上比 `PAIN` 更接近 Guignard、Joly 等文献所用的"术后疼痛加重、吗啡需要量增加"这一终点，也是 MedDRA 中唯一直接表达"镇痛不足"的 PT。

顺带核实：作者所选的两个"代理"其实都不合格——`CHRONIC PAIN SYNDROME` 全库仅 1 条且可疑（见 P1-3），`HYPERPATHIA` 全库仅 43 条（2015–2024 仅 28 条）。以此二者作为"慢性痛/痛觉过敏代理"，既无统计效力，也不构成概念覆盖。

**【为什么重要】** 本稿的核心论旨是"答案取决于术语选择"。作者把这一论旨用于 hyperalgesia（自证），却把自己的主结论 PAIN 当作术语无关的事实。一旦审稿人（或读者）用另一个 PT 复算，就会发现"最稳的结论"也不稳——这将同时摧毁 §3.4、§4.1、§4.3 与 §5。把它写进去反而会大幅提升本文的可信度：它证明作者的方法学警告是普适的，而不是只对自己不利的那个术语适用。

**【具体修改建议】**
1. 在 Table 2 增加一行 `INADEQUATE ANALGESIA`（或把 PAIN 一行的标签改为 "PAIN (broad proxy) / INADEQUATE ANALGESIA (specific proxy)"），并给出上表的四个 a、四个 ROR、三个 RORR 及区间。
2. 把 §3.4 首句替换为：
   > "Remifentanil was the lowest reporter of the single preferred term PAIN (a = 23; 0.14, 0.09–0.21). This is a property of that term rather than of the concept: for INADEQUATE ANALGESIA, the preferred term closest to the clinical endpoint used in the prospective literature, remifentanil reported more than sufentanil (RORR 1.33, 0.57–3.14) and more than morphine (1.40, 0.75–2.63), although neither interval excludes one."
3. 把 §5 中"它的疼痛低报告是大量、稳定并可在加拿大复现的"一句加上限定，改为"…for the single preferred term PAIN; the direction was not reproduced for every pain-related preferred term (see §3.4)"。
4. 在 Table S5 之后补一段说明：作者已做"阴性对照"以排除全局报告伪影，但未做"术语敏感度"检验；建议补做并报告全部候选 PT。

---

## 2. 重要问题（P1-1…）

### P1-1. Table 3 把"词典零"与"队列零"混为一谈；§3.5 的比较药数目有误

**【问题】** Table 3 的 `Confirmed` 列对 8 个术语一律写 "yes (zero in both)"，但其中只有 5 个是词典零（不可检索字符串），另有 3 个（`DRUG TOLERANCE`、`HYPERPATHIA`、`CHRONIC PAIN SYNDROME`）是可检索 PT，其零是**队列零**；两类零的语义完全不同，被同一措辞合并。另 §3.5 说加拿大库"remifentanil contributed no report of that term while both comparators did"，但比较药有三个。

**【证据】**
- Table 3（第 292–304 行）逐行："yes (zero in both)" 出现在 HYPERALGESIA、PAIN INCREASED、POSTOPERATIVE PAIN、CHRONIC PAIN、OPIOID WITHDRAWAL SYNDROME（词典零），以及 DRUG TOLERANCE、HYPERPATHIA、CHRONIC PAIN SYNDROME（队列零）。
- 表注仅说明前一类："The zero for the five unretrievable strings in both corpora reflects the absence of the string from the coding dictionary, not the absence of the event"，对后一类未作任何区分。
- 而 `DRUG TOLERANCE` 全库有 5 013 条（芬太尼 278、吗啡 79），是频次充足的 PT，其瑞芬太尼 0 条是**有信息量的队列零**；把它与"字符串不在词典里"并列，恰好犯了本稿警告的错误。
- §3.5（第 123 行）："in Canada remifentanil contributed no report of that term while both comparators did"。`cv/cv_pt_summary.csv` 的 HYPERAESTHESIA 行为 瑞芬太尼 0 / 芬太尼 18 / 舒芬太尼 **0** / 吗啡 30。故应为"two of the three comparators"。§3.3（第 109 行）同样只列"18 fentanyl, 30 morphine"，略去舒芬太尼 0——而舒芬太尼恰是最具药理学可比性的对照。

**【为什么重要】** Table 3 是本文"跨库确认"的唯一表格；把两类零合并，会让读者以为 `DRUG TOLERANCE` 也不在词典里。而"两个比较药"的表述是可直接查证的事实错误，会削弱审稿人对数据核对细致度的信任。

**【具体修改建议】** 把 `Confirmed` 列拆为两列：`Corpus retrievability (both / FAERS only / neither)` 与 `Cohort direction (reproduced / not reproduced / not estimable)`；并给出可直接粘贴的替换句：
> "In Canada Vigilance, remifentanil contributed no HYPERAESTHESIA report while two of the three comparators did (fentanyl 18, morphine 30; sufentanil also none), so the FAERS signal was not reproduced in the confirmation set, and the most pharmacologically comparable comparator (sufentanil) contributed none there either."

---

### P1-2. 措辞纪律：Table 2/3/4A/S5 把不可检索字符串印成 `0`，与 READUS-PV 清单自述及全文论旨冲突；另有 4 处可被读成"事件不存在"的句子

**【问题】** 作者在正文层面已经做到"not retrievable"，但在**表格层面**没有：五个词典零被放在计数列里显示为 `a = 0`，且 READUS-PV 清单声称它们"shown as not estimable rather than as zero"——两者互相矛盾。

**【证据】**
- Table 2（第 267 行起）："| HYPERALGESIA | narrow | 0 | — | …"；"| PAIN INCREASED | broad | 0 | …"；"| POSTOPERATIVE PAIN | broad | 0 | …"；"| CHRONIC PAIN | broad | 0 | …"；"| OPIOID WITHDRAWAL SYNDROME | broad | 0 | …"。同理 Table 3（第 292–298 行）、Table 4A（第 313、316、318–321 行）、Table S5（第 497、500、502、504、505 行）均以 `0` 呈现。
- `I_TableS2_READUS-PV_checklist.md` 条目 9 的答复文字："…terms that could not be estimated are shown as not estimable rather than as zero."（与表格不符）。
- 其余仍可能被读成"事件不存在"的句子：
  1. §3.2（第 103 行）"**No report in either corpus carried HYPERALGESIA as a reaction preferred term**" —— 主语是 "no report carried"，读者会读成"没有病例报告痛觉过敏"。
  2. §3.2（第 105 行）"**The zero is a property of the dictionary, not of the data.**" —— "not of the data" 断言了数据的性质，而作者只证明了查询的性质；且无法排除原始逐字词被编到别的 PT。
  3. §3.9（第 141 行）"supporting — not proving — that **the absent hyperalgesia signal** reflects the data, not the method." —— 在修正后的分析里并不存在"缺失的痛觉过敏信号"（HYPERAESTHESIA 已达标准）；此处"absent"指哪一个信号没有交代。
  4. §5（第 193 行）"a zero obtained from the clinical name alone is an artefact of terminology, not evidence of safety" —— 句子本身正确，但同段落前句"they establish that such an analysis reports whatever the chosen preferred term contains"未提示"关键词零 ≠ 病例零"的第三条可能（逐字词被编到未查询的 PT）。

**【为什么重要】** 本文的**唯一**卖点是零的语义学；表格里出现 `a = 0` 就等于在读者最常看的地方自我否证。审稿人会直接引用 Table 2 说："作者自己把不可检索字符串显示为 0 例。" READUS-PV 条目 9 的自述又与表格不符，属于可被规范类审稿人直接指出的内部不一致。

**【具体修改建议】** 
1. 把 Table 2、3、4A、S5 中五个不可检索字符串的计数单元一律由 `0` 改为 `NR`（not retrievable），并在脚注定义：`NR = the string is not retrievable as a reaction term in that corpus, so no count is interpretable; this is not a count of zero.` 全文（含图 1 图注）统一。
2. 三处句子替换：
   - §3.2 首句 → "The string HYPERALGESIA is not retrievable as a reaction term in either corpus: it returned no report among 20 692 687 FAERS reports and none among 1 154 017 Canadian reports, and an adjacent-token search returned none either."
   - §3.2 第 105 行 → "The zero is therefore a property of the query, not a count of the event: no report can be retrieved by that string in either corpus, which does not establish that no case of hyperalgesia was reported under a different preferred term."
   - §3.9 末句 → "…supporting — not proving — that the low reporting of hyperalgesia-related terms reflects reporting behaviour rather than an insensitive pipeline."
3. 在 §4.4 末补一句，把第三种可能写入："a string-level zero can also arise when the verbatim term was coded to a preferred term outside the searched set, which is why a term-set query rather than a single string is required (§2.3.1)."

---

### P1-3. "字符串只有是 PT 才会返回计数"这一前提对 FAERS 侧不成立；据此把 CHRONIC PAIN SYNDROME 列为"可检索的 PT"缺乏支持

**【问题】** §2.3、Table S4 脚注与 Analysis Plan Amendment 1 均断言"两个库的 reaction 字段只存 PT，因此字符串只有在是 PT 时才返回计数"。对加拿大侧成立；对 FAERS/openFDA 侧不成立——该索引中同时存在历史遗留的非 PT 字符串。

**【证据】**
我构造了若干"绝不可能是 PT"的字符串，用作者的同一 `.exact` 检索法查询，均返回计数：
- `patient.reaction.reactionmeddrapt.exact:"osteoarthritis,"`（**带尾随逗号**）= **1**
- `patient.reaction.reactionmeddrapt.exact:"memory loss,"`（带尾随逗号）= **1**
- `patient.reaction.reactionmeddrapt.exact:"sensiomotor peripheral neuropathy"`（小写）= **1**
这三个 1 都来自同一条报告：safetyreportid **9291134**，receivedate 2012-10-09，`reactionmeddraversionpt = 16.0`，其反应列表同时含 `'osteoarthritis,'` 与 `'Osteoarthritis'`、`'memory loss,'`、`'chronic pain syndrome'`（小写）、`'positive drug screen'`、`'Raynaud^s phenomenon'`——明显是一条遗留的自由文本病例。

因此 `CHRONIC PAIN SYNDROME` 的"1"与该条报告的 `'chronic pain syndrome'`（小写）是同一件事，**不能据此认定它是 MedDRA 的 PT**；加拿大库 4 474 923 行 reaction 中 `Chronic pain syndrome` 出现 0 次。同法确认 `.exact` 大小写不敏感：`Hypoaesthesia` 与 `HYPOAESTHESIA` 均返回 147 878，故小写不构成反证，也不构成正证。

另附一条对照：`POST PROCEDURAL PAIN` 全库 188 条，但 **2015–2024 年 0 条**、全部落在 2004–2010（我按年复核：`… AND receivedate:[20150101 TO 20241231]` = 0；`… [20040101 TO 20101231]` = 188），形态为全大写、无版本字段的遗留条目，属已不使用的历史术语；而 `PROCEDURAL PAIN` 2015–2024 有 16 936 条（全库 27 300）。这说明 FAERS reaction 字段确实混有新老两代字符串。

**【为什么重要】** 该前提是 Table S4 全部结论的逻辑基础（"检索不到 = 该字符串不是 PT"），也是 Analysis Plan Amendment 1 的核心论证。它若被推翻，Table S4 的 `Retrievable_as_preferred_term` 列就退化为"该字符串在库中出现过/没出现过"，而不是"是否为词典条目"——这恰好是作者批评别人的那种混淆。更严重的是，`CHRONIC PAIN SYNDROME` 被列为"CHRONIC PAIN 的最近可检索 PT"，是本文五个代理之一，若它根本不是 PT，则该代理名不副实。

**【具体修改建议】**
1. 把 §2.3 与 Table S4 脚注中的"only if"改为可辩护表述：
   > "In the Canadian extract the reaction field contains MedDRA preferred terms only; in openFDA the field is dominated by preferred terms but also retains legacy reaction strings from early reports, so a positive count establishes that the string occurs in the corpus and a zero establishes that it does not, and neither is by itself proof of dictionary membership."
2. 在 Table S4 增加一列 `Evidence of dictionary status`（取值如 `PT (corpus + hierarchy)` / `LLT (rolls up to PT …)` / `legacy string in 1 report (v16.0)` / `not found`），把 `CHRONIC PAIN SYNDROME` 改标为 `legacy string; not confirmed as a preferred term`。
3. 若作者确实持有 MedDRA 订阅，请在 Table S4 直接给出每个 PT 的 **MedDRA code 与 primary SOC**（我已核实可从库内或公开层次源取得，见 §4）；若无订阅，应明确声明"dictionary status was inferred from corpus occurrence, not from a licensed MedDRA release"，而不是断言其为 PT。

---

### P1-4. 五个"代理"中有两个不成立；应替换为频次充足的近义 PT 或 CMQ

**【问题】** 稿件把 HYPERAESTHESIA、HYPERPATHIA、PROCEDURAL PAIN、CHRONIC PAIN SYNDROME、DRUG WITHDRAWAL SYNDROME 统一称为"the preferred terms carrying the same concepts"并同等分析。按 MedDRA 层次与语义距离逐条评估，其中两个不能成立。

**【证据】** 逐条评估（层次与代码经公开来源核实，见 §4 与 §6）：

| 代理 PT | MedDRA code | 所在 HLT（→SOC） | 全库 FAERS | 目标概念 | 语义距离评估 |
|---|---|---|---|---|---|
| HYPERAESTHESIA | 10020568 | Paraesthesias and dysaesthesias → Nervous system disorders（次 SOC：Skin and subcutaneous tissue disorders） | 8 161 | OIH | **成立**。这是唯一能把临床词 HYPERALGESIA 收进来的 PT（其下有 LLT Hyperalgesia，见 §4）。但须声明它是"paraesthesia 家族"的感觉异常 PT，非疼痛特异，作者已在 §4.4 正确注明。 |
| HYPERPATHIA | 10065952 | Sensory abnormalities NEC → Nervous system disorders（UMLS C0020429，与 Hyperalgesia 同 CUI） | 43（2015–2024 仅 28） | 神经病理性疼痛/痛觉过敏 | **不成立**。语义上其实比 HYPERAESTHESIA 更贴近痛觉过敏，但全库仅 43 条、瑞芬太尼 0 条，"too rare to estimate"，不构成可分析的代理；把它放进 Table 2/S5/Figure 1 只是制造空行。建议：保留在术语表的 narrow 集合中，但明确声明为"登记在案、不用于估计"。 |
| PROCEDURAL PAIN | 10065800 系列 | Injury, poisoning and procedural complications（加拿大 v27.1 原生 SOC 核实） | 27 300 | 术后痛 | **部分成立**。它描述的是"操作过程中的疼痛"，不是术后疼痛；且作者在 `01_faers_results.csv` 中把它标为 SOC "General"，与加拿大库原生 SOC 不符（见 P2-2）。§4.3 已正确指出它是"procedural rather than pharmacological signal"。建议保留但降为 broad 集合，并补入 INADEQUATE ANALGESIA 作为主代理。 |
| CHRONIC PAIN SYNDROME | 未确认（见 P1-3） | 未确认 | 1（遗留自由文本） | 慢性痛 | **不成立**。全库 1 条、加拿大 0 条、疑似非 PT。以 1 条记录代表"慢性痛"与作者自己的术语学标准不符。建议替换为 **COMPLEX REGIONAL PAIN SYNDROME**（全库 1 468；芬太尼 41、吗啡 36、瑞芬太尼 0）与 **FIBROMYALGIA**（全库 1 246），并把慢性痛明确定义为一个 PT 集合而非单 PT。 |
| DRUG WITHDRAWAL SYNDROME | 10013624 | General disorders and administration site conditions（加拿大原生 SOC 核实） | 87 541 | 阿片戒断 | **成立但用法应改**。作为官方的 SMQ 成员（SMQ 20000100）它是正确的检索入口；但"the nearest retrievable preferred term to OPIOID WITHDRAWAL SYNDROME"这一表述把问题降格了——正确的做法是调用 SMQ 的 narrow/broad 检索词集合（见 M3）。 |

另：`OPIOID WITHDRAWAL SYNDROME` 在 FAERS 精确检索为 0，但 MedDRA 中有 `DRUG WITHDRAWAL SYNDROME NEONATAL`（14 763 条）——**词序**而非词本身决定了可检索性。这恰是本稿论旨的又一个更强例证，值得写入 §3.2 或 §4.4。

**【为什么重要】** "代理是否名副其实"直接决定结论的解释力。以 1 条记录和 43 条记录充当两个概念的代理，会让审稿人质疑作者是否真的理解 MedDRA 的层次与频次要求；而给出可替换的、频次充足的 PT 集合，是本文最容易达成、收益最大的修改之一。

**【具体修改建议】**
1. 把"五个 dictionary proxies"改为"a customised MedDRA query (CMQ) with narrow and broad scope"，并给出 Table S6（见 M3 建议 2）。至少应把 `CHRONIC PAIN SYNDROME` 移出估计集，加入 `COMPLEX REGIONAL PAIN SYNDROME`、`INADEQUATE ANALGESIA`。
2. 给每个代理补一列 `FAERS whole-corpus count` 与 `reports in remifentanil cohort`，让读者自行判断代理的可用性（现有 Table S4 已有全库列，缺队列列）。
3. §2.3 替换句：
   > "Terms were selected at the level of the MedDRA preferred term, but because a single preferred term can be too rare to estimate (HYPERPATHIA, 43 reports corpus-wide; CHRONIC PAIN SYNDROME, one legacy report) or too narrow (PROCEDURAL PAIN describes pain during a procedure), the five terms are presented as a query set with narrow and broad scope rather than as independently interpretable proxies."

---

### P1-5. Table 2 脚注给出的信号定义与表内星号自相矛盾

**【问题】** Table 2 脚注把信号定义为"a ≥ 3 且 95% CI 下界 > 1"，但表内 HYPERPATHIA 行的芬太尼（a = 2）与舒芬太尼（a = 1）都被标了星号。

**【证据】**
- Table 2（第 275 行）："| HYPERPATHIA | dictionary proxy (added) | 0 | — | 8.24* (1.99–34.06) | 75.63* (10.41–549.63) | — | — | — |"。
- Table S5（第 511 行）：HYPERPATHIA 的比较药 a 为 `2 / 1 / 0`。
- Table 2 脚注（第 286 行）："*Meets the signal criterion: a ≥ 3 and the lower bound of the 95% CI of the OR > 1." —— 2 与 1 均不满足 a ≥ 3。
- `01_faers_results.csv` 显示二者的 `FENTANYL_signal = True`、`SUFENTANIL_signal = True`，触发路径是 §2.4 的第三条分支（IC025 > 0：芬太尼 0.937、舒芬太尼 3.347）。可见正文方法（§2.4，第 75 行）是对的，**错的只是 Table 2 的脚注**。

**【为什么重要】** 星号是全文的信号标记，被规范类审稿人（尤其 READUS-PV 审阅者）逐一核对时会立刻暴露。且 a = 1 的"信号"本身不应被如此突出——它同时与 Table 2 末句"Remifentanil counts of fewer than 3 reports give unstable estimates"的自我克制相冲突。

**【具体修改建议】** 把 Table 2 脚注替换为与 §2.4 一致的完整定义：
> "*Meets any of the three signal criteria: a ≥ 3 with the lower bound of the 95% CI of the reporting odds ratio above 1; or a proportional reporting ratio ≥ 2 with χ² > 4; or a lower bound of the information component above 0. Estimates based on fewer than three reports are shown but are not interpretable."
并在 Table 2 的 HYPERPATHIA 行改为不标星、或在同一单元内注明触发分支（如 `8.24† (1.99–34.06)`，† = IC025 > 0）。

---

### P1-6. 第十条瑞芬太尼 HYPERAESTHESIA 报告并非"无日期"；9/10 集中在 6 个月内的事实被掩盖

**【问题】** §3.3 称"eight of the ten reports fall in 2024, one dated to 2021 and one **undated**"；Table 4C 脚注称"one has no usable receivedate"。该报告实际有可用日期。

**【证据】** 该报告 safetyreportid **25115900**，`receivedate = 20250325`、`receiptdate = 20250325`、occurcountry US、年龄 76、性别男。它之所以未进 Table 4C，是因为该表声明的时间窗为 2015–2024，而不是因为它"undated"。这与 M1 的发现叠加后，事实是：**10 条中的 9 条落在 2024-10-07 至 2025-03-25 的 5 个月内**。

**【为什么重要】** "一条无日期"读起来像零散数据；"九条在五个月内"读起来像一次事件。这一改动会直接改变读者对信号稳健性的判断，且是作者自己数据里就有的事实。

**【具体修改建议】** §3.3 替换为：
> "Eight of the ten reports were received in 2024, one in October 2024 and eight between 7 October 2024 and 12 December 2024; the tenth was received on 25 March 2025, outside the 2015–2024 window of Table 4C, and the tenth-after-that dates to 2021. Nine of the ten therefore fall within a single six-month window and share a single 76-year-old male profile (§3.x)."
Table 4C 脚注相应改为："nine reports fall in 2015–2024 and are shown; the tenth was received on 25 March 2025, outside the window of this table, and is not shown."

---

### P1-7. 加拿大库其实带有"反应持续时间/起病时间"字段，而稿件声明"无法分析起病时间"

**【问题】** §4.5 称"The FDA case-level files could not be retrieved, so time-to-onset could not be analysed"。这句话对 FAERS 成立，但忽略了加拿大 line-listing 自身携带的反应时间字段——而 OIH 的临床定义性特征正是"停药后出现"，起病时间是本主题最有价值的维度。

**【证据】** 我对 `cv/cvponline_extract_20241130/reactions.txt` 做了全量结构核验：
- 文件共 **4 474 923** 行（与 Table S4 所载完全一致）；
- 每行 10 个 `$` 分隔字段：1 = reaction 行 id，2 = report id，**3 = 时间数值，4 = 时间单位（英），5 = 时间单位（法）**，6 = PT（英），7 = PT（法），8 = SOC（英），9 = SOC（法），10 = MedDRA 版本；
- 字段 3–5 非空（即带时间信息）的共有 **185 926** 行（4 288 997 行三字段全空）；单位取值为 `Minutes / Hours / Days / Weeks / Months / Years / Seconds`（法文 `Heure(s)/Jour(s)/Semaine(s)/Mois/Années`），例：`"4707501"$"47075"$"24"$"Hours"$"Heure(s)"$"Somnolence"…`；
- 关键词中带时间信息的行数：**Hyperaesthesia 13、Procedural pain 57、Drug withdrawal syndrome 30、Allodynia 2、Dysaesthesia 2、Pain 1 196**。
- 版本字段核验：以 `"v.27.1"` 结尾的行 **4 474 767** 行、以空版本结尾 **156** 行——与 Table S4 所述"4 474 923 / 4 474 767 / 156"三个数字逐一吻合。

**【为什么重要】** ①该字段是加拿大库相对 FAERS 的一项真实优势，作者却把它当作不存在，减少了验证库的价值；②OIH 与"术后镇痛不足"的鉴别高度依赖时间关系（停药后数小时内出现 vs 术中/术后即时），作者已在 §4.5 承认起病时间不可得，而实际上部分可得；③这是一个只需描述性统计（n、中位数、四分位）就能补的小分析，能明显提升投稿竞争力。

**【具体修改建议】**
1. §4.5 改为：
   > "The FDA case-level files could not be retrieved, so time-to-onset could not be analysed in FAERS. The Canadian extract does carry a reaction time field (duration value and unit) for 185 926 of its 4 474 923 reaction rows, including 13 Hyperaesthesia and 57 Procedural pain rows, and we report it descriptively in Table S7."
2. 新增 **Table S7. Reaction time field in the Canadian extract for the study terms**：`PT | rows with a time value | unit distribution | median (IQR) in days | note that it is a duration field on the reaction, not a time-to-onset from first dose`。务必如实标注该字段是"reaction 持续时间"而非严格的"首次给药至起病时间"，避免过度解释。

---

## 3. 次要问题（P2-1…）

### P2-1. `10_term_dictionary.csv` 的布尔列掩盖了证据强度
**【问题】** `Retrievable_as_preferred_term` 是 yes/no 布尔值，把"8 161 条、跨多版本稳定存在"与"1 条 2012 年遗留自由文本"并列为 `yes`。
**【证据】** `10_term_dictionary.csv` 第 15、18 行：HYPERAESTHESIA `yes`（8 161）；CHRONIC PAIN SYNDROME `yes`（1）。稿件 Table S4 沿用同一布尔值。
**【为什么重要】** 该 CSV 是仓库中 Table S4 的唯一来源（§9 溯源表），审稿人会直接读它；布尔值让人无法判断代理的可用性。
**【具体修改建议】** 增列 `whole_corpus_count`、`cohort_count`、`meddra_code`、`primary_soc`、`evidence`（如 `PT; stable across releases 17.0–28.1` / `legacy string in one v16.0 report; dictionary status not confirmed`）。

### P2-2. `01_faers_results.csv` 的 SOC 列有两处与加拿大库原生编码不符
**【问题】** 该列似乎由启发式规则生成，与 v27.1 原生 SOC 不一致，而稿件从未在正文中给出任何术语的 SOC。
**【证据】** 我用 `reactions.txt` 的第 6、8 字段做了权威映射：`Procedural pain` → **Injury, poisoning and procedural complications**（该 CSV 标为 `General`）；`Drug withdrawal syndrome` → **General disorders and administration site conditions**（该 CSV 标为 `Psychiatric`）；`Pain`、`Drug tolerance`、`Drug ineffective` → General disorders and administration site conditions（与 CSV 一致）；`Hyperaesthesia`、`Allodynia`、`Paraesthesia`、`Dysaesthesia` → Nervous system disorders（与 CSV 一致）。
**【为什么重要】** 术语表里的 SOC 若与库内原生编码冲突，会直接动摇审稿人对术语处理的信任；且正文缺少 SOC 列，使"术语选择是否恰当"无法被核验。
**【具体修改建议】** 用加拿大库原生 SOC 替换该列，并在 Table S4 增设 `Primary SOC (MedDRA v27.1)` 与 `HLT` 两列（数据可直接取自 `reactions.txt` 第 8 字段）。

### P2-3. 仓库中 `_probe_meddra_level.py` 含美式拼写探针，会产生"拼写型假零"
**【问题】** 该探针对 `HYPERESTHESIA`、`DYSESTHESIA` 返回 0。MedDRA 采用英式拼写（`Hyperaesthesia`、`Dysaesthesia`），所以 0 是拼写造成的，而非词典事实；我实测加拿大库 `Dysaesthesia` 有 **154** 行。
**【证据】** `_probe_meddra_level.json`：`"HYPERESTHESIA": 0, "DYSESTHESIA": 0`；而 `reactions.txt` 中 `$"Dysaesthesia"$` 出现 154 次。稿件正文未使用这两个字符串，但 §9 溯源表与仓库 README 把它列为术语可检索性的证据来源。
**【为什么重要】** 本稿的核心论旨就是"字面检索会产生假零"，而作者自己的探针文件里正躺着一个拼写型假零；审稿人若发现，示范效应会反转。
**【具体修改建议】** 删除或改写这两个探针，并在 `_probe_meddra_level.py` 顶部加注释说明 MedDRA 使用英式拼写、拼写变体本身即构成假零来源；正文可把这一条作为论据（"US-spelling variants such as HYPERESTHESIA and DYSESTHESIA return zero although DYSAESTHESIA is retrievable in 154 Canadian rows"）。

### P2-4. §3.7 的 SOC 级陈述无法检验本文关心的 PT 级现象，应明确说明其分辨率不足
**【问题】** §3.7 称 "no class compatible with hyperalgesia or abnormal pain perception showed excess"。该结论只在 SOC 粒度成立，而本文关心的三个 PT（HYPERAESTHESIA、ALLODYNIA、HYPERPATHIA）**全部落在同一个 SOC（Nervous system disorders）**内，因此 SOC 级分析在结构上不可能检出它们。
**【证据】** 我用 `reactions.txt` 核实：`Hyperaesthesia`、`Allodynia`、`Dysaesthesia`、`Paraesthesia` 的 SOC 均为 Nervous system disorders；加拿大 Panel A 中 Nervous system disorders 的瑞芬太尼 ROR = 1.026（`cv/cv_soc_27.csv`）。同时 HYPERAESTHESIA 具多轴性，次 SOC 为 Skin and subcutaneous tissue disorders（ADReCS/MedDRA 层次），而 Panel A 的 Skin 类 ROR = 0.143——按主 SOC 归入 Nervous system 后，该 PT 会被 Skin 类分析完全漏掉。
**【为什么重要】** 读者会把 §3.7 读成"没有任何器官系统层面的痛觉异常信号"，从而过度解读为阴性证据；而实际上该分析对本文概念的分辨率不足。
**【具体修改建议】** §3.7 末句替换为：
> "This SOC-level comparison cannot resolve the terms of interest, which all sit within Nervous system disorders (HYPERAESTHESIA, ALLODYNIA, HYPERPATHIA), and the term-level analyses in §3.3 are the only meaningful test; the absence of an excess at SOC level is therefore uninformative about hyperalgesia and is reported only as a profile description."

### P2-5. §3.2 "well represented in both corpora" 的全库计数紧邻队列计数，易被误读
**【问题】** §3.2 用 8 161 / 523（全库）证明可检索性，紧接 §3.3 用 10 / 0（队列）作结论，同一量级语言容易让读者把两者混同。
**【证据】** §3.2 第 105 行 "…well represented in both corpora (8 161 FAERS reports, 523 Canadian reaction rows)"；§3.3 第 109 行 "remifentanil 10 reports"、"In Canada Vigilance remifentanil had no HYPERAESTHESIA report"。
**【为什么重要】** 这是本稿最容易被误引的一处；"well represented" 措辞在摘要中可能被当作"两库均证实"。
**【具体修改建议】** 改为 "…retrievable in both corpora (8 161 FAERS reports corpus-wide, 523 Canadian reaction rows corpus-wide; §3.3 gives the cohort counts, which are two orders of magnitude smaller)."

---

## 4. 我认为稿件站得住的地方（经核查无问题）

**4-1. 所有 FAERS 计数与全部加拿大计数，我在一天后独立复现，逐格完全一致。**
我用 `patient.reaction.reactionmeddrapt.exact` 对同一 openFDA 语料重新计数：HYPERAESTHESIA **8 161**、HYPERPATHIA **43**、PROCEDURAL PAIN **27 300**、CHRONIC PAIN SYNDROME **1**、DRUG WITHDRAWAL SYNDROME **87 541**、DRUG TOLERANCE **5 013**、DRUG INEFFECTIVE **1 299 278**、PAIN **607 176**、NAUSEA 778 546、VOMITING 462 663、PRURITUS 372 941、CONSTIPATION 213 536、ALLODYNIA 1 110、HYPERALGESIA 0（NOT_FOUND）；队列计数 `remifentanil AND HYPERAESTHESIA` = **10**，与稿件 a = 10 一致；年度分布 2021 = 1、2024 = 8，与 Table 4C 一致。加拿大侧我对 742 MB 原始文件做全量扫描：Hyperaesthesia **523**、Procedural pain **1 527**、Drug withdrawal syndrome **1 667**、Drug tolerance **387**、Allodynia **29**、Pain **49 260**、Drug ineffective **208 365**、Nausea **64 611**、Vomiting **39 131**、Pruritus **46 769**、Constipation **13 579**、Hyperalgesia/Hyperpathia/Chronic pain*/Postoperative pain/Pain increased/Opioid withdrawal syndrome 均为 **0**——与 Table S4 逐一吻合。**数据可复现性极好，这是本文最强的一点。**

**4-2. 关键 MedDRA code 断言是**正确**的；"HYPERALGESIA 是 LLT"这一断言也经多源交叉证实（尽管无法从一手 MedDRA 源验证）。**
- **10020568 = HYPERAESTHESIA**：经两个独立公开来源确认（厦门大学 ADReCS 的 ADR 条目给出 "MedDRA Code 10020568" 及层次 "Nervous system disorders → Neurological disorders NEC → Paraesthesias and dysaesthesias → Hyperaesthesia"；Wikidata 派生知识库给出 "Medical Dictionary for Regulatory Activities ID 10020568 = hyperesthesia"）。作者把 code 写进正文的风险，经核查**没有兑现**。
- "HYPERALGESIA 是映射到该 PT 的 LLT"：无法从一手来源核验（MedDRA 为订阅制），但有三条独立的旁证：(i) Cochrane 的 MedDRA 映射给 "Hyperalgesia" 分配 code **10020573**，该 code 落在 PT 10020568 的 LLT 编码块内（其邻居 10020569 = LLT "Hyperaesthesia skin"）；(ii) ADReCS 对 code 10020568 的同义词表含 "Hyperalgesia / Hyperalgesias / Hyperalgesic Sensations"；(iii) MedDRA PT 10020568 挂的 MeSH 描述符是 **D006930 = Hyperalgesia**（非 D006941 Hyperesthesia）。**结论：该断言可判为"高度可信、但须标注为间接核实"。** 稿件应以更准确的方式表述，见下方修改建议。
**可直接粘贴的替换句（§2.3）**：
> "HYPERALGESIA is a MedDRA lowest level term that rolls up to the preferred term HYPERAESTHESIA (MedDRA 10020568), so the clinical word cannot be retrieved by a preferred-term query in any database; neither corpus publishes lowest level terms, so the number of cases originally coded to the lowest level term 'Hyperalgesia' rather than to 'Hyperaesthesia' is not recoverable from either source. Dictionary status was checked against the published hierarchy rather than inferred from corpus counts."

**4-3. "加拿大库的 reaction 字段只存 PT"这一断言，经我全量结构核验为**正确**；我另发现了一个作者未提及的字段。**
reactions.txt 共 4 474 923 行、10 个 `$` 分隔字段，第 6 列是 PT（英）、第 8 列是 SOC（英），**不存在 LLT 列，也不存在 verbatim 列**；第 3–5 列是反应时间数值与单位（英/法），非 LLT。因此"未检索到 ≠ 未报告"这一论证的另一半（"加拿大库不可能藏着 LLT 或原始词"）**成立**。此外我核验的三个版本数字 **4 474 923 / 4 474 767 / 156** 与 Table S4 完全一致。

**4-4. 相邻词短语检索（match_phrase）的方法学描述是准确的，CHRONIC PAIN 的"1"也确实自洽。**
openFDA 的非 `.exact` 检索在 `reactionmeddrapt` 上是 token 相邻匹配：单 token 查询会命中所有含该 token 的 PT（`"PAIN"` = 2 213 093 vs `.exact` = 607 176），多 token 查询要求相邻（`"CHRONIC PAIN"` = 1）。我在作者缓存的 `__DISCO__CHRONIC PAIN_500` 中发现该次查询返回的唯一报告的 67 个反应 PT 列表里确实含 `CHRONIC PAIN SYNDROME`（count 1），与 Table S4 的 `CHRONIC PAIN SYNDROME = 1` 互为印证。作者的内部一致性成立，Table S4 脚注对该检索的第二路径作用的描述也站得住。

**4-5. 时间敏感性分析的算术正确，且"2024 年簇"的处置方向正确（虽理由需替换）。**
我复算 `04_sensitivity_year_hyperaesthesia.csv` 的 2024 年瑞芬太尼 OR：(8/440)/(329/1 318 337) = **72.86**，与文件一致；`04_sensitivity_2024cluster_hyperaesthesia.csv` 的 72.86/4.73 = **15.41** 一致；leave-2024-out 后 a = 1、ROR 0.70、RORR vs 芬太尼 0.11，与 Table 4C 脚注及 §3.8 一致。作者主动报告"该信号不稳定、并可能源于编码/上报迁移而不是药物"，这种自我克制是值得肯定的——问题只在于它把原因归错了（见 M1、M2）。

**4-6. §4.4 对 HYPERAESTHESIA 语义局限的自我注明是专业且正确的。**
"HYPERAESTHESIA denotes increased sensitivity to stimulation generally rather than to pain" —— 与 MedDRA 层次完全一致（该 PT 位于 HLT "Paraesthesias and dysaesthesias"，而 ALLODYNIA 与 HYPERPATHIA 位于 HLT "Sensory abnormalities NEC"）。作者能主动指出自己所选代理的非特异性，是本文术语学素养的体现。

---

## 5. 需要作者明确澄清的事实性问题

1. **FAERS 侧"相邻词短语检索"的精确检索式是什么？** 是否为 `patient.reaction.reactionmeddrapt:"<TERM>"`（无 `.exact`）？若否，请给出原字符串。
2. **作者是否看过 CHRONIC PAIN 那唯一一条命中是什么？** 若是，请说明为何 Table S4 仍把 `CHRONIC PAIN SYNDROME` 列为可比对的另一行、而正文未说明二者是同一报告。
3. **那 10 条瑞芬太尼 HYPERAESTHESIA 报告，作者是否检查过任何病例级字段（safetyreportid、receivedate、occurcountry、患者年龄/性别、并发用药、`primarysource.qualification`）？** 若未检查，请在修回稿中补做并说明 10 条代表多少位**不同患者**。
4. **第十条报告的 receivedate 在作者的抽取快照中是否为 20250325？** 若是，请说明 §3.3 的 "one undated" 与 Table 4C 脚注的 "no usable receivedate" 从何而来；若否（即当时确为缺失），请说明快照版本与复现方式。
5. **作者是否持有 MedDRA 订阅（或可访问 MedDRA Web-Based Browser / MVAT）？** 这决定了：(a) Table S4 的 PT 身份能否以 code 与 primary SOC 形式给出；(b) 能否按 SMQ/MQ 检索；(c) 能否用 MVAT 直接检验 HYPERAESTHESIA 与 PROCEDURAL PAIN 在近两年的版本变更记录。若无法访问，请明确声明术语身份是"由语料出现推断"而非"由词典查证"。
6. **"five dictionary proxies … analysed on the same footing"中的 "same footing" 具体指什么？** 五个 PT 的全库频次跨 4 个数量级（8 161 到 1），是否对代理的可用性设过任何下限（如全库 ≥ 100 或队列 a ≥ 3 才进入估计）？若没有，请说明理由。
7. **稿件是否考虑过 SMQ 或 CMQ？** 若是，请说明为何未采用；若否，请说明在"临床名称 ≠ 编码名称"这一立论下，为何手工选择五个 PT 优于构建术语集。这个问题需要正面回答，因为当前稿件的 READUS-PV 清单未覆盖该项。
8. **加拿大库 reactions.txt 第 3–5 字段的官方字段名是什么？** 请引用 Health Canada 的 Data Structure/Glossary 给出字段名（我读到的是"反应持续时间/单位"），并说明为何在 §4.5 称起病时间不可分析。
9. **`01_faers_results.csv` 的 `SOC` 列来源是什么？** 为何 `PROCEDURAL PAIN` 标为 `General` 而加拿大库原生 SOC 为 `Injury, poisoning and procedural complications`，`DRUG WITHDRAWAL SYNDROME` 标为 `Psychiatric` 而原生 SOC 为 `General disorders and administration site conditions`？
10. **`_probe_meddra_level.py` 中的 `HYPERESTHESIA` / `DYSESTHESIA` 两个美式拼写探针，是否被用于任何可检索性判断？** 若曾用于（即使只在内部），请说明如何避免把拼写差异误判为词典差异。

---

## 6. 我实际做的独立核查

### 6.1 读过的文件（未读取任何 REVIEW_*/RESPONSE_*/REVISION_*/01_任务状态.md/00_项目总览…/SUBMISSION_MANIFEST.md/GITHUB_DEPOSIT_SOP.md/author_verification_statement.md，也未读 _review_r5/ 下他人输出）

`_PANEL_BRIEF.md`；`I_正文_IMRaD_en.md`（全文）；`ANALYSIS_PLAN.md`；`01_faers_results.csv`；`10_term_dictionary.csv`；`_probe_pt_enum.json`；`_probe_meddra_level.json`；`_faers_cache.json`；`04_sensitivity_*.csv/.json`；`cv/cv_pt_summary.csv`；`cv/cv_soc_27.csv`；`cv/cvponline_extract_20241130/reactions.txt`（742 MB，全量扫描 + 抽样）；`I_TableS2_READUS-PV_checklist.md`；`key.txt`（仅读取以完成只读 API 查询，未记录其内容）。

### 6.2 外部独立来源
- openFDA drug/event API（实时，2026-09-17）：计数复核、报告级明细、按年检索、版本字段、SMQ 成员核验。
- Health Canada：Canada Vigilance 数据字典/术语表（含"每次 MedDRA 新版发布后回头重编"的官方说明）。
- MedDRA 层次/代码的公开旁证：厦门大学 ADReCS（10020568 及层次）、Cochrane 的 MedDRA 条件映射（10020573 Hyperalgesia；10040021 Sensory Abnormalities NEC；10065952 Hyperpathia）、Helmholtz PhenoDis（10053552 Allodynia）、BioPortal MEDDRA（10008479 Chest pain 的父级 HLT "Pain and discomfort NEC"）、MeSH D006930（Hyperalgesia）、SMQ 入门指南 v28.0（官方 SMQ 全表）与 SMQ 20000100 的 PT 清单。

### 6.3 我跑过的命令与关键结果（均为我本人执行）

```bash
# 1) 加拿大库结构核验（全量）
awk -F'\\$' '...' reactions.txt                     # （超时后改为 grep 方案）
grep -c '\$""\$""\$""\$' reactions.txt              # 4 288 997 行：第3–5列全空
grep -v '\$""\$""\$""\$' reactions.txt | head -15   # 第3–5列非空行实为"时间数值+单位(英/法)"
grep -c -E '\$"v\.27\.1"\r?$' reactions.txt         # 4 474 767
grep -c -E '\$""\r?$' reactions.txt                 # 156
wc -l < reactions.txt                               # 4 474 923
# 结论：10 列，无 LLT 列、无 verbatim 列；第3–5列共 185 926 行非空(时间字段)

# 2) 加拿大库术语计数（单次全量扫描 + 排序计数）
grep -o -E '\$"(Hyperaesthesia|Hyperesthesia|Hyperalgesia|Hyperpathia|Allodynia|Dysaesthesia|
  Paraesthesia|Chronic pain|Chronic pain syndrome|Postoperative pain|Pain increased|Procedural pain|
  Opioid withdrawal syndrome|Drug withdrawal syndrome|Nausea|Vomiting|Pruritus|Constipation|
  Drug ineffective|Drug tolerance|Pain|Pain in extremity|Abdominal pain)"\$' reactions.txt | sort | uniq -c
# 结果：523 / 1527 / 1667 / 387 / 29 / 49 260 / 208 365 / 64 611 / 39 131 / 46 769 / 13 579 / 154(Dysaesthesia)
#      其余（Hyperalgesia、Hyperpathia、Chronic pain*、Postoperative pain、Pain increased、
#            Opioid withdrawal syndrome、Hyperesthesia）均 0

# 3) 加拿大库 PT→SOC 权威映射（原生 v27.1）
grep -E '\$"(Pain|Hyperaesthesia|Hyperpathia|Allodynia|Procedural pain|Drug withdrawal syndrome|
  Drug tolerance|Dysaesthesia|Paraesthesia|Drug ineffective)"\$' reactions.txt | awk -F'\\$' '{print $6" ||| "$8}' | sort | uniq -c
# 结果：Procedural pain → Injury, poisoning and procedural complications
#       Drug withdrawal syndrome / Pain / Drug tolerance / Drug ineffective → General disorders and administration site conditions
#       Hyperaesthesia / Allodynia / Paraesthesia / Dysaesthesia → Nervous system disorders

# 4) FAERS 术语存在性/计数复核（openFDA API，含 api_key）
patient.reaction.reactionmeddrapt.exact:"<TERM>"    &limit=1
#    HYPERAESTHESIA 8161; HYPERPATHIA 43; PROCEDURAL PAIN 27300; CHRONIC PAIN SYNDROME 1;
#    DRUG WITHDRAWAL SYNDROME 87541; PAIN 607176; DRUG TOLERANCE 5013; DRUG INEFFECTIVE 1299278;
#    ALLODYNIA 1110; HYPERALGESIA / PAIN INCREASED / POSTOPERATIVE PAIN / CHRONIC PAIN /
#    OPIOID WITHDRAWAL SYNDROME / OPIATE WITHDRAWAL SYNDROME / NEONATAL WITHDRAWAL SYNDROME /
#    NEONATAL ABSTINENCE SYNDROME / HYPERESTHESIA / DYSESTHESIA / PAIN EXACERBATION / PAIN WORSENED = 0
#    POST PROCEDURAL PAIN 188; DRUG WITHDRAWAL SYNDROME NEONATAL 14763; INADEQUATE ANALGESIA 8465;
#    COMPLEX REGIONAL PAIN SYNDROME 1468; SENSORY DISTURBANCE 15917
#    (deliberate non-PT strings) exact:"osteoarthritis," = 1, exact:"memory loss," = 1,
#    exact:"sensiomotor peripheral neuropathy" = 1  ← 均来自 safetyreportid 9291134 (2012, v16.0)
#    exact:"Hypoaesthesia" 与 exact:"HYPOAESTHESIA" 同为 147 878（大小写不敏感）

# 5) FAERS 年度复现
exact:"HYPERAESTHESIA" AND receivedate:[YYYY0101 TO YYYY1231]
#   2004–2026 逐格：98,106,140,154,157,190,260,333,390,471,483,646,568,587,573,438,477,484,486,399,337,267,116
#   与 04_sensitivity_year_hyperaesthesia.csv 的 HYPERAESTHESIA_year_total 列完全一致
exact:"POST PROCEDURAL PAIN" AND receivedate:[20040101 TO 20101231]              = 188
exact:"POST PROCEDURAL PAIN" AND receivedate:[20150101 TO 20241231]              = 0

# 6) 10 条瑞芬太尼 HYPERAESTHESIA 报告逐条调阅
search=patient.drug.activesubstance.activesubstancename.exact:("REMIFENTANIL" "REMIFENTANIL HYDROCHLORIDE")
       AND patient.reaction.reactionmeddrapt.exact:"HYPERAESTHESIA"&limit=10
#   9/10 为同一美国来源（safetyreportid 24402565, 24641950, 24675457, 24690033, 24715261,
#   24716978, 24726643, 24727039, 25115900），年龄 76、性别男、qualification 2/3，
#   同一七药围术期配伍；第10条为日本 19700005 (2021-08-13)
#   逐条 reactionmeddraversionpt 取值为 24.0 / 27.1 / 28.1（另一 2014 记录为 17.0）

# 7) 其他术语的瑞芬太尼报告逐条核对
search=<REMIFENTANIL> AND exact:"PROCEDURAL PAIN"        → 14（含 2018 年 US 同一 42 岁女性 3 条连号、
                                                           2019 年 ES 同一 6 药组合 2 条，疑重复）
search=<REMIFENTANIL> AND exact:"DRUG WITHDRAWAL SYNDROME" → 7（含 3 条同一 62 岁患者）
search=<REMIFENTANIL> AND exact:"PAIN"                    → 23（含 2025 年 CA 同一 33 岁女性 7 条、2024 年 DE 同一 24 岁 3 条）
search=<REMIFENTANIL> AND exact:"ALLODYNIA"               → 1（JP, 2023-09-21）
```

### 6.4 我自己算出的关键数值（与稿件的差异）

| 量 | 稿件值 | 我的独立值 | 结论 |
|---|---|---|---|
| HYPERAESTHESIA 全库(FAERS) | 8 161 | 8 161 | 一致 |
| 瑞芬太尼 HYPERAESTHESIA a | 10 | 10 | 一致 |
| 2024 年瑞芬太尼 HYPERAESTHESIA a | 8 | 8 | 一致 |
| 2021 年瑞芬太尼 HYPERAESTHESIA a | 1 | 1 | 一致 |
| 第十条报告 receivedate | "无日期" | **2025-03-25** | **不一致（P1-6）** |
| 疑似同一病例的报告数 | 未报告 | **9/10** | **稿件缺失（M1）** |
| 舒芬太尼 2024 HYPERAESTHESIA a | 7 | 7（=该簇中带舒芬太尼的条数） | 一致，但**与瑞芬太尼 2024 点估计非独立（M1）** |
| 加拿大库 reaction 行数 | 4 474 923 | 4 474 923 | 一致 |
| 加拿大库 v27.1 行数 / 空版本行数 | 4 474 767 / 156 | 4 474 767 / 156 | 一致 |
| 加拿大库术语行数（12 项） | 523/1 527/1 667/387/29/49 260/208 365/64 611/39 131/46 769/13 579/0×6 | 全部一致 | 一致 |
| 加拿大库带时间字段行数 | 稿件未提 | **185 926** | **稿件缺失（P1-7）** |
| INADEQUATE ANALGESIA 瑞芬太尼 ROR（vs 舒芬太尼 3.76、吗啡 3.58） | 稿件未做 | **5.02（RORR 1.33 / 1.40）** | **方向与稿件主结论相反（M4）** |
| HYPERAESTHESIA 全库 2024 年报告数 | 337（作者文件中有） | 337（十年最低） | 一致，但**作者未用它否证自己的"2024 编码迁移"解释（M2）** |
| openFDA 是否暴露逐条 MedDRA 版本 | "exposes none" | **`patient.reaction.reactionmeddraversionpt` 可查** | **稿件表述有误（M2）** |
| HYPERAESTHESIA 是否为 10020568 | 是 | 是（两独立来源确认） | **一致，作者正确** |
| CHRONIC PAIN SYNDROME 是否为可检索 PT | "yes" | 存疑（唯一记录为 2012 年 v16.0 遗留自由文本，同报告含多个非 PT 串） | **缺乏支持（P1-3）** |

### 6.5 我未能独立核验的项目（明确声明"不可核实"）

1. **HYPERALGESIA = LLT 且其 PT 为 10020568**：MedDRA 为 ICH 订阅制词典，公开渠道无权威 LLT→PT 表。我给出的三条旁证（Cochrane 分配 code 10020573、ADReCS 同义词表、MeSH D006930 挂靠）**一致指向同一结论，但不构成一手核验**。核实路径：MSSO MedDRA Web-Based Browser（订阅）或 MVAT 中检索 LLT "Hyperalgesia" 与其 PT 归属；或 UMLS 许可版中的 MDR 源（含 LLT 层）。
2. **`POSTOPERATIVE PAIN`、`PAIN INCREASED`、`CHRONIC PAIN`、`OPIOID WITHDRAWAL SYNDROME` 是否为历史上的 MedDRA PT（曾存在、后被 demote）**：FAERS 中为 0、加拿大 v27.1 中为 0，只能证明"在当前语料中不可检索"，不能证明它们在 v7 等旧版中不曾是 PT。核实路径：MVAT 逐版本对比（v7.0 → v28.1）中的 LLT promotion/demotion 与"currency change"记录，或调阅 MSSO 各版本 "What's New / Change Request" 文档。值得注意的是：作者本人在 Analysis Plan Amendment 1 中承认先前的错误说法是"five absent strings are MedDRA preferred terms"，其更正方向正确，但更正后的表述仍有同样的可核验性缺口。
3. **我未能核验 2024 年 HYPERAESTHESIA / PROCEDURAL PAIN 是否发生 PT 升格或新增**：SMQ 层面 28.0 无新增 SMQ，第 28.0 版有 23 项 LLT→PT 升格与 35 项降格，但公开渠道无误不给出具体术语清单。核实路径：MSSO MVAT（订阅）+ "MedDRA Version Report"。**不过**，我用语料本身对该问题给出了一条更强的间接否证：HYPERAESTHESIA 在 v17.0 即有报告、且其全库年报告量在 2024 年降至十年最低（337 条），因此"2024 年新出现/升格"这一假设被语料证据排除（见 M2）。
4. **加拿大库第 3–5 字段的官方规范名称**：我通过全量数据形态（数值 + 英/法时间单位，单位取值为 Minutes/Hours/Days/Weeks/Months/Years/Seconds）判定其为反应时间（持续时间）字段，但 Health Canada 的 Data Structure 页面在本次访问中未返回字段清单，故**未能取得官方字段名**。核实路径：Health Canada, Canada Vigilance Adverse Reaction Online Database — Data Structure / Glossary（open.canada.ca 数据集页的 "Data Dictionary" 链接）。

---

## 7. 术语学必改清单（≤7 条，按优先级）

1. **[M1，必改] 报告病例级事实并把信号降级为术语演示。** 新增一节给出 10 条瑞芬太尼 HYPERAESTHESIA 报告的 `safetyreportid / receivedate / occurcountry / 年龄 / 性别 / primarysource.qualification / 并发用药数`，明写"10 条中有 9 条是同一个 76 岁男性病例、2024-10-07 至 2025-03-25 之间、同一围术期配伍，独立患者数为 2"，并把 §3.3 / §4.1 / §5 的"signal"改为"term-level demonstration"。
2. **[M3，必改] 引入 SMQ 与自定义 MedDRA 查询。** 新增 §2.3.1：戒断臂调用官方层级式 **SMQ "Drug abuse, dependence and withdrawal"（20000100）**（narrow + broad）；探针改用 **SMQ "Lack of efficacy/effect"**；疼痛臂定义 **CMQ** 并新增 Table S6（列：`PT | code | HLT | HLGT | primary SOC | narrow/broad | rationale`）。明确说明"无疼痛/hyperalgesia 官方 SMQ"。
3. **[M2，必改] 改正版本字段与版本迁移的表述，并补做版本检验。** 把"openFDA exposes none"改为"openFDA 通过 `patient.reaction.reactionmeddraversionpt` 暴露逐条版本"；补充说明加拿大库因 Health Canada 每次新版发布回头重编而呈单一版本标签；新增 HYPERAESTHESIA 全库报告的版本构成表，用以正式排除版本漂移。
4. **[P1-2，必改] 统一零的语义。** 把 Table 2 / 3 / 4A / S5 中五个不可检索字符串的计数单元由 `0` 改为 `NR`，脚注定义 `NR`；同步修改 READUS-PV 清单条目 9 的自述，使声明与表格一致。
5. **[P1-4 / M4，必改] 把"五个代理"替换为术语集，并补入一个能支撑疼痛结论的 PT。** 移除 `CHRONIC PAIN SYNDROME`（1 条遗留自由文本），加入 `INADEQUATE ANALGESIA`（8 465）、`COMPLEX REGIONAL PAIN SYNDROME`（1 468）与 `SENSORY DISTURBANCE`（15 917）；在 Table 2 增设 `INADEQUATE ANALGESIA` 行，使"瑞芬太尼所有疼痛术语均低报告"这一结论接受术语敏感度检验。
6. **[P1-3 / P1-5，必改] 把"只有是 PT 才返回计数"改为可辩护表述，并统一信号定义。** §2.3 / Table S4 脚注改为"加拿大侧仅含 PT；openFDA 侧亦保留早期遗留字符串"，Table S4 增设 `Evidence of dictionary status` 列；Table 2 脚注改为 §2.4 的三分支完整定义，并使 HYPERPATHIA（比较药 a = 1、2）的标注与之相容。
7. **[P1-1 / P1-6 / P1-7，必改] 三处一致性修正。** (a) Table 3 拆分"词典可检索性"与"队列方向"两列，§3.5 的 "both comparators" 改为 "two of the three comparators (sufentanil also none)"；(b) §3.3 与 Table 4C 脚注的"undated"改为"the tenth report was received on 25 March 2025, outside the window"；(c) §4.5 补充加拿大库 reaction 时间字段（185 926 行，含 Hyperaesthesia 13 行、Procedural pain 57 行）并新增描述性 Table S7，避免"起病时间完全不可分析"的绝对化表述。
