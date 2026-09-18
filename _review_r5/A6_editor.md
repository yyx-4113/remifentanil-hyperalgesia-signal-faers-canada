# Round-5 独立审稿 — A6_editor 资深编委（*Anaesthesia*）+ 报告规范（READUS-PV / RECORD / STROBE 类比）与可复现性审稿人

## 0. 审稿人身份与总体结论

**身份自述.** 麻醉学期刊资深编委与药物警戒报告规范审稿人，长期处理药物流行病学/药物警戒类原创研究，并负责核查投稿是否满足 *Anaesthesia* 现行作者指南与 READUS-PV、STROBE 类报告规范的逐条要求。本次以"第一次收到该投稿"的立场评审。

**Verdict: Major Revision（可保留 Original Article，但须满足 M1 所列的 4 项硬条件；若作者拒绝修正 M2，则应改为 Reject）。**

理由（具体到本稿）：

1. **贡献的真实内容小于稿件形式上的承诺.** §5 自陈"these findings do not establish whether hyperalgesia after remifentanil occurs"。整篇的实质增量是一句报告规范层面的警示——临床用词 HYPERALGESIA 不是 MedDRA 首选术语（PT），其父 PT 为 HYPERAESTHESIA——以及一次头对头负对照示范。这是真实但不大的方法学增量；能否够 *Anaesthesia* Original Article 的门槛，取决于作者是否肯把"报告设置（reporting setting）可以完全解释这一模式"这条**有数字支撑的正面结论**推到前台（见 M1）。
2. **稿件自称"a priori"与其自有分析计划相互矛盾，共 11 处.** `ANALYSIS_PLAN.md:5` 白纸黑字写着"This plan was written post hoc, once the data had been retrieved"，且代理术语是"看到 0 之后"加的（`ANALYSIS_PLAN.md:3`、:21–27）。稿件却反复用"defined a priori"。这不是措辞问题，是 READUS-PV 第 2b 条与期刊科研诚信条款下的可核查陈述。
3. **READUS-PV 自查表存在"声称已满足但正文没有"的情况.** 对照表 Part A 第 9 条写"Every estimate is given with a 95% confidence interval"，但 Table 3 的加拿大列、Table S1 两个面板、§3.7 全是**无区间**的点估计。这是本题最硬的一处不实陈述（详见 §1 M3）。
4. **本刊两条明文格式要求被违反.** 一是图内不得有 legend box（两图都有），二是补充材料"should be uploaded as separate documents and not included in the main document file"（S1/S3/S4/S5 整表嵌在正文文件里）。
5. **投稿信与稿件不一致（题名都不同）.** 投稿信题名结尾是"with negative controls defined a priori"，稿件题名结尾是"with a terminology caution"。这属于 triage 阶段就会被看见的错误。

---

## 1. 重大问题（Major, M1…）

### M1. 稿件类型裁断：可保留 Original Article，但必须补上四项，否则应改为 Science Letter 或方法学 Commentary

**【问题】** 按 *Anaesthesia* 编委的原创性/临床增量标准，本稿目前作为 Original Article 的贡献不足以支撑；其最有价值的发现是报告规范层面的，而稿件自己主动放弃了临床结论。

**【证据】**

- 本刊现行指南对 Original Article 的口径是正文字数与文献数（"Original articles should be between 3000–4000 words and contain up to 30–40 references"），并未单独规定"临床增量"门槛；门槛来自期刊定位："It publishes original, peer-reviewed articles on all aspects of general and regional anaesthesia... it publishes basic science papers if authors can demonstrate clinical relevance."（Guidance for Authors；Editorial Policies "Scope, aims"）。本稿没有任何临床建议（§1 末句："This study makes no clinical safety claim and issues no prevention recommendation"），§4.6 只说"decisions about prevention should rest on the prospective literature [7, 8]"。这意味着临床增量完全让渡给了已有文献。
- 真正的增量在 §4.4，且只有一句：术语决定答案，HYPERALGESIA 是 LLT 不是 PT。该事实（HYPERALGESIA 为 LLT、父 PT = HYPERAESTHESIA 10020568）本身是 MedDRA 的既有属性，不是本文的发现；本文的贡献是把"用临床用词检索必得 0"这件事**在两个国家级库上实证了一遍**，并给出负对照/probe 设计。这是合格的方法学短文，不是 4 000 词原创研究。
- 稿件唯一**有数字、稳定、可复现**的正面结论其实没有被当成主结论写：remifentanil 在所有非特异性术语上系统性地低报（PAIN，以及 4 个阴性对照中的绝大多数），而这一低报由报告来源构成解释——加拿大队列 91.9% 为 serious（`cv/cv_subgroups.csv:13`）、64.9% 来自"Other health professional"（`cv/cv_subgroups.csv:11`）。这正是审稿人/读者真正会用到的、关于**自发报告系统如何被围术期监护环境塑形**的结论，却被降格为 §3.6/§4.3 的解释段。
- 另需注意：本刊作者指南列出的常规栏目是 Editorials / Original articles / Reviews / Science Letters（≤800 词、≤8 文献、≤1 表 1 图）/ Correspondence（约 600 词）/ Case Reports（转投 *Anaesthesia Reports*）。本刊**没有**"Short Report"栏目，因此"降格"的实际落点是 Science Letter 或方法学 Commentary。

**【为什么重要】** 若以现状投 Original Article，最可能的结局是：编辑认可方法学价值但因"无临床结论 + 4 000 词"而不给送审，直接建议改投 Science Letter 或作为 Commentary——这是一种最浪费的拒稿方式（既不是内容错，也不是数据错）。反过来，如果作者按下面四条改写，它可以立住。

**【具体修改建议】** 维持 Original Article 必须补上以下四项，缺一即建议改栏目：

1. **把一个正面、有数字、非否定式的结论提到 Abstract/§5 的首句。** 直接可粘贴的英文句：
   > "In spontaneous reporting, remifentanil's apparent freedom from pain-related signals is explained by who reports it and in what setting, not by the drug: its reports came overwhelmingly from monitored perioperative care (91.9% serious; 64.9% from non-physician health professionals in Canada), and it under-reported four non-paradoxical opioid side effects by the same margin as the term of interest."
2. **新增一张表（Table 5）把这句变成可核查的量**：行 = 术语（PAIN + 4 个阴性对照 + HYPERAESTHESIA），列 = 瑞芬太尼 a、ROR（95% CI）、RORR vs 芬太尼（95% CI）、加拿大同项 RORR（95% CI）、**报告者类型构成（physician / other health professional / consumer 的百分比）**。第四列是当前表中唯一缺失、而恰恰是本文论证核心的变量。预期输出列名建议固定为：`PT, group, remi_a, remi_ROR, remi_ROR_95CI, RORR_vs_fentanyl, RORR_95CI, RORR_vs_morphine, RORR_95CI, CA_remi_RORR, CA_RORR_95CI, pct_serious, pct_physician, pct_other_HCP, pct_consumer`。
3. **把 ANALYSIS_PLAN.md 作为正式 Supplementary（Table S6 或 Appendix），不要仅以仓库文件名指代**，并据 M2 改写 a priori 措辞。
4. **把术语核查做成可复用的最小规范**（本文真正的卖点）：给出一段 5–10 行的"查询前必做"清单（先确认字符串是该库 reaction 字段里的 PT；再做 adjacent-token phrase 查询；再报数），并把它放进 §2.3 的方框/编号列表。这才对得起标题里的 "terminology caution"，也才值得 4 000 词。

---

### M2. 全稿 "defined a priori" 的表述与作者自有分析计划相互矛盾（11 处），构成可核查的不实陈述

**【问题】** 稿件反复声明结局术语、阴性对照与 probe 是"a priori"定义的；但随稿归档的分析计划自陈是**数据取出之后**写的，且承载核心结果的 5 个代理术语是**看到 0 之后**追加的。

**【证据】**

- `ANALYSIS_PLAN.md:5`："**Prospective registration:** **none.** This plan was written post hoc, once the data had been retrieved..."
- `ANALYSIS_PLAN.md:3`："finalised 16 September 2026, *after* data extraction (16 September 2026)"；而 `I_正文_IMRaD_en.md:51` 记载 FAERS 抽取日期也是 16 September 2026 —— 抽取与"计划定稿"同日。
- `ANALYSIS_PLAN.md:21–27`（Amendment 1）明确：five dictionary proxies "added on 16 September 2026, **after those zeros**"；稿件 §2.3（`I_正文_IMRaD_en.md:67`）自己也这么写："were added on 16 September 2026, after those zeros, and analysed on the same footing... they are reported as additions rather than a priori outcomes"。
- 稿件中 "a priori" 出现 **11 次**（我逐处计数）：标题页后的正文 §1:41、§2.3:65、§2.3:71、§2.4（间接）、§3.3 表注、§4.4、Summary 2 次、Table 2 注、Table S2 注、Cover letter 1 次。
- 同时 `I_正文_IMRaD_en.md:49` 声明 "the study is reported in accordance with the READUS-PV recommendations [13, 14]"，而 READUS-PV Part A 第 2b 条明确区分"to assess a **pre-specified** hypothesis"与常规药物警戒目的，并要求说明理由。

**【为什么重要】** 这是**诚信层面**而非文风层面的问题。编辑只要点开随稿的 `ANALYSIS_PLAN.md`（作者自己放在仓库里并请审稿人查阅），就会读到"written post hoc"，再回头看正文 11 处 "a priori"，结论会是"作者对分析时序的描述不可靠"。一旦形成这个印象，稿件里所有其他"我们已经核查过"的强声明（30 条文献全部按标识符核实、每个数字都可追溯到源文件）都会被连带打折。这是本稿最容易被升级为 Reject 的单一风险点。必须强调：**当前写法反而低估了作者**——"0 之后补代理并如实标注"是诚实且值得表扬的做法，完全没有必要伪装成 a priori。

**【具体修改建议】**

1. 全稿统一替换。把 "defined a priori in a dated analytical plan" 改为：
   > "specified in a dated analysis plan that was written after data extraction and before the results were interpreted; the plan is archived with the analysis code and is supplied as Supporting Information (Appendix S1). The analysis was not prospectively registered."
2. 首次出现处（§2.3）加一句直陈：
   > "Because no prospective registration exists, we describe the term groups, negative controls and specificity probe as 'specified in the analysis plan' rather than 'pre-specified'; the five dictionary proxies were added after the zero counts had been observed and are labelled as such throughout."
3. 把 Table 2 表注里 "terms defined a priori" 改成 "terms specified in the analysis plan (see Table S2, item 2b)"。
4. 同步修改 `ANALYSIS_PLAN.md:36`（"Terminology note — a priori vs pre-specified"）与投稿信（`I_投稿信_cover_letter.md:20` 同样写了 "defined a priori"），三处口径必须一致。
5. **不要**删掉 Amendment 1；它现在是稿件最可信的部分。

---

### M3. READUS-PV 依从性的真实性抽查：自查表 Part A 第 9 条声称"每个估计都有 95% CI"，正文与表格均不成立

**【问题】** 检查表对第 9 条（README 要求"Present all results including confidence intervals"）声明已满足，实际有至少三处结果只给点估计、无置信区间。

**【证据】**（我按"随机抽 6 条"的要求抽了 6 条，含 2 条声明 not applicable、≥2 条声明 addressed in §X；本条为其中之一）

- `I_TableS2_READUS-PV_checklist.md:39`（Part A 第 9 条）："Every estimate is given with a 95% confidence interval; terms that could not be estimated are shown as not estimable rather than as zero."
- 反证 1：`I_正文_IMRaD_en.md:290–294` Table 3 的加拿大列。列头是 "Canada remifentanil a | Canada RORR vs fentanyl / vs morphine"，单元格值形如 `2 | 0.235 / 0.146`、`25 | 1.277 / 1.703`。**全部为无区间的点估计**，而 FAERS 列（0.066 / 0.046）同表也是无区间。
- 反证 2：`I_正文_IMRaD_en.md:374–434` Table S1 两个面板的 `ROR`、`RORR vs fentanyl`、`RORR vs morphine` 三列共 27×2×3 = 162 个估计，**无一个带区间**。
- 反证 3：`I_正文_IMRaD_en.md:131` §3.7："remifentanil showed elevated ratios in pregnancy, respiratory, immune (2.363; 1.792 versus fentanyl), cardiac and vascular classes" —— 无区间。加拿大队列 n = 111，其中 Immune 仅 9 例（`cv/cv_soc_27.csv`），点估计必须配区间才有意义。
- 反证 4：`I_正文_IMRaD_en.md:117` §3.4 引用 prune。PRURITUS vs sufentanil 记载为 "1.310, 0.84–2.04"（有区间，正确）；但同段 DRUG INEFFECTIVE 的加拿大反转 "1.277 / 1.703" 无区间。
- 反证 5：`I_正文_IMRaD_en.md:119` §3.4 医生-only 分析 "5.921 and 10.604" 无区间，而这是在 n=111 队列里进一步按报告者类型切分后的结果（`cv/cv_pt_summary.csv` 列 `REMI_RORR_FEN_phys`、`REMI_RORR_MOR_phys`），单元格会非常小。

**【为什么重要】** READUS-PV 第 9 条存在的理由正是防止"用点估计掩盖不精确性"。本文全部加拿大结论都建立在 111 份报告上，免疫类只有 9 例、PAIN 只有 2 例；把 `2 → 0.235` 这样由 2 例支撑的比率不带区间地印在 Table 3 里，等于让读者按无信息量的精度去读它。审稿人一旦发现自查表在此处不实，会连带怀疑 Part A 其余 31 条的完成质量——而检查表正是本稿声称的规范合规证据。

**【具体修改建议】**

1. Table 3 每个加拿大 RORR 后补 95% CI，并把 FAERS 列也补齐（数据源已有，`cv/cv_pt_summary.csv` 有 `REMI_ROR` 与两组 RORR 的分子分母，2×2 可重建）。列头改为：`Canada remifentanil a | Canada RORR vs fentanyl (95% CI) | Canada RORR vs morphine (95% CI)`。
2. Table S1 的估计列全部改成 `value (95% CI)`；若区间过宽到无意义，就写 `not estimable`，不要只印点估计。
3. §3.4 与 §3.9 的每个比率后补区间；§3.9 的 `anaphylactic shock (532 events) and reaction (367)` 至少给出这 532 与 367 各自的分母（瑞芬太尼 5 375）。
4. 把自查表第 9 条的措辞改成可核实的版本：
   > "All estimates reported in Tables 2, 4A–4C, S5 and Figures 1–2 are given with 95% confidence intervals; point estimates without intervals appear in Table 3 (Canada column) and Table S1 and are labelled 'not estimable' where the interval could not be computed."
5. 若作者不愿补，则把 Table 3/S1 所有无区间项明确标注 `point estimate only; 95% CI not computed`，并同步修改自查表——**但不能两种版本同时存在**。

---

### M4. 图件违反本刊明文要求：两张图内都有 legend box；且 Figure 1 图注的分组方向与图相反

**【问题】** 本刊明文禁止图内有 legend box；两图均使用图内图例。另外 Figure 1 图注写"Terms are grouped from the top"，而实际排列是倒过来的。

**【证据】**

- 本刊指南原文（Guidance for Authors，图件部分）："There should be no titles, plot frames, gridlines or legend boxes within the graphs, and symbols and error bars should be explained in the caption."
- `I_fig1_rorr_forest.png`（4251×3960，600 ppi，789 852 B）：左上角有含 3 行文字的点型图例框（"Remifentanil vs fentanyl / vs sufentanil / vs morphine"）。
- `I_fig2_year_trend.png`（4251×2130，600 ppi，470 066 B）：左下角有含 3 行文字的图例框（含 "Pooled RORR (whole corpus)"）。
- 生成代码确认这是刻意的：`05_figures.py:170` `ax.legend(handles=handles, loc="upper left", frameon=False, ...)`、`05_figures.py:221` `ax.legend(handles=[h1, h2, h3], loc="lower left", frameon=False, ...)`。`frameon=False` 只去掉了图例的边框，**并没有去掉图例本身**，不符合"no legend boxes within the graphs"。
- 图注方向错误：`I_正文_IMRaD_en.md:522` 写 "Terms are grouped **from the top**: the preferred term carrying the hyperalgesia concept (HYPERAESTHESIA) and the two nearest retrievable siblings (PROCEDURAL PAIN, DRUG WITHDRAWAL SYNDROME); the pragmatic proxy PAIN; the four negative controls...; and the specificity probe DRUG INEFFECTIVE." 但 `05_figures.py:93–103` 的 `SHOWN` 顺序配合 `yi = ROW * i`（:143）与 `ax.set_ylim(-1.0, ROW*len(data)-0.4)`（:158）使 HYPERAESTHESIA 落在**最下**、DRUG INEFFECTIVE 落在**最上**；我在渲染文件中逐一核对，自上而下确为 DRUG INEFFECTIVE → CONSTIPATION → PRURITUS → VOMITING → NAUSEA → PAIN → DRUG WITHDRAWAL SYND. → PROCEDURAL PAIN → HYPERAESTHESIA。因此应写 "from the bottom"。
- 已核查**无问题**的部分（一并记录，避免作者过度修改）：两图均无图内标题、无网格线（`05_figures.py:64` `ax.grid(False)`）、无完整绘图边框（Fig 1 仅保留 bottom 脊线，`clean_axes(ax, keep=("bottom",))` :162；Fig 2 保留 left+bottom，:216——这是坐标轴而非"plot frame"）；图注确实解释了 symbol 与误差线；分辨率 600 ppi（实测 599.9988）、文件 771 KB / 459 KB，均满足 600 ppi 与 ≤10 MB。

**【为什么重要】** 这是**编辑办公室在送审前就会拦下**的硬性格式条文，属于最容易避免、也最不该出现的失分点。图注方向写反则是更糟的一类问题：它说明图注未经与图件对照，会直接侵蚀读者对"每个数字都核对过"这一整套声明（作者在 AI 声明与投稿信中反复强调）的信任。

**【具体修改建议】**

1. 删除两图的图内图例：
   ```python
   # 05_figures.py —— 两处 ax.legend(...) 整行删除
   ```
   同时把符号说明完整写进图注。Figure 1 图注改写（可粘贴）：
   > "Points are ratios of reporting odds ratios for each preferred term analysed, with 95% confidence intervals; the x axis is logarithmic. Filled circles, remifentanil versus fentanyl; open squares, remifentanil versus morphine; open triangles, remifentanil versus sufentanil. The dashed vertical line marks a ratio of 1."
   Figure 2 图注改写（可粘贴）：
   > "Filled circles, remifentanil versus fentanyl; open squares, remifentanil versus morphine; the two horizontal dotted lines are the pooled whole-corpus values (0.066 versus fentanyl, upper; 0.046 versus morphine, lower); the dashed line marks a ratio of 1."
2. 修正方向词：把 "Terms are grouped from the top" 改为 "Terms are grouped from the bottom"，或改为中性表述 "Terms are ordered, from the bottom of the panel: ..."。
3. 投稿只上传 `.tif`（或 `.pdf`）——本刊可接受的图件格式是 ".pdf, .jpg, .tiff or .pptx"，**`.png` 不在其列**，不要随稿附 PNG。

---

### M5. 补充材料整表嵌在正文文件里，违反本刊明文要求，且与投稿信自相矛盾

**【问题】** 本刊要求补充材料作为独立文件上传、不得放进正文文件；本稿把 Table S1、S3、S4、S5 的**全部表格内容**写在了正文文件里，只有 S2 单独成文件；而投稿信却说五张补充表都在一个独立的 Supporting Information 文件里。

**【证据】**

- 本刊指南原文："Additional material ... should be **uploaded as separate documents and not included in the main document file**. Please refer to all supporting information in the manuscript as online Supporting Information Table S1, online Supporting Information Figure S1, etc. **The captions for supporting information should be listed at the very end of your submission** AND included in each supporting information file." 以及 "The elements should be in separate files – i.e. **all supporting tables in one file**, all supporting figures in another and all appendices in another."
- 稿件现状：`I_正文_IMRaD_en.md:368–434`（Table S1 两面板，27×2 行数据）、`:442–460`（Table S3）、`:462–487`（Table S4，18 行）、`:491–516`（Table S5，18 行）全部内嵌于正文文件；只有 `I_TableS2_READUS-PV_checklist.md` 是独立文件。
- 投稿信 `I_投稿信_cover_letter.md:26`："the five supplementary tables, including the READUS-PV checklist and the complete head-to-head matrix, are in a separate Supporting Information file." ——与文件实际内容不符。
- 另：`I_正文_IMRaD_en.md:370`（S1 题注）、`:436`、`:487` 中的正文把 S1 当作正文内容引用（"Full class-by-class values are in Table S1."，`:131`），需要按"online Supporting Information Table S1"的命名规范统一。

**【为什么重要】** 一来违反明文包装要求，二来投稿信对包装的描述与实物不符——编辑在核对投稿信时会认为作者没有检查过自己的文件包。这类问题不会导致拒稿，但会消耗信任额度，而本稿正需要把信任额度用在 M1/M2 上。

**【具体修改建议】**

1. 新建一个文件 `Supporting_Information.docx`，把 Table S1–S5 **及** READUS-PV checklist（S2）按 S1…S5 顺序放入同一文件；正文文件中只保留 S1–S5 的题注（放在 References 之后，与主表题注一起），并按指南改成 "online Supporting Information Table S1" 的写法。
2. 若坚持 S2 独立成文件，则必须改写投稿信，使其与实际文件包一致。
3. 题注（可粘贴）：
   > "**online Supporting Information Table S2.** Completed READUS-PV checklist for this analysis, mapping each recommendation for the manuscript body and for the abstract to the section of this manuscript in which it is addressed, with an explicit note on the items that are not applicable (case-by-case analysis; protocol registration)."

---

### M6. 投稿信与稿件存在四处实质不一致，其中题名不同

**【问题】** 投稿信中的题名与稿件题名不同；另有三处事实性描述在稿件中不成立。

**【证据】**

- 题名不一致：`I_投稿信_cover_letter.md:10` 为 "...: a head-to-head disproportionality study with **negative controls defined a priori**"；`I_正文_IMRaD_en.md:1` 为 "...: a head-to-head disproportionality study with **a terminology caution**"。两者相差整个副标题。
- 表数不一致：投稿信 `:26` 与稿件 `:13` 均称 "four tables (Table 4 in three panels)"。但正文文件中带独立题注的展示表实为 **6 张**：Table 1、Table 2、Table 3、Table 4A、Table 4B、Table 4C（`I_正文_IMRaD_en.md:254, :263, :288, :309, :334, :351`）。4A/4B/4C 的列结构彼此不同（分别为 7/7/7 列但字段集不同，4B 给 fentanyl 与 morphine 的 OR、4C 给 fentanyl 与 morphine 的 a），不构成同一张表的面板。投稿信与封面声明的数字都是错的。
- 年份数不一致：投稿信 `:16` 称 PAIN 的结果 "in the same direction... across **ten** calendar years"；稿件 Table 4B 注（`:349`）与 §3.4（`:117`）均只能估计 **8** 年（2018、2019 年瑞芬太尼无 PAIN 报告，`04_sensitivity_year_pain.csv` 中该两年对应单元格为空），§3.8（`:135`）也写 "eight estimable years"。
- SI 位置不一致：见 M5。

**【为什么重要】** 题名不一致是投稿三分钟内必然被发现的错误，且会让编辑怀疑投稿信是套模板生成的（尤其本稿是第一作者单作者投稿，反而更容易被解读为"没有亲自通读"）。"ten years"的夸大也会被统计审稿人当作精度夸大的证据。

**【具体修改建议】**

1. 投稿信题名与稿件题名逐字一致；若采纳 M1 的新题名建议，两边同步。
2. 投稿信中改为："four main tables (Table 4 given as three separate panels, 4A–4C) and five online Supporting Information tables"。
3. 投稿信中改为："in the same direction in the eight calendar years in which an estimate was possible"。
4. 按 M5 统一 SI 描述。

---

## 2. 重要问题（P1-1…）

### P1-1. READUS-PV 自查表的"定位列"普遍不准（抽查 6 条中 3 条指向错误章节）

**【问题】** 检查表把若干条目的满足位置指到了不含该内容的章节；作者若按此自查会以为已完成。

**【证据】**（随机抽 6 条，含 2 条 not applicable、4 条 addressed in §X）

1. **Part A 第 11 条（抽查项，声明 addressed）**——`I_TableS2_READUS-PV_checklist.md:42` 声明 "the immune-class finding is explicitly designated a sensitivity control rather than an emerging signal (§3.9, §4.5)"。§3.9（`I_正文_IMRaD_en.md:139–141`）确实称其为 "post hoc, exploratory sanity check"，**但 §4.5（:169–181）通篇未提免疫类发现**；§4.5 的六个小标题依次为 spontaneous reporting、openFDA case-level、de-duplication、heuristic mapping、setting、geographic independence。**指向 §4.5 的一半不成立。**
2. **Part A 第 12c 条（抽查项，声明 addressed）**——`checklist:45` 声明 "§4.6: prospective studies with quantitative sensory testing remain the appropriate design"。§4.6（:183–187）只有"对临床医生"和"对药物警戒"两段，**没有提出后续研究设计**；该句实际在 §4.5（:171）。
3. **Part A 第 7c 条（附带核对）**——`checklist:33` 声明 "§2.4 (the reference set restricted correspondingly in the serious-report analysis)"。§2.4（:73–77）只讲 2×2、信号标准与 RORR 的 Woolf 区间，**不含任何受限分析的描述**；该内容在 §2.6（:87）。
4. **Part A 第 7d 条（抽查项，声明 not performed）**——`checklist:34` 与笔记 `checklist:75` 声明未做 case-by-case 分析、理由是案例级 FDA 文件不可获取。正文核对：全文无任何个案审查内容，§2.3（:67）与 §4.5（:173）分别说明 openFDA 未去重、案例级文件不可获取。**此条经核查无问题**（唯一瑕疵：主表 7d 行指"§4.5"而笔记第 1 条指"§4.6"，两处不一致，§4.6 不含该内容）。
5. **Part A 第 10 条（抽查项，声明 not performed）**——`checklist:40`："Not performed (see item 7d)"。正文无个案分析结果。**经核查无问题。**
6. **Part B 第 2e 条（抽查项，声明 not applicable）**——`checklist:65`："Not performed, so none is described in the Summary"。Summary（`I_正文_IMRaD_en.md:19–27`）确实不含 case-by-case 描述。**经核查无问题。**
7. **Part A 第 9 条（抽查项，声明 addressed）**——见 M3，**不成立**。

小结：抽 6 条中，**2 条（第 9、第 11 条）声明与正文不符，1 条（第 12c）定位错误，1 条（第 7c）附带定位错误**；2 条 not applicable 与 1 条 not performed 属实。

**【为什么重要】** READUS-PV 检查表在投稿中的功能是"作者已经逐条核过"的担保。若 6 条里 3 条定位不实，编辑会合理推断整张表是形式化填写的，从而**不再把该表当作合规证据**——这会同时削弱 M3 的补正空间（作者本来就靠这张表主张合规）。

**【具体修改建议】**

1. 第 11 条改为："`§3.9` (the immune-class analysis is explicitly designated a post hoc, exploratory sensitivity check rather than an emerging signal)". 若希望保留 §4.5 指向，则在 §4.5 新增一句：
   > "The immune-class excess (§3.9) is reported as a post hoc sensitivity check on the pipeline, not as an emerging safety signal."
2. 第 12c 条改为 "§4.5, last paragraph of the limitations" 或把该句从 §4.5 移入 §4.6。
3. 第 7c 条把 "§2.4" 改为 "§2.6"。
4. 修正 `checklist:75` 笔记第 1 条的 "§4.6" → "§4.5"。
5. 建议对整张表做一次机械性核验：把每条定位串（§x.y）在正文中检索，确认该串确实出现在被指向的小节内再定稿。

---

### P1-2. AI 使用声明不完整，且与"每个数字都由归档脚本直接读出"的绝对表述存在张力（Figure 2 数值为硬编码）

**【问题】** 声明的**位置**（Acknowledgements）合规，但**内容要素**缺三项，且其中一句与仓库代码实况冲突。原任务设问中"是否需要单独声明、是否允许用于语言润色/代码、是否要在 cover letter 复述"，逐条核查结果如下。

**【证据】**（先给本刊/Wiley 的现行要求，再对照稿件）

- 本刊作者指南页面**完全没有** AI 条款（我在 guidance for authors 全文检索 "artificial intelligence"/"AI"/"ChatGPT"，零命中）。本刊现行的 AI 要求来自两个上位文本：
  - *Anaesthesia*/*Anaesthesia Reports* 编辑们的立场声明（Wiles 等，DOI 10.1111/anae.16071）："artificial intelligence systems do not meet the criteria for authorship"；"Whilst artificial intelligence may be used to support the process of writing a paper, it should not be used as the primary source of text, figures, images or graphics"；"The authors remain fully responsible for any and all information submitted to the journal... Failure to do so, or to declare artificial intelligence use as a primary source of data, will be treated as scientific misconduct and managed accordingly."
  - Wiley Best Practice Guidelines（稿件自己引用的就是这一份）："If an author has used AI Technology to substantially edit, develop, or translate any part of a manuscript, its use must be described transparently and integrated into the manuscript"；"Tools used solely for spelling, grammar, and general editing are not included in these disclosure requirements"；AI "may be used for creating data visualizations and illustrations"。Wiley 的若干期刊版模板进一步要求投稿时的 AI Use Declaration 逐项写明："**Which tools were used, including names and version**；**Date of use**；How the tool(s) were applied...；How you validated the AI outputs for accuracy；How privacy and compliance requirements were maintained for sensitive, proprietary, or human subject data"。
- 逐条判断稿件（`I_正文_IMRaD_en.md:211` 的 "Use of generative artificial intelligence" 段）：
  - **单独声明？** 不需要。Wiley 只要求写在 Methods 或 Acknowledgements；本刊立场声明也未要求独立声明节。稿件写在 Acknowledgements，**合规（PASS）**。
  - **是否允许用于语言润色？** 允许，且"spelling, grammar and general editing"本可豁免声明；稿件主动声明了，属于**多报（合规）**。
  - **是否允许用于代码？** 允许。"creating data visualizations and illustrations"与"substantially edit, develop"均在被允许/须声明之列。稿件已声明，**合规（PASS）**。
  - **是否要求在 cover letter 复述？** 不要求。但作者已在 cover letter 复述（`I_投稿信_cover_letter.md:24`），**不构成问题**。
  - **工具名与版本：缺失（FAIL）**。稿件只写 "Large language model assistants, accessed through a desktop AI agent environment (WorkBuddy, which routes each request to one of several commercial large language models)"。"one of several commercial large language models"无法满足"names and version"。
  - **使用日期：缺失（FAIL）**。全文只有数据抽取日与作图日的间接线索（python 3.13.14 / matplotlib 3.11.1），无 AI 使用日期。
  - **隐私与合规：缺失（FAIL）**。声明未说明是否向第三方模型输入过未公开内容（本文数据均为公开库，风险低，但需要一句明确否定）。
  - **验证方式：部分给出（PASS with caveat）**。"any candidate citation that did not resolve to a real bibliographic record being discarded, with all 30 cited references verified by identifier"与"Every reported value is a direct read of the analysis output files by the archived scripts"。
  - **与代码实况冲突（FAIL）**：`05_figures.py:179–185` 中 Figure 2 的全部数值是**手写常量**——
    ```python
    fen = [(0.093, 0.02, 0.37), (0.039, 0.01, 0.28), (0.051, 0.01, 0.36), None, None,
           (0.044, 0.01, 0.18), (0.014, 0.00, 0.10), (0.016, 0.00, 0.11),
           (0.112, 0.03, 0.45), (0.168, 0.05, 0.53)]
    mor = [...]  # 同样为手写
    overall_fen, overall_mor = 0.066, 0.046
    ```
    我逐个与 `04_sensitivity_year_pain.csv` 比对：8+8 个点估计与 8+8 组区间、以及两条 pooled 参考线（0.066 / 0.046）**目前全部正确**。但它们不是"运行期从源文件读出"，而是人工转录。Figure 1 则是真读源文件（`05_figures.py:113–114` 读 `01_faers_results.csv`）。此外 `_check_consistency.py:111–117` 只把 CSV 的 min/max 与字面常量比对，**并不比对 `05_figures.py` 里的常量**。
  - **"30 条文献全部按标识符核实过"是否需要附证据？** 期刊不要求。但这是可核查的强声明，编辑很可能会抽查。我抽了 3 条：DOI 10.1007/s40264-024-01421-9（ref 13）解析为 Drug Safety 47: 575–584、标题一致，**通过**；DOI 10.1007/s40264-025-01560-7（ref 29）解析为 Drug Safety 48: 1119–1126，**通过**；DOI 10.1007/s40264-019-00899-y（ref 30）解析为 Drug Safety 43: 351–362，**通过**。标识符层面声明属实。

**【为什么重要】** 本刊立场声明把"declare artificial intelligence use"与"科学性不端"直接挂钩。缺工具名与版本是**形式不合规**；而"每个数字由归档脚本直接读出"与 Figure 2 手写常量并列，一旦被较真的审稿人发现，性质就变成"声明与实物不符"。这正是本题问的"过度披露反过来损害可信度"的具体机制：**不是因为披露太多，而是因为披露的强度超过了可验证的强度。**

**【具体修改建议】**

1. 补齐三个缺失要素（可粘贴替换整段首句，或作为 (i)–(vi) 列表续写）：
   > "Large language model assistants were used through a desktop AI agent environment (WorkBuddy) between 12 and 17 September 2026; the underlying models were Anthropic Claude and OpenAI GPT-series models [填实际所用模型与版本], accessed as a commercial API. No unpublished, proprietary, patient-identifiable or otherwise restricted content was entered into any AI tool at any stage: every input was either publicly available source data or the author's own draft text."
2. 把 (iv) 的文献声明改为可验证的表述，并把核验记录放进仓库：
   > "Every one of the 30 cited references was retrieved by its DOI or PMID and its bibliographic record checked against Crossref and the publisher record; the machine-readable verification record (identifier, resolver, date, resolution status) is archived with the analysis code as `refs_verification.csv`."
3. 二选一消除 Figure 2 的矛盾（推荐前者）：把 `05_figures.py` 的 Figure 2 改为运行期读取 `04_sensitivity_year_pain.csv`（与该文件其余部分一致）；或把声明里的 "Every reported value is a direct read of the analysis output files by the archived scripts" 改为
   > "Every value in the tables is a direct read of the analysis output files by the archived scripts; the values plotted in Figure 2 were transcribed from `04_sensitivity_year_pain.csv` and are re-checked against it by the consistency script."
4. (ii) 与 "no AI tool was used to create, alter or manipulate the figures" 并列易被误读，建议合并为一句：
   > "AI assistance was limited to writing the plotting code; the figures themselves were produced by executing that code on the analysis output, and no AI tool generated, retouched or altered any plotted value or image."

---

### P1-3. 数据可用性声明的可核查性：仓库可访问但未版本化；OGL-Canada 兼容性需明说；缺检索式

**【问题】** 声明本身合规范式，但作为可复现性承诺缺三个要素：版本定位、授权兼容性表述、检索语句。

**【证据】**

- **仓库 URL 可访问（经核查通过）**：以 GitHub REST API 查询 `https://api.github.com/repos/yyx-4113/remifentanil-hyperalgesia-signal-faers-canada`，返回 `private: false`、`visibility: "public"`、`license: MIT`、`default_branch: "main"`、`created_at: 2026-09-16T10:36:01Z`、`pushed_at: 2026-09-17T13:19:04Z`。`/releases` 返回五个版本：v1.0.0（2026-09-16T10:42:02Z，results-bundle.zip 789 134 B）到 **v1.4.0**（2026-09-17T13:19:37Z，results-bundle.zip 1 023 056 B）。**因此不存在"URL 打不开"的问题**；此项判定为 PASS。
- **但正文没有给出任何版本锚点**。`I_正文_IMRaD_en.md:209` 只给仓库 URL，既无 tag、也无 commit 哈希、也无 release 版本。而稿件内部 §10（:555）声称 "with tag `v1.0.0`"，仓库当前最新版本却是 **v1.4.0**——声明的指向与实际不一致，读者无法知道该复现哪一版。
- **"permanently available" 过强**。`:209` 与投稿信 `:22` 均写 "permanently available at the study repository"。GitHub 公共仓库可被删除或改私有，不构成"permanent"。期刊要求的是"statement on data availability"，不是永久性承诺。
- **"Neither raw dataset is redistributed" 与 OGL-Canada 的兼容性**：**不冲突**。Open Government Licence – Canada 允许再分发（含商业用途），要求署名并保留许可信息；**不再分发是比重分发更严格的做法，完全在许可范围内**（`I_正文_IMRaD_en.md:91` 也已正确声明"the Canada Vigilance extract under the Open Government Licence – Canada"并给出署名来源）。需要补的不是合法性，而是**说清哪些内容被分发**：仓库里有派生的加拿大逐 PT 计数（`cv/cv_pt_summary.csv`）与逐 SOC 计数（`cv/cv_soc_27.csv`），这些是派生数据，应当明确声明其可再分发性，否则 "Neither raw dataset is redistributed" 会被读成"什么都不共享"。
- **检索式：稿件给了日期，未给检索语句。** READUS-PV（按稿件自己复现的条目文本）第 5b 条要求 "Specify the **extraction dates** and describe and justify all choices used for data pre-processing"；稿件在 `:51`、`:53` 给了两个抽取日期（16 September 2026）与预处理理由，**满足 5b**。但 READUS-PV 要求的是可复现的最小信息集，而**具体检索语句确实缺失**：`:51` 只给了端点 `https://api.fda.gov/drug/event.json`，`:59` 给了字段名与取值列表（`patient.drug.activesubstance.activesubstancename.exact`，`("REMIFENTANIL" "REMIFENTANIL HYDROCHLORIDE")` 等），但没有给出任何一条可粘贴执行的 openFDA `search=` 表达式；加拿大侧同样只给了匹配规则（`name == target OR name.startswith(target + " ")`，`:61`）而无实际执行语句或行数统计。同样地，`10_term_dictionary.csv` 的"adjacent-token phrase query"（Table S4 第三列）代表什么具体查询也未说明。

**【为什么重要】** 本文的核心可推广主张是"术语可检索性核查"，读者最需要的恰恰是**能照着做的检索语句**。缺了它，本文的方法学贡献就停留在"我们查过"，而不是"你可以这样查"——这对一篇以方法学为卖点的稿件是实质性削弱。版本缺失则使"可复现"停留在口号层面。

**【具体修改建议】**

1. 数据可用性声明改为（可粘贴）：
   > "The analysis code, the analysis plan, the number-to-source traceability table and all derived result files are available at `https://github.com/yyx-4113/remifentanil-hyperalgesia-signal-faers-canada` (tag `v1.4.0`, `results-bundle.zip`); the version archived with this manuscript is tag `v1.4.0`, commit `[hash]`. Neither raw source dataset is redistributed; the derived counts that are redistributed contain no individual case information. Source data: United States Food and Drug Administration, openFDA drug/event data (`https://api.fda.gov/drug/event.json`, accessed 16 September 2026); Health Canada, Canada Vigilance Adverse Reaction Online Database, adverse reactions line-listing extract `extract_extrait.zip`, Open Government Licence – Canada (`https://open.canada.ca/data/en/dataset/...`, accessed 16 September 2026)."
2. 新增 **online Supporting Information Table S6：Search and extraction log**，列名固定为 `source, endpoint_or_file, exact_query_or_filter, fields_or_columns, date_executed, returned_n, note`，把 openFDA 的完整 `search=` 表达式（含 cohort 的每个取值、term 的每个字符串、adjacent-token 查询的写法）与加拿大的匹配规则、行数全部写入。
3. 把 §2.3 的 adjacent-token 查询用一句英文定义清楚，例如："Adjacent-token phrase query: the two tokens were submitted as a space-separated phrase to the openFDA `count` endpoint on `patient.reaction.reactionmeddrapt.exact`, so a match is returned whenever the phrase occurs anywhere in a stored preferred term, even if the term is longer than the phrase."
4. 删去"permanently"，改为"available at"。

---

### P1-4. Summary 的"无缩写"要求：未出现 FAERS/ROR/CI，但出现了未定义符号 `a = 1` 与未解释的 "preferred term"

**【问题】** 任务设问假定摘要里出现了 FAERS、ROR、CI 等缩写。**我逐词核对后确认：这些缩写并未出现**（这是需要更正的前提）。真正的问题是两个：一个未定义的 2×2 单元格符号，以及一个未向普通读者解释的专有概念。

**【证据】**

- 逐一检索 `I_正文_IMRaD_en.md:19–27`（Summary 全文）：`FAERS`、`ROR`、`RORR`、`CI`、`PT`、`MedDRA`、`OIH`、`FDA`、`US` **均无命中**。稿件把 FAERS 写全为 "the United States Food and Drug Administration Adverse Event Reporting System"，把 CI 写全为 "95% confidence interval"，把 ROR 写全为 "reporting odds ratios"。**在"无缩写"这一条上，实际是合规的（PASS）**，且做得比多数投稿更干净。
- 但 `:25` 有 "and disappears when 2024 is excluded (**a = 1**)"。"a" 是 §2.4 的 2×2 单元格命名（`:75` "a: drug and event"），Summary 里首次出现且未定义。这属于被"abbreviations should not be used except for units of measurement"覆盖的情形（一个未声明的符号约定）。
- `:23`、`:25` 出现 "preferred term"（首选术语）4 次。它不是缩写，但对 *Anaesthesia* 的普通临床读者是纯行话，且是全文论证的关键概念，摘要中未作任何解释。

**【为什么重要】** 摘要的读者是"要不要读下去"的临床医生。`a = 1` 会让他们停下来，`preferred term` 会让他们不确定作者在说什么——而这两个点恰好是本文唯一结论所依赖的机制。本刊对摘要的要求是"abbreviations should not be used except for units of measurement"，精神是**摘要必须自足**。

**【具体修改建议】**

1. 把 "(a = 1)" 改为 "(a single report)"；所有无法避免的符号都不进摘要。
2. 首次出现时给 preferred term 一个括注："the term stored in the coding dictionary for that reaction"。或干脆改用平实表述："the word stored in the coding dictionary"。
3. 采用 §8 我提供的整段替代稿（280 词，已逐项核过不含缩写）。

---

### P1-5. 字数与表数声明错误，且正文零余量

**【问题】** 封面声明与实际不符；正文字数正贴 4 000 上限，任何编辑侧计数差异都会越界。

**【证据】**（我逐项自算）

- Summary：`I_正文_IMRaD_en.md:13` 声明 "Summary 300 words"。我统计（含 Introduction./Methods./Results./Discussion. 四个段首标签）为 **299 词**；不含标签为 **295 词**。**在 250–300 之内，PASS**，但已无余量。
- 正文：`:13` 声明 "main text 4 000 words (Introduction to Conclusion, section headings included). Verified with `_wordcount.py`"。我按同一口径（§1 首行至 §5 末行，去 markdown 标记、保留章节标题）统计为 **3 996 词**；不含标题为 **3 865 词**。分节为：Introduction 371 / Methods 1 187 / Results 1 090 / Discussion 1 045 / Conclusion 172。**在 3000–4000 之内，PASS**，但距上限仅 4 词。风险是真实的：期刊侧（Word 或生产排版）对连字符词、`§x.y` 引用、数字串的计数口径与脚本不同，且本刊明文 "Original articles should be between 3000–4000 words"。一旦越界，轻则退回删减，重则按"over length"处理。
- 表数：`:13` 声明 "**Tables:** 4 (Table 4 in three panels) plus 5 supplementary"。正文文件中带独立题注的展示表实为 **6 张**（Table 1、2、3、4A、4B、4C）；4A/4B/4C 列结构不同，不能算同一张表的面板。**声明的数字是错的**（本刊未对 Original Article 规定表数上限，所以这不是违规，而是声明不实）。
- 参考文献：30 条，本刊要求 "up to 30–40 references"，**PASS**。
- 关键词：5 个，要求 3–5 且在题名页（`:11`），**PASS**。
- Short title：`:3` "Remifentanil hyperalgesia reporting: two-database study" = **55 字符**，要求 "up to 60 characters"，**PASS**（建议标签由 "Running head" 改为本刊用词 "Short title"）。
- 题名：`:1` 我逐词计数为 **17 词**，要求 "in general, this should not exceed 20 words"，**长度 PASS**。但 "with a terminology caution" 属于**宣告结论倾向**的短语，与本刊 "Title should not state a conclusion or pose a question" 及 "Title should be non-declarative" 相抵触——不是硬性越界，但会被要求修改。另本刊建议题名含研究设计关键词（"randomised controlled trial", "prospective", "observational"），现题名缺该类词。

**【为什么重要】** 封面数字是编辑对稿件规模的第一印象；三个数字里错了一个、另外两个贴死上限，会直接促成"请先压缩再送审"的处理路径。

**【具体修改建议】**

1. 删除脚本名与内部门禁的提及：
   > "**Word count:** Summary 280 words; main text 3 850 words (Introduction to Conclusion, section headings included). **Tables:** 6 main tables (Table 4 given as three panels, 4A–4C) and five online Supporting Information tables. **Figures:** 2."
2. 为正文预留 ≥150 词余量。可删的具体段落（每项都标注可省词数，皆不与核心论证冲突）：
   - §4.2 第二段后半（`:155`）"Under the correct preferred term the data contain the concept and code it disproportionately for every opioid; they show no remifentanil-specific excess, and the stronger database contributed no remifentanil report."（约 33 词）——§3.3、§4.1 已陈述两遍，此为该结果的第三次陈述，删去最划算。
   - §4.3 末两句（`:161`）关于 DRUG TOLERANCE 与 DRUG WITHDRAWAL SYNDROME 的生理学解释（约 34 词）——与表 2 数据无关的解释性猜测，且未做任何检验。
   - §4.4（`:167`）末句 "Remifentanil's lowest-of-four ranking is most parsimoniously explained by the same under-reporting that affects every other term, not by a genuinely lower hyperalgesia burden."（约 31 词）——与 §4.1、§5 重复。
   - §4.5 "Limited geographic independence" 段中 `[30]` 的括注 "（the EVDAS-referenced median PT-level overlap, not a pairwise figure）"（约 16 词）——把方法学细节留在引用处即可，正文不必自证。
   - Table 2 表注中 Bonferroni 说明（`:286`，约 40 词）——移入 online Supporting Information 或 Results 一句话。
   合计可省约 150 词，正文落到 ~3 845 词。
3. 题名建议（17 词，无结论倾向，含设计词）：
   > "Remifentanil and hyperalgesia reporting in two national pharmacovigilance databases: an observational head-to-head disproportionality analysis"
   （若须保留术语主题，用 "…: an observational disproportionality analysis with negative controls"，18 词。）

---

### P1-6. 参考文献格式：refs 29、30 违反本刊作者列举规则（已用 Crossref 核实为 7 位作者）

**【问题】** 本刊规定 7 位及以上作者只列前三位加 et al.；第 29、30 条各列了 7 位。

**【证据】**

- 本刊指南原文："List all authors unless there are seven or more, in which case give the first three followed by 'et al.'"
- ref 29（`I_正文_IMRaD_en.md:247`）："Janiczak S, Tanveer S, Tom K, Zhang R, Ma Y, Wolf L, Muñoz MA." —— 我查 Crossref（DOI 10.1007/s40264-025-01560-7）返回作者恰为 7 位：Janiczak Scott；Tanveer Sarah；Tom Karen；Zhang Rongmei；Ma Yong；Wolf Lisa；Muñoz Monica A.。**应为 "Janiczak S, Tanveer S, Tom K, et al."**
- ref 30（`:248`）："Vogel U, van Stekelenborg J, Dreyfus B, Garg A, Habib M, Hosain R, Wisniewski A." —— Crossref（DOI 10.1007/s40264-019-00899-y）返回恰为 7 位：Vogel Ulrich；van Stekelenborg John；Dreyfus Brian；Garg Anju；Habib Marian；Hosain Romana；Wisniewski Antoni。**应为 "Vogel U, van Stekelenborg J, Dreyfus B, et al."**
- 反向核查（作者已正确使用 et al. 的条目）**无障碍**：ref 12 "Cutroneo PM, Sartori D, Tuccori M et al."、ref 13/14 "Fusaroli M, Salvo F, Begaud B et al."、ref 25 "Andreaggi CA, Novak EA, Mirabile ME et al." 三字加 et al.，符合规则。
- 其余格式经核查无问题：30 条编号与正文引用一致；27 条期刊文献**全部带 https://doi.org/... **（我逐条统计），refs 15/16/18 为网页/词典，按规则无需 DOI；正文引用使用方括号置于标点前；期刊名缩写+斜体、卷号加粗的形式符合模板。

**【为什么重要】** 参考文献的作者列举是最容易被生产编辑逐条核对的形式项，且这 2 条恰好都出现在"重复报告/信号重叠"这一支撑 §4.5 局限性的位置上，被挑出会显得格外刺眼。

**【具体修改建议】**

1. `:247` 改为："Janiczak S, Tanveer S, Tom K, et al. An evaluation of duplicate adverse event reports characteristics in the Food and Drug Administration Adverse Event Reporting System. *Drug Saf* 2025; **48**: 1119–26. https://doi.org/10.1007/s40264-025-01560-7"
2. `:248` 改为："Vogel U, van Stekelenborg J, Dreyfus B, et al. Investigating overlap in signals from EVDAS, FAERS and VigiBase. *Drug Saf* 2020; **43**: 351–62. https://doi.org/10.1007/s40264-019-00899-y"
3. 建议对外提供 `refs_verification.csv`（见 P1-2），把"30 条按标识符核实"变成可被编辑直接抽验的文件，而不是只有一句声明。

---

### P1-7. Table S2 题注引用了错误的文献编号

**【问题】** Table S2（READUS-PV 检查表）的题注把 READUS-PV 引为 [10, 11]，而这两条是 Angst 2003 与 Yu 2016；READUS-PV 是本稿的 [13, 14]。

**【证据】**

- `I_正文_IMRaD_en.md:440`："Completed READUS-PV checklist **[10, 11]** mapping each of the 32 recommendations for the manuscript body and the 12 recommendations for the abstract..."
- 本稿文献表：`[10]` = Angst MS, Koppert W, Pahl I, Clark DJ, Schmelz M. Short-term infusion of the μ-opioid agonist remifentanil in humans causes hyperalgesia during withdrawal. *Pain* 2003（`:228`）；`[11]` = Yu EHY, Tran DHD, Lam SW, Irwin MG. Remifentanil tolerance and hyperalgesia... *Anaesthesia* 2016（`:229`）。
- READUS-PV 的两篇是 `[13]`、`[14]`（`:231–232`），且 §4.6（`:187`）与 §2.1（`:49`）均正确引为 [13, 14]。检查表文件自身也把 READUS-PV 引为 [1, 2]（`I_TableS2_READUS-PV_checklist.md:83–84`），与正文编号体系不同。
- 附带核对：同一题注写 "32 recommendations for the manuscript body and the 12 recommendations for the abstract"，与检查表 Part A/B 的条目数一致（Part A 16 行编号但含 1a/1b、2a–2c 等细分共 32 项；Part B 12 项）。此部分正确。

**【为什么重要】** 这是本刊"参考文献必须按正文顺序编号并被正确引用"规则下最典型的错误样式，且发生在作者主要合规证据的题注上。生产编辑一定会核对，读者若按 [10, 11] 去找 READUS-PV 会找不到。

**【具体修改建议】**

1. `:440` 改为："Completed READUS-PV checklist [13, 14] mapping each of the 32 recommendations for the manuscript body and the 12 recommendations for the abstract to the section of this manuscript in which it is addressed..."
2. Table S4 题注（`:464`）与 §4.6 无需改动，已正确引 [13, 14]。
3. 建议在检查表文件中统一采用正文的编号体系（把 [1,2] 改为 [13,14]），避免评审时出现两套编号。

---

## 3. 次要问题（P2-1…）

### P2-1. 正文文件残留大量内部工作痕迹（§9、§10、"Formatting note (not for submission)"、脚本名、仓库文件名）

**【问题】** 稿件把内部工作区写在了投稿文件里。

**【证据】** 逐处定位：

- `:15` "**Formatting note (not for submission).** ... Number-to-source traceability is in §9."（明确写着 not for submission）
- `:13` "Verified with `_wordcount.py`."
- `:65` "...archived with the repository (ANALYSIS_PLAN.md)"
- `:217` References 之前的说明句："References are numbered in order of first citation. Journal names are abbreviated and italicised; volume numbers are bold. All journal articles carry a DOI, as required by *Anaesthesia*."
- `:436` 表注中 "listed in the study repository (`03_soc_27.csv`)"
- `:440` 表注中 "Supplied as a separate file with the submission (`I_TableS2_READUS-PV_checklist.md`)"
- `:528–547` 整节 "## 9. Number-to-source traceability"（表格列的是 `01_faers_results.csv`、`_gen_table_s1.py`、`D_27SOC_openFDA事件级.md` 等仓库文件名）
- `:549–566` 整节 "## 10. Outstanding items before submission"，首行自注 "*(Internal working section, not part of the submitted manuscript.)*"

**【为什么重要】** 这些内容（尤其 §10）一旦随稿提交，后果不是"格式不规范"这么轻：§10 会向编辑披露"作者有一份内部待办清单"、"github 页面在本环境打不开（egress block）"、"X（Twitter）账号无"、"reviewer suggestions 无：inventing names... would be worse"、"Author Guidelines compliance audit (2026-09-17, 更新于 round 2 之后)"。其中三项直接有害：(a) "the github.com page itself cannot be opened from this environment" 与数据可用性声明"permanently available"并列，会让编辑质疑作者从未亲眼确认过自己给出的链接；(b) "updated after round 2" 披露了内部多轮修改流程；(c) 关于 reviewer suggestions 的辩解口吻读起来像给编辑的解释信，而非稿件内容。这些叠加足以触发一次科研诚信询问，而询问的成本远高于删掉两节。

**【具体修改建议】**

1. 删除 `:15`、`:217`、`:528–566`（§9 与 §10 全节）；删除 `:13` 中 "Verified with `_wordcount.py`"。
2. `:65` 改为："Three groups of terms were specified in a dated analysis plan that is supplied as online Supporting Information (Appendix S1) and archived with the analysis code."
3. `:436` 改为："Preferred terms that the heuristic could not map, with their counts, are listed in the study repository."
4. `:440` 改为："Supplied as online Supporting Information (Table S2)."
5. 溯源表本身是好东西，**不要丢**——把它作为 online Supporting Information Appendix S2（From manuscript value to source file）提交，它对本文的"可复现"卖点有实质加分。

### P2-2. 只上传可接受格式的图件（`.png` 不在本刊之列）

**【问题】** 稿件同时提供 `.tif/.pdf/.png` 三种图件，而本刊只接受 ".pdf, .jpg, .tiff or .pptx"。

**【证据】** 本刊指南原文（图件格式）：".pdf, .jpg, .tiff or .pptx"；同页另有 "Word format is not acceptable for figure files"。稿件 `:15` 与 `05_figures.py:12–14` 均产出 `.tif/.pdf/.png` 三份；文件清单见工作目录（`I_fig1_rorr_forest.tif` 789 852 B、`.pdf` 34 560 B、`.png` 254 655 B；`I_fig2_year_trend.tif` 470 066 B、`.pdf` 32 695 B、`.png` 173 968 B）。

**【为什么重要】** 提交非白名单格式会被投稿系统退回或由生产部门要求替换，纯粹浪费来回时间。分辨率与体积本身都合格（实测 600 ppi，远低于 10 MB 上限），只差格式取舍。

**【具体修改建议】** 投稿只上传 `.tif`（首选）或 `.pdf`；不要上传 `.png`。若要保留可预览版本，留在本地即可，不进入投稿包。

### P2-3. Figure 2 保留了 left+bottom 脊线，属"plot frames"的边界情形（低风险）

**【问题】** 本刊禁止图内出现 "plot frames"。Figure 1 只保留 x 轴（`05_figures.py:162`），Figure 2 保留 left+bottom 两条脊线（`:216`）。

**【证据】** `05_figures.py:60–65` 的 `clean_axes` 对 top/right 一律关闭，`keep` 参数分别传 `("bottom",)` 与 `("left","bottom")`。我在渲染文件中确认：两图均**没有**四边框；Figure 1 只有底部轴线，Figure 2 是 L 形两轴。

**【为什么重要】** 严格读法下"plot frame"指环绕绘图区的框，两图都无；宽松读法下任何边框线都可能被计。我倾向判定为 PASS，但既然本刊把该条写在明文里，Figure 2 与 Figure 1 的脊线配置不一致本身也值得统一。

**【具体修改建议】** 把 Figure 2 的 `keep` 也设为 `("bottom",)`，与 Figure 1 一致；与 M4 的图例删除一并处理。若不愿改动，至少在两图之间保持一致，避免被指出"同一稿内两图做法不同"。

### P2-4. §3.3 一句话里把两种不同量放在同一个括号里，容易被读错

**【问题】** §3.3 用 "weakest" 描述 ROR 排名，却紧接给出 RORR 数值，读者会误以为 0.696 就是瑞芬太尼的 OR。

**【证据】** `:109`："Remifentanil's was the weakest (**0.696, 0.37–1.31**, versus fentanyl; 0.389, 0.21–0.73, versus morphine)"。而瑞芬太尼的 HYPERAESTHESIA OR 为 **4.73 (2.54–8.80)**（`01_faers_results.csv:15`；我按 a=10、b=5 365、c=8 151、d=20 659 161 复算 OR = 4.724，与稿件 4.73 一致），四药 OR 依次为 4.73 / 6.80 / 8.61 / 12.17——"weakest" 指的是这一列。同一括号里的 0.696、0.389 是**头对头比率**，不是 OR。

**【为什么重要】** 本文的论证核心就是区分"药物与事件的关联强度"与"两药之间的相对报告强度"。把两者并置而不标明，会让最关键的区分在读者那里失效。

**【具体修改建议】** 改为："Among the four opioids remifentanil had the lowest reporting odds ratio (4.73, 95% confidence interval 2.54–8.80), and the head-to-head ratios were also below one (0.696, 0.37–1.31, versus fentanyl; 0.389, 0.21–0.73, versus morphine)."

### P2-5. Table S3 中芬太尼与吗啡的 "Other health professional" 计数完全相同（均 2 056），建议确认

**【问题】** 两个规模相差近 1.6 倍的队列，报告者类型中同一类的计数完全相同，属统计学上的低概率巧合，值得回查原始抽取。

**【证据】** `cv/cv_subgroups.csv:27` = `FENTANYL,reporter,Other health professional,2056,42.12`；`cv/cv_subgroups.csv:57` = `MORPHINE,reporter,Other health professional,2056,26.79`。稿件 Table S3（`:449`）照录为 "2 056 (42.1)" 与 "2 056 (26.8)"。我已确认该值不是硬编码常量（`cv/cv_subgroups.csv` 由 `cv/cv_process.py` 从 `reports.txt` 第 34 列聚合得到，全流程无此常量），且各自分母归一正确（2056/4881 = 42.1%；2056/7675 = 26.8%）。因此**要么是真巧合，要么是 join 层面的同一类错误**，我在本次审稿中无法从已处理文件中判定（`reports.txt` 为 422 MB，逐一重算需重新跑聚合）。

**【为什么重要】** 该数字出现在用于解释主结论（低报由报告来源解释，§3.6/§4.3）的关键表里。

**【具体修改建议】** 请作者从原始 `reports.txt` 重新聚合一次报告者类型分布，并在仓库里提供 `cv/cv_reporter_recount.csv`（列：`drug, reporter_type, n, denominator, pct`）作为该表的溯源；若确认巧合，在 Table S3 加一句脚注说明两个数值相同是巧合而非重复计数。

### P2-6. Table 4C 的 "(a = 1)" 定义不清：只有把分母限制在 2015–2024 才成立

**【问题】** "leave-2024-out leaves a = 1" 只在 2015–2024 窗口内成立；对全库做 leave-2024-out，瑞芬太尼应剩 2 例。

**【证据】**

- 稿件 `:137` §3.8："A leave-2024-out sensitivity leaves a single remifentanil report (a = 1) and no signal (reporting odds ratio 0.70, 0.10–4.98...)"；Summary `:25` 同样写 "(a = 1)"。
- 我的复算：`01_faers_results.csv:15` 显示瑞芬太尼 HYPERAESTHESIA 全库 a = 10；`04_sensitivity_year_hyperaesthesia.csv` 显示 2024 年 a = 8、2021 年 a = 1（另有 1 例无 receivedate）。全库 leave-2024-out 得 a = 10 − 8 = **2**。
- 得 a = 1 的唯一路径是把分析集限制在 2015–2024：`_round4_leave2024.py:26–29` 的 `leave2024()` 只在 `04_sensitivity_year_hyperaesthesia.csv` 的年度行上求和，`cohort_excl2024` = 3 798 = 2015–2023 各年瑞芬太尼报告数之和（`04_sensitivity_leave2024_hyperaesthesia.csv` 首行 REMIFENTANIL 3 798 与我复算的 4 246 − 448 = 3 798 一致）。
- 稿件未在任何位置说明该敏感性分析的分母被限制在 2015–2024。Table 4C 的注（`:366`）只说 "nine reports carry a usable receivedate in 2015–2024 (eight in 2024; the tenth omitted), so the table holds nine rows"。

**【为什么重要】** 一个按 Table 2 复算的读者会得到 a = 2，与摘要的 a = 1 冲突；这类"同一稿件内两个数对不上"的体验，比数字本身大小更伤可信度。本文正是靠"数字可追溯"立论，这里恰好不可追溯。

**【具体修改建议】**

1. §3.8 改为："A sensitivity analysis restricted to reports received in 2015–2024 and excluding 2024 left a single remifentanil report (a = 1) and no signal (reporting odds ratio 0.70, 95% confidence interval 0.10–4.98; ratio versus fentanyl 0.106, 0.015–0.758; versus morphine 0.058, 0.008–0.413)."
2. 在 `04_sensitivity_leave2024_hyperaesthesia.csv` 增加一列 `analysis_window`（值 `2015-2024`），使窗口限制写在数据里而不是只写在脚本里。
3. Summary 与 §5 同步写法："excluding 2024 from the 2015–2024 window left one report and no signal"。

---

## 4. 我认为稿件站得住的地方

以下五点均经我独立核查，属"经核查无问题"，作者不应因评审意见而改动它们。

1. **核心数字准确，且我从原始 2×2 复算过。** HYPERAESTHESIA 瑞芬太尼 OR：a = 10、b = 5 375 − 10 = 5 365、c = 8 161 − 10 = 8 151、d = 20 692 687 − 5 375 − 8 161 + 10 = 20 659 161，OR = a·d/(b·c) = 4.724，稿件写 4.73，一致。Bonferroni 说明也经得起复算：以 72 次比较的 z ≈ 3.39 重算，下界 = exp(ln(4.729) − 3.39 × 0.3171) = **1.614**，稿件写 1.61（`:286`），正确。这类"声明了就不怕算"的地方，是本稿最值得保留的品质。
2. **跨库设计是真的跨库，且作者对两个库的强弱定位诚实。** 加拿大侧用的是原生 `SOC_NAME_ENG` 与 `Suspect` 角色限制（`I_正文_IMRaD_en.md:61, 81`；`cv/cv_soc_27.csv` 27 行可逐格复核），而非把 FAERS 的做法照搬；FAERS 侧的 SOC 分析被明确降级为探索性并写明"counting is event-level and the rules are not authoritative"（`:83`）。我在 `03_soc_27.csv` 头部也看到同样的自注（"事件级近似"、"仅作定性互证"）。这种**主动给自己的次优分析贴标签**的做法，在投稿中相当少见。
3. **统计量的自检做得到位，尤其"2024 单年簇"的发现。** 作者没有把 HYPERAESTHESIA 的 4.73 当成结论卖，而是主动做了三件事：披露 10 例中 8 例在 2024 年（`:137`）、给出 leave-2024-out 后无信号、并给出四个阿片各自的 2024-vs-pooled 比值（15.4 / 4.3 / 4.9 / 1.7，见 `04_sensitivity_2024cluster_hyperaesthesia.csv`）以说明这是全库性的年份偏移而非瑞芬太尼特有事件。我复核了 `04_sensitivity_year_hyperaesthesia.csv` 的全部行，2024 年四药 ROR（72.856 / 29.199 / 42.172 / 20.845）与 pooled 之比确为 15.41 / 4.30 / 4.90 / 1.71，与稿件一致。**主动把自己最好的数字拆掉，是这类研究最需要的诚实。**
4. **负对照 + 特异性探针的设计是真的先在的、且结论被如实报告为不成立。** 四个阴性对照共 12 个可计算比率，我按 Table S5 逐格复算：11 个 < 1，唯一例外 PRURITUS vs sufentanil = 1.310 (0.84–2.04)，区间含 1，与稿件 `:117` 的表述完全一致。更关键的是 DRUG INEFFECTIVE 在两个库方向相反（FAERS 0.568/0.470 低于 1；加拿大 1.277/1.703 高于 1，`cv/cv_pt_summary.csv`），作者没有把它藏起来，而是写"it narrows rather than settles the interpretation"（`:163`）。探针失灵被如实报告，比探针成功更让人相信作者没有挑选结果。
5. **规范层面的自觉程度高于同类投稿。** 30 条文献的 DOI 我抽验 3 条全部解析正确（refs 13、29、30，见 P1-2）；Python 3.13.14 与 matplotlib 3.11.1 的版本声明我实测确认（本地解释器 `python -c "import sys; print(sys.version)"` 返回 `3.13.14 (main, Jun 11 2026...)`；`matplotlib.__version__` 返回 `3.11.1`）——**这一条属于"我原本怀疑但核查后无问题"**；图件分辨率实测 599.9988 ppi、体积 771 KB / 459 KB，与 600 ppi 及 ≤10 MB 的要求相符；全稿未检出美式拼写（我检索 analyzed/center/pediatric/behavior/modeling/color 等 18 个常见美式词形，零命中），UK 拼写一致；仓库经 GitHub API 确认为公开、MIT 许可、含 v1.0.0–v1.4.0 五个带结果包的 release。这些都是需要作者额外投入才能做到的。

---

## 5. 需要作者明确澄清的事实性问题

以下问题我给出的是"我需要知道什么"，不替作者猜答案。

**关于分析时序与注册**

1. `ANALYSIS_PLAN.md:5` 写着"This plan was written post hoc, once the data had been retrieved"，且 `:3` 记载计划定稿日与数据抽取日同为 2026-09-16。请明确：**在写下五个代理术语（HYPERAESTHESIA 等）之前，作者是否已经看过除这五个 0 以外的任何结果？** 具体说，`01_faers_results.csv` 中四个阿片在所有 a priori 术语上的 ROR、RORR 是否在 Amendment 1 之前就已计算并存盘？如能给出该文件的 mtime 与仓库中 Amendment 1 提交的时间戳先后，本条即可关闭。
2. 稿件全稿 11 处 "defined a priori"。请确认这些位置在定稿时将全部改为何种统一表述，以及该表述是否会在投稿信与 `ANALYSIS_PLAN.md` 中同步。

**关于数据与检索**

3. openFDA 侧的完整检索语句是什么？请提供**可粘贴执行**的 URL（含 `search=` 与 `count=` 参数、`limit` 值、是否使用 API key），以及每条语句的执行日期与返回条数。特别是 `patient.drug.activesubstance.activesubstancename.exact` 的 cohort 查询、18 个术语在 reaction 字段的查询、以及 Table S4 第三列"adjacent-token phrase query"的确切写法。
4. 加拿大侧：`cv_pt_summary.csv` 给出逐 PT 计数，但抽取脚本对 `reactions.txt` 的处理是否保留同一报告内重复 PT？`Suspect` 角色的判定字段是 `report_drug.txt` 的哪一列、取值如何映射？请给出 `cv_process.py` 中对应的行号。
5. 仓库当前最新 release 是 v1.4.0，而 §10 说 "with tag `v1.0.0`"。**投稿时稿件指向的那个版本是哪一个？** 是否有 commit 哈希？是否会为投稿打一个冻结 tag？

**关于具体数字**

6. Table 4C 的 "(a = 1)"：请确认 leave-2024-out 的分析集是否限制在 2015–2024。若是，为什么全库其他年份（2004–2014 及无日期报告）被排除；若不是，为何 a 不是 2（全库 10 例减去 2024 年的 8 例）。
7. Table S3 中 FENTANYL 与 MORPHINE 的 "Other health professional" 计数均为 2 056。请从原始抽取重算一次并给出结果；若确为巧合，请说明如何排除 join/去重层面的同一类错误。
8. §3.7 与 Table S1 Panel A 中，加拿大免疫类仅有 9 例、妊娠类仅 3 例、PAIN 仅 2 例。请给出这些单元格的 95% CI；若区间过宽（例如下界远小于 1），请说明为何仍以"elevated ratios"表述。

**关于图表与包装**

9. Table 3 与 Table S1 的所有点估计：不补 CI 的理由是什么？若理由是"区间过宽无信息量"，是否考虑直接标为 not estimable 而不是印点估计？
10. 投稿包最终形态：正文文件是否只保留主表 + 图注 + 补充材料题注？五张补充表是否合并为一个文件？S2（READUS-PV 检查表）是并入该文件还是独立文件？投稿信是否会同步改写？
11. 两图的 legend box 是否会在投稿版中删除（图注已能完整解释符号，删除后不损失信息）？

**关于 AI 声明与文献**

12. AI 声明中 "one of several commercial large language models" 具体指哪些模型与版本、使用区间是何日期？是否曾向 AI 工具输入任何非公开内容（含未发表草稿之外的任何受限制材料）？
13. "all 30 cited references verified by identifier" 的核验记录（标识符、解析器、日期、解析结果）是否存在并可随仓库提供？作者是否逐篇核读过被引文献的正文内容以确认其确实支持正文中的引用陈述？——后一点是本刊立场声明中"authors remain fully responsible for... correctly referencing any supporting work"的直接要求，我需要在稿件里看到这句承诺。
14. `05_figures.py:179–185` 中 Figure 2 的数值为手写常量（我核对后与 `04_sensitivity_year_pain.csv` 一致），而 AI 声明称"Every reported value is a direct read of the analysis output files by the archived scripts"。请确认将以何种方式消除二者之间的不一致（改代码读文件，还是改声明措辞）。

**关于稿件类型**

15. 作者是否接受把 §3.6/§4.3 的"低报由报告来源与设置解释"提升为主结论之一（并配 M1 建议的 Table 5）？如不接受，请说明本稿作为 Original Article 相对 Science Letter（≤800 词、≤8 文献、≤1 表 1 图）的额外价值在哪里。

---

## 6. 我实际做的独立核查

**（1）逐字读过的文件**

- `I_正文_IMRaD_en.md`（全文 566 行，含 Summary、§1–§5、Acknowledgements、30 条 References、Tables 1–4C、Tables S1–S5、图注、§9、§10）
- `ANALYSIS_PLAN.md`（全文 37 行，含 Amendment 1 与"Terminology note — a priori vs pre-specified"）
- `I_TableS2_READUS-PV_checklist.md`（全文 85 行，Part A 32 项、Part B 12 项）
- `I_投稿信_cover_letter.md`（全文 38 行）
- 数据文件：`01_faers_results.csv`、`10_term_dictionary.csv`、`04_sensitivity_year_pain.csv`、`04_sensitivity_year_hyperaesthesia.csv`、`04_sensitivity_leave2024_hyperaesthesia.csv`、`04_sensitivity_2024cluster_hyperaesthesia.csv`、`04_sensitivity_estimable_years.json`、`03_soc_27.csv`、`cv/cv_drug_totals.csv`、`cv/cv_pt_summary.csv`、`cv/cv_soc_27.csv`、`cv/cv_subgroups.csv`、`cv/cv_summary.md`
- 代码：`05_figures.py`、`_round4_leave2024.py`、`_check_consistency.py`（第 95–145、438–455 行）

**（2）我自算并比对的结果**

| 项目 | 我的计算 | 稿件 | 判定 |
|---|---|---|---|
| 题名词数 | 17 | 未声明（要求 ≤20） | 一致，PASS |
| Short title 字符数 | 55 | 未声明（要求 ≤60） | 一致，PASS |
| Summary 词数（含段首标签 / 不含） | 299 / 295 | 声明 300 | 一致，PASS，零余量 |
| 正文词数（含标题 / 不含标题） | 3 996 / 3 865 | 声明 4 000 | 一致，PASS，零余量 |
| 分节词数 | Intro 371 / Methods 1 187 / Results 1 090 / Discussion 1 045 / Conclusion 172 | — | 供删减定位 |
| 参考文献数 | 30（27 条期刊文献全部带 DOI；refs 15/16/18 为网页/词典） | 30 | PASS；refs 29、30 作者列违规 |
| 主表数 | 6（1、2、3、4A、4B、4C） | 声明 4 | **不一致** |
| Figure 1 分辨率 / 体积 | 599.9988 ppi / 789 852 B | 未声明 | PASS |
| Figure 2 分辨率 / 体积 | 599.9988 ppi / 470 066 B | 未声明 | PASS |
| HYPERAESTHESIA 瑞芬太尼 OR | a=10,b=5 365,c=8 151,d=20 659 161 → 4.724 | 4.73 | 一致 |
| HYPERAESTHESIA Bonferroni 下界（72 次比较） | 1.614 | 1.61 | 一致 |
| 负对照可计算比率 | 12 个中 11 个 < 1；例外 PRURITUS vs sufentanil = 1.310 | 同 | 一致 |
| 2024 簇 2024/pooled 比值 | 15.41 / 4.30 / 4.90 / 1.71 | 15.4 / 4.3 / 4.9 / 1.7 | 一致 |
| leave-2024-out 瑞芬太尼 a（2015–2024 窗口 / 全库） | 1 / **2** | 摘要与 Table 4C 均写 1 | **定义不清** |
| Python / matplotlib 版本 | 3.13.14 / 3.11.1（实测） | 同 | 一致，无问题 |
| 美式拼写检索（18 个词形） | 0 命中 | — | PASS |
| 正文 "a priori" 出现次数 | 11 | — | 见 M2 |

**（3）外部查证（均为实际检索/查询，不是凭记忆）**

- *Anaesthesia* Guidance for Authors（期刊官网 For Authors 页面）：逐字取得 Original Article 字数与文献数（"between 3000–4000 words and contain up to 30–40 references"）；摘要（"A 250–300 word Summary... structured, i.e. Introduction, Methods, Results, Discussion"、"no references and abbreviations should not be used except for units of measurement"）；题名（"in general, this should not exceed 20 words"、"Title should be non-declarative"、"Title should not state a conclusion or pose a question"）；关键词（"3–5 keywords on the title page"）；图件（"300 pixels per inch for photographs and 600 pixels per inch for line art..."、"Please do not send image files larger than 10MB"、"There should be no titles, plot frames, gridlines or legend boxes within the graphs, and symbols and error bars should be explained in the caption"、格式 ".pdf, .jpg, .tiff or .pptx"）；补充材料（"should be uploaded as separate documents and not included in the main document file"、"all supporting tables in one file"、"The captions for supporting information should be listed at the very end of your submission"）；参考文献（"List all authors unless there are seven or more, in which case give the first three followed by 'et al.'"、"DOIs should be included for each journal article reference"）。该页 **完全没有** AI 条款（我对 "artificial intelligence"/"AI"/"ChatGPT" 做了全文检索，零命中）。
- *Anaesthesia* Editorial Policies 页面：取得期刊范围与作者责任条款（"We may ask authors to send us original data... and we expect authors to comply with such a request"），同样无 AI 条款。
- *Anaesthesia* / *Anaesthesia Reports* 编辑立场声明（DOI 10.1111/anae.16071）：取得 AI 相关原文（不得作为作者；可用于支持写作但"should not be used as the primary source of text, figures, images or graphics"；"Failure to do so, or to declare artificial intelligence use as a primary source of data, will be treated as scientific misconduct"）。该声明确实存在，投稿信对它的引用不是虚构。
- Wiley Best Practice Guidelines on Research Integrity and Publishing Ethics 与 Wiley 的 AIGC 立场页：取得披露要求（写在 Methods 或 Acknowledgements；"Tools that are used to improve spelling, grammar, and general editing are not included"；AI "may be used for creating data visualizations and illustrations"），以及投稿时 AI Use Declaration 需涵盖的要素（工具名与版本、使用日期、如何应用、如何核验输出、隐私与合规）。
- GitHub REST API：`/repos/yyx-4113/remifentanil-hyperalgesia-signal-faers-canada` 返回 public、MIT、default branch main、created 2026-09-16、pushed 2026-09-17；`/releases` 返回 v1.0.0（results-bundle.zip 789 134 B）至 v1.4.0（1 023 056 B）五个版本。**数据可用性 URL 可访问，此项判定为 PASS，不存在"无法核实"的情形。**
- Crossref REST API 抽验 3 条 DOI：10.1007/s40264-024-01421-9（ref 13，Drug Safety 47: 575–584，标题一致）✓；10.1007/s40264-025-01560-7（ref 29，Drug Safety 48: 1119–1126，**作者恰为 7 位**）✓ 但格式违规；10.1007/s40264-019-00899-y（ref 30，Drug Safety 43: 351–362，**作者恰为 7 位**）✓ 但格式违规。

**（4）图件目视核查**

对 `I_fig1_rorr_forest.png` 与 `I_fig2_year_trend.png` 逐图查看：Figure 1 自上而下的术语顺序为 DRUG INEFFECTIVE / CONSTIPATION / PRURITUS / VOMITING / NAUSEA / PAIN / DRUG WITHDRAWAL SYND. / PROCEDURAL PAIN / HYPERAESTHESIA，与图注所写 "grouped from the top: ... (HYPERAESTHESIA) ... (DRUG INEFFECTIVE)" **方向相反**；两图各有一个图内图例框（Figure 1 左上、Figure 2 左下），违反本刊明文要求；两图均无图内标题、无网格线、无四边绘图框。

**（5）我判定为"无法核实"、故不给 FAIL 的项**

- 投稿包的最终形态（`.docx` 是否符合 Times New Roman 12 pt、双倍行距、连续页码；`.docx` 中是否真的零内嵌图件）：我审查的是 markdown 源文件与图件文件本身，未读取构建产物，故不作判定。
- `reports.txt`（422 MB）中报告者类型的逐药重算：仅确认 2 056 不是硬编码常量，未重跑聚合，故按"需澄清"处理（P2-5），不判定为错误。
- 30 条文献的**内容**是否确实支持正文中的每一处引用陈述：我只核验了 3 条的标识符与题录，未逐篇比对被引内容，故在 §5 第 13 条向作者提出，而不是直接判 FAIL。

---

## 7. 交付物 (a) 逐项格式合规对照表

要求一栏引自 *Anaesthesia* Guidance for Authors（期刊官网现行版本）与 *Anaesthesia*/*Anaesthesia Reports* 编辑立场声明；"PASS" 表示经我核查满足，"FAIL" 表示不满足，"无法核实" 表示我无法从所审文件判定。

| # | 本刊现行要求（原文依据） | 稿件现状 | 结论 |
|---|---|---|---|
| 1 | Original article 正文 "between 3000–4000 words" | 我计 3 996（含标题）/3 865（不含）；封面声明 4 000 | **PASS**（零余量，勿再加字） |
| 2 | "contain up to 30–40 references" | 30 条，编号与正文一致 | PASS |
| 3 | "A 250–300 word Summary... structured, i.e. Introduction, Methods, Results, Discussion" | 299（含段首标签）；四段结构 | PASS（贴上限） |
| 4 | "The Summary should contain no references and abbreviations should not be used except for units of measurement" | 无参考文献；无 FAERS/ROR/CI 等缩写（经逐词检索）；但含未定义符号 `a = 1` 与未解释的 "preferred term" | **FAIL（轻度）** |
| 5 | 题名 "in general, this should not exceed 20 words" | 17 词 | PASS |
| 6 | "Title should be non-declarative" / "Title should not state a conclusion or pose a question" | "with a terminology caution" 带结论倾向；缺 "observational" 类设计词 | **FAIL（轻度）** |
| 7 | Short title "up to 60 characters suitable for a running header" | 55 字符 | PASS（建议标签改称 Short title） |
| 8 | "3–5 keywords on the title page" | 5 个，位于题名页 | PASS |
| 9 | 图件"supply each Figure as a separate file and not embedded within the Word document"；格式 ".pdf, .jpg, .tiff or .pptx" | `.tif`/`.pdf`/`.png` 各 2 个独立文件；`.png` 不在白名单 | PASS（勿上传 PNG） |
| 10 | 分辨率 "600 pixels per inch for line art" | 实测 599.9988 ppi（两图） | PASS |
| 11 | "Please do not send image files larger than 10MB" | 789 852 B / 470 066 B | PASS |
| 12 | "There should be no titles, plot frames, gridlines or legend boxes within the graphs" | 无标题、无网格、无四边框；**两图各有一个图内图例框** | **FAIL** |
| 13 | "symbols and error bars should be explained in the caption" | 两图图注均解释符号与误差线；Fig 1 图注分组方向写反（"from the top"，实为自下而上） | **FAIL（图注方向）** |
| 14 | 表格（含题名）、图注、"supporting information captions" 均置于正文文件 | 主表题注、图注、S1–S5 题注均在正文文件 | PASS |
| 15 | 补充材料 "should be uploaded as separate documents and not included in the main document file"；"all supporting tables in one file" | Table S1/S3/S4/S5 **全表内容内嵌正文文件**；仅 S2 独立成文件 | **FAIL** |
| 16 | 参考文献 "numbered sequentially as they appear"；方括号、空格后标点前 | 编号连续、体例一致 | PASS |
| 17 | "List all authors unless there are seven or more, in which case give the first three followed by 'et al.'" | refs 29、30 各列 7 位作者（Crossref 已核实为 7 位） | **FAIL** |
| 18 | "DOIs should be included for each journal article reference" | 27 条期刊文献全部带 DOI；15/16/18 为网页/词典，无需 | PASS |
| 19 | 期刊名缩写+斜体、卷号加粗、无期号 | 体例一致 | PASS |
| 20 | UK 拼写（期刊为英国期刊，全稿体例） | 我检索 18 个常见美式词形，零命中 | PASS |
| 21 | 投稿文本格式 ".doc 或 .docx" | 我所审为 `.md` 源文件与图件；构建产物未读 | 无法核实 |
| 22 | AI 声明须 "described, transparently and in detail, in the Methods section (or via a disclosure or within the Acknowledgements section)" | 位于 Acknowledgements，内容详尽 | PASS |
| 23 | AI 声明须涵盖工具名与版本、使用日期、应用方式、核验方式、隐私与合规（Wiley 模板要素） | 有应用方式与部分核验方式；**缺工具名与版本、缺使用日期、缺隐私与合规**；"每个数字由归档脚本直接读出"与 `05_figures.py:179–185` 手写常量冲突 | **FAIL** |
| 24 | AI 不得为 "primary source of text, figures, images or graphics"（编辑立场声明） | 稿件明确声明 AI 非主要来源、且作者承担全部责任 | PASS |
| 25 | AI 不得作为作者 | 已声明无 AI 列为作者 | PASS |
| 26 | 数据可用性声明（含代码可用性与软件版本） | 有仓库 URL、源数据、软件版本（我实测 3.13.14 / 3.11.1 属实）；**无版本锚点**；"permanently available" 过强；未说明分发的是派生计数 | **FAIL（轻度）** |
| 27 | READUS-PV（作者自行声明遵循）：Part A 第 9 条 "Present all results including confidence intervals" | Table 3、Table S1、§3.7、§3.9 多处点估计无区间，而自查表声称"Every estimate is given with a 95% confidence interval" | **FAIL** |
| 28 | READUS-PV Part A 第 11、12c、7c 条的"位置"列 | 抽查 6 条，3 条定位指向不含该内容的章节（第 11 条 §4.5 缺内容、第 12c 条 §4.6 缺内容、第 7c 条 §2.4 缺内容） | **FAIL** |
| 29 | READUS-PV Part A 第 7d/10、Part B 第 2e（声明 not performed / not applicable） | 正文确无 case-by-case 内容，§4.5 有相应限制说明 | PASS |
| 30 | READUS-PV Part A 第 14d（数据/代码/软件版本/注册声明） | 四项齐备；注册声明如实说"not prospectively registered" | PASS（措辞须按 M2 统一） |
| 31 | 参考文献 DOI 声明 "all 30 cited references verified by identifier" | 我抽验 3 条，标识符与题录全部正确 | PASS（建议附核验记录） |
| 32 | 表中引用的文献编号正确 | Table S2 题注把 READUS-PV 引为 [10, 11]，实为 [13, 14] | **FAIL** |

**汇总**：硬性 FAIL 6 项——#12（图内 legend box）、#15（补充材料整表内嵌正文文件）、#17（refs 29、30 作者列举）、#23（AI 声明缺工具名与版本等三要素）、#27（多处点估计无 95% CI，自查表却称"每个估计都有"）、#28（READUS-PV 定位列 3 处指向错误章节）、#32（Table S2 题注引用编号错误）；轻度 FAIL 4 项——#4（摘要含未定义符号 `a = 1`）、#6（题名带结论倾向）、#13（Fig 1 图注方向写反）、#26（数据可用性无版本锚点）。**其中 #12、#15 是本刊明文条文，属于编辑办公室可先行拦截的形式问题；#23、#27、#28 属可核查陈述的真实性问题，性质更重。**

---

## 8. 交付物 (b) 重写摘要（280 词，可直接替换）

**替换说明（供作者与编辑核对，不入稿）**：

- `FAERS` → 全称 "the United States Food and Drug Administration Adverse Event Reporting System"（未缩写、未再定义缩写）；
- `ROR` → "reporting odds ratio"；`RORR` → "ratio of reporting odds ratios"；`CI` → "95% confidence interval"；三者均以完整词组出现，**摘要中不出现任何缩写**；
- 原稿的 `a = 1` → 改为 "a single report"（消除未定义的 2×2 单元格符号）；
- 原稿的 "preferred term" → 改为 "the dictionary term carrying the same concept" / "a term in either dictionary"（消除未向临床读者解释的专有名词）；
- 删除原稿 Methods 中"两个 a priori 结局不可估计"的技术枝节（属 READUS-PV 可由正文承担的内容），把腾出的词数用于补上原摘要缺失的**信号判定标准**与**阴性对照方向**，使摘要在不增词的前提下信息密度更均衡。
- 字数：**280 词**（含 Introduction./Methods./Results./Discussion. 四个段首标签），落在 250–300 区间且留 20 词余量。

---

**Introduction.** Hyperalgesia after remifentanil has a large prevention literature, but the clinical evidence is contested and real-world reporting unexamined.

**Methods.** We analysed spontaneous reports from two national databases: the United States Food and Drug Administration Adverse Event Reporting System (primary; 20 692 687 reports) and the Health Canada Canada Vigilance line-listing (confirmation; 1 154 017 reports). Cohorts were remifentanil, fentanyl, sufentanil and morphine. We calculated the reporting odds ratio, proportional reporting ratio, information component and empirical Bayes geometric mean for each drug and event, and compared remifentanil with each comparator as the ratio of reporting odds ratios. Each term was first checked for retrievability, since a count is returned only if the dictionary stores that term. Four established opioid side effects were negative controls and one non-pain term a specificity probe.

**Results.** The clinical word hyperalgesia is not a term in either dictionary and returned no report, whereas the dictionary term carrying the concept returned reports in both and met the signal criterion for all four opioids, remifentanil included (reporting odds ratio 4.73, 95% confidence interval 2.54 to 8.80). That rested on ten remifentanil reports, eight from 2024; excluding 2024 from the 2015 to 2024 window left one report and no signal, and Canada did not reproduce it. For pain, remifentanil reported less than every comparator in both databases (ratio of reporting odds ratios 0.066 and 0.046 in the United States, 0.235 and 0.146 in Canada) and less than every negative control, stably across years and with serious reports only.

**Discussion.** The answer depended on the dictionary term chosen, so the analysis is hypothesis-generating. A zero obtained from the clinical name alone is an artefact of terminology, not evidence of safety.

---

## 9. 交付物 (c) 投稿前必改清单（8 条）

| 序号 | 必改内容 | 不改的后果 |
|---|---|---|
| 1 | 删除 `I_正文_IMRaD_en.md` 的 `:15` "Formatting note (not for submission)"、`:217` 参考文献前的说明句、`:528–566` 的 §9 与 §10 全节；删除 `:13` 中的 "Verified with `_wordcount.py`"；把 §9 溯源表改作 online Supporting Information Appendix S2 提交 | **会被 desk-reject**（内部工作信息随稿提交，§10 披露"本环境打不开 github 页面""无 reviewer suggestions""更新于 round 2 之后"，足以触发科研诚信询问） |
| 2 | 投稿信题名改为与稿件题名逐字一致（现两处副标题完全不同）；并修正投稿信中 "ten calendar years"（实为 8 年可估计）、"four tables"（实为 6 张带题注的表）、SI 位置描述 | **会被 desk-reject**（题名不一致在 triage 阶段必然被发现） |
| 3 | 删除两图内的 legend box（`05_figures.py:170`、`:221` 两处 `ax.legend(...)`），符号说明全部移入图注；把 Figure 1 图注 "grouped from the top" 改为 "from the bottom" | **会被要求返修**（本刊明文 "no titles, plot frames, gridlines or legend boxes within the graphs"；图注方向与图相反会连带损害"数字已核对"的声明） |
| 4 | 把 Table S1/S3/S4/S5 的表格内容从正文文件移出，与 READUS-PV 检查表（S2）合并为**一个**独立 Supporting Information 文件，正文只保留题注并改用 "online Supporting Information Table Sx" 写法 | **会被要求返修**（本刊明文 "uploaded as separate documents and not included in the main document file"、"all supporting tables in one file"） |
| 5 | 全稿 11 处 "defined a priori" 统一改为如实表述（"specified in the analysis plan, which was written after data extraction and before the results were interpreted"），并在 Methods 与 Limitations 明确声明未前瞻注册；同步修改 `ANALYSIS_PLAN.md:36` 与投稿信 `:20` | **会被要求返修；若作者拒绝，升级为 Reject**（与随稿计划书自陈 "written post hoc" 直接冲突，属科研诚信条款下的可核查陈述） |
| 6 | Table 3 与 Table S1 的全部估计补 95% CI（或在表格中标注 `point estimate only; 95% CI not computed`）；§3.7、§3.9 的比率补区间；同步把 READUS-PV 检查表 Part A 第 9 条的措辞改为与实际一致 | **会被要求返修**（自查表声称"每个估计都有 95% CI"，实际三处没有） |
| 7 | 修正三处引用/编号错误：Table S2 题注 `[10, 11]` → `[13, 14]`；refs 29、30 作者列由 7 位改为"前 3 位 + et al."（Crossref 已核实均为 7 位）；Table 4C/§3.8/摘要的 "(a = 1)" 明确写成"在 2015–2024 窗口内排除 2024 年后" | **会被要求返修**（生产编辑与统计审稿人都会逐条核对） |
| 8 | AI 声明补齐工具名与版本、使用日期、隐私与合规三项，并加一句作者已逐篇核读被引文献；同时消除"每个数字都由归档脚本直接读出"与 `05_figures.py:179–185` 手写常量的矛盾（推荐把 Figure 2 改为运行期读取 `04_sensitivity_year_pain.csv`）；建议随仓库提供 `refs_verification.csv` | **建议改**（若编辑在返修中追问，会升级为"会被要求返修"） |

**另附三条"建议改"（不计入 8 条）**：① 正文压缩至 ~3 850 词以规避计数口径风险（可删段落见 P1-5）；② 题名去掉 "with a terminology caution"，改用含设计词的表述；③ 投稿只上传 `.tif`/`.pdf` 图件，不上传 `.png`。
