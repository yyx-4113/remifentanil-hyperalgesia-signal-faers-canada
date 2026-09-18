# Round-5 独立审稿 — A1_clinical_OIH 临床麻醉学与阿片类药物诱导痛觉过敏（OIH）专家

## 0. 审稿人身份与总体结论

我是一名长期从事瑞芬太尼与阿片类临床研究、熟悉 OIH 定量感觉测试（QST）与预防性用药文献的临床麻醉学研究者，作为本稿在 *Anaesthesia* 的审稿人之一。

**Verdict: Major Revision**（按 Original Article 标准；若作者拒绝按 §6 清单重构论证框架，则应 Reject，转投药物警戒类期刊）

理由：

1. 本稿方法学上最扎实、最值得保留的贡献是"术语可检索性核验"——我独立复核后确认这个发现是真的（FAERS 缓存中 `HYPERALGESIA` 返回 0、加拿大库 742 MB 反应表前 100 万行中 `Hyperalgesia` 出现 0 次而 `Hyperaesthesia` 出现 166 次）。这一点足以支撑一篇有价值的"方法学警示"短文。
2. 但本稿自称的"改正后主发现"——"概念存在且在四种阿片中都达到信号标准"——本身在临床语义上站不住：作者自己在 §4.4 承认 `HYPERAESTHESIA` "is not pain-specific"，却仍把它当作"carrying the hyperalgesia concept"的代理来承载全文结论。一个被作者明确否定其特异性的术语，不能同时充当结论的证据。
3. 稿件对临床证据网络的定位已过时约十年，且漏掉了唯一能在**表型层面**证伪其"PAIN 可作代理"逻辑的人体实验证据（Mauermann 2016：芬太尼高剂量下 NRS 下降 0.83 分、痛觉过敏面积上升 30.5%、而 allodynia 不变，P = 0.682）。这不是"少引一篇"的问题，而是让 §2.3 与 §4.2 的核心论断失去支点。
4. §3.9 用作"管线灵敏度正对照"的免疫系统信号，临床上不可能是真信号（5 375 份瑞芬太尼报告中有 532 份编码为 ANAPHYLACTIC SHOCK，占 9.9%；芬太尼为 0.28%），它证明的是管线会产生伪信号，而不是管线能检出真信号。作者的工作稿里已标注"不作因果解读"，但正文把它升级成了阳性对照。
5. 最稳健的发现（PAIN 低报）作者自己承认反映报告场景而非药理，因此 §4.6 对临床医生等于零信息。这可以修——用稿件已有的数据就能改成一句可执行的话——但不修的话，这篇稿子对 *Anaesthesia* 的读者没有可操作价值。

---

## 1. 重大问题（Major）

### M1. 全文的"改正后主发现"建立在一个作者自己承认非疼痛特异性的术语上，代理关系不成立

**【问题】** 作者把 `HYPERAESTHESIA` 标为"carrying the hyperalgesia concept"的代理，并据此宣称"概念存在且在四种阿片中都达到信号标准"；但同一篇稿子又承认该术语不是疼痛特异的。这两句话不能同时成立，而前者承载了标题级结论。

**【证据】**
- 稿件 §2.3（`I_正文_IMRaD_en.md:67`）："No conclusion rests on these strings, so five dictionary proxies — the preferred terms carrying the same concepts (HYPERAESTHESIA, HYPERPATHIA, PROCEDURAL PAIN, CHRONIC PAIN SYNDROME, DRUG WITHDRAWAL SYNDROME) — were added..."（把 HYPERAESTHESIA 列为"carrying the same concepts"）。
- 同一稿 §4.4（`I_正文_IMRaD_en.md:167`）："...HYPERAESTHESIA denotes increased sensitivity to stimulation generally rather than to pain, though it cannot be read as evidence of pain-specific sensitisation because HYPERAESTHESIA is not pain-specific..."
- 表 S4 行标签（`I_正文_IMRaD_en.md:481`）："preferred term carrying the hyperalgesia concept (MedDRA 10020568)"。
- 我核对了 MedDRA 层级事实与数据可得性：`HYPERAESTHESIA` 在 FAERS 全库 8 161 份、加拿大库 523 行反应记录（`_faers_cache.json`、`10_term_dictionary.csv`），数量本身无误。但**两个库都不暴露 LLT**——我把加拿大 extract 的 `cv/cvponline_extract_20241130/reactions.txt` 字段结构逐列拆开核对：`report_id $ reaction_seq $ duration_value $ duration_unit_EN $ duration_unit_FR $ PT_EN $ PT_FR $ SOC_EN $ SOC_FR $ release`，字段 3–5 是"持续时间数值/单位"，不是 LLT（抽样 100 000 行仅 2 行非空，均为 duration，例如 `"4707501"$"47075"$"24"$"Hours"$"Heure(s)"$"Somnolence"...`）。因此**"这 8 161 份里有多少是 hyperalgesia 语义、多少是普通感觉过敏语义，在本数据里原则上不可分解**。
- 因此 Table 2 中 `HYPERAESTHESIA` 的 a = 10（`01_faers_results.csv:15`）是一个**混合物计数**，作者无法证明它的主要成分是 OIH。

**【为什么重要】** 这是全文唯一的"阳性结论"。如果它站不住，本稿就只剩"术语零值 + PAIN 低报"两个发现，而作者自己已承认后者不可药理归因。审稿人会问：既然代理非特异且不可分解，凭什么说"the concept is present and meets the signal criterion for all four opioids"？更尖锐地说，作者在 §4.4 已经把答案写出来了（"cannot be read as evidence of pain-specific sensitisation"），却在 §3.3、§4.1、§5 三处把它当作主结论陈述——这是同一篇稿子内部的结论分级不一致，属于修改文字可以解决、但不改就必然被拒的类型。

**【具体修改建议】**
1. 把 `HYPERAESTHESIA` 从"dictionary proxy（代理）"重新定级为**非特异性感觉术语（non-specific sensory term, sensitivity analysis）**，不再称其为"carrying the concept"。表 2、表 3、表 S4、图 1 图注中的相应标签统一改为：
   > `HYPERAESTHESIA | non-specific sensory term (exploratory) | not pain-specific; absorbs hyperaesthesia of any modality`
2. 把**唯一疼痛特异且可检索**的 PT `ALLODYNIA` 提升为并列主要终点，并在 Results 首句就点明它的走向，形成如下可直接粘贴的段落：
   > **Results, opening sentence (replacement).** "Of the two retrievable preferred terms that denote altered pain sensitivity, only ALLODYNIA is pain-specific; remifentanil contributed 1 report (reporting odds ratio 3.47, 95% confidence interval 0.49–24.67) against 48 for fentanyl and 30 for morphine, so the analysis is uninformative for remifentanil. HYPERAESTHESIA, a term for increased sensitivity to stimulation of any modality, was reported disproportionately for all four opioids, but it is not pain-specific and its reports cannot be decomposed into hyperalgesia-sense and other-sense coding in either database, because neither corpus exposes the lowest level term."
3. 在 §2.3 增补一句明确的方法学声明（这是本稿最该说却没有说的一句话）：
   > "Neither corpus exposes the MedDRA lowest level term, so the proportion of HYPERAESTHESIA reports originating from the LLT *Hyperalgesia* is unknown and unbounded; no PT in either dictionary denotes opioid-induced hyperalgesia as a syndrome."
4. 结论段（`I_正文_IMRaD_en.md:193`）中删去"shows disproportionate coding for fentanyl, sufentanil, morphine and, in the larger database, remifentanil"这一表述的"支撑结论"语气，改为"shows disproportionate coding of a non-specific sensory term"。

---

### M2. 作者排除了一个对自己有利、且被自身数据部分支持的临床解释——瑞芬太尼可能真的 OIH 负担更低

**【问题】** 稿件把"瑞芬太尼四药中最弱"单向归因于报告行为（§4.4："most parsimoniously explained by the same under-reporting that affects every other term, not by a genuinely lower hyperalgesia burden"），却既未陈述、也未检验替代假说：瑞芬太尼**结构上不可能**产生其比较药所经历的慢性暴露路径，而 OIH 的最强临床证据恰恰来自慢性暴露人群。更严重的是，稿件未能利用数据中唯一在给药途径与报告场景上与瑞芬太尼匹配的比较药——舒芬太尼。

**【证据】**
- 稿件 §4.4（`I_正文_IMRaD_en.md:167`）："Remifentanil's lowest-of-four ranking is most parsimoniously explained by the same under-reporting that affects every other term, not by a genuinely lower hyperalgesia burden."
- 但同一稿 §4.3（`I_正文_IMRaD_en.md:161`）已经对另外两个术语给出了药理归因："For DRUG TOLERANCE and DRUG WITHDRAWAL SYNDROME part of the low reporting is probably physiological: remifentanil's ultrashort half-life and lack of oral or transdermal formulation make true tolerance and withdrawal clinically uncommon." ——**同一个"无口服/无透皮"的事实，在 §4.3 是药理归因，在 §4.4 对 HYPERAESTHESIA 却被拒绝使用**。
- 我核对了各药的暴露结构（`02_route_stratified.csv:5-75`）：瑞芬太尼与舒芬太尼为纯静脉/手术室用药；芬太尼有透皮 21.55%、口服 30.52%；吗啡有口服 49.12%、透皮 3.31%。芬太尼与吗啡的 FAERS 报告池因此包含大量门诊/慢性用药人群。
- 关键被埋没的比较：**舒芬太尼是唯一与瑞芬太尼在途径（纯静脉）、剂型（无口服/透皮）与报告场景（围术期）上匹配的对照药**，而它的方向与另两药相反。我复核 `01_faers_results.csv` 并自行重算 ROR：
  - HYPERAESTHESIA：瑞芬 ROR 4.729（a = 10）；芬太尼 6.795（a = 315）；**舒芬太尼 8.611（a = 22）**；吗啡 12.166（a = 262）。
  - PAIN：瑞芬 0.142；芬太尼 2.138；**舒芬太尼 0.505**；吗啡 3.083。
  - 即舒芬太尼的 PAIN 比例（0.505）与瑞芬一样低于 1，**但它的 HYPERAESTHESIA 比例（8.611）高于芬太尼**。换言之，在场景匹配的对照中，瑞芬太尼是**唯一对所有疼痛相关术语都系统性低报**的那一个——这既支持作者的报告行为解释，也说明"全药池平均"掩盖了真正有信息量的那一组比较。
- 我复核了瑞芬 vs 舒芬太尼的全部 RORR（`01_faers_results.csv`，我自己重算，与表 S5 一致）：HYPERAESTHESIA 0.549（0.26–1.16，**区间跨 1**）、PAIN 0.281（0.18–0.44）、NAUSEA 0.563、VOMITING 0.969、PRURITUS 1.310（**>1**）、CONSTIPATION 0.210、DRUG INEFFECTIVE 0.784、PROCEDURAL PAIN 2.124（>1）。所以"瑞芬对所有术语一律低报"在舒芬太尼对照下**并不成立**（2 个术语反向），这比作者目前"the same under-reporting that affects every other term"的说法更准确、也更有意思。

**【为什么重要】** 一位麻醉科审稿人读到"瑞芬太尼 OIH 负担更低"被一句话排除、而排除理由与作者自己在 §4.3 使用的药理理由直接冲突时，会认为作者有结论先行的嫌疑——尤其因为这个替代假说对作者"不利"的方向恰恰是临床上更合理的（无慢性暴露 → OIH 更少，与 Higgins 2019 的 meta 分析结论一致：OIH 在阿片使用障碍人群中比在疼痛患者中更明显）。这同时改写了 §5 的措辞：目前 §5 第 192 行"These findings do not establish whether hyperalgesia after remifentanil occurs"过于中立，没有告诉读者数据把可能性推向哪一边。

**【具体修改建议】**
1. 在 Table 2 与 Figure 1 中把**瑞芬 vs 舒芬太尼**提到与芬太尼/吗啡并列的位置（数据已在 `01_faers_results.csv`，无需新分析），并在 §3.3 增加一句：
   > "Sufentanil is the only comparator matched to remifentanil on route (intravenous only) and on care setting; against it, remifentanil's HYPERAESTHESIA ratio was 0.549 (95% confidence interval 0.26–1.16), an interval that includes parity, whereas its PAIN ratio was 0.281 (0.18–0.44). Relative to the setting-matched opioid, therefore, remifentanil under-reports pain but shows no demonstrable difference in reporting of the non-specific sensory term."
2. 用以下段落替换 §4.3/§4.4 中单向归因的句子，明确列出两个假说并指出哪个比较能区分它们：
   > "Two explanations remain open for remifentanil's lowest-of-four ranking. It may reflect the reporting behaviour described above; it may also reflect a genuinely lower burden, because remifentanil, uniquely among these four drugs, has no oral or transdermal formulation and no chronic-use population, and opioid-induced hyperalgesia in clinical populations is most evident after chronic exposure and in people with opioid use disorder. The sufentanil comparison is the one that partially separates them: sufentanil shares remifentanil's route and care setting yet reports the non-specific sensory term more than fentanyl does, so remifentanil's ranking cannot be attributed wholesale to perioperative reporting alone. We cannot distinguish the two explanations with these data."
3. §5 结论句改为可判断的表述：
   > "Remifentanil's reporting of the only pain-specific retrievable term was too sparse to estimate, and its low reporting of pain is reproduced across databases and years but is confounded by indication; the data therefore neither establish nor exclude a lower hyperalgesia burden in remifentanil, and the direction of the available comparison is compatible with both."

---

### M3. §3.9 的"管线灵敏度正对照"在临床上是伪信号，逻辑方向也错了

**【问题】** 作者用"免疫系统类信号"作为"分析在信号存在时能检出信号"的证据（"supporting — not proving — that the absent hyperalgesia signal reflects the data, not the method"）。但该信号本身的量级在临床上不可能为真，因此它证明的是管线**会产生**类水平伪信号，而不是管线**能检出**真信号。

**【证据】**
- 稿件 §3.9（`I_正文_IMRaD_en.md:141`）："Remifentanil showed a strong immune-class signal (10.951; 8.613 versus fentanyl), driven by anaphylactic shock (532 events) and reaction (367), also seen in Canada (2.363), supporting — not proving — that the absent hyperalgesia signal reflects the data, not the method."
- 数据源：`03_soc_27.csv:16` 给出 REMI 免疫类 1 108 事件（占 20.61%）、ROR 10.951、RORR vs 芬太尼 8.613；`D_27SOC_openFDA事件级.md:76-88` 给出 PT 拆解：ANAPHYLACTIC SHOCK 瑞芬 532 / 芬太尼 341；ANAPHYLACTIC REACTION 367 / 1 049。
- 我自己换算：532/5 375 = **9.9%** 的瑞芬太尼报告被编码为过敏性休克；芬太尼为 341/121 819 = **0.28%**。相差 35 倍。瑞芬太尼围术期过敏性休克（IgE 介导）在文献中是罕见事件（个案报道级别），9.9% 不可能是药物效应；最可能的成因是报告层面的：瑞芬太尼作为静脉麻醉常用药，会被一并写进"围术期过敏反应"报告的药物列表中，而本稿的 FAERS 队列是**角色不可区分（role-agnostic）**的（§2.2，`I_正文_IMRaD_en.md:59`），因此会被大量卷进这类报告。
- 反向证据：在报告级、原生 MedDRA、限定 suspect 角色的加拿大库中，免疫类占比为**舒芬太尼 17.5% > 瑞芬 8.1% ≈ 吗啡 9.6% > 芬太尼 4.7%**（`cv/cv_soc_27.csv`，我逐行核对）。也就是说在更干净的库里这个"信号"并不落在瑞芬太尼头上。作者把加拿大 RORR 2.363 当作"跨库复现"，但加拿大队列仅 9 例免疫类报告 / 111 例，且舒芬太尼更高。
- 作者自己的工作稿 `D_27SOC_openFDA事件级.md:89` 已明确写："⚠️ 该信号超出本文（OIH）范围，不作因果解读"；正文却把它升级为正向推断的支柱。同文件第 108–114 行还自承该表"事件级而非报告级""ROR 被放大""启发式关键词映射不是权威 MedDRA"。

**【为什么重要】** 一个麻醉科审稿人只要看到"532 例过敏性休克 / 5 375 份报告"，立刻会判定这是编码/报告伪影，而作者用同一段文字去论证"方法没问题"。这会反噬全稿可信度：读者会问，如果 10.95 的类水平 ROR 是伪信号，那么 4.73 的 PT 水平 ROR 凭什么不是？此外，作者在 `D_27SOC_openFDA事件级.md:112` 自承 `DRUG INEFFECTIVE` 被规则错误归入 Injury/poisoning（权威 MedDRA 应为 General disorders / Product issues），而 `01_faers_results.csv:6` 与表 2 又把它标为 "General"——两套 SOC 映射互相矛盾却都被引用。

**【具体修改建议】**
1. 删除 §3.9 的"灵敏度正对照"论证，或改写为**伪信号示例**。可直接替换为：
   > **§3.9 (replacement).** "An unexpected class-level finding illustrates the limits of this arm rather than its sensitivity. In the exploratory FAERS class analysis remifentanil showed a strong immune-class signal (reporting odds ratio 10.95), driven by 532 reports coded ANAPHYLACTIC SHOCK among 5 375 remifentanil reports (9.9%), against 0.28% of fentanyl reports. A drug-specific anaphylaxis rate of this magnitude is not clinically plausible, and in the Canadian report-level analysis the immune class was led by sufentanil (17.5% of its cohort) rather than remifentanil (8.1%); the FAERS cohorts are role-agnostic, so a drug co-administered during anaphylaxis reports is captured in that drug's cohort. The class arm therefore demonstrates that this pipeline can generate large class-level artefacts, and it is reported here for that reason only."
2. 在 §4.5 Limitations 增补一句，明确 FAERS 探索性 SOC 臂**不承担灵敏度论证职能**：
   > "The exploratory class analysis cannot serve as a positive control: the strongest class-level result it produced is not clinically plausible (§3.9), so no sensitivity inference is drawn from it."
3. 补齐或删除 §3.9 中"是否作正向论证"与其工作稿立场之间的冲突；至少须在正文中注明 `DRUG INEFFECTIVE` 的 SOC 归属在两条映射链中不同。

---

## 2. 重要问题（P1）

### P1-1. 对 Fletcher 2014 的转述丢掉了"显著"与"瑞芬太尼特异"，并且后 2016 年的定量证据全部缺失

**【问题】** 稿件把最有分量的瑞芬太尼特异性 meta 分析（Fletcher & Martinez 2014）描述为"small, heterogeneous effects"，抹去了其"显著"与"主要归因于瑞芬太尼"的结论方向；同时全稿未引用 2016 年之后任何定量综合、叙述性综述或指南类文献，导致"contested"这一框架停留在 2014 年的证据状态。

**【证据】**
- 稿件 §1（`I_正文_IMRaD_en.md:37`）："a meta-analysis reported small, heterogeneous effects [9]."
- Fletcher & Martinez 原文摘要（PMID 24829420，DOI 10.1093/bja/aeu137，我逐一核对）：27 项 RCT、1 494 例；高剂量术中阿片组术后疼痛评分高于对照，**1 h MD 9.4（95% CI 4.4–14.5）、4 h MD 7.1（2.8–11.3）、24 h MD 3.0（0.4–5.6）**（100 mm VAS），24 h 吗啡用量 **SMD 0.70（0.37–1.02）**；且 "These results were **mainly associated with the use of remifentanil**"；结论 "high intra-operative doses of remifentanil are associated with **small but significant** increases in acute pain after surgery"。稿件同时丢掉了"significant"、"mainly remifentanil"两项，也未给出任何效应量。
- §4.6（`I_正文_IMRaD_en.md:185`）把临床决策交给 "[7, 8]"（Rivosecchi 2014、Kim 2015），**独独漏掉 [9]**——而 [9] 正是三项里唯一给出瑞芬太尼特异性阳性合并估计的那一篇。
- 我核对了 Rivosecchi 2014 原文摘要（PMID 24669819）：35 篇、16 支持 / 6 反对、22 篇为预防研究，"remifentanil does induce a degree of hyperalgesia, but we do not believe that it reaches a level of clinical significance that requires prevention"。稿件 §1 的转述（"16 studies supporting... and 6 refuting it, concluding the effect is real but too small to require prevention"）**在数字与方向上均正确**，此点经核查无问题。
- 缺失的定量/指南类证据（我逐一核实了作者、年份、期刊、卷页、DOI）：
  | 文献 | 为何影响本稿论证 |
  |---|---|
  | **Huang X, Cai J, Lv Z, et al. Postoperative pain after different doses of remifentanil infusion during anaesthesia: a meta-analysis. *BMC Anesthesiol* 2024; 24: 36. DOI: 10.1186/s12871-023-02388-3（PMID 38218762）** | 31 项 RCT / 2 019 例，是当前最新的瑞芬太尼剂量-反应 meta 分析；低剂量较高剂量在 1–2 h、3–8 h、24 h、48 h 疼痛评分更低，且**专门合并了切口周围与前臂 allodynia**（Fig. 3）。它把临床问题从"是否存在"推进到"什么剂量/停药方式"——本稿"contested"框架未反映这一进展。 |
  | **Higgins C, Smith BH, Matthews K. Evidence of opioid-induced hyperalgesia in clinical populations after chronic opioid exposure: a systematic review and meta-analysis. *Br J Anaesth* 2019; 122: e114–26. DOI: 10.1016/j.bja.2018.09.019（PMID 30915985）** | 26 项研究 / 2 706 例。**"There was no evidence of OIH when assessing pain detection thresholds"**；阳性证据出现在疼痛耐受（thermal）而非阈值；且 **OIH 在阿片使用障碍人群中比在疼痛患者中更明显**。这直接冲击本稿 §4.2 "Quantitative sensory testing detects a threshold change" 的表述，并给出作者声称不存在的药理学解释（见 M2）。 |
  | **Adams TJ, Aljohani DM, Forget P. Perioperative opioids: a narrative review contextualising new avenues to improve prescribing. *Br J Anaesth* 2023; 130: 709–18. DOI: 10.1016/j.bja.2023.02.037（PMID 37059626）** | 同刊 2023 年权威综述直言："**Clinically, it has been consistently shown that high intra-operative doses of remifentanil result in hyperalgesia**... hyperalgesia associated with remifentanil can be measured as a reduced mechanical pain threshold close to the wound, and... rate of remifentanil withdrawal influences the increase in pain sensation to external hot and cold stimuli." 用 "consistently shown" 而非 "contested"，与本稿 §1/§4.2 的定调直接冲突。 |
  | **Colvin LA, Bull F, Hales TG. Perioperative opioid analgesia—when is enough too much? A review of opioid-induced tolerance and hyperalgesia. *Lancet* 2019; 393: 1558–68. DOI: 10.1016/S0140-6736(19)30430-1（PMID 30983591）** | 该主题最显眼的综述之一；对以 OIH 为临床落点的稿件，缺引即为定位失败。 |
  | **Koo CH, Yoon S, Kim BR, et al. Intraoperative naloxone reduces remifentanil-induced postoperative hyperalgesia but not pain: a randomized controlled trial. *Br J Anaesth* 2017; 119: 1161–8.** | 标题即结论：纳洛酮降低瑞芬太尼所致痛觉过敏、但**不改变疼痛**。这是"疼痛"与"痛觉过敏"在人体 RCT 中可分离的直接证据。 |

**【为什么重要】** 一位麻醉科审稿人会先看 Introduction 的证据定位。用 2014 年的三项研究支撑"contested"，而漏掉 2019 BJA meta、2019 Lancet 综述、2023 BJA 综述、2024 BMC 剂量 meta，会被判定为文献回顾不完整且带有选择性（只保留了支持"证据不足"这一侧的两篇）。且 §4.6 把临床决策交给 [7, 8] 而跳过给出阳性估计的 [9]，是段落内部的证据挑选，会被直接质疑。

**【具体修改建议】**
1. 重写 §1 关于 Fletcher 的句子：
   > "A meta-analysis of 27 randomised trials (1 494 patients) found that high intra-operative opioid doses increased postoperative pain (mean difference 9.4 mm on a 100 mm scale at 1 h, 7.1 mm at 4 h, 3.0 mm at 24 h) and 24-h morphine consumption (standardised mean difference 0.70), an effect attributed mainly to remifentanil [9]; a systematic review of 35 studies judged the effect real but too small to require prevention [7], and a second found the evidence insufficient to support or refute it [8]. A 2024 meta-analysis of 31 trials (2 019 patients) reported a dose–response relation and pooled allodynia outcomes [new ref], and a 2019 meta-analysis of clinical populations found that the evidence for hyperalgesia depended on assessment: pain tolerance to thermal stimuli was affected but pain detection thresholds were not [new ref]."
2. 把 §4.2 的 "contested rather than supportive" 改为有时效性的表述：
   > "The prospective literature has moved from asking whether remifentanil-induced hyperalgesia exists to asking at what dose and with what withdrawal profile it occurs [9, new ref Huang 2024, new ref Adams 2023]; neither question is answerable from spontaneous reports."
3. §4.6 的引用改为 "[7, 8, 9, new ref Huang 2024]"。
4. §4.2 中 "Quantitative sensory testing detects a threshold change" 改为：
   > "Quantitative sensory testing detects a change in stimulus–response function: in the largest synthesis of clinical populations the signal was carried by pain tolerance rather than by pain detection thresholds [new ref Higgins 2019]."
5. 增补 §1 中 "has not been examined" 的限定（见 P1-5）。

---

### P1-2. 漏掉唯一在表型层面证伪"PAIN 可作代理"的人体证据（指定遗漏文献：Mauermann 2016）

**【问题】** 本稿的核心方法学动作是"用 PAIN 作为 OIH 的实用代理"，并仅以一句断言（§2.3 "necessarily imperfect proxy"、§4.2 "QST detects a threshold change but not its clinical recognition or reporting [24]"）支撑其不可解读性。但该断言有直接的随机对照人体证据，作者未引。

**【证据】（指定遗漏文献）**
> **Mauermann E, Filitz J, Dolder P, Rentsch KM, Bandschapp O, Ruppen W. Does fentanyl lead to opioid-induced hyperalgesia in healthy volunteers? A double-blind, randomized, crossover trial. *Anesthesiology* 2016; 124: 453–63. DOI: 10.1097/ALN.0000000000000976（PMID 26655493）**
> 21 名健康男性，随机双盲交叉，静脉芬太尼低剂量（1 µg/kg）vs 高剂量（10 µg/kg）。高剂量组疼痛评分**下降** 0.83 分（95% CI 0.63–1.02，P < 0.001），而痛觉过敏面积**增加** 30.5%（16.6–44.4%，P < 0.001）；冷加压痛阈与耐受均上升；**ALLODYNIA 两组无差异（+4.0%，−15.4 至 23.5%，P = 0.682）**。结论："A higher dose of fentanyl increased hyperalgesia from 4.5 to 6.5 h in healthy volunteers **while simultaneously decreasing pain scores**."

该文献同时打击本稿三处：
1. **PAIN 代理**：它证明疼痛评分与痛觉过敏可以**反向**移动。因此 §3.4 把"瑞芬太尼 PAIN 低报"当作"报告行为"的证据虽仍成立，但把它与 OIH 的解读脱钩需要引用它，否则读者会认为"PAIN 低报 → 提示 OIH 更少"。
2. **ALLODYNIA 代理**：它证明在高剂量芬太尼下 **allodynia 不变**，改变的是"痛觉过敏面积"。因此本稿（以及我将建议的）用 ALLODYNIA 作疼痛特异代理同样打错了靶——真正的 OIH 表型是**阈值位移/面积扩大**，而 MedDRA 中**不存在**对应"面积"的 PT。这比作者现有论证更锋锐：不只是"临床名不是 PT"，而是"OIH 的定义性测量在 MedDRA 里根本没有对应的事件术语"。
3. **§4.3 的归因**：作者把比较药（芬太尼）的高报告率完全归因于"setting and indication, not pharmacology"（`I_正文_IMRaD_en.md:161`）。但芬太尼的痛觉过敏**有**健康志愿者人体药理证据；该归因因此不完整。

**【为什么重要】** 漏掉这一篇会让 §2.3 与 §4.2 的关键论断变成无据断言，而补上它反而**加强**本稿的术语学论点（"PAIN 不是 OIH 的代理"从"我们推测"变成"已有人体证据"）。这是"漏了它会让某句结论站不住"的典型，也是"漏了它本可以补强某处"的典型。

**【具体修改建议】**
1. 在 §2.3 关于 PAIN 代理的句子后插入：
   > "That pain and hyperalgesia can move in opposite directions is not speculative: in healthy volunteers, high-dose fentanyl lowered pain scores while increasing the area of hyperalgesia, and left allodynia unchanged [new ref Mauermann 2016]. A negative-control result for PAIN therefore carries no information about hyperalgesia, in either direction."
2. 在 §4.2 取代对 [24] 的单点依赖：
   > "The dissociation between the two outcomes has been demonstrated directly in volunteers: high-dose fentanyl reduced pain scores while enlarging the area of hyperalgesia, with allodynia unchanged [Mauermann 2016]; in patients, naloxone reduced remifentanil-induced hyperalgesia without changing pain [Koo 2017]. Neither the area of hyperalgesia nor a threshold shift is represented as a MedDRA preferred term, so a spontaneous-reporting analysis can record at most a reporter's word choice, never the phenotype."
3. 在 §1 关于机制段落后加一句，把"表型无对应术语"提前点明：
   > "The syndrome is defined by a shift in stimulus–response function measured over an area of skin, not by a discrete symptom, and no preferred term in either dictionary denotes it."

---

### P1-3. §4.6 对临床医生近乎零信息；补上两句就能产生真实价值

**【问题】** §4.6 第一句给出的是"既不支持 A 也不支持非 A"，作为 *Anaesthesia* 的临床读者读完不能改变任何决策。本稿其实握有两个可一般化的结论，却没有说出来：（a）本稿隐含的**报告完备度数量级**；（b）**任何用临床名检索的既有药物警戒分析都必然得到零**——这才是本稿对解读既有文献的真实价值。同时，全文只用 ROR/RORR（临床医生不直观），从未给出"每 X 份报告出现 1 份该术语"的可比量化。

**【证据】**
- 稿件 §4.6（`I_正文_IMRaD_en.md:185`）："For clinicians, these data support neither a large remifentanil-specific hyperalgesia reporting burden nor its absence, so decisions about prevention should rest on the prospective literature [7, 8]."
- 我用 `01_faers_results.csv` 的 a 值与 `_faers_cache.json` 的队列数自行计算每报告占比（这是同一个 2×2 表可直接换算的量）：
  - 承担 OIH 概念的 PT（HYPERAESTHESIA）：**瑞芬 10/5 375 = 1/538（0.186%）**；芬太尼 315/121 819 = 1/387（0.259%）；舒芬太尼 22/6 513 = 1/296（0.338%）；吗啡 262/56 501 = 1/216（0.464%）。
  - 唯一疼痛特异 PT（ALLODYNIA）：瑞芬 1/5 375 = **1/5 375**；芬太尼 48/121 819 = 1/2 538；吗啡 30/56 501 = 1/1 883。
  - 全库 PAIN 占比 607 176/20 692 687 = 2.93%，而阿片类之间差 14 倍（0.43% vs 6.03%）。
- 报告完备度：瑞芬太尼 FAERS 累计仅 5 375 份报告（`_faers_cache.json`），而按 Fletcher 2014 与 Adams 2023 所述，高剂量瑞芬太尼术后痛觉过敏在临床试验中是**可重复、多数患者可测**的效应；即使按 1% 的报告完备度也应有数百份报告，实测为 10 份。
- "既有文献解读"这一推论本稿已有雏形（§4.6 "report a clinical-name zero as unretrievable, not reassuring"），但只写给药物警戒人员，未写成一个 F AERS 文献读者可用的判断。

**【为什么重要】** *Anaesthesia* 的读者是临床医生。一个既不能改变用药决策、也不能改变读者解读文献方式的结论，会被要求说明"so what"。反之，只要把上述两点写出来，本稿就从"又一个阴性 FAERS 分析"变成"一个说明此类分析天花板在哪里的方法学论文"——这是 *Anaesthesia* 会接受的定位。

**【具体修改建议】**
1. §4.6 第一段（针对临床医生）替换为：
   > "For clinicians, the practical content of these data is a ceiling, not a comparison. The preferred term that carries the hyperalgesia concept appears in 1 in 538 remifentanil reports and 1 in 387 fentanyl reports, and the only pain-specific retrievable term appears in 1 in 5 375 remifentanil reports. Because clinically evident hyperalgesia after high-dose remifentanil is a reproducible finding in prospective studies, the implied reporting completeness is of the order of 10⁻⁴ or lower. Spontaneous reporting therefore cannot carry a remifentanil hyperalgesia signal at any plausible incidence, and its silence is not evidence about the syndrome."
2. 在 §4.6 第二段（针对药物警戒/文献读者）增补一句可直接引用、改变既有文献解读的推论：
   > "A further consequence concerns the existing literature. Because the string *hyperalgesia* is absent from both coding dictionaries as a preferred term, any disproportionality analysis that queried the clinical name in FAERS would have returned zero reports for every opioid and every comparator — a null that is guaranteed by the dictionary and independent of the data. Reports of no hyperalgesia signal in FAERS should therefore be read as unretrievable rather than reassuring, unless the analysis states which preferred term was used."
3. 在 Results 中加一列或一段"每 X 份报告"表述（无需新分析，变量为 `a / drug cohort`，输出列：`PT, drug, reports_with_term, cohort_size, reports_per_case`），并在 Figure 1 的图注中给出该换算说明。
4. §4.6 末句保留，但把 "find which preferred term carries the concept" 改为 "report the preferred term actually queried, and treat a clinical-name zero as unretrievable".

---

### P1-4. 可读性障碍：两个 60 词以上的句子，其一是自相矛盾的

**【问题】** 摘要 Results 首句 65 词且含两个无标签括号与 `(a = 1)`；§4.4 有一句 61 词，并在同一句内先允许、后禁止同一推断，构成论证上的自相矛盾。

**【证据】**（我自己从 `I_正文_IMRaD_en.md` 抽出并计数）
- 摘要 Results（`I_正文_IMRaD_en.md:25`），**65 词**：
  > "The clinical word is not a preferred term in either dictionary and returned no report, whereas the proxy preferred term carrying it was present in both (8 161; 523) and met the signal criterion for all four opioids, remifentanil included (4.73, 2.54–8.80), but the signal rests on ten reports, eight in 2024, and disappears when 2024 is excluded (a = 1); it did not reproduce."
  问题："in both" 指代不明；`(8 161; 523)` 未标注单位与库；`(4.73, 2.54–8.80)` 未标注是 OR 与 95% CI；`(a = 1)` 是统计格计数，临床读者不可解。此外 `Anaesthesia` 要求摘要不用缩写，而本句直接给出统计量参数符号。
- §4.4（`I_正文_IMRaD_en.md:167`），**61 词**：
  > "A reader who stops at the first query reports a structural absence; one who checks finds a signal that may not be the one intended, because HYPERAESTHESIA denotes increased sensitivity to stimulation generally rather than to pain, though it cannot be read as evidence of pain-specific sensitisation because HYPERAESTHESIA is not pain-specific and the cross-drug ordering is confounded by cohort composition."
  问题："may not be the one intended... though it cannot be read as evidence" 在同一句内以"because X" 先给出警告、再以"because X" 重复同一理由并转换推论方向；后半句的逻辑是"它不能作为疼痛特异性的证据，因为它不是疼痛特异的"——这是**支持**怀疑的理由被写成了**让步**结构，读者无法判断作者主张什么。
- §3.8（`I_正文_IMRaD_en.md:137`）："Its position as the weakest of the four is a corpus-wide average, not a yearly property." —— "Its" 指代不明（前句主语是 2024 年的升高，不是瑞芬太尼的地位）。
- §3.4（`I_正文_IMRaD_en.md:117`）同一句里出现两个"the exception"（指代两个不同的例外），语义冲突。

**【为什么重要】** 摘要的 65 词句是本稿唯一会被广泛阅读的部分（多数读者只读摘要），而它恰好是最不可读的一句；§4.4 的自相矛盾句出现在"全文最有用的贡献"这一段落，会被审稿人当作逻辑缺陷而非文风问题。

**【具体修改建议】**
1. 摘要 Results 首句替换为（4 句，共约 58 词，去掉参数符号）：
   > "The word hyperalgesia is not a preferred term in either database, and searching it returned no report at all. The preferred term that carries the concept was present in both databases (8 161 and 523 reports) and was reported disproportionately for all four opioids, including remifentanil (reporting odds ratio 4.73, 95% confidence interval 2.54 to 8.80). That signal rested on ten reports, eight of them from 2024, and vanished when that year was excluded, leaving one report. It was not reproduced in Canada."
2. §4.4 长句替换为：
   > "A reader who stops at the first query concludes that the event does not exist. A reader who checks finds a signal, but it is not a pain-specific one: HYPERAESTHESIA denotes increased sensitivity to stimulation of any modality, not to pain. It therefore cannot be read as evidence of pain-specific sensitisation, and the ordering among the drugs is confounded by cohort composition."
3. §3.8 末句改为："Remifentanil's position as the weakest of the four is an average over the whole corpus, not a property of any single year."
4. §3.4 的句子改为："The same pattern held for every negative control across all three comparators (Tables 2 and S5): eleven of the twelve computable ratios were below one. The exception was pruritus versus sufentanil (1.310, 0.84–2.04), whose interval includes one. The single term outside the negative-control group that remifentanil reported more often than fentanyl is PROCEDURAL PAIN (§3.3)."

---

### P1-5. "该问题尚未被研究"这一新颖性主张不实；且未与既有 FAERS 阿片研究定位

**【问题】** §1 声称"瑞芬太尼是否在自发报告系统中产生失衡报告尚未被考察"。事实上瑞芬太尼的 FAERS 不良事件谱已被多次分析。真正新颖的是**术语可检索性核验**，而非这个分析本身。以不实的新颖性主张开局，会被要求撤回并重写。

**【证据】**
- 稿件 §1（`I_正文_IMRaD_en.md:39`）："...whether remifentanil generates disproportionate hyperalgesia reporting in the spontaneous reporting systems that drive signal detection has not been examined."
- 存在的同类研究（我核实了题录）：
  - **Hirai R, Uesawa Y. Analysis of opioid-related adverse events in Japan using FAERS database. *Pharmaceuticals* 2023; 16: 1541. DOI: 10.3390/ph16111541（PMID 38004407）**——从 FAERS 提取包括瑞芬太尼在内的 12 种阿片，计算 ROR 并做聚类，瑞芬太尼自成一簇。
  - **Dai M, Chen M, et al. Strong opioids-induced cardiac, neurologic, and respiratory disorders: a real-world study from 2004 to 2023 based on FAERS. *Naunyn-Schmiedeberg's Arch Pharmacol* 2023. DOI: 10.1007/s00210-023-02844-4**——明确纳入 remifentanil 与 sufentanil，用 ROR/PRR/BCPNN/EBGM 四法。
- 本稿 30 篇参考文献中**没有任何一篇是基于 FAERS 的既有阿片研究**，因此无法向药物警戒读者交代"与已有文献的关系"这一必备内容。

**【为什么重要】** 新颖性是 *Anaesthesia* 的接收门槛之一。以"尚未被考察"开局而实际已有同类文献，且未引用它们，会让审稿人怀疑文献检索的认真程度（这将连带影响对 P1-1 的判断）。反过来，只要把新颖性主张收敛到"术语可检索性核验"，并引用既有 FAERS 文献作为对照，这篇稿子的定位反而更牢。

**【具体修改建议】**
1. §1 该句替换为：
   > "The drug's adverse-event profile has been examined in FAERS [Hirai 2023; Dai 2023], but, as far as we can determine, no analysis in this field has verified whether the term it queried is retrievable in the dictionary that coded the database — the step that determines whether a zero means that the event was never reported or that the string was never codeable."
2. 在 §4.2 增加一句与既有 FAERS 文献的对照，并把 P1-3 第 2 条的推论挂靠上去：
   > "Previous pharmacovigilance analyses of opioids, including one that clustered remifentanil separately from other opioids on its FAERS reporting profile [Hirai 2023], did not report which preferred term was used for hyperalgesia; where the clinical name was used, the resulting zero is a property of the dictionary rather than a finding about the drug."

---

## 3. 次要问题（P2）

### P2-1. 表 4A 把 specificity probe 错标为 "OIH-wide"

**【问题】** 同一术语在两处的分组标签互相矛盾。
**【证据】** 表 2（`I_正文_IMRaD_en.md:280`）`| DRUG INEFFECTIVE | probe | ...`；表 4A（`I_正文_IMRaD_en.md:317`）`| DRUG INEFFECTIVE | OIH-wide | ...`；而 §2.3（`I_正文_IMRaD_en.md:71`）明确把它定义为 specificity probe。源文件 `01_faers_results.csv:6` 的 category 为 `OIH-wide`。
**【为什么重要】** 特异性探针的解读前提是它不属于 OIH 术语组；把它并入 OIH-wide 会使"探针方向反了"这一关键论证在表层面自相矛盾，可能被读者误读为"作者自己把探针当成了结局"。属可在校对中捕获的表级一致性错误。
**【具体修改建议】** 统一 `01_faers_results.csv` 的 category 为 `probe`，并让表 2、4A、S5、图 1 的分组标签一律为 `specificity probe`；同时把表 4A 的分组标题说明补全为四组（OIH-narrow / OIH-wide / negative-control / specificity probe / dictionary-proxy，共五组）。

### P2-2. 医师亚组 DRUG INEFFECTIVE 比值（5.921、10.604）未给区间或格计数

**【问题】** 该数值被用作"反向性在医师专属分析中增强"的证据，但既无 95% CI，也未给出分子分母。
**【证据】** §3.4（`I_正文_IMRaD_en.md:119`）："the reversal strengthened in a physician-only analysis (5.921 and 10.604)"。源文件 `cv/cv_pt_summary.csv:6` 的 `REMI_RORR_FEN_phys = 5.921`、`REMI_RORR_MOR_phys = 10.604` 同样不含区间。而瑞芬太尼整队列仅 111 份报告、医师报告仅 19 份（`cv/cv_subgroups.csv:13`），DRUG INEFFECTIVE 在队列内为 25 份，医师子集内必然是个位数。
**【为什么重要】** 用一位数格计数支撑 10.6 的比值，会被统计审稿人要求删除或补区间。临床上它也影响对"报告者身份决定记录内容"这一论点的信任度——而这个论点正是 §3.6/§4.3 的支柱。
**【具体修改建议】** 在 `cv/cv_pt_summary.csv` 增列 `..._phys_a`, `..._phys_n`, `..._phys_CI`，在 §3.4 改写为带区间的表述；若区间宽到跨 1，则把该句改为"在医师子集中方向相同但格计数过小，无法估计（a = n）"。

### P2-3. §4.5 把途径分配的计数单位说成"报告"

**【问题】** "21.1% of its reports" 与源文件的口径不符。
**【证据】** §4.5（`I_正文_IMRaD_en.md:173`）："...received oral-route assignment in 21.1% of its reports."；源文件 `02_route_stratified.csv:5` 为 `REMI,5375,048,Oral,1134,21.1,184.3`，其中最后一列 `KnownRouteCoverage%` = **184.3%**，说明该列统计的是**药-途径条目**而非报告（一份报告含多个药品条目时被多次计数），平均值 1.84 条目/报告。
**【为什么重要】** 该缺陷正是作者用来解释"为什么不能做途径分层"的依据；把单位说错会让审稿人怀疑作者是否理解自己数据的结构，从而削弱对整段局限性论证的信任。
**【具体修改建议】** 改为：
> "...remifentanil, which has no oral or transdermal formulation, nonetheless carried an oral route code in 1 134 of its 5 375 drug-entry records (21.1% of entries; route codes sum to 184.3% of reports because a report may carry several drug entries)."
并在 §2.2 补一句说明 FAERS 的途径字段是药-条目级。

### P2-4. 摘要使用 PT/ROR/RORR 等术语与参数符号，与期刊对摘要的要求不符

**【问题】** 期刊要求摘要不使用缩写；本稿摘要密集使用 `preferred term`、`reporting odds ratios`、`ratio of reporting odds ratios`、`(a = 1)`。
**【证据】** 稿件自述格式要求（`I_正文_IMRaD_en.md:15`）："structured Summary of 250–300 words without abbreviations or references"；摘要正文（`:23`–`:27`）使用了上述术语与符号。
**【为什么重要】** 摘要的读者是临床医生；术语密度是本文最大的可读性来源。此项属形式合规，但会直接影响编辑的第一印象。
**【具体修改建议】** 见 P1-4 第 1 条的替换句：摘要中把 `preferred term` 改为 "the dictionary term"，把 `(a = 1)` 改为 "leaving one report"，把 `reporting odds ratio` 首次出现处写全并在第二次起用 "the ratio"。正文可保留全部术语。

---

## 4. 我认为稿件站得住的地方（附证据）

1. **"术语可检索性"这一核心发现是真的，而且我独立复核通过。** 我在 `_faers_cache.json` 中确认 `patient.reaction.reactionmeddrapt.exact:"HYPERALGESIA"` 的计数为 **0**，而 `HYPERAESTHESIA` 为 **8 161**、`PAIN` 为 **607 176**、`ALLODYNIA` 为 **1 110**；我又直接检索了 742 MB 的加拿大库反应原始表，前 1 000 000 行中 `"Hyperalgesia"` 出现 **0** 次，而 `"Hyperaesthesia"` 出现 **166** 次、`"Allodynia"` 4 次、`"Paraesthesia"` 未计入（另计）。即：临床名零值是字典属性而非数据属性，这个结论经得起检验，且是本稿真正的贡献。
   附带确认一处作者未声明、但对其有利的事实：openFDA 的 REAC 字段按查表只存 PT，因此**用临床名查询在任何药物、任何数据库上都会返回零**——这使该发现具有普遍性而非仅适用于瑞芬太尼。

2. **算术极其干净，18×4 的 ROR 与全部 RORR 我逐格重算，与稿件完全一致。** 我用 `01_faers_results.csv` 的 a 值、`_faers_cache.json` 的队列数与 PT_total 重建 2×2 表（c = PT_total − a，d = N − n − PT_total + a）后重算，得到 HYPERAESTHESIA：瑞芬 **4.729**、芬太尼 **6.795**、舒芬太尼 **8.611**、吗啡 **12.166**；RORR 瑞芬/芬 **0.696**、/舒 **0.549**、/吗 **0.389**；PAIN：0.142 / 2.138 / 0.505 / 3.083，RORR 0.066 / 0.281 / 0.046。全部与表 2、表 S5 三位小数吻合。我也复核了表 4C 中 2024 年瑞芬 ROR **72.856**（a = 8、队列 448、年 PT 总数 337）与 4C 的 RORR 2.495 / 3.495，均与源文件一致。
   我还独立验证了表 2 脚注中的 Bonferroni 下界：ln(4.729) − 3.396 × 0.31700 = 0.477，exp = **1.612**，与稿件所写 1.61 一致。对单作者稿件而言，这种可复算性是加分项。

3. **对 2024 年聚集性的自我否证做得比多数药物警戒论文更严格，且数字正确。** 作者没有停在"合并信号"，而是（a）按年分层、（b）做 leave-2024-out、（c）计算各药"2024 年 ROR / 合并 ROR"以检验是否为瑞芬特异性。我核对了 `04_sensitivity_2024cluster_hyperaesthesia.csv`：瑞芬 72.86/4.73 = **15.41**、芬太尼 4.30、舒芬太尼 4.90、吗啡 1.71，与稿件 §3.8 的"15.4, 4.3, 4.9 and 1.7"完全一致；`04_sensitivity_leave2024_hyperaesthesia.csv` 显示剔除 2024 后瑞芬 a = 1、ROR 0.701（0.099–4.978）、`signal_met = NO`，与 §3.8 一致。作者据此把合并估计判定为"single-year cluster, not a stable finding"，这是正确的推断，也是本稿最值得保留的方法学行为。

4. **加拿大队列的分组与局限声明与实际数据完全一致，没有过度声称。** 我逐行核对 `cv_pt_summary.csv`：瑞芬 HYPERAESTHESIA = **0**、PAIN = **2**（RORR vs 芬 0.235、vs 吗 0.146）、DRUG INEFFECTIVE = 25（RORR 1.277 / 1.703）；`cv_drug_totals.csv` 瑞芬 111、芬太尼 4 881、舒芬太尼 63、吗啡 7 675；`cv_subgroups.csv` 与表 S3 完全对应（严重 91.89%、其他医护 64.86%、消费者 5.41%、医师 17.12%）。稿件在 §3.5 明确写"Canada neither confirms nor refutes the FAERS signal"，未把 0 例包装成阴性证据——这个克制是合格的。另：我核对了 `ascii/2024Q4/` 为空目录，因此 §2.2/§4.5 关于"无法获得个案级文件、无法做 suspect-role 限制、无法做 TTO"的陈述在本地可查范围内**无矛盾**，此点经核查无问题。

5. **格式合规经我实测通过。** 摘要 **299–300 词**（我在 `I_正文_IMRaD_en.md:19-29` 上计数得 299 词，含小标题则约 300 词），Introduction 至 Conclusion 正文 **3 994 词**（含 26 个章节标题共 129 词），均在期刊 300–4000 词的区间内；参考文献 30 篇、带 DOI，编号与正文引用顺序一致（我抽查 [1]–[11] 与 [24]–[30] 的顺序无错位）。这些不是小问题，是很多稿子被退回的理由。

---

## 5. 需要作者明确澄清的事实性问题

1. **`HYPERAESTHESIA` 的"概念承载"依据是什么，能否给出任何可核验的边界？** 具体地：作者认为 8 161 份 FAERS 报告与 523 行加拿大记录中，有多大比例来自 LLT *Hyperalgesia* 语义、多大比例来自普通"感觉过敏"语义？我在 `cv/cvponline_extract_20241130/reactions.txt` 逐列拆解后确认该 extract 的字段为 `report_id | reaction_seq | duration_value | duration_unit_EN | duration_unit_FR | PT_EN | PT_FR | SOC_EN | SOC_FR | release`——**只有 PT，没有 LLT**，抽样 100 000 行中字段 3–5 仅 2 行非空且均为 duration。因此该比例在现有数据中不可分解。请说明作者是否同意这一判断，以及若同意，Table S4 中 "preferred term carrying the hyperalgesia concept" 这一描述的依据与边界是什么。

2. **2024 年那 8 份瑞芬太尼 HYPERAESTHESIA 报告是否相互独立？** 请给出这 8 份报告的 `primaryid`/`receivedate` 分布、报告国、是否带文献引用标记、是否共享同一生产企业或同一批伴随用药。理由是：作者自己引用了 Han 2024（DOI 10.1139/cjpp-2024-0078）与 Janiczak 2025（DOI 10.1007/s40264-025-01560-7）讨论 FAERS 重复报告问题；若这 8 份中有一部分是重复个案或同一文献簇，则合并信号将由 a = 10 降至 a = 2，整个"改正后主发现"随之消失。若作者无法从 openFDA 聚合接口获取，请明确写出这一不可核查性。

3. **每报告的报告完备度是多少？** 请给出作者所信任的前瞻性文献中"高剂量瑞芬太尼后临床可测痛觉过敏"的比例，并据此换算在 5 375 份 FAERS 报告下的期望报告数。稿件从未给出这个换算，因此读者无法判断"a = 10"是提示"事件罕见"还是"报告系统天花板"。这是判断本稿结论方向的前提数字。

4. **为什么把场景匹配的对照药（舒芬太尼）只放在 Table S5？** 舒芬太尼是四药中唯一与瑞芬太尼同属纯静脉、纯手术室场景、且无口服/透皮剂型的对照（我核对 `02_route_stratified.csv:41-57`）。请作者说明：对 HYPERAESTHESIA，瑞芬 vs 舒芬 RORR = 0.549（0.26–1.16，区间含 1），而 PAIN 的 RORR = 0.281（0.18–0.44）；在"报告场景恒定"的比较中，瑞芬太尼的低报并非对所有术语一致（VOMITING 0.969、PRURITUS 1.310、PROCEDURAL PAIN 2.124 均高于 1）。作者如何解释这种非一致性，以及它是否动摇了"under-reporting that affects every other term"这一表述？

5. **作者是否接受"瑞芬太尼 OIH 负担本就更低"这一替代解释？若不接受，依据是什么？** 作者在 §4.3 用"无口服/透皮、超短半衰期"解释了 DRUG TOLERANCE 与 DRUG WITHDRAWAL SYNDROME 的低报告是药理性的；同一事实为何在 §4.4 对 HYPERAESTHESIA 被排除？请给出明确的判断，而不是留给读者推断。

6. **§3.9 的免疫系统信号，作者是否认为其量级可信？** 5 375 份瑞芬太尼报告中有 532 份编码为 ANAPHYLACTIC SHOCK（9.9%），对照芬太尼为 0.28%。作者自己的工作稿 `D_27SOC_openFDA事件级.md:89` 标注"不作因果解读"，但正文把它用作"分析能检出信号"的证据。请说明：若作者也认为该量级不可能是药物效应，那么它作为灵敏度正对照的资格从何而来？

7. **医师亚组 DRUG INEFFECTIVE 的格计数与 95% CI 是多少？** 瑞芬太尼加拿大队列中医师报告仅 19 份（`cv/cv_subgroups.csv:13`）。在该子集中得到 RORR 5.921 与 10.604 所依据的分子分母分别是什么，区间是否跨 1？

8. **`DRUG INEFFECTIVE` 的 SOC 归属是哪一条？** `03_soc_27.csv` 的启发式规则把它归入 Injury/poisoning/procedural（作者在 `D_27SOC_openFDA事件级.md:112` 自承此归法有误），而 `01_faers_results.csv:6` 标为 General。请确认正文引用的是哪一条映射链。

---

## 6. 我实际做的独立核查

**读过的文件（全文）**：`I_正文_IMRaD_en.md`、`ANALYSIS_PLAN.md`、`01_faers_results.csv`、`10_term_dictionary.csv`、`cv/cv_pt_summary.csv`、`cv/cv_drug_totals.csv`、`cv/cv_summary.md`、`cv/cv_subgroups.csv`、`cv/cv_soc_27.csv`、`04_sensitivity_ps_only.csv`、`04_sensitivity_year_pain.csv`、`04_sensitivity_year_hyperaesthesia.csv`、`04_sensitivity_leave2024_hyperaesthesia.csv`、`04_sensitivity_2024cluster_hyperaesthesia.csv`、`04_sensitivity_estimable_years.json`、`03_soc_27.csv`、`02_route_stratified.csv`、`_faers_cache.json`、`_probe_meddra_level.json`、`D_27SOC_openFDA事件级.md`。

**我跑过的核查与结果**

| 核查 | 方法 | 结果 |
|---|---|---|
| FAERS 全库与队列计数 | 解析 `_faers_cache.json` | 全库 20 692 687；瑞芬 5 375、芬太尼 121 819、舒芬太尼 6 513、吗啡 56 501；HYPERALGESIA 0；ALLODYNIA 1 110；HYPERAESTHESIA 8 161；PAIN 607 176 —— 与稿件 §3.1/§3.2 完全一致 |
| 18×4 的 ROR 全部重算 | 由 `01_faers_results.csv` 的 a + 队列数 + PT_total 重建 2×2（c = PT_total − a）| 与表 2 逐格三位小数一致：HYPERAESTHESIA 4.729 / 6.795 / 8.611 / 12.166；PAIN 0.142 / 2.138 / 0.505 / 3.083 等 |
| 全部 RORR 重算 | 同上 | 与表 2、表 S5 一致：HYPERAESTHESIA RORR 0.696（芬）/ 0.549（舒）/ 0.389（吗）；PAIN 0.066 / 0.281 / 0.046 |
| Bonferroni 下界 1.61 | exp(ln 4.729 − 3.396 × 0.31700) | 1.612 → 稿件"1.61"正确 |
| 2024 聚集性倍数 15.4 / 4.3 / 4.9 / 1.7 | `04_sensitivity_2024cluster_hyperaesthesia.csv` | 文件值为 15.41 / 4.30 / 4.90 / 1.71，一致 |
| 剔除 2024 后 a = 1、无信号 | `04_sensitivity_leave2024_hyperaesthesia.csv` | 瑞芬 a = 1、ROR 0.701（0.099–4.978）、signal_met NO，一致 |
| 2024 年 PT 层 ROR 72.856 | 用 `04_sensitivity_year_hyperaesthesia.csv` 的 a = 8 / 队列 448 / 年 PT 总数 337 重算 | 72.86，一致 |
| 严重报告亚组 | `04_sensitivity_ps_only.csv` | 瑞芬 PAIN RORR 0.072 / 0.044；HYPERAESTHESIA a = 10、ROR 4.309 —— 与表 4A 一致 |
| 加拿大队列与 PT 计数 | `cv_pt_summary.csv`、`cv_drug_totals.csv`、`cv_subgroups.csv`、`cv_soc_27.csv` | 与表 1、表 3、表 S1、表 S3 全部一致（瑞芬 HYPERAESTHESIA 0、PAIN 2；严重 102/111 = 91.89%） |
| 每报告占比（我自己算的新量） | a / 队列 | HYPERAESTHESIA 1/538（瑞芬）、1/387（芬）、1/296（舒）、1/216（吗）；ALLODYNIA 1/5 375（瑞芬）|
| **加拿大库原始表字段结构** | 逐行拆分 `reactions.txt`（10 列，`$` 分隔） | 字段为 report_id / reaction_seq / **duration_value / duration_unit_EN / duration_unit_FR** / PT_EN / PT_FR / SOC_EN / SOC_FR / release —— **无 LLT**；抽样 100 000 行仅 2 行字段 3–5 非空，均为持续时间 |
| **加拿大库原始表术语检索** | `head -n 1000000` 后 `grep -c -F` | `Hyperalgesia` = **0**；`Hyperaesthesia` = 166；`Allodynia` = 4；`Neuralgia` = 264；`Burning sensation` = 1 522（前 100 万行样本，非全量）——部分独立证实稿件核心主张 |
| 途径分层 | `02_route_stratified.csv` | 瑞芬 IV 分层 PAIN RORR 0.077（vs 芬 IV）、0.038（vs 吗 IV）；瑞芬 oral 途径 1 134 条目、覆盖率 184.3%（→ 单位是药-条目而非报告）|
| 本地是否存在个案级 FAERS 数据 | `ls -laR ascii/` | `ascii/2024Q4/` 为空目录 → 稿件"无法做 suspect-role 限制与 TTO"的陈述无可查矛盾 |
| 词数合规 | 正则切分并计数 | 摘要 299 词（稿件称 300）；Introduction–Conclusion 3 994 词（含标题 129 词）；均在限内 |
| 长句定位 | 按分句切分取最长 | 摘要 Results 首句 **65 词**；§4.4 句 **61 词**；§2.3 句 49 词；§3.2 句 51 词 |

**我未能独立复现的部分（如实说明）**：加拿大库**全量**术语计数（HYPERAESTHESIA 523、ALLODYNIA 29、PAIN 49 260）我未能在本次会话内跑完全量 742 MB 扫描（全量 awk 在后台运行中未返回）；我只完成了前 100 万行样本的检索（Hyperalgesia 0、Hyperaesthesia 166）。因此 523 这一具体数值我**未能独立证实**，只能证实该字符串在表中存在且 `Hyperalgesia` 不被用作 PT。另：`CHRONIC PAIN` 的"相邻词查询命中 1 次"属 openFDA 在线查询结果，本地文件无法核验。

**我实际做的外部文献核对（WebSearch/WebFetch）**：核对了 Fletcher & Martinez 2014（PMID 24829420）摘要的效应量与结论方向；Rivosecchi 2014（PMID 24669819）摘要的 35/16/6 与"too small to require prevention"——**稿件转述正确**；Mauermann 2016（PMID 26655493，DOI 10.1097/ALN.0000000000000976）的效应量与"疼痛下降而痛觉过敏面积上升、allodynia 无差异（P = 0.682）"；Higgins 2019（PMID 30915985，DOI 10.1016/j.bja.2018.09.019）"pain detection thresholds 无证据、疼痛耐受有证据、OUD 人群更明显"；Adams 2023（PMID 37059626，DOI 10.1016/j.bja.2023.02.037）"consistently shown"的表述；Colvin 2019（PMID 30983591，DOI 10.1016/S0140-6736(19)30430-1）；Huang 2024（PMID 38218762，DOI 10.1186/s12871-023-02388-3）31 项 RCT / 2 019 例与 allodynia 合并；Koo 2017（BJA 119:1161–8）；Hirai & Uesawa 2023（PMID 38004407，DOI 10.3390/ph16111541）。

**我未发现的问题（同样计入审稿结论）**：稿件引用的 Rivosecchi 2014 数字与结论方向正确；表 2/表 3/表 4A–4C/表 S1/S3/S4/S5 与被引源文件之间未发现算术不符；队列数、PT 总数、SOC 面板、人口学面板全部可追溯一致；摘要与正文字数均在期刊限内。**唯一发现的表格级错误是 P2-1（`DRUG INEFFECTIVE` 在表 4A 被标为 `OIH-wide`）。**

---

## 7. 临床层面必改清单（按优先级）

| # | 必改项 | 具体动作（可直接执行） | 对应意见 |
|---|---|---|---|
| 1 | 撤销"HYPERAESTHESIA 承载 OIH 概念"这一代理定位，并把 `ALLODYNIA` 提升为并列主要终点 | 表 2/表 3/表 S4/图 1 的该行标签改为 `non-specific sensory term (exploratory)`；在 §2.3 增补"两个库都不暴露 LLT，该 PT 的语义成分不可分解；没有任何 PT 代表 OIH 这类综合征"；§3.3 用"ALLODYNIA 对瑞芬 a = 1，分析对瑞芬无信息量"开篇 | M1 |
| 2 | 把"报告行为"从唯一解释降为两个并列假说，并把场景匹配对照（舒芬太尼）提到正文 | 在表 2 与图 1 并列瑞芬 vs 舒芬的 RORR；§4.3/§4.4 改写为双假说段（含"无口服/透皮 → 无慢性暴露路径"与 Higgins 2019 的 OUD 证据）；§5 结论句改为方向可判断的表述 | M2 |
| 3 | 删除或反转 §3.9 的"灵敏度正对照" | 改写为"伪信号示例"（9.9% vs 0.28% 的过敏性休克、加拿大库中舒芬太尼免疫类占比更高、FAERS 队列角色不可区分）；§4.5 增补"该臂不承担灵敏度论证职能" | M3 |
| 4 | 补上表型层面的关键文献并修正证据定位 | 引 Mauermann 2016（痛觉下降而痛觉过敏面积上升、allodynia 不变）与 Koo 2017（纳洛酮降低痛觉过敏但不改变疼痛），替换 §2.3/§4.2 的裸断言；§1 中 Fletcher 补回"significant"与"mainly remifentanil"及效应量；§4.6 引用改为 [7, 8, 9, Huang 2024]；新增 Higgins 2019、Adams 2023、Colvin 2019、Huang 2024 四条 | P1-1、P1-2 |
| 5 | 让 §4.6 产生真实临床价值 | 加入"每 X 份报告出现 1 份该术语"表（瑞芬 1/538、芬太尼 1/387、舒芬太尼 1/296、吗啡 1/216；allodynia 瑞芬 1/5 375）+ 报告完备度数量级句 + "用临床名检索的既有 FAERS 分析必得零，应读作不可检索而非安心"这一推论 | P1-3 |
| 6 | 收敛新颖性主张并修正可读性硬伤 | §1 "has not been examined" 改为"术语可检索性尚未被核验"并引 Hirai 2023、Dai 2023；替换摘要 Results 首句（65 词）与 §4.4 自相矛盾句（61 词）；修正表 4A 的 `DRUG INEFFECTIVE` 分组标签、§4.5 的 21.1% 口径、§3.4 的医师亚组缺区间 | P1-4、P1-5、P2-1、P2-2、P2-3 |
