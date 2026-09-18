# Round-5 独立审稿 — A5_epi_causal 药物流行病学与因果推断专家

## 0. 审稿人身份与总体结论

本人从事药物流行病学与自发报告数据方法学工作，长期研究的正是本次稿件所处的三个交叉地带：自发报告中的混杂结构、negative control 设计的合法性边界，以及"报告行为"与"真实风险"在失衡分析里的可分离性。

**Verdict: Major Revision**

理由（具体到本稿）：

1. 稿件反复承认适应证混杂（§2.3、§4.3、§4.5），却从未量化；而**量化它所需的数据就在作者自己的数据目录里**——加拿大抽取包内有 `report_drug_indication.txt`（330 万行，含可归因到**具体药品记录**的英文适应证）。我据此补做了稿件声称"无法做"的分析，结果显示：瑞芬太尼队列的适应证是 111/111 围术期麻醉类，而芬太尼/吗啡由慢性痛、类风湿、心绞痛、偏头痛等构成；把适应证固定到"围术期麻醉"层后，PAIN 的 RORR 从 0.235 升到 0.399（0.048–3.295，区间跨 1），而在"疼痛适应证"层 PAIN 的 RORR 反转为 1.791。§5 关于 PAIN 低报"large, stable and reproduced in Canada"的表述因此站不住。
2. 稿件把 NAUSEA/VOMITING/PRURITUS/CONSTIPATION 定义为 negative controls，但这四个术语都是**阿片类已知的因果效应**，合格 negative control outcome 的必要条件是与暴露无因果关联，因此该设计在概念上不成立；而作者自己的结果（PRURITUS 在多处 >1、DRUG INEFFECTIVE 在加拿大与在 FAERS 的部分层 >1、免疫 SOC 极度富集）恰好证明这些术语方向并不一致，也就无法承担"全局低报"的推论。
3. 我独立算出一个稿件完全没有考虑的结构性混杂：**每份报告的反应术语条数**在四个队列间差 2.3–3.8 倍（瑞芬 1.694 / 芬太尼 3.899 / 舒芬 4.111 / 吗啡 6.502）。因为作者的 RORR 在代数上等于"队列内事件优势比"（c、d 相消），它**天然**被报告深度压低。按报告深度做 Mantel–Haenszel 分层后，PAIN vs 吗啡从 0.146 变为 0.978（0.04–22.8），vs 芬太尼从 0.235 变为 0.640（0.03–14.9）。也就是说，"低报"与"报告深度更低"在本设计下不可分辨，而稿件把前者当成了关于药物的陈述。
4. 两处可核实的算术/事实错误（§3.8 与其自家 Table 4A 冲突；§5 与 `cv/cv_pt_summary.csv` 冲突），一处估计量错误（所谓 "physician-only analysis" 实为分子限定医师、分母用全队列的混合量）。
5. 站得住的地方也真实存在：术语可检索性核验（Table S4）是货真价实的方法学贡献，我逐条复核全部 18 个术语的两个库计数均与 `10_term_dictionary.csv` 一致；leave-2024-out 与 2024 年簇诊断（Table 4C）是同类文献中罕见的诚实做法，我复核其数值全部正确。因此**不是 Reject**，而是 Major Revision：结论的因果层级必须整体下调，且必须补上作者手上数据本就支持的定量分析。

---

## 1. 重大问题（Major, M1…）

### M1. 适应证混杂被反复承认却从未量化，而数据就在作者手上；补做后结论方向不稳

**【问题】** 稿件把"适应证/报告场景混杂"当作既定解释（§4.3 "Cohort composition explains the pattern"、§4.5 "indication cannot be adjusted for"），但从头到尾没有给出任何一个经过适应证控制或分层后的估计；而加拿大抽取包里含可归因到具体药品记录的适应证字段，该断言与作者自己持有的数据不符。

**【证据】**
- 稿件原文：§4.5 "**Setting and residual confounding.** The comparators are used in different care settings ... **indication cannot be adjusted for**, so §4.3 is an interpretation consistent with the subgroup data, not a mediation analysis."
- 反证：`cv/cvponline_extract_20241130/report_drug_indication.txt`（330 万行，`$` 分隔）列为 `col1=REPORT_ID, col2=DRUG_PRODUCT_ID, col3=brand, col4=indication(EN), col5=indication(FR)`。我验证了 col2 确为产品号：`drug_products.txt` 中 `8248=REMICADE`、`6353=APO-PAROXETINE`、`4743=BETASERON`，与该文件 col3 品牌名逐行一致。因此适应证可精确归因到"哪条药品记录"，而不只是报告级。
- 我据此把适应证归因到各队列的靶药嫌疑记录（REMI 111 份报告中 98 份有适应证；FEN 3,878/4,881；MOR 5,028/7,675），得到（报告数）：
  - **REMIFENTANIL**：`Induction of anaesthesia` **111**、`Anaesthesia` 94、`General anaesthesia` 54、`Maintenance of anaesthesia` 41、`Anaesthetic premedication` 37、`Sedative therapy` 24、`Sedation` 9、`Surgery` 6、`Pain` 6。
  - **FENTANYL**：`Product used for unknown indication` 12,098、`Pain` 1,265、`Complex regional pain syndrome` 741、`Rheumatoid arthritis` 534、`Neuralgia` 393、`Drug abuse` 378、`Ankylosing spondylitis` 313、`Chronic spontaneous urticaria` 181。
  - **MORPHINE**：`Product used for unknown indication` 48,061、`Rheumatoid arthritis` 8,466、`Hypertension` 5,841、`Coronary artery disease` 5,811、`Angina pectoris` 5,396、`Chest pain` 4,710、`Pain` 4,601、`Fibromyalgia` 2,531、`Migraine` 2,510。
- 我做的分层头对头（我算出，作者未做；RORR 定义与作者一致 = 队列内事件优势比）：
  - **限定到围术期/麻醉适应证**（REMI n=84、FEN n=239、SUF 22、MOR 43）：PAIN 瑞芬 vs 芬太尼 **0.399（0.048–3.295）**（未分层 0.235）、vs 吗啡 **0.161（0.016–1.593）**（未分层 0.146）→ 方向保留但幅度衰减约 1.7 倍，**区间已跨 1**。
  - **限定到疼痛适应证**（REMI n=4、FEN n=631、MOR n=824）：PAIN **1.791（0.184–17.397）** vs 芬太尼、**1.416（0.146–13.706）** vs 吗啡 → **方向反转**。
  - FAERS 侧（我用 openFDA `search=` 分层查询，接口可用）：PAIN vs 芬太尼 合并 0.066，18–64 岁 **0.098**、≥65 岁 **0.028**、女 **0.072**、男 **0.036** → 幅度随年龄层变动 3.5 倍。

**【为什么重要】** 这是本稿第二大结论（"瑞芬太尼报告的疼痛最少"）的成立条件。初读时我会接受"0.066"作为一个稳定的头对头比值；但当我知道瑞芬太尼队列 100% 是围术期麻醉适应证、而对照由慢性痛/癌痛/消费者报告构成、且把适应证固定后比值升到 0.399 甚至反转为 1.79 时，0.066 就只能读作"两种用药场景的构成比之差"。若作者不补这一分析，任何审稿人只要打开抽取包就会发现 `report_drug_indication.txt` 的存在，稿件的"无法校正适应证"就变成事实性错误，而由此支撑的 §3.6、§4.1、§5 会一起失效。

**【具体修改建议】**
补一张 **Table 5（新增）**，标题与列定义照抄即可用：

> **Table 5. Canada Vigilance: indication- and composition-stratified head-to-head ratios.**
> Columns: `Stratum | Definition (recorded indication / demographic) | Remifentanil n | Remifentanil a | Fentanyl n | Fentanyl a | Morphine n | Morphine a | RORR vs fentanyl (95% CI) | RORR vs morphine (95% CI)`
> Rows: (1) all suspect reports; (2) any perioperative–anaesthesia indication (MedDRA-like terms: induction/general/maintenance of anaesthesia, anaesthetic premedication, sedative therapy, sedation, surgery, preoperative care); (3) any pain indication; (4) age 18–64 y; (5) age ≥65 y; (6) reporter = physician; (7) reporter = other health professional; (8) serious only; (9) non-serious only.
> Terms tabulated: PAIN, HYPERAESTHESIA, DRUG INEFFECTIVE, NAUSEA, VOMITING, PRURITUS, CONSTIPATION.
> Footnote to state: the indication field is attributed to the suspect drug record (`report_drug_indication` joined on report id + drug product id); reports with no recorded indication (13/111 remifentanil, 1,003/4,881 fentanyl) form their own stratum.

并把 §4.5 该句改为可粘贴的英文：

> "Recorded indications were available for the suspect drug record in the Canadian extract and were used to define a common-support stratum; an indication-matched analysis is reported in Table 5. An indication-matched analysis was not possible in FAERS, where the drug and indication arrays cannot be coupled at the drug-record level, so the FAERS ratios remain susceptible to confounding by indication in the direction of the comparator's indication load."

### M2. 四个 "negative controls" 在概念上不成立；而作者对它们的解释与对 DRUG TOLERANCE/WITHDRAWAL 的解释自相矛盾

**【问题】** 稿件把 NAUSEA/VOMITING/PRURITUS/CONSTIPATION 定义为 negative controls，即"与暴露无因果关联"的结局；但这四个都是阿片类受体介导的**已确立因果效应**，因此它们低报既可能来自报告行为，也可能来自真实的药理学差异，设计上无法区分。更严重的是，作者同时对 DRUG TOLERANCE/DRUG WITHDRAWAL SYNDROME 使用药理学解释、对阴性对照使用报告行为解释，这两套解释逻辑不能在同一份稿件里并存。

**【证据】**
- 稿件 §2.3：`"NAUSEA, VOMITING, PRURITUS and CONSTIPATION served as negative controls, defined a priori as established, non-paradoxical opioid effects unrelated to hyperalgesia"` —— 注意定义是"与痛觉过敏无关"，而不是"与暴露无因果关联"。negative control outcome 的标准要求是后者（Lipsitch 等的负对照定义），"与目标结局无关"是另一种东西（充其量是 control outcome for the hypothesis）。
- 自相矛盾的两段：§4.3 `"Cohort composition explains the pattern"`（阴性对照低报 = 报告行为）与同一段 `"For DRUG TOLERANCE and DRUG WITHDRAWAL SYNDROME part of the low reporting is probably physiological: remifentanil's ultrashort half-life and lack of oral or transdermal formulation make true tolerance and withdrawal clinically uncommon."`（同为低报 = 药理学）。生理学论证若对后两者成立，对恶心/呕吐/瘙痒/便秘同样成立（后四者恰恰被阿片类的受体作用与用药时长决定），作者的论证可以双向使用，因此不构成证据。
- 数据反证"方向一致"：我把四个对照的全部可算比值逐一核过。FAERS 主分析 12 个可算比值中 11 个 <1、1 个 >1（PRURITUS vs 舒芬 1.310）；但在**严重报告子集**（`04_sensitivity_ps_only.csv`）中 PRURITUS vs 芬太尼 **1.087**、vs 舒芬 **1.218** 均 >1，12 个中 2 个 >1；在加拿大，唯一可算的阴性对照比值 VOMITING vs 芬太尼为 **1.066**（>1）。若这些是真正的"无效应"对照，不应系统性出现反向。
- 我另外算出：四个队列的**每报告反应术语条数**差异巨大（见 M3），这本就使"所有术语一律 <1"成为机制性预期，而不是关于药理学的证据。

**【为什么重要】** 关键词 "negative controls" 一旦被审稿人认定为不合法，§4.3 的"analgesic superiority cannot be inferred"与 §5 的"the four negative controls are stable within FAERS"就都失去了设计依据。更关键的是，稿件用"全局低报"来**排除**痛觉过敏特异性信号，又用 DRUG INEFFECTIVE 反转来**证明**不是全局伪影——这两处互相拆台（见 M4）。此外，作者未识别 M3 的报告深度混杂，恰恰是阴性对照"全低报"的正确解释；把阴性对照当作药理学对照反而掩盖了真正需要控制的变量。

**【具体修改建议】**
1. 术语层面：把 "negative controls" 全文替换为 `"control outcomes (established opioid effects unrelated to the target concept)"`，并在 §2.3 明确写出"these outcomes are causally related to opioid exposure and therefore cannot establish absence of a reporting artefact; they serve only to characterise the drug-wide reporting profile."
2. 真正可用的负对照是**负对照暴露**而不是负对照结局：加入一个**同场景、非阿片**的暴露（如丙泊酚、罗库溴铵或昂丹司琼）——若"低报"源于围术期报告者/报告深度，则该药对同一批术语也应出现类似比值。可粘贴句：
> "To separate a drug-specific deficit from a setting-specific one, we added a negative-control exposure: propofol, a non-opioid drug used by the same perioperative reporters. Because the control outcomes above are causally related to opioid exposure, only a negative-control exposure can test whether the deficit is drug-specific or setting-specific (Table S6)."
3. 删除 §4.3 中把 DRUG TOLERANCE/WITHDRAWAL 归因于药理学的那一句，或与阴性对照统一处理（二者只能择一）。替换句：
> "The low reporting of DRUG TOLERANCE and DRUG WITHDRAWAL SYNDROME shares the same ambiguity as the control outcomes: it may reflect the ultrashort half-life and the absence of oral or transdermal formulations, or the reporting depth of perioperative reports, and these data cannot separate the two."

### M3. 报告深度（每报告反应术语条数）是本设计下的结构性混杂，未控制即无法把"该术语低报"与"整体低报"分开

**【问题】** 作者的 RORR 在代数上等于"队列内事件优势比"，与背景库计数无关，因此每份报告平均记录多少条反应术语会**等比**压低所有术语的比值。四个队列的每报告反应条数差 2.3–3.8 倍，而这个变量从未被报告、分层或校正。这使 §3.4、§4.1、§5 的"低报"陈述与"报告深度更低"在观测上等价。

**【证据】**
- 代数事实：RORR = [(a_r/c)/(b_r/d)] ÷ [(a_c/c)/(b_c/d)] = (a_r·b_c)/(b_r·a_c)，c 与 d 精确相消。我用稿件数值反算验证：PAIN 瑞芬 a=23/n=5,375，芬太尼 a=7,349/n=121,819 → (23/5,352)/(7,349/114,470) = 0.0669，与 `01_faers_results.csv` 的 0.066 一致。**RORR 并不使用背景库**，它不是"失衡"对比，而是"队列内事件构成"对比。
- 我独立统计加拿大各队列的报告深度（`reactions.txt` 逐行按报告计数；4,474,923 行中归属靶药队列者）：
  - REMIFENTANIL：111 份报告 / 188 条反应 = **1.694 条/报告**，单条反应报告占 **69.4%**；
  - FENTANYL：4,881 / 19,029 = **3.899**，单条占 39.9%；
  - SUFENTANIL：63 / 259 = **4.111**；
  - MORPHINE：7,675 / 49,905 = **6.502**，单条占 27.1%。
- 按深度层（1 / 2 / 3–4 / ≥5 条反应）做 Mantel–Haenszel 分层后的 RORR（我算，作者未算，且作者未报任何深度统计）：
  - PAIN vs 芬太尼：**MH 0.640（0.027–14.898）**，而作者未分层值 0.235；
  - PAIN vs 吗啡：**MH 0.978（0.042–22.751）**，而作者未分层值 0.146 —— **几乎归零**；
  - DRUG INEFFECTIVE vs 芬太尼：MH 1.663（0.218–12.718），未分层 1.277；
  - DRUG INEFFECTIVE vs 吗啡：MH 2.409（0.315–18.403），未分层 1.703；
  - VOMITING vs 芬太尼：MH 3.765（0.237–59.828），未分层 1.066。
  - 另一条等价路径（用"该术语占本队列全部反应条数的比例"）：PAIN 瑞芬 1.064% vs 芬太尼 1.855% → 比值 **0.573**（未分层 0.235）；vs 吗啡 1.721% → **0.618**（未分层 0.146）；DRUG INEFFECTIVE 13.298% vs 4.756% → **2.796**（未分层 1.277）。
- 上表中每个深度层的瑞芬太尼 PAIN 事件数只有 0 或 1，故 MH 区间极宽（0.03–14.9）：**这不是"校正后证明没有低报"，而是"未校正的 0.235 根本无法作为药物特异性低报的估计"**。

**【为什么重要】** 这是本稿最深的流行病学设计缺陷：作者想用"阴性对照也低报"来说明"低报是全局的、因此痛觉相关术语的低报不可解释为特异性"，但如果全局低报本身是报告深度造成的，那么**同一机制也按比例压低了 HYPERAESTHESIA、ALLODYNIA 等目标术语**，于是"目标术语未见特异信号"这个结论同样不可靠。审稿人一旦指出这一点，§4.1、§4.4、§5 关于"它是四个中最弱"的判断就需要在深度校正后重做。

**【具体修改建议】** 补一张 **Table 6**，并把结论句改为深度感知的表述：

> **Table 6. Report depth and depth-adjusted head-to-head ratios (Canada Vigilance).**
> Columns: `Preferred term | Reaction terms per report (remifentanil / fentanyl / sufentanil / morphine) | Reports with a single reaction term (%) | Crude RORR vs fentanyl | MH-adjusted RORR vs fentanyl (95% CI) | Share-of-reaction-terms ratio vs fentanyl | Same four columns vs morphine`
> Strata for the MH estimator: 1, 2, 3–4, ≥5 reaction terms per report; state that strata with an empty cell contribute to the point estimate but not to the variance.

> "Because the ratio of reporting odds ratios is algebraically the ratio of the within-cohort event odds, it is depressed in proportion to the number of reaction terms recorded per report, which differed 2.3-fold (fentanyl) to 3.8-fold (morphine) between cohorts. After Mantel–Haenszel adjustment for the number of recorded reaction terms the PAIN ratio moved from 0.235 to 0.640 versus fentanyl and from 0.146 to 0.978 versus morphine, and the VOMITING ratio moved from 1.066 to 3.765 versus fentanyl; the direction of the crude deficit is therefore not identifiable from these data."

### M4. specificity probe 无法排除全局伪影：在数据库内它并不与其它术语反向，而反转只出现在 111 份报告的加拿大库

**【问题】** 稿件用 DRUG INEFFECTIVE 在加拿大反转来论证"不是统一的全局报告伪影"（§3.4、Table 3 脚注），但**在作为主分析的 FAERS 中，该术语的表现与其它术语完全一致（0.568、0.470，均 <1）**，因此它并未在能够判定的数据库里完成判别功能；反向只出现在 111 份报告、CI 极宽的加拿大库，且该库的 DRUG INEFFECTIVE 基线流行率是 FAERS 的约 2.8 倍，属典型的两库编码/上报习惯差异。

**【证据】**
- `01_faers_results.csv` 第 6 行：DRUG INEFFECTIVE 瑞芬 a=208、ROR 0.601、RORR vs 芬太尼 **0.568（0.49–0.65）**、vs 吗啡 **0.470**、vs 舒芬 **0.784** —— 三向全部 <1，与 PAIN、四个对照、HYPEREASTHESIA 同向。因此"a global artefact would have pushed this term in the same direction as everything else; it did not"（§3.4）在 FAERS 中不成立。
- 我统计了 FAERS 主分析中全部可算 RORR 的方向：**29 个可算比值中 26 个 <1，仅 3 个 >1**（PROCEDURAL PAIN vs 芬/舒、PRURITUS vs 舒芬）。DRUG INEFFECTIVE 是那 26 个之一。
- 我用 openFDA 分层查询（接口实测可用）发现 DRUG INEFFECTIVE vs 舒芬太尼在 FAERS 内部也反转：18–64 岁 **1.079**、≥65 岁 **1.058**、男性 **1.783**，而合并值为 0.784。所以"探针是否反转"取决于分层，不是"数据库特异性 vs 全局伪影"的可判定证据。
- 基线流行率（我算）：加拿大 DRUG INEFFECTIVE 报告 205,227 / 1,154,017 = **17.8%**；FAERS 1,299,278 / 20,692,687 = **6.3%**，相差 2.8 倍。两库对同一术语的编码倾向本就不同。
- 稿件 §4.3 自己也承认：`"consistent with term-specific reporting but also compatible with database differences, so it narrows rather than settles the interpretation."` 这与 §3.4、Table 3 脚注的断言（"argues against a uniform global reporting artefact"）互相冲突。

**【为什么重要】** specificity probe 是作者用来回应"你的阴性结果只是工具不灵"这一必然质疑的唯一装置。若探针在主分析库里不判别、在弱库里反向、且方向随分层翻转，那么"特异"与"全局"的二分就没有被检验，§3.4 的结论句必须收回。作者问"反向是否真能排除全局报告伪影"——我的判断是：**不能**。它兼容至少三种解释：(i) 加拿大对"疗效不足"的上报口径不同（可核：该库 DRUG INEFFECTIVE 占全部报告 17.8%，FAERS 6.3%）；(ii) 两库报告者与适应证构成不同（加拿大瑞芬队列 64.9% 为非医师卫生专业人员，吗啡 23.6% 为消费者）；(iii) 围术期报告者对"疗效不足"的记录习惯与慢性痛/消费者报告者不同（这正是作者自己的"who reports"假说，与"非全局伪影"直接冲突）。

**【具体修改建议】**
删除 §3.4 末句与 Table 3 脚注中的反证断言，改为：

> "In the primary database the specificity probe behaved like every other term (0.568 versus fentanyl; 0.470 versus morphine), so it does not discriminate a term-specific deficit from a drug-wide one. Its reversal was confined to the smaller Canadian database, whose prevalence of DRUG INEFFECTIVE among all reports is 17.8% against 6.3% in FAERS, and it reverses again within FAERS when the cohort is restricted to adults aged 18–64 years (1.079 versus sufentanil). The probe therefore narrows nothing: the two databases differ in coding and reporter mix, and the probe cannot separate those differences from a drug-specific effect."

### M5. 四队列并非互斥暴露组：瑞芬太尼队列有 37.7% 与对照重叠；且 RORR 不是失衡量

**【问题】** 稿件把设计写成"四药头对头"（§1、§2.4、Table 1），但 `patient.drug` 是数组、分队列是 role-agnostic 的（§2.2 自述），因此同一份报告可同时进入多个队列；叠加 M3 的代数事实，"RORR"其实是"队列内事件构成之比"。二者合并后，"头对头"的可解释性所剩不多。

**【证据】** 我用 openFDA 同字段 AND 查询（实测可用）算出 FAERS 重叠矩阵：
- 单药：瑞芬 5,375 / 芬太尼 121,819 / 舒芬 6,513 / 吗啡 56,501（与稿件 Table 1 完全一致）；
- 两两：瑞芬∩芬太尼 **1,575**、瑞芬∩舒芬 483、瑞芬∩吗啡 323、芬∩吗 6,185、芬∩舒 299、舒∩吗 596；
- 三重：瑞芬∩芬∩舒 30、瑞芬∩芬∩吗 136、瑞芬∩舒∩吗 18、芬∩舒∩吗 55；四重 **4**。
- 容斥计算：瑞芬太尼队列中至少有 1,575+483+323−2×(30+136+18)+3×4 = **2,025 份报告（37.7%）同时含至少一个对照药**；仅与芬太尼重叠即占瑞芬队列的 **29.3%**。
- 加拿大侧同样不互斥：四队列规模之和 111+4,881+63+7,675 = 12,730，而并集仅 **12,171**（我在重建队列时实测），即 559 份报告（占并集 4.4%）属于 ≥2 个队列。
- 代数事实见 M3：RORR = (a_r·b_c)/(b_r·a_c)，与背景计数无关。

**【为什么重要】** 若说"瑞芬太尼 vs 芬太尼"，读者会默认两个互斥暴露组；实际有近 30% 的瑞芬太尼报告同时是芬太尼报告（同一例围术期联用），这些报告同时进入分子与分母臂，使比值被拉向 1，并让对比变成"两种上报构成之差"而非"两药之差"。对一篇自称 head-to-head 的稿件，这是设计层缺陷；对仅宣称"terminology caution"的稿件可以接受，但必须明写并做敏感性分析，否则 §3.3–§3.5 的全部对比性表述都过度承诺。

**【具体修改建议】**
1. 新增 **Table S7**：4×4 重叠矩阵（对角线为队列规模，非对角为交集计数），并给出"含 ≥1 对照药的瑞芬报告占比"。
2. 定义互斥队列并重跑关键行，作为敏感性分析：`exclusive cohort = 报告仅含四种阿片之一`。列：`Cohort definition | Remifentanil n | Fentanyl n | PAIN RORR vs fentanyl (95% CI) | DRUG INEFFECTIVE RORR vs fentanyl (95% CI)`。
3. 措辞改为：
> "Cohorts were not mutually exclusive: 1,575 of 5,375 remifentanil reports (29.3%) also named fentanyl and 2,025 (37.7%) named at least one comparator, so the comparison is between overlapping reporting profiles rather than between disjoint exposure groups. A mutually exclusive-cohort sensitivity analysis is given in Table S7. Because the ratio of reporting odds ratios is algebraically a ratio of within-cohort event odds, it measures the composition of each cohort's reported events, not the strength of a disproportionality signal."

### M6. "independent confirmation" 的框架不成立；Table 3 的"Confirmed"列有 10 行中 8 行是同义反复

**【问题】** 稿件标题式地把加拿大库称为 "the independent Canadian database"（§3.5）并设 "Cross-database confirmation"，但作者自己在 §4.5 已承认两库同属北美、共享 MedDRA、药市场重叠，且所引文献恰说明跨库重叠高达 ~85%。同时 Table 3 的 "Confirmed" 列把"某字符串不是首选语"与"某发现被复现"混为一谈。

**【证据】**
- §3.5 原文：`"Three findings were reproduced in the independent Canadian database (Table 3)"`，而 §4.5 原文：`"FAERS and Canada Vigilance are both North American systems sharing MedDRA coding and much the same drug market, so agreement here is weaker than across regulatory regions, where about 85% of signals overlap at the preferred-term level [30]"`。同一稿件内 `independent` 与 `sharing ... much the same drug market` 不能并存。
- 我在 `cv/cv_pt_summary.csv` 上逐术语核对可算性（见 §6）：18 个术语中**只有 3 个**在加拿大能算出 vs 芬太尼的 RORR——PAIN（0.235）、DRUG INEFFECTIVE（1.277）、VOMITING（1.066）。也就是说，**没有任何一个 a priori 痛觉过敏术语（窄定义或宽定义）、也没有 HYPERAESTHESIA 能在加拿大算出头对头比值**。加拿大对主结局的贡献为零。
- Table 3 共 14 行，其中 "yes" 10 行。10 行中 HYPERALGESIA、PAIN INCREASED、POSTOPERATIVE PAIN、CHRONIC PAIN、OPIOID WITHDRAWAL SYNDROME、DRUG TOLERANCE、HYPERPATHIA、CHRONIC PAIN SYNDROME 共 **8 行标为 "yes (zero in both)"** —— 这些字符串不是首选语（Table S4 已自证），"两个库里都是 0"是词典属性，在任何数据库、任何药物上都成立，不构成复现。ALLODYNIA 的 "yes" 是"两库都无信号"（加拿大 0 例 vs 芬太尼 3 例），亦非复现。**真正被复现的只有 1 行：PAIN 的方向（0.235 / 0.146）**，且该行没有 CI——我算出的区间是 **0.235（0.058–0.957）**，上界距 1 仅 4.5%。
- 独立验证的条件：(i) 来源人群不重叠；(ii) 病例确认相互独立；(iii) 编码体系或验证机制不共享；(iv) 报告者群体不重叠。FAERS 与 Canada Vigilance 在 (iii)(iv) 上部分共享；更关键的是**跨国上市许可持有人依法需向多个监管机构递交同一病例**，同一份病例可同时出现在两库，作者无法排除。稿件自己也说未使用欧洲或日本库（§4.5）。

**【为什么重要】** "independent confirmation" 是稿件可信度叙事的支柱之一；一旦被认定为非独立，读者会重新审视为何只有一个方向被"复现"，以及为什么"复现"是 2 例事件。审稿人会直接质疑：把一个 2 事件、区间上界 0.957 的方向一致，称为 "confirmed in the non-independent database"，是在给最弱的证据贴最强的标签。

**【具体修改建议】**
1. 全文替换：`"the independent Canadian database"` → `"the Canadian database (a second, methodologically cleaner but non-independent North American system)"`；§3.5 标题 `Cross-database confirmation` → `Cross-database comparison`。可粘贴句：
> "Canada Vigilance is not an independent replication set: it shares MedDRA coding, a largely overlapping drug market and, for multinational marketing-authorisation holders, potentially the same individual cases with FAERS. A European or Japanese database would provide genuinely independent replication and neither was available; the Canadian analysis should therefore be read as a check on the direction of the sign in a differently ascertained cohort, not as independent confirmation."
2. Table 3 删除 "Confirmed" 列中 8 行 "yes (zero in both)"，改为 "not applicable — the string is not a preferred term (Table S4)"；并把标题改为 `Cross-database comparison of terms that are estimable in both corpora`，只保留 3–4 行真正可算的术语。
3. 所有加拿大 RORR 补 95% CI（作者已在 §2.4 声明用 Woolf 近似，故无技术障碍）。

---

## 2. 重要问题（P1-1…）

### P1-1. 所谓 "physician-only analysis"（5.921 / 10.604）不是医师限定分析，而是分子限定医师、分母用全队列的混合估计量；且未给 CI

**【问题】** 稿件在 §3.4 用 `"the reversal strengthened in a physician-only analysis (5.921 and 10.604)"` 支撑探针论证，但该数值实际是"医师层的事件数 ÷ 全队列的非事件数"，分子与分母处于不同分层，不对应任何可解释的流行病学量。

**【证据】** 我从 `cv/cv_process.py:229-232` 复现其定义：`an=len(target_pt_phys["REMIFENTANIL"][p]); bn=len(target_reports["REMIFENTANIL"])-an` —— 队列规模取**全队列** 111 而非医师层 19。代入我独立统计的计数（医师层：瑞芬 DRUG INEFFECTIVE 16/19；芬太尼 135/589；吗啡 120/535）：
- 作者值 = (16/(111−16)) ÷ (135/(4881−135)) = 0.168421/0.028445 = **5.921** ✓（与稿件一致），vs 吗啡 = 0.168421/(120/7555) = **10.604** ✓。
- 真正医师限定 = (16/(19−16)) ÷ (135/(589−135)) = 5.3333/0.297357 = **17.936（5.149–62.478）** vs 芬太尼；vs 吗啡 = 5.3333/(120/415) = **18.444（5.286–64.362）**。
两值相差约 3 倍，且真正医师限定的 CI 极宽（跨 5–62），根本不能支持 "strengthened"。

**【为什么重要】** 这是本稿唯一一处声称"反向加强"的定量支撑，也是 Table 3 中 DRUG INEFFECTIVE 反转证据的一部分。用一个不可识别的混合量、且不给 CI，去支撑一个被反复使用的判别性论断，属于方法学错误而非笔误；读者若自行复算会发现数值无法还原。

**【具体修改建议】** 若保留该分析，改为正确估计量并给 CI，措辞降级：

> "Among physician-reported cases only (remifentanil 19 reports, fentanyl 589, morphine 535), the DRUG INEFFECTIVE ratio was 17.94 (95% CI 5.15–62.48) versus fentanyl and 18.44 (5.29–64.36) versus morphine; with 16 of 19 remifentanil physician reports carrying the term, this subgroup estimate is too imprecise to support an inference and is reported for completeness only (Table S8)."

（若只需一句，也可选择删除该句及 `cv_pt_summary.csv` 中 `REMI_RORR_FEN_phys`/`REMI_RORR_MOR_phys` 两列的对应结论。）

### P1-2. §3.8 与 §4.1 的 "all negative controls stayed below 1" 与作者自己的 Table 4A 冲突

**【问题】** 稿件两处声称严重报告子集中所有阴性对照比值均 <1，但 Table 4A 自身印出的 PRURITUS vs 芬太尼即 >1。

**【证据】** `04_sensitivity_ps_only.csv` 中阴性对照（严重报告子集）：NAUSEA 0.249 / 0.114、VOMITING 0.403 / 0.181、**PRURITUS 1.087（0.78–1.51）/ 0.324**、CONSTIPATION 0.112 / 0.058；未印出的 PRURITUS vs 舒芬亦为 **1.218**。因此 8 个可算比值中 2 个 >1。稿件 §3.8 原文 `"and all negative controls stayed below 1"`、§4.1 原文 `"all four negative controls against both comparators, stably across serious-report restriction"` —— 与 Table 4A 第 324 行（稿内表格行）自相矛盾。注意主分析（Table 2）中该陈述成立（11/12 与 8/8 均 <1），错误只出现在严重报告子集。

**【为什么重要】** 这是可被门禁或复算直接捕获的错误；更重要的是它把"经过严重度限制后结果稳定"这一敏感性的结论夸大。审稿人看到 Table 4A 自己打自己，会质疑其余敏感性叙述是否也经过校对。

**【具体修改建议】** 改为：

> "Restricting to serious reports left the PAIN findings unchanged (0.072 versus fentanyl and 0.044 versus morphine) and left three of the four control outcomes below one against both comparators; the exception was PRURITUS, whose ratio versus fentanyl rose to 1.087 (0.78–1.51) and versus sufentanil to 1.218, with intervals that include one."

### P1-3. §5 "the four negative controls ... could not be tested in Canada" 与 `cv/cv_pt_summary.csv` 冲突

**【问题】** 结论声称四个阴性对照在加拿大无法检验，但其中 VOMITING 在加拿大正是可算的，且其 vs 芬太尼 比值 >1。

**【证据】** `cv/cv_pt_summary.csv` 第 12 行：`VOMITING, negctrl, 3, 124, 1, 508, 0.806, 1.066, 0.392` —— 即瑞芬 3/111、芬太尼 124/4,881 → RORR **1.066**（我算 CI 0.334–3.403）；vs 吗啡 **0.392**。我重建队列亦得同值。稿件 §5 原文 `"the four negative controls are stable within FAERS but could not be tested in Canada, whose cohorts were too small."`；§4.5 的较弱表述 `"its negative-control cohorts were too small for most ratios to be computed"` 可以接受，§5 的绝对表述不可接受。此外，"stable within FAERS" 已被 P1-2 否定。

**【为什么重要】** 这是结论段的绝对化表述被自家结果文件推翻。更实质的是：加拿大唯一可算的阴性对照比值恰好 >1（对芬太尼），而稿件把它当作不存在——这既掩盖了对"全局低报"叙事不利的一条数据，也说明作者未系统核查加拿大侧的可算性。

**【具体修改建议】** 改为：

> "The control outcomes were largely untestable in Canada (only VOMITING could be computed: 1.066 versus fentanyl, 0.392 versus morphine), so that part of the pattern rests on FAERS alone; within FAERS it was stable for three of the four control outcomes but not for PRURITUS, whose ratio versus fentanyl exceeded one in the serious-report subset."

### P1-4. 途径限制的论证是循环的：用被污染的"IV 层"来证明途径错配无关

**【问题】** §4.5 用"限制到静脉层后比值几乎不变"来论证途径错配"对称稀释"故无害；但作者自己在 `02_route_summary.md` 中已证明该"IV 层"由报告内其它药物的途径污染而成（瑞芬 route 覆盖率 184%、口服 21.1%），因此这个"IV 层"不是静脉层，用它证明途径错配无害是循环论证。

**【证据】** 稿件 §4.5：`"remifentanil, which has no oral or transdermal formulation, received oral-route assignment in 21.1% of its reports. Restricting the PAIN comparison to the intravenous stratum left the ratio unchanged (0.077 versus fentanyl, 0.038 versus morphine), so the defect dilutes both arms symmetrically."`；作者文件 `02_route_summary.md:18-24`：`"openFDA 的 patient.drug 为数组，其 search 为 report-level（cross-field）而非 drug-record 级（nested）"`、`"各药 route 覆盖率 >100%（REMI 184%）"`、`"本分析的'route 分布'实为报告内伴随药物的途径谱"`。若层级确实错配，则该分层不含途径信息；用不含途径信息的分层证明途径不影响结论，逻辑上无内容。

**【为什么重要】** "对称稀释"是一个关于偏倚方向的实质断言，不是可以顺带给出的；错配在两个臂上的方式不同（对照药有真实口服/透皮剂型，瑞芬没有），因此谈不上对称。审稿人会把这条与 §2.2 的 role-agnostic 问题合并，视作对 FAERS 侧"无法做药物记录级归因"的一次不诚实处理。

**【具体修改建议】** 二选一：(a) 删除该句与 Table（仅保留"FAERS 途径无法归因"的局限陈述）；或 (b) 改为明确的不确定性表述：

> "Route could not be attributed to a drug record in openFDA, so the intravenous-stratum analysis in the Supporting Information is a report-level approximation in which route is carried by co-reported drugs; it cannot demonstrate that route misclassification is symmetric and is therefore reported only to document the defect, not to exclude it. Attributing route would require the FAERS case-level DRUG table, which was not retrievable in this environment (the quarterly ASCII download returned empty)."

### P1-5. 加拿大侧全部 RORR 未给置信区间，而唯一实质性"复现"的区间上界仅 0.957

**【问题】** §2.4 声明头对头比值按 Woolf 近似给 95% CI，但 Table 3 与 §3.5 的加拿大数值只有点估计；补上区间后，"复现"的证据强度应被重新描述。

**【证据】** 我算（Woolf，log 尺度，Σ1/单元格）：加拿大 PAIN vs 芬太尼 **0.235（0.058–0.957）**、vs 吗啡 **0.146（0.036–0.591）**；DRUG INEFFECTIVE vs 芬太尼 1.277（0.813–2.005）、vs 吗啡 1.703（1.086–2.671）；VOMITING vs 芬太尼 1.066（0.334–3.403）。稿件 §3.5 原文仅 `"(0.066 and 0.046 in FAERS against 0.235 and 0.146 in Canada)"`。PAIN 的加拿大区间上界 0.957 距 1 仅 0.043，且全部由 a=2 支撑；而 44.1% 的瑞芬队列年龄缺失、13/111 无登记适应证。

**【为什么重要】** "复现"的力度取决于区间而非点估计。把 a=2、区间勉强排除 1 的结果与 FAERS 的 a=23 并列，会让读者高估跨库一致性。作者既已声明 CI 方法，缺 CI 属不一致执行。

**【具体修改建议】** Table 3 与 §3.5 全部补 CI，并加一句：

> "The Canadian PAIN ratio rests on two remifentanil reports (0.235, 95% CI 0.058–0.957 versus fentanyl), so the interval excludes one only marginally and the agreement in direction is weaker than the point estimates suggest."

### P1-6. §3.9 的"管线有效性"事后核查不能证明方法灵敏，其数值本身更像本设计引入的伪影

**【问题】** 作者用免疫 SOC 的强信号作 post hoc sanity check（"supporting — not proving — that the absent hyperalgesia signal reflects the data, not the method"），但该"阳性"极可能恰恰是 role-agnostic 队列 + 事件级 top-500 PT 计数带来的伪影，因而不能承担该功能。

**【证据】** 稿件 §3.9：`"Remifentanil showed a strong immune-class signal (10.951; 8.613 versus fentanyl), driven by anaphylactic shock (532 events) and reaction (367)"`。而 Table S1 panel B 中舒芬太尼免疫类为 **1,828（占其队列 28.1%）**、瑞芬 1,108（20.6%）——一只用于麻醉、安全性记录良好的短效阿片，其免疫类事件占报告池 20–28%，在临床上不可信。`D_27SOC_openFDA事件级.md:88` 自述 `"瑞芬的速发型超敏（anaphylaxis 类）占其报告池的 899/5,375 ≈ 16.7%，远高于芬太尼的 1,390/121,819 ≈ 1.1%"`。围术期过敏性休克的标准归因对象是肌松剂/抗生素/乳胶，而该设计把报告内任一药都计入队列（§2.2 role-agnostic），因此共享病例会自动把事件赋予同报告的所有阿片。panel B 又是事件级近似（§2.5、Table S1 脚注）。因此这是"方法产生的阳性"，不是"方法检出真阳性"。

**【为什么重要】** 这一核查是作者回应"阴性结果=工具不灵"的主要防线。若该阳性本身被认定为设计伪影，则防线失效，读者会更倾向于认为全篇的阴性/低报不能与工具灵敏度分离——而这正是 M3 指出的同一问题。

**【具体修改建议】** 删除 §3.9 的"支持方法可靠"式表述，改为：

> "A post hoc class analysis returned an immune-system signal that is implausible as a drug-specific effect (20.6% of remifentanil's cohort in FAERS, 28.1% of sufentanil's), and it is best explained by the role-agnostic cohort definition and event-level counting rather than by pharmacology. It therefore demonstrates that the pipeline returns positives, not that it returns valid ones, and it cannot be used to argue that the absent hyperalgesia signal reflects the data rather than the method."

---

## 3. 次要问题（P2-1…）

### P2-1. §2.4 关于"共享背景参考 d 的协方差可忽略"的说明在本设计下是空的

**【问题】** 论述暗示 RORR 与背景库共享 d 因而存在被忽略的协方差，但 RORR 代数上不含 c、d。

**【证据】** RORR = (a_r·b_c)/(b_r·a_c)（我用稿件数值复算 PAIN 得 0.0669 ≈ 0.066，见 M3）。因此"with 20 692 687 background reports the ignored covariance is under 0.001% of the variance, so it is conservative"所述问题不存在。

**【为什么重要】** 该句会让读者以为 RORR 是经背景校正的量，从而把"队列内事件构成之比"误读为失衡强度。这是本稿全部头对头结论的解释基础。

**【具体修改建议】** 替换为：

> "Because both ratios share the same control cells, the ratio of reporting odds ratios reduces exactly to (a_r·b_c)/(b_r·a_c) — a ratio of the within-cohort event odds. The background database does not enter it; the measure compares the composition of reported events between cohorts, and is not a background-adjusted disproportionality statistic."

### P2-2. Table 3 的 "Confirmed" 列把"不是首选语"与"发现被复现"混同

（证据与改法见 M6 第 2 条。）

### P2-3. 摘要中"in each of the eight estimable years"的归属含混

**【问题】** 摘要句把阴性对照、严重报告限制与"八个可估年份"并列，读者会理解为阴性对照也做了年份分层。

**【证据】** 摘要：`"The same direction held for every negative control, on serious-report restriction, and in each of the eight estimable years."` 但 `04_sensitivity_estimable_years.json` 显示只有 PAIN 有 8 个可估年份、HYPERAESTHESIA 仅 2 个；阴性对照从未按年份分层。且"on serious-report restriction"在 PRURITUS 上为假（P1-2）。

**【为什么重要】** 摘要会被单独阅读与引用，此处把 PAIN 的年份稳健性扩张到阴性对照，属可被源头文件直接否证的过度概括。

**【具体修改建议】** 改为：

> "For pain, the same direction held for every computable head-to-head ratio, on restriction to serious reports, and in each of the eight calendar years in which an estimate was possible; three of the four control outcomes behaved the same way, but the fourth (pruritus) did not."

### P2-4. 分组标签在两个库之间不一致：DRUG INEFFECTIVE 在加拿大被归入 OIH 宽定义组

**【问题】** 探针在加拿大实现中被写入 `OIH_broad` 分组，而非 `probe`，与 `ANALYSIS_PLAN.md` 及 Table 2 的分组不一致。

**【证据】** `cv/cv_pt_summary.csv` 第 6 行 `DRUG INEFFECTIVE,OIH_broad,...`；`cv/cv_process.py:48` `"DRUG INEFFECTIVE":"OIH_broad"`；而 `01_faers_results.csv` 第 6 行为 `DRUG INEFFECTIVE,OIH-wide,...` 但 Table 2 标为 `probe`，`ANALYSIS_PLAN.md` 亦列为 `Specificity probe`。即同一术语在三个地方三种归类。

**【为什么重要】** specificity probe 的成立前提是"该术语与痛觉过敏无关"；在加拿大侧把它并入 OIH 宽定义组，会使"加拿大复现"的分组边界失去一致性，也让"探针未复现"的说法变得难以核对。审稿人对分组标签的一致性很敏感，因为它直接关系到多重比较与 a priori 声明的可信度。

**【具体修改建议】** 统一为 `probe`，并在 `cv_pt_summary.csv` 与生成脚本中同步修正；在 Table S5 脚注中说明该术语在所有分析中均按 probe 处理。

### P2-5. "HYPERALGESIA 不是首选语"的论证是经验性的；建议补一次词典层面的直接引证

**【问题】** 稿件以"两库检索均为 0 + 相邻词检索为 0"证明该字符串不是首选语，但"某 PT 在全库无报告"与"该字符串不是 PT"在逻辑上不可区分；结论虽被 MedDRA 层级编码（10020568）支持，但缺一次可核查的词典层面引证。

**【证据】** `_probe_meddra_level.json` 显示 `HYPERALGESIA: 0`、`HYPERESTHESIA: 0`（美式拼写为 0，而英式 `HYPERAESTHESIA: 8161`），与 MedDRA 使用英式拼写的惯例一致，间接支持作者结论；Table S4 亦给出 LLT→PT 的映射与编码。**此点经核查方向正确、无需推翻**，仅为补强建议。

**【为什么重要】** 本稿的核心卖点正是"临床用词不是编码用词"，若该论断仅建立在计数为 0 之上，会被更严格的审稿人要求出示 MedDRA 词典条目或 MSSO 检索记录。补引证成本极低，收益是该结论不可反驳。

**【具体修改建议】** 在 §2.3 Term-level verification 中加一句，并保留 Table S4：

> "The level of the string was confirmed against the MedDRA hierarchy rather than inferred from a zero count: HYPERALGESIA is a lowest level term whose parent preferred term is HYPERAESTHESIA (MedDRA code 10020568). A zero returned by a corpus query alone would not distinguish 'not a preferred term' from 'never reported', which is why the level was checked directly."

---

## 4. 我认为稿件站得住的地方

**S1. 术语可检索性核验（§2.3 + Table S4）是真实且执行正确的方法学贡献。** 我没有读到任何一篇同类失衡分析做过"在解释任何零之前，先在两库逐术语验证字符串是否为首选语"。我逐条复核 `10_term_dictionary.csv`：ALLODYNIA 1,110/29、PAIN 607,176/49,260、DRUG TOLERANCE 5,013/387、DRUG INEFFECTIVE 1,299,278/208,365、NAUSEA 778,546/64,611、VOMITING 462,663/39,131、PRURITUS 372,941/46,769、CONSTIPATION 213,536/13,579、HYPERAESTHESIA 8,161/523、HYPERPATHIA 43/0、PROCEDURAL PAIN 27,300/1,527、CHRONIC PAIN SYNDROME 1/0、DRUG WITHDRAWAL SYNDROME 87,541/1,667 —— 全部与稿件 Table S4 一致；MedDRA 版本覆盖我独立复核 `reactions.txt`：**4,474,923 行、156 行版本字段为空、其余 4,474,767 行全部为 v.27.1**，与 Table S4 脚注完全一致。**此点经核查无问题。**

**S2. leave-2024-out 与 2024 年簇诊断（§3.8、Table 4C）是同类文献中罕见的诚实做法，且数值全部正确。** 我复核 `04_sensitivity_year_hyperaesthesia.csv`：2021 年 a=1、2024 年 a=8（合计 9 行有日期），`04_sensitivity_leave2024_hyperaesthesia.csv` 显示剔除 2024 后瑞芬 a=1、ROR 0.701、RORR vs 芬 0.106、未达信号；`04_sensitivity_2024cluster_hyperaesthesia.csv` 的 2024/合并比 15.41 / 4.30 / 4.90 / 1.71 与稿件 §3.8 的 "15.4, 4.3, 4.9 and 1.7" 一致。作者主动把"T"（可能为真的信号）降格为"单年簇"，并明写 `"the pooled estimate is a single-year cluster, not a stable finding"`。**此点经核查无问题**，且应作为本稿最值得保留的部分。

**S3. 对 ALLODYNIA（a=1）的处理正确且克制。** §3.3 明写 `"the only defensible fact is the absence of a signal, not its direction"`，Table 2 用 `†` 标注 not estimable，Figure 1 不再绘入该术语，`01_faers_summary.md:58` 亦记录"原稿此处的方向性解读已在 Amendment 1 中删除"。我复核 `01_faers_results.csv` 第 3 行：瑞芬 a=1、ROR 3.471（0.49–24.67）、RORR vs 芬 0.455（0.06–3.30）——区间宽到无信息，作者拒绝解读是正确的。**此点经核查无问题。**

**S4. 加拿大 arm 的方法学选择优于 FAERS arm，且作者主动把定量 SOC 结论全部押在加拿大库。** 使用原生 `SOC_NAME_ENG`（无映射）、限定 suspect 角色、报告级计数，并把 FAERS 侧的启发式面板降级为探索性、明写事件级重复计数与 top-500 截断（Table S1 脚注、§2.5）。我复核 `cv/cv_soc_27.csv` 的 SOC 行（妊娠 2.995/1.733、呼吸 2.641/2.463、免疫 2.363/1.792、心脏 2.288/1.866、血管 1.966/2.288、胃肠 0.101、皮肤 0.143、全身 0.361）与 §3.7 完全一致。**此点经核查无问题。**

**S5. 数值可复算性极高。** 我用 openFDA 独立查询得单药总数 5,375 / 121,819 / 6,513 / 56,501，与 Table 1 逐字一致；我用原始抽取包独立重建加拿大队列得 111 / 4,881 / 63 / 7,675，逐字一致；72/111=64.86%、102/111=91.89%、1,810/7,675=23.58%、535/7,675=6.97% 与 Table S3 的 64.9%、91.9%、23.6%、7.0% 一致；Table 2 脚注的 Bonferroni 下界我独立复算为 1.615（z=3.39，72 次比较），与稿件的 1.61 一致。**此点经核查无问题。**

---

## 5. 需要作者明确澄清的事实性问题

1. **`report_drug_indication.txt`（330 万行，含可归因到产品号的英文适应证）是否在作者的分析范围内？** 若是，为何 §4.5 写 "indication cannot be adjusted for"？若不是，作者如何解释该文件存在于其数据目录 `cv/cvponline_extract_20241130/`？我核对该文件 col2 与 `drug_products.txt` 的产品号（8248=REMICADE 等）逐行一致，故适应证可按药品记录精确归因。
2. **加拿大侧可算性到底是几个术语？** 我在 `cv/cv_pt_summary.csv` 上数出恰好 3 个（PAIN、DRUG INEFFECTIVE、VOMITING），其中**没有任何一个 a priori 痛觉相关术语**。请作者确认这是否与 "so it confirms direction only where it has numbers" 的读者印象一致，并说明为何 §5 写"四个阴性对照在加拿大无法检验"，而 VOMITING 是可算的且 vs 芬太尼 >1。
3. **`cv_pt_summary.csv` 中 `REMI_RORR_FEN_phys` / `REMI_RORR_MOR_phys` 两列的分子、分母口径是什么？** 我复算出稿件值 5.921 只能由 `16/(111−16) ÷ 135/(4881−135)` 得到，即分母用全队列而非医师层。请确认这是否为作者的预期估计量，若是，它对应什么目标参数？
4. **四药队列的重叠是否被评估过？** 我测得瑞芬太尼队列中 1,575 份（29.3%）同时含芬太尼、2,025 份（37.7%）含至少一个对照，加拿大侧 12,730 份队列成员仅对应 12,171 份唯一报告。请说明是否考虑过互斥队列的敏感性分析。
5. **四个队列的每报告反应术语条数是否被测量过？**（我测得 1.694 / 3.899 / 4.111 / 6.502。）若未测量，作者如何排除"低报"只是"报告更简略"这一解释？
6. **"独立确认"的操作定义是什么？** 请作者说明在共享 MedDRA、共享北美药市场、且跨国 MAH 可能向两库递交同一病例的条件下，加拿大库在什么意义上"独立"。
7. **§3.8 的 "all negative controls stayed below 1" 与 Table 4A 的 PRURITUS vs 芬太尼 1.087 如何并存？** 请确认是笔误还是不同口径。
8. **加拿大 RORR 的 95% CI 为何全部缺失？** §2.4 已声明 CI 方法。

---

## 6. 我实际做的独立核查

**读过的核心文件（不含任何评审/回复类记录）**：`I_正文_IMRaD_en.md`（全文）、`ANALYSIS_PLAN.md`、`01_faers_results.csv`、`04_sensitivity_ps_only.csv`、`04_sensitivity_year_pain.csv`、`04_sensitivity_year_hyperaesthesia.csv`、`04_sensitivity_leave2024_hyperaesthesia.csv`、`04_sensitivity_2024cluster_hyperaesthesia.csv`、`04_sensitivity_estimable_years.json`、`10_term_dictionary.csv`、`03_soc_27.csv`、`D_27SOC_openFDA事件级.md`、`02_route_summary.md`、`01_faers_summary.md`、`_probe_meddra_level.json`、`cv/cv_pt_summary.csv`、`cv/cv_drug_totals.csv`、`cv/cv_subgroups.csv`、`cv/cv_summary.md`、`cv/cv_soc_27.csv`、`cv/cv_process.py`。

**在加拿大原始抽取包上自行编写的分析（`cv/cvponline_extract_20241130/`，`$` 分隔）**：

| 我做的核查 | 结果 |
|---|---|
| 独立重建四个 suspect 队列 | **111 / 4,881 / 63 / 7,675**，与 Table 1 逐字一致；并集 12,171（队列之和 12,730 → 559 份属 ≥2 队列） |
| 复核 72/111、102/111、吗啡消费者与医师占比 | 64.86%、91.89%、23.58%、6.97% —— 与 Table S3 的 64.9/91.9/23.6/7.0 一致 |
| 复核 `cv_pt_summary.csv` 全部 RORR | PAIN 0.235/0.146、DRUG INEFFECTIVE 1.277/1.703、VOMITING 1.066/0.392 全部一致；补算 CI：0.058–0.957 / 0.036–0.591 / 0.813–2.005 / 1.086–2.671 / 0.334–3.403 / 0.124–1.239 |
| 加拿大术语可算性普查 | **18 个术语中仅 3 个**可算（PAIN、DRUG INEFFECTIVE、VOMITING），a priori 痛觉术语与 HYPERAESTHESIA 全部不可算 |
| **年龄分层**（`_a5_strat.py`） | 18–64 岁：PAIN 0.381（0.052–2.795）vs 芬、0.234（0.032–1.705）vs 吗；DRUG INEFFECTIVE **2.946（1.559–5.566）** vs 芬。≥65 岁：瑞芬 0 例 PAIN，不可估 |
| **报告者分层** | 医师层：瑞芬 PAIN **0 例**（不可估）；其他卫生专业人员 0.294（0.040–2.139）；消费者 1 例 → **1.638（0.190–14.152）** |
| **严重度分层** | 严重层 PAIN 0.155（0.022–1.115）；非严重层 **0.912（0.113–7.355）** |
| **医师层混合量复刻** | 稿件 5.921 只能由 16/(111−16) ÷ 135/(4881−135) 得到；正确医师限定值 **17.936（5.149–62.478）**，吗啡向 **18.444（5.286–64.362）** |
| **适应证归因**（`_a5_cv_indication.py` / `_a5_cv_indication_strata.py`） | 验证 `report_drug_indication.txt` col2 = DRUG_PRODUCT_ID（8248=REMICADE 等）；瑞芬队列适应证 111/111 围术期麻醉类；芬太尼无痛/慢性痛类为主；吗啡为 RA/高血压/心绞痛/纤维肌痛/偏头痛等 |
| **适应证分层头对头**（我补做） | 围术期层（n=84/239/22/43）：PAIN **0.399（0.048–3.295）** vs 芬、0.161（0.016–1.593）vs 吗；DRUG INEFFECTIVE **2.355（1.244–4.459）** vs 芬、2.375（0.824–6.848）vs 吗。疼痛适应证层（n=4/631/2/824）：PAIN **1.791（0.184–17.397）** vs 芬、1.416（0.146–13.706）vs 吗（方向反转） |
| **报告深度统计**（`_a5_depth.py`） | 每报告反应条数 **1.694 / 3.899 / 4.111 / 6.502**；单条反应报告占比 69.4% / 39.9% / 31.8% / 27.1% |
| **深度分层 MH 与份额归一**（`_a5_depth_strata.py`） | PAIN vs 芬 **0.640（0.027–14.898）**、vs 吗 **0.978（0.042–22.751）**（未分层 0.235 / 0.146）；DRUG INEFFECTIVE vs 芬 1.663、vs 吗 2.409；VOMITING vs 芬 3.765。反应份额比：PAIN 0.573/0.618、DRUG INEFFECTIVE 2.796/5.931 |
| **MedDRA 版本与反应行计数** | `reactions.txt` **4,474,923 行**、156 行版本为空、其余 **4,474,767 行全部 v.27.1** —— 与 Table S4 脚注逐字一致 |

**通过 openFDA API 做的独立查询**（`_a5_faers_strata.py`、`_a5_overlap_faers.py`）：

| 核查 | 结果 |
|---|---|
| 单药总数 | 5,375 / 121,819 / 6,513 / 56,501 —— 与 Table 1 一致 |
| **队列重叠矩阵** | 瑞芬∩芬 1,575、瑞芬∩舒 483、瑞芬∩吗 323、芬∩吗 6,185、芬∩舒 299、舒∩吗 596；三重 30/136/18/55；四重 4。容斥：瑞芬队列 **2,025 份（37.7%）** 含 ≥1 对照 |
| **年龄分层** | PAIN vs 芬：合并 0.066 → 18–64 **0.098**、≥65 **0.028**；DRUG INEFFECTIVE vs 芬：0.568 → 0.638 / 0.457 |
| **性别分层** | PAIN vs 芬：女 0.072、男 0.036；DRUG INEFFECTIVE vs 芬：女 0.381、男 0.641 |
| **探针分层内反转** | DRUG INEFFECTIVE vs 舒芬：合并 0.784 → 18–64 **1.079**、≥65 **1.058**、男 **1.783**（均 >1） |
| 阴性对照方向统计 | 主分析 12 个可算比值 11 个 <1（例外 PRURITUS vs 舒芬 1.310）；严重报告子集 8 个中 2 个 >1（PRURITUS vs 芬 1.087、vs 舒 1.218）；全部 29 个可算 RORR 中 26 个 <1 |

**我未能完成的核查（如实说明）**：尝试通过 openFDA 分页拉取完整记录以计算 FAERS 侧每报告反应条数，该环境下载记录级响应多次超时/返回 403，故 FAERS 的报告深度未测；`ascii/2024Q4/` 为空目录，证实作者所述"FAERS 个案层文件未取到"，因此 FAERS 侧的 role / 途径 / 时间-事件分析确实不可行——**§4.5 关于个案层不可得的陈述经核查成立**。

**我复核后认为没有问题的稿件陈述（同样计入审稿成果）**：Table S4 全部计数；MedDRA 版本覆盖数字；Table 2 脚注的 Bonferroni 下界 1.61；2024 年簇比值 15.4/4.3/4.9/1.7；§3.7 全部 SOC 数值；Table S3 全部百分比；ALLODYNIA 的 not-estimable 处理；Table 1 与 cv_drug_totals.csv 的一致性；`_probe_meddra_level.json` 与"美式拼写 HYPERESTHESIA=0"所间接支持的 LLT→PT 结论。

---

## 附：因果推断层面必改清单（7 条）

**A. 必须补分析（数据已在作者手上，全部可执行）**

| # | 补什么 | 用什么 | 预期输出 |
|---|---|---|---|
| 1 | 适应证匹配的头对头（本文 M1 的核心） | `cv/cvponline_extract_20241130/report_drug_indication.txt` join `report_drug` on (report id, drug product id) | **Table 5**：`Stratum \| Remifentanil n \| a \| Fentanyl n \| a \| Morphine n \| a \| RORR vs fentanyl (95% CI) \| RORR vs morphine (95% CI)`；层：全样本 / 围术期麻醉 / 疼痛适应证 / 18–64 岁 / ≥65 岁 / 医师 / 其他卫生专业人员 / 严重 / 非严重；代表术语 PAIN、HYPERAESTHESIA、DRUG INEFFECTIVE 及四个对照 |
| 2 | 报告深度控制（本文 M3） | `reactions.txt` 逐报告计数；MH 分层 + 反应份额归一 | **Table 6**：`PT \| terms per report（四药） \| 单条反应报告% \| crude RORR vs FEN \| MH-adjusted RORR vs FEN (95% CI) \| share-of-terms ratio vs FEN \| 同四列 vs MOR` |
| 3 | FAERS 侧年龄/性别/报告者分层（补 §4.5 "按 sex/age/role 的亚组未做"） | openFDA `search=` 组合查询（我已实测可用） | **Table 5 Panel B**，至少 18–64 / ≥65 / 女 / 男 / `primarysource.qualification=1`（医师）；并报告 44.1% 年龄缺失对瑞芬队列的影响 |
| 4 | 互斥队列敏感性（本文 M5） | 队列重叠矩阵 + 仅含单一阿片者 | **Table S7**：4×4 重叠矩阵；`Cohort definition \| n (四药) \| PAIN RORR vs FEN (95% CI) \| DRUG INEFFECTIVE RORR vs FEN (95% CI)` |

**B. 必须改措辞（不需要新数据，但必须在本轮全部落实）**

| # | 位置 | 改什么 |
|---|---|---|
| 5 | §3.6 标题与首句、§4.4 末句、§4.3 "explains"、§5 "large, stable and reproduced in Canada" | 把因果动词降为关联/一致性表述；删除或定量化"large and stable"（我给出可粘贴替换句于 M1、M3）；删除 §4.3 中仅对 DRUG TOLERANCE / WITHDRAWAL 使用药理学解释的双标句 |
| 6 | §3.5 "independent Canadian database"、§3.5 标题 "Cross-database confirmation"、Table 3 "Confirmed" 列、§1 摘要 "for confirmation" | 改为 "a second, methodologically cleaner but non-independent North American system" / "Cross-database comparison"；删除 8 行 "yes (zero in both)"，只保留可算术语；摘要同步修改 |
| 7 | §3.8 与 §4.1 "all negative controls stayed below 1"、§5 "could not be tested in Canada"、§3.4 的 "physician-only analysis (5.921 and 10.604)"、§3.4 与 Table 3 脚注的 "argues against a uniform global reporting artefact"、§3.9 的管线有效性结论、§4.5 的途径"对称稀释"句 | 逐条按 P1-1/P1-2/P1-3/P1-4/P1-6/M4 给出的替换句改写；加拿大侧全部 RORR 补 95% CI |
