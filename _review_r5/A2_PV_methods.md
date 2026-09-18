# Round-5 独立审稿 — A2_PV_methods 药物警戒信号检测（disproportionality analysis）方法学家

## 0. 审稿人身份与总体结论

我从事自发报告系统失衡分析的方法学研究与监管实务审查，熟悉 ROR/PRR/IC/EBGM 的统计构造、FDA/EMA/UMC 的信号检测规程，以及自发报告数据库固有偏倚（notoriety bias、masking、competition bias、under-reporting、报告者效应、重复报告与随访版本）。

**Verdict: Major Revision**（按 Original Article 标准）

理由（具体到本稿）：

1. 稿件最关键的两条"可行性声明"经我实测为**不成立**：§2.2 称"a role-restricted analysis was not possible, the case-level file needed to attribute role being inaccessible"，§4.5 称"The FDA case-level files could not be retrieved"。但 openFDA **就是**个案级数据源——`patient.drug.drugcharacterization` 在 20 692 690/20 692 687 条记录上存在，且 `search` 端点直接返回嵌套的 `patient.drug` 数组（我取到一条含 7 个 drug entry、瑞芬太尼为 `drugcharacterization=2`、`route=INTRAVENOUS`、`safetyreportversion=3` 的记录）。**两项最大局限（role-agnostic 队列、无 TTO）不是数据不可得，而是分析未做。**
2. 四药队列**远非独立**：瑞芬太尼队列中 29.3%（1 575/5 375）的报告同时含芬太尼；标题术语 HYPERAESTHESIA 的 10 例瑞芬太尼报告中 **6 例同时含芬太尼**。剔除共同报告后，RORR vs 芬太尼由 0.696 (0.37–1.31) 变为 0.393 (0.15–1.06)，瑞芬太尼自身 ROR 由 4.73 (2.54–8.80) 变为 2.67 (1.00–7.12)；全稿**唯一** >1 的显著头对头比值 PROCEDURAL PAIN vs 芬太尼由 1.962 (1.14–3.39) 变为 1.386 (0.65–2.96)，不再显著。这一破坏从未被界定或检验。
3. FAERS 语料是**案例版本（case version）**而非报告：4 938 726 条（23.9%）带 `safetyreportversion ≥ 2`，且随访版本占比在四队列间**不同**（瑞芬太尼 33.7%、芬太尼 27.7%、舒芬太尼 29.6%、吗啡 39.6%）。仅按 version 1 重算，HYPERAESTHESIA 的 RORR vs 芬太尼由 0.696 变为 **0.979 (0.48–1.99)**，vs 吗啡由 0.389 变为 0.550 (0.27–1.13)——即"四者中最弱"这一核心定量结论**在作者自己的数据源上不能成立**。§4.5 的"counts are inflated across every cohort, which would not generate the observed direction"是无证据断言，且前提（各队列等比例膨胀）本身就是错的。
4. §2.4 声明了三种（实为四种）测量并列的信号判定，Table 2 脚注却只写 ROR 一条；我逐格重算 72 个 2×2 表后确认，26 个星号中有 2 个（HYPERPATHIA/芬太尼 a=2、HYPERPATHIA/舒芬太尼 a=1）**不满足脚注写明且强调的 a ≥ 3**，只能由 PRR/IC025 触发。43 个可估计格中，ROR 规则触发 24 个、PRR 规则 18 个、IC025 规则 26 个、三者交集仅 16 个——"signal"的数目随所选测量在 18–26 之间摆动，而稿件从未披露。
5. "阴性对照"标签在概念上错误（四个术语都是阿片类**已知**ADR，芬太尼的 PAIN、NAUSEA、VOMITING、CONSTIPATION 均 OR>1），其中 PRURITUS 在鞘内/椎管内阿片中是**典型效应**（舒芬太尼常规鞘内给药），把它当阴性对照并把它唯一的 >1 比值（1.310）解释为"区间含 1 的例外"，是把一个已预期的机制性差异降格为噪声。
6. 稿件把 FAERS 与加拿大描述为 "primary + confirmation" 并称加拿大 "methodologically cleaner"，但两库的 RORR 是**不同估计量**（加拿大的 c、d 精确抵消，FAERS 的不抵消，差约 0.7%–3.2%），且两库分母是不同对象（FAERS 20 692 687 为案例版本，加拿大 1 154 017 为源去重报告）。"跨库确认"应降格为"两个单库分析的方向比较"。

---

## 1. 重大问题（Major）

### M1. 报告级数组导致四队列互相重叠，"头对头"不成立；RORR 的实际破坏程度可量化且很大

**【问题】** 稿件 §4.5 承认"`patient.drug` is an array and the search is report-level"，但只把它当作 route 归因的小瑕疵处理；实际上它同时摧毁了 §2.2 的 cohort 定义与 §3 全部头对头结论所依赖的"四药队列相互独立"这一隐含前提。

**【证据】**（openFDA 实时查询，2026-09-17，查询串见 §6）
- 队列规模：REMIFENTANIL 5 375、FENTANYL 121 819、SUFENTANIL 6 513、MORPHINE 56 501。
- 两两重叠（同一报告同时含两药）：**R∩F = 1 575**（占瑞芬队列 29.3%）、R∩S = 483（9.0%）、R∩M = 323（6.0%）、F∩S = 299、F∩M = 6 185、S∩M = 596。
- 四队列并集 = **180 982**，而四者朴素加和 = 190 208，即 **5.1% 的重复计入**（`search=(R OR F OR S OR M)`）。
- 标题术语的破坏最大：**HYPERAESTHESIA 的 10 例瑞芬太尼报告中 6 例同时含芬太尼**（`R AND F AND PT:'HYPERAESTHESIA'` = 6）。
- 我用"瑞芬队列剔除与对照共同报告"重算（单对剔除口径）：
  - HYPERAESTHESIA：a 10→4，队列 5 375→3 800，瑞芬 ROR **4.73 (2.54–8.80) → 2.67 (1.00–7.12)**（下界触及 1，按本人 a≥3 且下界 >1 的规则已不成立）；RORR vs 芬太尼 **0.696 (0.37–1.31) → 0.393 (0.15–1.06)**。
  - PROCEDURAL PAIN：14 例中 7 例共同报告；RORR vs 芬太尼 **1.962 (1.14–3.39) → 1.386 (0.65–2.96)**——**全稿唯一显著 >1 的头对头比值消失**。
  - 稳健者：PAIN 0.066→0.057；DRUG INEFFECTIVE 0.568→0.600；DRUG WITHDRAWAL SYNDROME 0.046→0.055。

**【为什么重要】** 这不是精度问题，而是**估计量失效**：RORR 的分母里装着分母药自己的病人（瑞芬太尼与芬太尼在麻醉中常规联用）。审稿人一旦意识到 29.3% 的共用率，Table 2 的每一行 RORR、"remifentanil was the weakest of the four"、"eleven of the twelve computable negative-control ratios were below 1"都会被要求重算；而我在瑞芬太尼队列内做的重叠剔除显示，**正向发现（PROCEDURAL PAIN）消失、反向发现（PAIN/DRUG INEFFECTIVE）稳健**——恰好是作者最需要知道的结论。

**【具体修改建议】**
1. 补做队列互斥化分析并在新增 Table S6 给出：列为 `PT | a_REMI | a_REMI&F | RE MI_only_a | RE MI_only_cohort | ROR_remi_only | RORR_vs_FENTANYL_exclOverlap (95%CI) | RORR_as_published`，对 18 个术语全表输出。
2. Methods 明确写出：`Cohorts are report-level sets that are not mutually exclusive: 1 575/5 375 (29.3%) of remifentanil reports also name fentanyl. Head-to-head ratios are therefore re-estimated on a remifentanil set from which co-reported comparator reports have been removed (Table S6).`
3. Abstract 的 `remifentanil's signal is the weakest of the four` 在补做完成前应删去。

---

### M2. FAERS 语料是案例版本集合，随访版本占比在队列间不同（27.7%–39.6%），"weakest of four"不能存活

**【问题】** 稿件把 20 692 687 称为 "reports"，§4.5 只把去重问题说成"the FDA's case-level de-duplication"的缺失，并断言"which would not generate the observed direction"。实际上 openFDA 存的是**同一病例的多个版本**，且各队列的版本膨胀因子不同。

**【证据】**
- `_exists_:safetyreportversion` = 17 683 862；`safetyreportversion:1` = 12 745 136；`safetyreportversion:[2 TO *]` = **4 938 726（占全库 23.9%）**。
- 各队列随访版本占比：REMIFENTANIL **33.7%**（1 812/5 375）、FENTANYL **27.7%**（33 710/121 819）、SUFENTANIL **29.6%**（1 925/6 513）、MORPHINE **39.6%**（22 361/56 501）。极差 1.43 倍，**不是等比例膨胀**。
- 仅保留 `safetyreportversion:1`（N = 12 745 136；各队列 3 563 / 88 109 / 4 588 / 34 140；HYPERAESTHESIA 全库 8 161→4 059，分药 a 为 8/194/16/135）后我重算：

| PT | RORR vs F（原稿） | RORR vs F（version 1） | RORR vs M（原稿） | RORR vs M（version 1） | 瑞芬 ROR（原稿→version 1） |
|---|---|---|---|---|---|
| HYPERAESTHESIA | 0.696 (0.37–1.31) | **0.979 (0.48–1.99)** | 0.389 (0.21–0.73) | **0.550 (0.27–1.13)** | 4.729 → **7.076** |
| PAIN | 0.066 (0.04–0.10) | 0.056 (0.03–0.10) | 0.046 | 0.045 | 0.142 → 0.123 |
| PROCEDURAL PAIN | 1.962 (1.14–3.39) | 3.549 (1.76–7.14) | 0.878 | 1.726 (0.85–3.51) | 1.977 → 2.336 |
| DRUG INEFFECTIVE | 0.568 (0.49–0.65) | 0.592 (0.50–0.71) | 0.470 | 0.518 | 0.601 → 0.541 |
| PRURITUS | 0.833 (0.61–1.14) | **1.114 (0.77–1.62)** | 0.328 | 0.425 | 0.419 → 0.482 |
| CONSTIPATION | 0.122 (0.07–0.22) | 0.051 (0.01–0.20) | 0.062 | 0.024 | 0.197 → 0.067 |

**【为什么重要】**
- HYPERAESTHESIA 的 RORR 从 0.70 变成 0.98，CI 跨 1；vs 吗啡从 0.389 变成 0.550，CI 也跨 1。**§4.1 "Remifentanil's signal is the smallest of the four" 与 §5 Conclusion 的同一句在作者的原始数据上无法复现。**
- PRURITUS vs 芬太尼由 0.833（<1）翻为 1.114（>1），"eleven of the twelve computable ratios were below 1"这一稳健性陈述也随之改变。
- 更根本的是，退一版/去重后的方向**与原文相反**（瑞芬太尼 HYPERAESTHESIA 从"低于芬太尼 30%"变成"与芬太尼持平"），这意味着原稿的头对头结论**部分由重复计数的差异驱动**。这是审稿人最难接受的一类发现。

**【具体修改建议】**
1. 补做：以 `safetyreportid` 为主键，仅保留每例的**最新版本**（而非 version 1），并对 `safetyreportversion` 字段缺失的 3 008 825 条记录单列一类；把"最新版本去重"的 Table 2/3/4 与现稿并列给出。
2. §4.5 的 `counts are inflated across every cohort, which would not generate the observed direction` 必须替换为可执行表述，例如：
   `openFDA indexes each case version separately: 4 938 726 records (23.9%) carry safetyreportversion 2 or higher, and the proportion differs by cohort (remifentanil 33.7%, fentanyl 27.7%, sufentanil 29.6%, morphine 39.6%). Version-deduplicated re-estimation changed the HYPERAESTHESIA head-to-head ratio from 0.696 (0.37-1.31) to 0.979 (0.48-1.99) against fentanyl and from 0.389 (0.21-0.73) to 0.550 (0.27-1.13) against morphine, so the direction of this specific comparison is not robust to de-duplication (Table 4D).`
3. Table 1 表头 `Total reports` 应改为 `Total case versions indexed`，并在脚注给出 version 分布。

---

### M3. 两项核心可行性声明（role 不可限定、个案层不可得）不成立

**【问题】** §2.2 与 §4.5 把 role-agnostic 队列与"无 TTO"归因于数据不可得。该归因经实测为假，因而这不是 limitation，而是未完成的分析。

**【证据】**
- `_exists_:patient.drug.drugcharacterization` = **20 692 690**（占全库 99.99999%）。分药取值可查：`R AND drugcharacterization:1`（suspect）→ 5 314；`:2`（concomitant）→ 3 570；`:3`（interacting）→ 225；`:4` → 1。
- openFDA `search` 端点**返回完整嵌套结构**：我以 `search=patient.drug.activesubstance.activesubstancename.exact:("REMIFENTANIL" "REMIFENTANIL HYDROCHLORIDE")&limit=1` 取到一条记录，`patient.drug` 有 7 个 entry，其中 `medicinalproduct=REMIFENTANIL HYDROCHLORIDE`、`drugcharacterization=2`、`openfda.route=["INTRAVENOUS"]`，且该记录 `safetyreportversion=3`。脚本同批读到的 `report_drug.txt`（加拿大侧）role 字段同样是逐药行的（示例行 `"PRIMROSE OIL"`、`"Concomitant"`），作者已在加拿大侧正确使用。
- 因此 role 限定只需**翻页**：`limit=1000`、`skip` 上限 25 000，按 `receivedate` 分年切块即可取全 5 375 条瑞芬太尼记录（约 6 次请求），芬太尼 121 819 条按年切块同样可取全。
- 仓库内 `ascii/2024Q4/` 目录存在但**为空**，说明作者尝试过 FDA 季度 ASCII 文件而失败，但未尝试这条路（也说明 `patient.drug.drugcharacterization` 并未被检索过）。
- 同时可得的还有：`patient.drug.drugindication`（18 542 325 条）、`patient.drug.openfda.route`（17 747 483 条）、`patient.drug.drugstartdate`（11 017 932 条；瑞芬太尼 2 426/5 375）。

**【为什么重要】** 稿件把"role-agnostic"写进了 Methods 与 Limitations 两处，并据此把加拿大的 suspect 限定当作"验证"；如果 role 本来可限定，则**主分析可以做得和加拿大一样干净**，而"加拿大更干净所以只做方向确认"的整个论证结构（§2.1、§4.5）失去依据。审稿人只要自己查一次 `patient.drug.drugcharacterization`，就会把这条 limitation 读成"作者没做"。

**【具体修改建议】**
1. 补做 case-level 抓取与 role 限定主分析：对四个药分别翻页取回全部记录，仅在**目标药自身的 drug entry** 上判定 `drugcharacterization == 1`（suspect），重建队列表与 Table 2；输出列 `cohort_role_restricted`、`a_role_restricted`、`ROR`、`RORR_vs_FENTANYL`。
2. 删除 §2.2 与 §4.5 的两处不可得声明，改为：
   `Role attribution requires the drug-level record, which the search API returns as a nested array and which we retrieved by paging the search endpoint (limit=1000, partitioned by receivedate); the primary analysis is therefore additionally reported with cohorts restricted to reports in which the target substance itself carried drugcharacterization = 1 (suspect).`

---

### M4. 信号判定与 Table 2 星号不自洽；四种测量实际只用了一种来判定；EBGM 未报告且不是 MGPS 估计

**【问题】** §2.4 声明三种规则之并，Table 2 脚注只写 ROR 一条，且星号集合与该脚注冲突；EBGM 声称计算却从不打印、也不进入判定。

**【证据】**（我用 `_faers_cache.json` 的 a/n/PT_total/N 逐格重算 18 × 4 = 72 个 2×2 表）
- Table 2 共 **26 个星号**；星号集合与 `01_faers_results.csv` 的 `*_signal` 列**完全一致（0 处不符）**，而该列等于三条规则的**并集**。
- 但其中 **2 个星号不满足脚注的唯一判据**：HYPERPATHIA/芬太尼（**a = 2**，ROR 8.237，CI 1.99–34.06）与 HYPERPATHIA/舒芬太尼（**a = 1**，ROR 75.634），二者只能由 PRR≥2 且 χ²>4 与 IC025>0 触发；脚注明写 `a ≥ 3 and the lower bound of the 95% CI of the OR > 1`，自相矛盾。
- 43 个可估计格中，各规则独立触发数：**ROR 24、PRR 18、IC025 26、并集 26、三者全中仅 16**。信号总数随测量在 18–26 间摆动（+44%）。
- 三规则互相分歧的**全部 10 行**（这是"结论依赖单一测量"最直接的暴露处）：

| PT | 药物 | a | ROR 下界 | PRR | χ² | IC025 | ROR 规则 | PRR 规则 | IC025 规则 |
|---|---|---:|---:|---:|---:|---:|---|---|---|
| DRUG INEFFECTIVE | FENTANYL | 8 062 | 1.03 | 1.05 | 22.25 | 0.043 | ✔ | ✘ | ✔ |
| DRUG INEFFECTIVE | MORPHINE | 4 450 | 1.24 | 1.26 | 229.26 | 0.283 | ✔ | ✘ | ✔ |
| NAUSEA | FENTANYL | 4 928 | 1.05 | 1.08 | 25.84 | 0.063 | ✔ | ✘ | ✔ |
| VOMITING | FENTANYL | 3 483 | 1.25 | 1.28 | 211.38 | 0.306 | ✔ | ✘ | ✔ |
| PRURITUS | MORPHINE | 1 291 | 1.21 | 1.27 | 72.76 | 0.263 | ✔ | ✘ | ✔ |
| CONSTIPATION | FENTANYL | 2 011 | 1.55 | 1.61 | 451.53 | 0.614 | ✔ | ✘ | ✔ |
| HYPERPATHIA | FENTANYL | 2 | 1.99 | 8.24 | 6.14 | 0.937 | ✘ | ✔ | ✔ |
| HYPERPATHIA | SUFENTANIL | 1 | 10.41 | 75.62 | 17.49 | 3.347 | ✘ | ✔ | ✔ |
| PROCEDURAL PAIN | REMIFENTANIL | 14 | 1.17 | 1.97 | 5.79 | 0.224 | ✔ | ✘ | ✔ |
| DRUG WITHDRAWAL SYNDROME | SUFENTANIL | 42 | 1.13 | 1.52 | 7.06 | 0.170 | ✔ | ✘ | ✔ |

- EBGM：`01_faers_results.csv` 的 `*_EBGM` 列存在，但**全稿没有任何表格或正文打印过 EBGM/EB05 值**，且 §2.4/Table 4A 的判定规则里没有 EBGM 项。并且该 EBGM **不是 MGPS 的 EBGM**：`_01_rerun.log:7` 记录 `EBGM 先验 Gamma alpha=0.540 beta=0.00001`，先验仅由 **top-500 个 PT** 的计数矩估计（`01_核心FAERS失衡分析.py:137-146`），得到退化先验（β = 1e-5 ⇒ 几乎无收缩），故 EBGM ≡ (a + 0.540)/E。我复核：HYPERAESTHESIA 瑞芬 (10+0.540)/(5 375×8 161/20 692 687) = 10.540/2.1197 = **4.972**，与 CSV 的 4.972 一致；ALLODYNIA 瑞芬 (1+0.540)/0.28833 = **5.34**，亦一致。

**【为什么重要】** 稿件摘要把"signal"定义压缩成"a lower confidence bound above one"，与 §2.4 的三规则并集不符，与 Table 2 脚注更不符；而 26 个星号里有 2 个按作者自己写的判据是不该有的。审稿人若抽出 Table 2 任一星号要求说明是哪条规则触发的，作者目前无法回答；若改用"三者交集"作为定义，需要印出来的信号会从 26 个降到 16 个，而 HYPERAESTHESIA 四个药恰好属于交集内 16 个之一（我逐一验证 ROR/PRR/IC025 三条对四药全部为真），所以收紧定义**对主结论无损、对可信度有极大增益**。

**【具体修改建议】**
1. Table 2 增加三列布尔值 `ROR rule / PRR rule / IC025 rule`（或至少在脚注列出 10 个分歧格），并把脚注改写为：
   `A cell is starred when at least one of three pre-stated rules is met: (i) a >= 3 and the lower 95% bound of the reporting odds ratio > 1; (ii) PRR >= 2 with chi-squared > 4; (iii) the lower 95% bound of the information component > 0. The three rules disagree in 10 of the 43 estimable cells (Table S7); two starred cells (HYPERPATHIA for fentanyl, a = 2, and for sufentanil, a = 1) meet only rules (ii) and (iii). Restricting the definition to the intersection of the three rules leaves 16 signals, including remifentanil's HYPERAESTHESIA.`
2. 删除 §2.4 中 `the empirical Bayes geometric mean under MGPS [22]` 的表述，改为 `an empirical-Bayes geometric mean whose Gamma prior was estimated from the 500 most frequently reported preferred terms (alpha = 0.540, beta = 1e-5), reported for completeness and not used in the signal definition`；或按完整 MGPS 重估先验并报告 EB05。
3. 摘要句 `Signals required at least three reports with a lower confidence bound above one` 需同步改为三规则并集，或改为交集。

---

### M5. "primary + confirmation"的两库框架方法学上不成立，应降格为两个单库分析的方向比较

**【问题】** 两库的 RORR 是**不同估计量**、分母是**不同对象**、病例可能**跨库重复**，且加拿大的"确认"依赖一个低于稿件自身阈值的单元格。

**【证据】**
- 估计量不同：加拿大 `cv/cv_process.py:221-226` 用同一 `c = len(global_pt[p])` 与 `d = N - c` 计算两侧 ROR，故 c、d 精确抵消，RORR 等价于 (a_r·b_c)/(b_r·a_c)（我复核 PAIN：(2×4528)/(109×353) = **0.2354** ✓ 与 `cv_pt_summary.csv` 的 0.235 一致）。FAERS 则不然：`c = PT_total - a`、`d = N - a - b - c` 在两臂间都不同——HYPERAESTHESIA 的 d_r = 20 679 161、d_f = 20 563 022（相差 **116 139**，占 N 的 0.56%），c_r = 8 151、c_f = 7 846。非抵消因子 (d_r·c_f)/(c_r·d_f) = **0.968**，即 FAERS 的 RORR 比真正的组内优势比低 3.2%（PAIN 为 0.993）。
- 因此 §2.4 的 `Both ratios share the same background reference, so comparator-specific terms cancel` 与 `they share the background reference d` **均为事实错误**：两臂的 d 不是同一个数。
- 分母不同类：FAERS 20 692 687 为案例版本（23.9% 为随访版本），加拿大 1 154 017 为源去重报告。
- 加拿大"确认"的强度：PAIN 的加拿大瑞芬太尼 **a = 2**（`cv_pt_summary.csv`），低于稿件自己要求的 a ≥ 3；DRUG INEFFECTIVE 的"reversal strengthened in a physician-only analysis (5.921 and 10.604)"在 `cv/cv_process.py:229-232` 中 `bn = len(target_reports["REMIFENTANIL"]) - an`，分母用的是**全队列**而非医师亚组，故它不是 physician-only 分析（我用 17.1%/12.1% 的医师占比复原：按代码得 5.877，按正确的医师-only 分母应为约 5.35；数值差异不大，但口径与标签不符）；且该处只印点估计、无 CI。
- 独立性：§4.5 用文献 [30] 的"约 85% PT 级信号重叠"讨论两库独立性，但那是**信号层面**的重叠，不是**病例层面**的重复。FAERS 与 Canada Vigilance 都由同一批上市许可持有人提交，可能描述同一患者。稿件未讨论跨库病例重复。

**【为什么重要】** "head-to-head + 跨库验证"是本文题目与卖点之一。若两库用的是不同估计量、不同分母对象、且病例可能重复，则"three findings were reproduced in the independent Canadian database"中的 independent 一词不可用，加拿大只能在"方向是否一致"这一最弱的意义上被引用——这恰好也是作者真正做的。降格表述不损失任何实测内容，却堵住了这个方法学攻击面。

**【具体修改建议】**
1. 两库统一为同一估计量并在 Methods 写明：
   `Head-to-head comparison uses the within-cohort reporting odds ratio RORR = (a_r * b_c) / (b_r * a_c), in which the reference cell cancels exactly; it is therefore invariant to the size and composition of the background corpus and to competition between terms. The value computed from the full 2x2 tables differs from this by at most 3.2% (Table S8) and the two are given for transparency.`
2. §2.1 与题目中的 framing 改为：
   `Two independent single-database analyses are reported; agreement is assessed as directional only, because the two systems differ in denominator definition, case de-duplication, role restriction and MedDRA release, and because the same cases may be submitted to both regulators.`
3. Table 3 新增 `Canada remifentanil a` 旁的脚注：`the Canadian PAIN comparison rests on two remifentanil reports, below the a >= 3 threshold used in the primary analysis, and is reported as directional only`；并补做/补印 physician-restricted RORR 及其 95% CI。

---

## 2. 重要问题

### P1-1. 四个"阴性对照"标签错误；PRURITUS 在鞘内/椎管内阿片中是典型效应，不宜作对照

**【问题】** §2.3 把 NAUSEA/VOMITING/PRURITUS/CONSTIPATION 定义为 `negative controls ... established, non-paradoxical opioid effects`。"已确立的阿片效应"与"阴性对照"在定义上互斥：阴性对照应为与该药无因果关联的术语。

**【证据】**
- 全部四个术语在对照药上 OR>1：芬太尼 PAIN 2.138、NAUSEA 1.079、VOMITING 1.289、CONSTIPATION 1.616（`01_faers_results.csv`）；吗啡 3.083/2.235/2.841/3.148。它们是**阳性对照（类效应）**，不是阴性对照。
- PRURITUS 是椎管内阿片的标志性效应，而舒芬太尼正是常规鞘内/硬膜外用药。全稿唯一 >1 的"阴性对照"比值正是 **PRURITUS vs 舒芬太尼 = 1.310 (0.84–2.04)**（Table S5），稿件把它写成"the exception ... whose interval includes one"（§3.4、Table S5 脚注）。把它并入"噪声/例外"处理，掩盖了一个由**给药途径**驱动、方向可预期的真实差异。
- 反向也成立：芬太尼 PRURITUS ROR = 0.503、舒芬太尼 0.320（均 <1），说明该术语在**全库参照**下也被稀释，与"阿片类必然高报瘙痒"的直觉相反——这本身是需要解释的 competition 现象，而稿件未讨论。

**【为什么重要】** 阴性对照的作用是"证明仪器在工作"。若把类效应术语当阴性对照，则在瑞芬太尼上观察到的 ROR<1 既可能是真低报、也可能是"该术语本来就不该有信号"；两种解释无法区分，§4.3 的整个推理（"if remifentanil under-reports the hyperalgesia terms and the controls alike, no hyperalgesia-specific inference can be drawn"）因此失去支点。

**【具体修改建议】** 把该组改名为 `specificity control terms (expected class effect)`，并在 Table 2 中增加一列 `expected direction`；把 PRURITUS 单列说明为 route-driven（`PRURITUS is the signature adverse effect of neuraxial opioids and sufentanil is used intrathecally; the ratio of 1.310 against sufentanil is therefore an expected route effect, not a negative-control failure`）；另增设一个真正的阴性对照（例如与阿片类无关、由其他药类主导的 PT），并在 Table 2 与 Table S5 中同列。

### P1-2. 适应症混杂被写成"无法调整"，但 openFDA 提供 `patient.drug.drugindication`，可量化且应量化

**【问题】** §4.5：`indication cannot be adjusted for, so §4.3 is an interpretation consistent with the subgroup data, not a mediation analysis`。该字段在 openFDA 上可得。

**【证据】** `_exists_:patient.drug.drugindication` = **18 542 325**。我按药取 top 适应症：
- 瑞芬太尼：`PRODUCT USED FOR UNKNOWN INDICATION` 1 001、`INDUCTION OF ANAESTHESIA` 704、`ANAESTHESIA` 643、`Maintenance of anaesthesia` 553、`GENERAL ANAESTHESIA` 528、`Sedation` 253、`ANTIBIOTIC PROPHYLAXIS` 201 —— **几乎全部是术中/麻醉场景**。
- 芬太尼：`PAIN` 36 336、`PLASMA CELL MYELOMA` 4 154、`BACK PAIN` 2 680、`BREAKTHROUGH PAIN` 2 033、`CANCER PAIN` 1 431、`Drug abuse` 1 459。
- 其中 `PLASMA CELL MYELOMA`（4 154 条，占芬太尼队列 3.4%）是一个方向明确的透皮癌痛/诉讼型簇，直接抬高对照臂的分母与 PAIN 事件数。

**【为什么重要】** PAIN 的 RORR = 0.066 是本文最稳、最被强调的定量结果（§3.4、§3.8、§4.1、§5）。它现在完全靠"报告构成"的口头解释支撑（§4.3、§4.4、§4.5 三段都在讲这件事），而**实测数据就在手边**。把一个可量化的混杂写成"cannot be adjusted for"，是审稿人最容易认定为"回避"的写法。

**【具体修改建议】** 补做一个 Table S9：`Indication (top 15) | REMIFENTANIL n (%) | FENTANYL n (%) | SUFENTANIL n (%) | MORPHINE n (%)`，并补做按适应症分层（至少 PAIN / 麻醉-操作 / 其他三类）的 PAIN RORR，输出列 `stratum | a_r | b_r | a_c | b_c | RORR (95% CI)`；把 §4.5 该句改为：
`Indication is measurable in this corpus (patient.drug.drugindication is populated for 18 542 325 records) and differs sharply between cohorts (remifentanil: anaesthesia and sedation; fentanyl: chronic and cancer pain); stratifying the PAIN comparison by indication stratum leaves the ratio below one in every stratum (Table S9).`

### P1-3. 无 TTO：真正的边界比稿件写的窄，且最有价值的替代分析并不需要 TTO

**【问题】** §4.5 把无 TTO 完全归于个案层不可得（见 M3），因而没有交代"即便拿到个案层，TTO 仍不可做"这一真实边界。同时，替代分析被压缩成了 route 分层一项。

**【证据】** openFDA 字段实测：`patient.reaction.reactiondate` 与 `patient.onsetdate` 均返回 **404（字段不存在）**；`patient.drug.drugstartdate` 存在（11 017 932 条；瑞芬太尼 **2 426/5 375 = 45.1%**）、`drugenddate` 5 659 451 条。加拿大抽取包 `reports.txt` 前 42 列我看到 col4/col5 两个日期（示例行均为 `05-JUN-73`），未见反应发生日期或用药起止日期。

**【为什么重要】** 结论层面：无 TTO 对本文结论的损害是**有限的但真实**。本文的核心是"术语选择决定答案"（§4.4）与"瑞芬太尼低报是报告构成所致"（§4.3），二者都不需要 TTO；但"是否真是 RIH"这一问题需要的时间维度确实缺失，且 §4.2 用"a real but modest phenomenon, coded rarely"把缺失时间维度的结果与前瞻研究对接，这一步在无 TTO 时是**未经验证的桥接**。恰因如此，必须把"能做什么"说清楚，而不是笼统归因于数据不可得。

**【具体修改建议】**
1. 把 limitation 改为准确边界：
   `openFDA exposes no reaction-onset or event date field (patient.reaction.reactiondate and patient.onsetdate are not part of the schema), so time-to-onset from drug start to event onset cannot be reconstructed even from case-level records; only drug start date (available for 2 426 of 5 375 remifentanil records, 45.1%) and the report received date are present.`
2. 在当前约束下应补做（按价值排序）：(i) 案例版本去重 + role 限定的主分析重算（见 M2/M3）；(ii) 按 `patient.drug.drugindication` 分层的 PAIN 与 HYPERAESTHESIA 分析（见 P1-2）；(iii) 以 `receivedate − drugstartdate` 定义的**报告滞后**分布（不是 TTO，须如此命名）用于检验 2024 簇是否为申报积压；(iv) 报告级"每报告 PT 数"标准化分析，用于排除瑞芬太尼报告系统性携带更多术语导致的稀释。第 (i)(ii) 两项的信息量远高于 TTO 本身。

### P1-4. §4.5 关于"去重不会产生观测方向"的断言无依据，且其前提不成立

**【问题】** `openFDA does not apply the FDA's case-level de-duplication, so counts are inflated across every cohort, which would not generate the observed direction [28, 29]`。前半句把"版本重复"（同病例多版本）与"去重"（mega-duplicate）混为一谈；后半句是无检验的断言。

**【证据】** 见 M2：随访版本占比在队列间为 27.7%–39.6%，**不是等比例**；按 version 1 重算后 HYPERAESTHESIA 的 RORR 由 0.696 变为 0.979，PRURITUS vs 芬太尼由 0.833 变为 1.114——**去重确实会改变观测方向**。

**【为什么重要】** 这句话被用来一次性化解稿件最明显的构造缺陷。由于它是错的，读者会连带质疑 §4.5 其他断言的可信度。

**【具体修改建议】** 按 M2 第 2 条的替换句改写，并补做去重敏感性表（Table 4D），给出全部 18 术语的 `RORR as published | RORR after version de-duplication (95% CI) | direction preserved?`。

### P1-5. 加拿大 PT 表的 2×2 记账不成立（a 被重复计入 c），虽数值影响极小

**【问题】** `cv/cv_process.py:202` 与 `:221` 用 `c = len(global_pt[p])`（含本药自己的 a）与 `d = N - c` 构造 2×2，于是 `a+b+c+d = N + a ≠ N`，与稿件 §2.4 宣称的 conventional 2×2 不符。

**【证据】** 以 PAIN 为例：a = 2、n = 111、c = 49 260、N = 1 154 017，代码得 0.4115，`cv_pt_summary.csv` 印 0.42；正确应为 `c' = 49 258, d' = N - n - c + a`，得 0.4115（差异 < 0.02%）。DRUG INEFFECTIVE 的偏差因子 c/(c−a) = 208 365/208 340 = 1.00012。**数值上可忽略**，但因为它同时解释了为什么加拿大的 RORR 恰好等价于组内优势比（c、d 抵消），这一点必须在 Methods 说清，否则读者会以为两库用了同一构造（见 M5）。

**【具体修改建议】** 修正 2×2 构造为 `d = N - a - b - c` 并重跑（预期无任何印刷值变化），同时在 Methods 明写：
`In both databases the reference cell is the whole-corpus remainder, so it contains the comparator cohorts; in the Canadian analysis the reference cell additionally cancels exactly from the head-to-head ratio, so Canadian ratios are within-cohort odds ratios, whereas the FAERS ratios retain a 0.7-3.2% non-cancellation (Table S8).`

### P1-6. §2.4 的方差/协方差论证方向对、表述错

**【问题】** `treating the two ratios as independent although they share the background reference d; with 20 692 687 background reports the ignored covariance is under 0.001% of the variance, so it is conservative`。

**【证据】** 数值本身正确：HYPERAESTHESIA 时 Var(log ROR_r) ≈ 0.10031、1/d_r = 4.84×10⁻⁸，比值为 4.7×10⁻⁷ = 0.000047%，确在 0.001% 以下。但"share the background reference d"不成立：d_r = 20 679 161、d_f = 20 563 022，两者相差 116 139。另外，RORR 真正被忽略的依赖不是共享 d（可忽略），而是**队列重叠**（M1），量级为万分之几〜数个百分点，与稿件的量级判断相反。

**【为什么重要】** 审稿人会把这句读作"作者用 0.001% 的小量级论证掩盖了真正的大依赖"，从而怀疑其自检的取向。

**【具体修改建议】** 删去"share the same background reference"，改为：
`Confidence intervals for the ratio of reporting odds ratios treat the two ratios as independent. The covariance induced by the common background corpus is negligible (1/d_r = 4.8e-8, i.e. 4.7e-7 of the variance here), but the two cohorts are not independent at the report level: 29.3% of remifentanil reports also name fentanyl, and the ratio is therefore additionally reported on a remifentanil set from which co-reported comparator reports have been removed (Table S6).`

---

## 3. 次要问题

### P2-1. Table 2 的 26 个星号中，有 8 个的 PRR 分支完全未触发，另有 2 个违反 a≥3；两处需在表内注明
**【问题】** 读者无法从印出的 ROR 与星号反推判定来源。
**【证据】** PRR 分支未触发（PRR<2）但带星号：DRUG INEFFECTIVE/芬太尼(PRR 1.054)、DRUG INEFFECTIVE/吗啡(1.255)、NAUSEA/芬太尼(1.076)、VOMITING/芬太尼(1.281)、PRURITUS/吗啡(1.269)、CONSTIPATION/芬太尼(1.605)、PROCEDURAL PAIN/瑞芬(1.975)、DRUG WITHDRAWAL SYNDROME/舒芬(1.525)。违反 a≥3：HYPERPATHIA/芬太尼(a=2)、HYPERPATHIA/舒芬(a=1)。
**【为什么重要】** 一旦审稿人发现脚注与星号不符，会怀疑全部 26 个星号的可复现性。
**【具体修改建议】** Table 2 加 `Rule(s) met` 列（取值 `ROR` / `PRR+IC` / `ROR+IC` 等），或按 M4 的脚注替换句整体改写。

### P2-2. Bonferroni 数字我已复现，建议在表内写清 family 与公式
**【问题】** `with a Bonferroni correction across all 72 drug-term comparisons the lower bound of the remifentanil HYPERAESTHESIA interval remains above one (1.61)` 未给公式。
**【证据】** 我用 z = Φ⁻¹(1 − 0.05/72/2) = 3.3918、se = sqrt(1/10 + 1/5365 + 1/8151 + 1/20679161) = 0.31672、ROR = 4.7288，得下界 **1.615 → 1.61 ✓ 完全复现**。此点经核查无问题。
**【为什么重要】** 这是稿件自检做得最扎实的一处，但读者无法验证；写明公式反而增强可信度。
**【具体修改建议】** 脚注补：`(Bonferroni: z = Phi^-1(1 - 0.05/(2 x 72)) = 3.392 applied to the log-scale standard error of 0.317)`。

### P2-3. 2018 年芬太尼报告数异常（30 290）未被察觉
**【问题】** 年份分层表中 2018 年的芬太尼队列突然变为 3 倍，作者未提及。
**【证据】** `receivedate` 口径芬太尼：2017 = 11 725、**2018 = 30 290**、2019 = 9 212、2020 = 11 635；`receiptdate` 口径同向（2018 = 29 857），故非查询口径问题。同年瑞芬太尼 506→481 平稳，全库 N 亦平稳（1 251 778→1 428 121→1 434 195）。该年正是 Table 4B 中芬太尼 PAIN OR 唯一 <1 的年份（0.716）。
**【为什么重要】** 一个 3 倍的年度跳变提示存在批量提交/数据重载，且恰好落在稿件用作"逐年稳健"证据的表格里。审稿人会问：如果 2018 的芬太尼是可以异常膨胀的，那么"所有年份方向一致"这个论证有多强？
**【具体修改建议】** 在 §3.8 或 Table 4B 脚注加：`The fentanyl cohort recorded 30 290 reports with a 2018 receipt date against 11 725 in 2017 and 9 212 in 2019 (same direction by receiptdate); this single-year inflation is unexplained and is the only year in which the fentanyl PAIN odds ratio fell below one.` 并补一段排查（是否为同一主报告者的批量提交）。

### P2-4. Table S4 加拿大列的口径应写明为"报告数"
**【问题】** `Canada_reaction_rows_whole_corpus` 按**反应行**计数（`10_term_dictionary.py:107` 逐行累加），而 `cv/cv_process.py` 的失衡分析按**去重报告**计数（`global_pt[p]` 为 REPORT_ID 集合）。
**【证据】** 对 PAIN，加拿大 49 260 同时出现在 Table S4 与 `cv_pt_summary.csv` 的 c 单元中（我用反解确认 c ≈ 49 260 才能得到印出的 0.42），说明该抽取包中同一 PT 每报告至多出现一次，两者恰好相等；但标签仍会把读者引向错误的量。
**【为什么重要】** 两库计数对象不同是本文最容易被误读的地方（FAERS 报告级 vs 加拿大报告级 vs FAERS SOC 事件级），标签失准会被放大。
**【具体修改建议】** 表头改为 `Canada reports with the term (whole corpus)`，并在脚注加：`In this extract each preferred term occurs at most once per report, so a reaction-row count and a report count coincide; the imbalance analysis uses report counts.`

### P2-5. HYPERPATHIA 仅 43 条全库计数，却贡献 2 个星号，应加稀有度警示
**【问题】** Table 2 把 HYPERPATHIA 与其它代理术语同列，其星号建立在 a = 1、a = 2 之上，且 RR 高达 75.63/113.71（EBGM）。
**【证据】** `10_term_dictionary.csv`：HYPERPATHIA 全库 43 条；`01_faers_results.csv` 中 HYPERPATHIA 的 EBGM 为 10.032（芬太尼，a=2）与 113.713（舒芬，a=1）——纯先验伪影（β=1e-5，见 M4）。
**【为什么重要】** EBGM 113.7 这种数值若被引用会被立即质疑；目前它虽未印出，但已存在于交付的 CSV 中。
**【具体修改建议】** 在 Table 2 与 Table S5 的 HYPERPATHIA 行加注 `whole-corpus count 43; both starred cells rest on a = 1 and a = 2 and are not interpretable`；或在主表中移除该术语、仅置于 Table S5。

### P2-6. Table S1 Panel B 的百分比口径会误导
**【问题】** FAERS Panel B 是事件级（PT 计数之和），分母却写成各药队列报告数（如 remifentanil 1 108/5 375 = 20.6%），于是"比例"可无上界。
**【证据】** `03_soc_27.csv` 头部已注明事件级；Panel B 中吗啡 General disorders 为 34 281，占其 56 501 报告的 60.7%，显然不是报告占比。
**【为什么重要】** 读者会把 20.6% 与加拿大 Panel A 的 8.1% 直接比较并得出"两库不一致"的错误结论。
**【具体修改建议】** Panel B 表头改为 `events (mapped preferred-term count, not reports)`，并注明 `the denominator is the cohort report count, so percentages may exceed 100% and are not comparable with Panel A`。

### P2-7. Summary/§5 的 "not reproduced" 与 §3.5 的措辞需要与加拿大样本量一致
**【问题】** 加拿大 HYPERAESTHESIA 瑞芬太尼 a = 0，稿件在两处写成 "did not reproduce"（Table 3 `Confirmed = no`），另处写 "Canada neither confirms nor refutes"（§3.3）。
**【证据】** `cv/cv_pt_summary.csv` HYPERAESTHESIA 行：0 / 18 / 0 / 30；加拿大瑞芬队列 111 例，按稿件自己的 a ≥ 3 规则不可能产生信号。
**【为什么重要】** "did not reproduce" 会被读成"证伪"，而 a = 0 在 111 例队列上是**不可检验**而非阴性。
**【具体修改建议】** Table 3 该行 `Confirmed` 列改为 `not testable (a = 0 of 111; no power for a term this rare)`；§3.5 的 `did not reproduce` 统一改为 `could not be tested`。

---

## 4. 我认为稿件站得住的地方

### 4.1 术语可检索性核验（Table S4 / `10_term_dictionary.py`）是真正的方法学贡献，且数字可复现
**【证据】** 我把 `10_term_dictionary.csv` 全部 18 行的 FAERS 列与 `_faers_cache.json` 逐条比对：**18/18 完全一致**（HYPERALGESIA 0、ALLODYNIA 1 110、PAIN 607 176、DRUG TOLERANCE 5 013、DRUG INEFFECTIVE 1 299 278、NAUSEA 778 546、VOMITING 462 663、PRURITUS 372 941、CONSTIPATION 213 536、HYPERAESTHESIA 8 161、HYPERPATHIA 43、PROCEDURAL PAIN 27 300、CHRONIC PAIN SYNDROME 1、DRUG WITHDRAWAL SYNDROME 87 541，五个不可检索串均为 0）。"先验证字符串是否为首选语，再解读零"这一顺序，在该领域绝大多数同类论文中确实缺失；把 LLT→PT 的映射错误（HYPERALGESIA 是 LLT，父 PT 为 HYPERAESTHESIA）做成可复现产物，是本稿最有价值的产出。
### 4.2 队列规模一致性与 2×2 完整性检验全部通过（但需说明它是恒等式）
**【证据】** 我按 `01_核心FAERS失衡分析.py:107-113` 的构造，对 **18 个 PT × 4 药 = 72 张表**逐张计算 a+b+c+d：**72/72 全部等于 20 692 687**（N = `patient.reaction.reactionmeddrapt:[* TO *]` = 20 692 687），无一例外。也需要指出：d 是由 `d := N - a - b - c` 反解得到，所以这条检验是**代数恒等式**，它验证的是四格记账没有溢出，而非分母选择是否正确。分母是"全库余数（含三个对照药）"这一点，我另行核验：HYPERAESTHESIA 的 d_r = 20 679 161 = 20 692 687 − 5 375 − 8 161 + 10，其中确实包含芬太尼的 315、舒芬太尼的 22、吗啡的 262 例该术语报告——这是标准的"单药对全库"口径，选择本身合理，但稿件未说明，且由此产生的 RORR 非抵消（M5）也未说明。
### 4.3 作者用自己的数据推翻了两个自身卖点，这是高水平的自检
**【证据】** §3.8 与 Table 4C：作者主动报告了八成的 HYPERAESTHESIA 报告集中在 2024、leave-2024-out 后 a = 1 且无信号、且 2024 年的抬升四药共有（year/pooled 比 15.41 / 4.30 / 4.90 / 1.71，`04_sensitivity_2024cluster_hyperaesthesia.csv`），并据此把结论定为"single-year cluster, not a stable finding"。同时 §3.9 主动做了"管线能检出信号"的后验抽查。这类**主动消解自己阳性结果**的操作在同类投稿中罕见，且 `04_sensitivity_estimable_years.json` 把"可估计年份数"机器化落盘，防止正文出现 "every year" 这类不可核对的表述。
### 4.4 RORR 对 competition/masking 偏倚的稳健性，经我验证确实成立
**【证据】** 我做一个直接的扰动实验：把术语全库计数 PT_total 人为放大 1.5 倍与 3 倍（模拟 DRUG INEFFECTIVE 这类高频术语造成的竞争性稀释），重算 RORR vs 芬太尼：PAIN 0.0665 → 0.0668 → 0.0671；DRUG INEFFECTIVE 0.5678 → 0.5690 → 0.5706；HYPERAESTHESIA 0.6960 → 0.7050 → 0.7140。**变动均 <3%。** 原因是 RORR 中 c 项在（近似）组内优势比中抵消。这意味着稿件的主要阴性结论（瑞芬太尼低报 PAIN 等）**不是**高频术语竞争造成的假象——这是选择 RORR 而非单药 ROR 作为主结局的正确回报，值得在 Discussion 里明确写出。
### 4.5 严重报告与途径分层的敏感性分析做得规范，且把自身缺陷量化留证
**【证据】** `04_sensitivity_run.log`：N_ser = 11 882 968，瑞芬太尼 serious = 5 270/5 375（98.0%），与正文完全一致；`04_sensitivity_ps_only.csv` 中 HYPERAESTHESIA 瑞芬 a = 10、ROR 4.309、signal = True 在严重报告子集内保持。途径分层虽然没有做成个案级，但 `02_route_stratified.csv` 用 `KnownRouteCoverage% = 184.3`（瑞芬太尼）把"route 是报告级属性、各 route 计数可超过队列规模"这一事实**直接印在结果文件里**，并在 IV 匹配分层下得到 RORR 0.077/0.038（与全库 0.066/0.046 同向），处理方式是诚实的。
### 4.6 统计自检里最容易出错的两处，作者做对了
**【证据】** (i) Bonferroni 下界我复现为 1.615，与印出的 1.61 一致；(ii) EBGM 先验虽然退化，但 `01_核心FAERS失衡分析.py` 的注释明确记录了"limit=1000 会 403、已改 500 使先验真正由语料估计"这一中间事故，说明作者对 API 行为做过实测并有留痕习惯。
---

## 5. 需要作者明确澄清的事实性问题

请逐条回答，不要以"已知局限"代替答案。

1. **20 692 687 是什么？** 仓库里的取数式是 `patient.reaction.reactionmeddrapt:[* TO *]`，返回的是 openFDA 的**案例版本**数；全库 4 938 726 条（23.9%）带 `safetyreportversion ≥ 2`。Table 1 的 `Total reports` 指的是报告还是案例版本？若指前者，去重后总数是多少？
2. **`patient.drug.drugcharacterization` 为何被判定为不可用？** 该字段在 20 692 690/20 692 687 条记录上存在，且 `search` 端点返回完整嵌套 `patient.drug` 数组（我取到的记录含 7 个 drug entry，瑞芬太尼为 `drugcharacterization=2`、`route=INTRAVENOUS`）。请说明 §2.2 结论所依据的具体 API 失败现象。
3. **是否尝试过翻页取个案记录？** openFDA `search` 支持 `limit=1000`，`skip` 上限 25 000，按 `receivedate` 分年切块可覆盖任意规模队列。仓库中 `ascii/2024Q4/` 为空，是否意味着只尝试了 FDA 季度 ASCII 这一条路？
4. **26 个星号各自的判定来源？** 请对 Table 2 逐格列出触发的规则；我算得的分布是 ROR 规则 24 格、PRR 规则 18 格、IC025 规则 26 格、三者交集 16 格，与脚注只写 ROR 一条不一致。
5. **Bonferroni 的 family 是什么，是否只用于瑞芬太尼 HYPERAESTHESIA 一格？** 若 72 格都要求同样校正，Table 2 中除该格外还有哪些格子能存活？
6. **加拿大 PAIN 的"确认"建立在 a = 2 上，是否与稿件自身 a ≥ 3 的信号规则冲突？** 若冲突，请说明为何仍可作为 confirmation。
7. **2018 年芬太尼 30 290 条是否排查过？** 该年芬太尼报告数为 2017 年的 2.6 倍、2019 年的 3.3 倍（receiptdate 口径一致），且是 Table 4B 中芬太尼 PAIN OR 唯一低于 1 的年份。
8. **加拿大抽取包是否存在用药起止日期或反应发生日期？** `reports.txt` 我只见 col4/col5 两个日期字段（示例行两值相同）；`report_drug.txt` 前 21 列在我抽样行中为空。若存在可用的 onset/起始日期，则 TTO 在**验证库**中是可做的，Limitations 的表述需相应修改。
9. **`DRUG TOLERANCE`、`DRUG WITHDRAWAL SYNDROME` 是否真属于"hyperalgesia-related"？** 二者已列为宽定义组，但 §4.3 把瑞芬太尼的低报部分归因于药代动力学（半衰期短、无口服/透皮剂型），而不是归因于报告行为；这与"宽定义组用于检验术语选择假设"的定位是否需要区分？

---

## 6. 我实际做的独立核查

**读过的文件**：`_review_r5/_PANEL_BRIEF.md`；`I_正文_IMRaD_en.md`（全文）；`ANALYSIS_PLAN.md`；`01_faers_results.csv`（全 18 行）；`01_faers_summary.md`；`01_核心FAERS失衡分析.py`；`04_sensitivity.py`；`04_sensitivity_ps_only.csv`；`04_sensitivity_year_pain.csv`；`04_sensitivity_year_hyperaesthesia.csv`；`04_sensitivity_leave2024_hyperaesthesia.csv`；`04_sensitivity_2024cluster_hyperaesthesia.csv`；`04_sensitivity_estimable_years.json`；`04_sensitivity_run.log`；`02_route_stratified.csv`；`03_soc_27.csv`；`10_term_dictionary.csv`；`10_term_dictionary.py`；`cv/cv_process.py`；`cv/cv_pt_summary.csv`；`cv/cv_drug_totals.csv`；`cv/cv_summary.md`；`cv/cv_soc_27.csv`；`cv/cv_subgroups.csv`；`_faers_cache.json`（612 条缓存）；`_01_rerun.log`；`_fda_auth.py`。未读取任何 `REVIEW_*/RESPONSE_*/REVISION_*`、`01_任务状态.md`、`00_项目总览*`、`SUBMISSION_MANIFEST.md`、`GITHUB_DEPOSIT_SOP.md`、`author_verification_statement.md`，也未读取 `_review_r5/` 下其他审稿人的输出。

**（1）2×2 表完整性与分母口径**
- 以 `_faers_cache.json` 的 `patient.reaction.reactionmeddrapt:[* TO *]` = **20 692 687** 为 N，按 `01_核心FAERS失衡分析.py:107-113` 的构造对 18 PT × 4 药逐张计算 a+b+c+d。
- **结果：72/72 张表全部等于 20 692 687，无一例外。** 该检验因此通过；但 d 是 `d := N - a - b - c` 的反解，故它是恒等式，不构成对分母选择的验证。
- 分母身份：HYPERAESTHESIA 的 d_r = 20 679 161 = 20 692 687 − 5 375 − 8 161 + 10，**内含**芬太尼 315、舒芬太尼 22、吗啡 262 例该术语报告 → 作者用的是"全库余数（含三个对照药在内）"，不是"四药合并"，也不是"排除四药后的其余"。四药队列朴素加和仅占 N 的 0.92%（190 208/20 692 687），故对单药 ROR 影响可忽略；对 RORR 的影响是非抵消因子 0.968–0.993（见 M5）。

**（2）队列重叠（openFDA 实时查询）**
- `R AND F` = 1 575；`R AND S` = 483；`R AND M` = 323；`F AND S` = 299；`F AND M` = 6 185；`S AND M` = 596。
- `(R OR F OR S OR M)` = **180 982**，对四者加和 190 208 的重复计入率 = **5.1%**。
- 逐术语的重叠：HYPERAESTHESIA a_R = 10 而 `R AND F AND PT` = **6**（60%）；PAIN 23 → 9（对 F）、8（对 M）；PROCEDURAL PAIN 14 → 7；DRUG INEFFECTIVE 208 → 53；DRUG WITHDRAWAL SYNDROME 7 → 1；ALLODYNIA 1 → 0；HYPERPATHIA、DRUG TOLERANCE、CHRONIC PAIN SYNDROME 为 0。
- 剔除共同报告后的重算（本人计算，非稿件数字）：HYPERAESTHESIA ROR 4.729→**2.672 (1.00–7.12)**、RORR vs F 0.696→**0.393 (0.15–1.06)**；PROCEDURAL PAIN RORR vs F 1.962→**1.386 (0.65–2.96)**；PAIN 0.066→0.057；DRUG INEFFECTIVE 0.568→0.600；DRUG WITHDRAWAL 0.046→0.055。

**（3）案例版本（去重）敏感性（openFDA 实时查询 + 本人计算）**
- `_exists_:safetyreportversion` = 17 683 862；`safetyreportversion:1` = 12 745 136；`: [2 TO *]` = 4 938 726。
- 随访版本占比：瑞芬 33.7%、芬太尼 27.7%、舒芬 29.6%、吗啡 39.6%。
- version-1 队列：3 563 / 88 109 / 4 588 / 34 140（N = 12 745 136）；术语计数见 M2 表。重算结果：HYPERAESTHESIA RORR vs F **0.696→0.979 (0.48–1.99)**、vs M **0.389→0.550 (0.27–1.13)**、瑞芬自身 ROR 4.729→7.076；PRURITUS vs F 0.833→**1.114**；PROCEDURAL PAIN vs F 1.962→3.549；PAIN 0.066→0.056；DRUG INEFFECTIVE 0.568→0.592。

**（4）四测量一致性与星号复原**
- 我用 cache 中的 a/n/PT_total/N 独立重算 ROR（含 Woolf CI）、PRR、χ²、IC 与 IC025，与 `01_faers_results.csv` 逐格比对：**ROR 全部一致**，signal 布尔值与三条规则的并集**完全一致（0 处不符）**。
- 从 `I_正文_IMRaD_en.md` 解析 Table 2 的星号（共 **26** 个），与 CSV 的 `*_signal` 列比对：**0 处不符**。但与脚注（纯 ROR 规则）比对：**2 处不符**（HYPERPATHIA/芬太尼 a=2、HYPERPATHIA/舒芬太尼 a=1）。
- 各规则触发计数（43 个可估计格）：ROR 24、PRR 18、IC025 26、并集 26、交集 16；三规则互相分歧 **10 行**（清单见 M4）。
- EBGM 复核：以 `_01_rerun.log:7` 的 α = 0.540、β = 1e-5 复算 HYPERAESTHESIA 瑞芬 = 4.972、ALLODYNIA 瑞芬 = 5.34，与 CSV 一致，确认 EBGM ≡ (a+0.540)/E（无实质收缩）。

**（5）openFDA 字段可得性（用于 M3 / P1-2 / P1-3）**
- `_exists_:patient.drug.drugcharacterization` = 20 692 690；分取值 REMI：1→5 314、2→3 570、3→225、4→1。
- `search=R&limit=1` 返回完整个案：`patient.drug` 含 7 个 entry，其中一个为 `REMIFENTANIL HYDROCHLORIDE / drugcharacterization=2 / openfda.route=["INTRAVENOUS"]`，`safetyreportversion=3`。
- `_exists_:patient.drug.drugindication` = 18 542 325；`patient.drug.openfda.route` = 17 747 483；`patient.drug.drugstartdate` = 11 017 932（瑞芬太尼 2 426/5 375）；`drugenddate` = 5 659 451。
- **不存在**：`patient.reaction.reactiondate`、`patient.onsetdate`（均 404）。
- 适应症 top 分布：瑞芬太尼为麻醉/镇静/操作相关；芬太尼为 `PAIN` 36 336、`PLASMA CELL MYELOMA` 4 154、`BACK PAIN` 2 680、`BREAKTHROUGH PAIN` 2 033、`CANCER PAIN` 1 431。

**（6）年份分母与 2018 异常**
- 逐年的 `receivedate` 全库计数与芬太尼计数：2015 = 1 187 780 / 10 017；2017 = 1 251 778 / 11 725；**2018 = 1 428 121 / 30 290**；2019 = 1 434 195 / 9 212；2020 = 1 455 117 / 11 635；2024 = 1 319 106 / 2 412。`receiptdate` 口径同向（2018 = 29 857），排除查询口径问题。

**（7）加拿大侧**
- `cv/cv_process.py:202` 与 `:221` 的 2×2 构造缺陷（c 含自身 a、d = N − c，故四格和 = N + a）；反解确认 PAIN 的 c ≈ 49 260 才得到印出的 0.42，证实该缺陷数值影响 <0.02%。
- `cv/cv_process.py:229-232` 的"physician-only"用全队列分母（bn = 111 − an）；按 17.1%/12.1% 医师占比复原，得 5.877（与印出的 5.921 同量级），正确医师-only 口径应为约 5.35。
- 加拿大 PAIN 的瑞芬太尼 a = 2（`cv/cv_pt_summary.csv`），低于稿件 a ≥ 3 阈值。
- 加拿大 RORR 的抵消性质经实例验证：PAIN (2×4528)/(109×353) = 0.2354，与印出的 0.235 一致。

**（8）我复核为"无问题"的项（明确列出，避免误伤）**
- Bonferroni 下界 1.615 → 1.61 **正确**（z = 3.3918）。
- 严重报告子集 N_ser = 11 882 968、瑞芬太尼 5 270/5 375 = 98.0% **正确**。
- Table 4B 的"8 of 10 estimable years"**正确**（2018、2019 瑞芬太尼 PAIN a = 0）。
- Table 4C 的"9 rows / 8 in 2024 / 1 in 2021"**正确**。
- 留一 2024 后 a = 1、ROR 0.70 (0.10–4.98)、RORR vs F 0.106、vs M 0.058 与 `04_sensitivity_leave2024_hyperaesthesia.csv` **一致**。
- 2024 簇四药 year/pooled 比 15.41/4.30/4.90/1.71 与 `04_sensitivity_2024cluster_hyperaesthesia.csv` **一致**。
- Table S4 的 18 个 FAERS 计数与 `_faers_cache.json` **18/18 一致**。
- 四药队列规模 5 375 / 121 819 / 6 513 / 56 501 与缓存 **一致**；加拿大 111 / 4 881 / 63 / 7 675 与 `cv_drug_totals.csv` **一致**。
- 2×2 四格和 = N 的检验 **72/72 通过**（性质见上）。

---

## 7. 方法学必改清单（按优先级排序，共 7 条）

| # | 条目 | 类型 | 对应问题 |
|---|---|---|---|
| 1 | **去版本重复 + role 限定的主分析重算**：按 `safetyreportid` 保留每例最新版本；翻页取个案记录，仅在目标药自身 drug entry 上要求 `drugcharacterization = 1`；重出 Table 1/2/3/4 与全部 RORR，并与现稿并列。 | **必须补做** | M2, M3, P1-4 |
| 2 | **两库统一 RORR 估计量并量化队列重叠**：改用 (a_r·b_c)/(b_r·a_c)；新增 Table S6 给出 18 个术语的"剔除共同报告"RORR；在 Methods 明写 29.3% 的瑞芬-芬太尼共用率，并删除 Abstract 的 "weakest of the four"。 | **必须补做** | M1, M5, P1-6 |
| 3 | **适应症表 + 分层分析**：用 `patient.drug.drugindication`（18 542 325 条可用）出 Table S9，并补做按适应症分层的 PAIN / HYPERAESTHESIA RORR；替掉"indication cannot be adjusted for"。 | **必须补做** | P1-2 |
| 4 | **修正 signal 定义与 Table 2 脚注**：脚注写全三条规则；印出（或至少在补充材料列出）10 个分歧格与 2 个违反 a≥3 的星号；删除对 MGPS EBGM 的表述或按完整 MGPS 重估先验并报 EB05；摘要定义同步。 | **必须补做** | M4, P2-1, P2-5 |
| 5 | **撤回两处不可得声明**：删除"case-level file ... inaccessible""FDA case-level files could not be retrieved""role-restricted analysis was not possible"，替换为准确边界（`patient.reaction.reactiondate`/`patient.onsetdate` 确不存在，故 TTO 不可做；但 role 可限定、个案可翻页获取）。 | **可只改措辞**（但第 1 条的补做必须同时做） | M3, P1-3 |
| 6 | **重构标签与框架**：四个"negative controls"改名为 specificity control terms 并单列 PRURITUS 的途径机制；"primary + confirmation"降格为"two independent single-database analyses compared for direction"，Table 3 的 "Confirmed = no" 改为 "not testable"。 | **可只改措辞** | P1-1, M5, P2-7 |
| 7 | **清理表述与记账**：修正 §2.4 的 "share the same background reference" 与非抵消因子（0.7%–3.2%）；修正加拿大 2×2 记账（c 含自身 a）与 "physician-only" 分母并补 CI；补 2018 年芬太尼 30 290 条的排查说明；Table S4 加拿大列表头改为报告数；Table S1 Panel B 表头标注事件级。 | **可只改措辞**（记账修正需重跑，预期无印刷值变化） | P1-5, P2-3, P2-4, P2-6 |

**若第 1、2 条补做后 HYPERAESTHESIA 的 RORR 仍跨 1（按我现有计算，去重后为 0.979，剔除共同报告后为 0.393 但 CI 上界 1.06），稿件可以接受；但"remifentanil 是四者中最弱"这一结论必须删除，题目中的 "head-to-head" 须改为非重叠队列口径或直接去掉。**
