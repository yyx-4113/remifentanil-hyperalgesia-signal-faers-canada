# 第二轮同行评审报告（复审 + 扩大专家团）

**稿件标题：** Remifentanil and hyperalgesia reporting in two national pharmacovigilance databases: a head-to-head disproportionality study with controls defined a priori
**送审版本：** `main` @ `0695a91`（tag `v1.1.0`），正文 3 983 词 / Summary 299 词
**目标期刊：** *Anaesthesia* (Wiley / Association of Anaesthetists) — Original Article
**第一轮决定：** Major Revision；**本轮性质：** 复审（re-review）+ 新增两名专家
**评审日期：** 2026-09-17

> **说明。** 本报告为**模拟同行评审**，用于稿件内部质量提升，不是真实期刊评审流程。所有对数字的质疑均已回到原始数据源（`01_faers_results.csv`、`04_sensitivity_ps_only.csv`、`10_term_dictionary.csv`、`cv/cv_pt_summary.csv`，以及 Canada 抽取原始文件 `reactions.txt`，4 474 923 行）逐条重算验证，不经任何中间摘要转述。

---

## 0. 编辑部总体评价与决定

**决定：Major Revision（第二轮）。**

第一轮 13 条意见已实质落实，稿件由一个"阴性结果研究"成功转型为**术语学警示**研究，方向正确、论点站得住、且比原版更有发表价值。三位复审专家一致认为新的核心论点（临床用词 HYPERALGESIA 是低位语、零值来自词典而非数据）是本稿真正的贡献。

但本轮发现 **4 处可证伪的事实错误**，其中 3 处位于**摘要或结论**，且**现有 385 条门禁全部未能拦截**。另有 1 处**结构性缺口**：论文的新核心发现（HYPERAESTHESIA 4.73, 2.54–8.80）**从未进入任何敏感性分析**。此外，本轮暴露出**门禁自身存在互相矛盾的断言**——它把一个错误数字（521）固化成了"必须包含"的检查项，因此"385 条全绿"目前提供的是虚假的安全感。

**这不是文风问题，是数字问题。** 一句话可修的有 3 处，需要重跑查询的只有 1 处。但不清零就投稿，风险极高：这些错误都位于审稿人最先读、也最容易被一个 grep 推翻的位置。

---

## 1. 第二轮评审专家团

| 编号 | 专业领域 | 本轮职责 | 状态 |
|---|---|---|---|
| **R1** | 生物统计与药物警戒方法学 | 复审第一轮 A2/A3/A5/A6；新查多重性、敏感性覆盖、CI 近似 | 复审 |
| **R2** | **MedDRA 术语学与编码本体** | 审查代理术语的有效性与特异性 | **新增**（因 A2 已改变论文方向，术语学须有专职专家） |
| **R3** | 临床麻醉与 OIH 证据 | 复审 B1/B2/B3 | 复审 |
| **R4** | 药物流行病学与 READUS-PV 报告规范 | 复审 C1/C2/C3；新查 a priori / post hoc 披露 | 复审 |
| **R5** | **数据溯源与可重复性审计** | 逐数回源核验；**审计门禁本身** | **新增**（第一轮无此角色，而本轮全部硬伤都在这一层） |
| **R6** | 学术英语与 *Anaesthesia* 发表规范 | 复审 D1/D2；抽查数字型措辞 | 复审 |

---

## 2. 第一轮 13 条意见逐条复核

| # | 原意见 | 判定 | 复核证据 |
|---|---|---|---|
| P0-1 | A1/C3：`prespecified` 诚信问题 | ✅ **已落实** | 全库检索 `prespecified`：正文/封面信/README/清单为 0（仅 READUS 条目原文保留 2 处）；新增 `ANALYSIS_PLAN.md`，门禁用正则断言 `Prospective registration:** none` |
| P0-2 | A2：5 个零术语须证明 PT 级 | ✅ **已落实且超出要求** | 不仅澄清层级，还实测出 HYPERALGESIA 为 **LLT**（父 PT 10020568），并据此**更正主结论**；新建 `10_term_dictionary.csv`（18 术语 × 双库双层计数）与 Table S4 |
| P0-3 | D1：探针"方向反转"过度概括 | ✅ **已落实** | §4.1 改为 "a specificity probe behaved inconsistently between them"；§3.4 如实写出 FAERS 同向、Canada 反向 |
| P1-4 | A3：ALLODYNIA n=1 不得作方向性论断 | ✅ **已落实** | 表 2 加 † "not estimable…shown only to document that report"；已移出 Figure 1；图注明写不展示理由 |
| P1-5 | A4/C1：主/验证分配倒置 | ✅ **已落实** | §2.1 新增整段论证 FAERS 为"体量 vs 纯度"的权衡；§4.5 补"Canada suspect-role 分析已复现 PAIN 方向" |
| P1-6 | A5：SOC 全景探索性 + 阳性对照事后 | ✅ **已落实** | §3.7 明标 "exploratory and hypothesis-generating…no multiplicity correction"；§3.9 改名 "Post hoc demonstration" |
| P1-7 | B3：适应症混杂循环风险 | ✅ **已落实** | §4.5 "Setting and residual confounding" 独立成段，明写"非中介分析" |
| P1-8 | B1：方法学定位 | ✅ **已落实** | 题名、§1 末段、封面信均改写为 "methodological caution" |
| P2-9 | C2：加 JADER 第三库 | ❌ **未落实，且陈述失准** | 见 **P1-7**：正文反称 "Neither JADER nor a European database could be retrieved"，与第一轮评审记录冲突 |
| P2-10 | B2：PAIN 作为 surrogate 的桥接 | ✅ **已落实** | §2.3 改为 "a pragmatic and necessarily imperfect proxy" + 引 [17]；明写"不可反向推断" |
| P2-11 | B4：扩充参考文献 | ✅ **已落实** | 20 → 30 篇，按首引顺序编号，门禁校验连续性与无越界引用 |
| P2-12 | D2：弱化 "structurally unable" | ✅ **已落实** | 门禁已设禁止性断言；全文检索为 0 |
| P2-13 | A6/C4/C5/D3：统计近似、使用条款、AI 声明、图 1 占位 | ⚠️ **部分落实** | C4/C5/D3 已落实；**A6 仅定性说明，未量化**——见 **P2-4**（本轮已代算） |

**小结：** 13 条中 11 条完全落实、1 条部分落实、1 条未落实且衍生出新的诚信问题。

---

## 3. 第二轮新发现

### 3.1 P0（必须清零，否则退稿风险）

---

#### **P0-1｜摘要与 §3.2 的 "521 Canadian reaction rows" 与权威源不符，正确值为 523**

**提出人：** R5（数据溯源审计）

**位置（4 处）：**
- `I_正文_IMRaD_en.md` **L25**（Summary）：`…present in both databases (8 161; 521)…`
- `I_正文_IMRaD_en.md` **L105**（§3.2）：`…(8 161 FAERS reports, 521 Canadian reaction rows)…`
- `README.md` L25
- `I_TableS2_READUS-PV_checklist.md` L66

**证据（三重，逐层回源）：**
1. `10_term_dictionary.csv` L15 → `HYPERAESTHESIA, …, 523, yes`
2. 稿件 Table S4（L459）→ `523`
3. **直接从 Canada 原始抽取重数**：`reactions.txt`（4 474 923 行，字段以 `$` 分隔、PT 英文在第 6 字段、大小写混合）→ **Hyperaesthesia = 523**

同一次重数还验证了其余术语，全部与 `10_term_dictionary.csv` 一致（Pain 49 260、Nausea 64 611、Allodynia 29、Drug tolerance 387、Procedural pain 1 527、Drug withdrawal syndrome 1 667、Chronic pain 0、Hyperpathia 0），**证明是"521"这一处孤立错误，而非系统性偏差**。

**严重性：** 这是论文新主结论的两个支撑数字之一（8 161 / 521），位于摘要第一结果句。

**修改要求：** 4 处全部改 523；门禁把 `"521"` 从"必须包含"翻转为"必须不包含"（见 §5 G-1）。

---

#### **P0-2｜摘要与结论称"每一年（2015–2024）/ 十个日历年"，实际仅 8 年可估计**

**提出人：** R1（统计）+ R6（措辞）

**位置（3 处）：**
- L25（Summary）：`…and in every year from 2015 to 2024.`
- L147（§4.1）：`…stably across serious-report restriction and ten calendar years…`
- L191（§5 结论）：`…stable across serious-report restriction and ten calendar years…`

**证据：** Table 4B（L329–341）中 **2018 与 2019 瑞芬太尼 PAIN a = 0，无估计**；正文 §3.8（L135）自己写明 `remifentanil had no PAIN reports in 2018 or 2019, so no estimate was possible`。可估计年份为 2015、2016、2017、2020、2021、2022、2023、2024 = **8 年**。

**严重性：** 摘要与结论自我矛盾于结果段；"every year"是一个读者用一张表就能推翻的绝对化断言。

**修改要求：** 三处统一改为 `in the eight years in which an estimate was possible` / `eight calendar years`。门禁加禁止性断言 `assert "ten calendar years" not in ms` 与 `assert "in every year from 2015" not in ms`。

---

#### **P0-3｜§3.2 断言其余四个串"表现完全相同"（相邻 token 也返回零），但 CHRONIC PAIN 相邻 token 查询返回 1**

**提出人：** R2（术语学）+ R5

**位置：** L103（§3.2）：`an adjacent-token search returned zero. The other four hyperalgesia-related strings behaved identically…`

**证据：** Table S4（L451）CHRONIC PAIN 行 → `FAERS adjacent-token phrase = 1`；`10_term_dictionary.csv` L7 → `1`。

**严重性：** 这是全文唯一一处可被读者用一个查询直接推翻的断言，且恰好落在论文最核心的段落（"零是词典属性"这一论点的证据链上）。它不影响结论（1 个相邻 token 命中不是精确 PT 匹配），但**表述超出了数据**。

**修改要求：** 改为 `the other four returned no exact-match report; one of them (CHRONIC PAIN) returned a single adjacent-token hit, which is not an exact preferred-term match and does not change the conclusion.`

---

#### **P0-4｜新主结局 HYPERAESTHESIA 完全未进入任何敏感性分析**

**提出人：** R1（统计）——**本轮最重要的发现**

**位置：** Table 4A（L307–325，严重报告限制）、Table 4B（L327–342，年份分层）、§3.8（L135）。

**证据：** `04_sensitivity_ps_only.csv` 只含 **13 个 PT**（第一轮前的 a priori 集），**5 个 dictionary proxy 一行都没有**；`04_sensitivity.py` L5 明写"重算 **13 PT** × 4 药"，`PTS` 硬编码。即：Amendment 1 之后新增的 5 个术语（含新的主结局）从未被纳入稳健性检验。

**后果：** 论文现在的核心数字（瑞芬 10 例，ROR 4.73，2.54–8.80）在唯一的稳健性检验中**不存在**。审稿人必然问：限制为严重报告后这 10 例还剩几例？信号是否消失？目前无法回答。

**修改要求（须重跑查询，非文字修改）：**
1. 把 5 个 proxy（HYPERAESTHESIA、HYPERPATHIA、PROCEDURAL PAIN、CHRONIC PAIN SYNDROME、DRUG WITHDRAWAL SYNDROME）加入 `04_sensitivity.py` 的 `PTS`，重跑，Table 4A 增补 5 行；
2. 年份分层（Table 4B）同样尝试 HYPERAESTHESIA——若因 a 太小不可行，须在表注明示"瑞芬太尼多数年份该术语计数为 0，无可估计年份"，而不是留白；
3. 门禁新增断言：Table 4A 的行集必须等于 Table 2 的 18 术语行集。

---

### 3.2 P1（必须修改）

---

#### **P1-1｜Table 2 的星号是手工渲染的，与源布尔值不一致**

**提出人：** R5

> **【2026-09-17 修订本条】** 初稿本条凭目视认定"PRURITUS-芬太尼 0.503 被误标星号"。改用脚本逐格比对后发现**该判断有误**：稿件中 0.503 **本就没有星号**，与源文件的 `FENTANYL_signal = False` 一致。真实的不一致在别处，见下。**教训：星号这类符号必须用脚本比对，目视不可靠——这正是本条要求做的事。**

**实际错误（脚本查实）：** DRUG WITHDRAWAL SYNDROME 的**舒芬太尼**列，稿件为 `1.53 (1.13–2.07)`，**缺星号**；而 `01_faers_results.csv` 中 `SUFENTANIL_signal = True`（a = 42 ≥ 3，CI 下限 1.13 > 1）。这是全表 43 个可估计单元格中唯一的不一致。

**证据：** `_check_asterisks.py` 逐格比对结果：`checked 43 estimable cells across 18 terms; mismatches = 1`（修正后为 0）。

**修改要求：** 补上该星号；**并要求表 2/表 4A 的星号改由脚本从 `*_signal` 列渲染**，门禁逐格比对"星号 ⇔ signal == True"——目视核对在本例中先漏掉了真错误、又制造了一个假错误。

---

#### **P1-2｜Table 4A 的 "Signal" 列与源 CSV 矛盾，且两个脚本的信号判定规则不同**

**提出人：** R1

**证据：**
- `04_sensitivity_ps_only.csv` → `ALLODYNIA, …, 1, 3.105, -1.197, True`（signal = True）
- 稿件 Table 4A（L312）→ `| ALLODYNIA | 1 | 3.105 | **no** |`
- 根因：`04_sensitivity.py` L82 的判定为 `(lower CI > 1) or (PRR >= 2)`，**无 a ≥ 3 要求、无 χ² > 4**；而主分析 §2.4 的规则为 `a ≥ 3 且 CI 下限 > 1，或 PRR ≥ 2 且 χ² > 4`。

**判定：** 稿件的 "no" 是对的（a = 1 不应判信号），**源文件的 True 是脚本缺陷**。但这使 Table 4A 的 Signal 列不可溯源——与本项目"每个数字可追溯到产物文件"的标准冲突。

**修改要求：** 统一两处判定规则（建议敏感性沿用主分析规则并加 a ≥ 3），重跑后重新渲染 Table 4A；若刻意保留放宽规则，须在表注写明。

---

#### **P1-3｜Figure 1 图注一句话内三处错误**

**提出人：** R6（措辞）+ R2

**位置：** L471：`…and the **two** proxy terms too rare to estimate in the remifentanil cohort (**HYPERPATHIA, CHRONIC PAIN SYNDROME, DRUG TOLERANCE**) are not estimable…`

**错误：** ① 说 "two" 却列了 **3 个**术语；② **DRUG TOLERANCE 不是 proxy**，它属于 a priori broad 组；③ DRUG TOLERANCE 也不是"too rare"——它可检索（全库 5 013 行），瑞芬太尼是 **0 例（a = 0）**，性质是"零"而非"稀有"。

**修改要求：** 改写为 `HYPERPATHIA and CHRONIC PAIN SYNDROME (too rare in the remifentanil cohort) and DRUG TOLERANCE (no remifentanil report) are not estimable and are not shown.`

---

#### **P1-4｜舒芬太尼的头对头比值被计算却从不展示，"全部低于 1"类表述无法被读者审计**

**提出人：** R1 + R4

**证据：** `01_faers_results.csv` 含 `RORR_REMI_vs_SUFENTANIL` 列，其中 > 1 的有 **PRURITUS 1.31 (0.84–2.04)**、**PROCEDURAL PAIN 2.124 (0.89–5.07)**。但 Table 2、Table 3、Figure 1 **均无舒芬太尼头对头列**。

**受影响表述：**
- L109（§3.3）：`the ratio against fentanyl is 1.96, the only one above 1 in that comparison set`
- L117（§3.4）：`all eight ratios were below 1`

两句在"只报两对照"的前提下都成立，但**读者无法核验前提**，且"为什么排除舒芬太尼"从未说明。

**修改要求（二选一）：**
- **(a)** Table 2 增加 `RORR vs sufentanil` 列、Figure 1 增加第三组符号（最透明，推荐）；或
- **(b)** 在 §2.4 明确说明舒芬太尼不作为头对头对照的理由（队列最小 6 513、与瑞芬太尼同属术中用药、对照价值有限等），并把 §3.3/§3.4 改为 `among the two comparators reported here` 类限定语。

---

#### **P1-5｜代理术语为事后添加（Amendment 1），但摘要未披露、Table S4 未标注**

**提出人：** R4（READUS-PV）

**事实：** 5 个 dictionary proxy 是在观察到零之后于 2026-09-16 加入的（`ANALYSIS_PLAN.md` Amendment 1 已诚实记录）。但：
- **摘要 Methods（L23）完全未提**这一 amendment；
- §2.3（L67）仅用被动式 `were added`，**未给日期、未说明"在零之后"**；
- Table S4 未标 post hoc。

**风险：** 标题说 `controls defined a priori`（阴性对照确实 a priori，此说**准确**），但读者可能读成"全部结局 a priori"，而真正产出主发现的术语并非如此。READUS-PV 第 3 条（假设是否预先设定）与第 14d 条（方案注册）均要求交代这一点。

**修改要求：**
1. 摘要 Methods 增补 `the proxies were added after the zero counts were observed and are dated in the archived plan`（约 15 词，摘要余量 1 词——需先在别处省出 ~15 词）；
2. §2.3 明确 `added on 16 September 2026, after the zero counts had been observed`；
3. Table S4 在 5 个 proxy 行的 Group 列标注 `dictionary proxy (added a posteriori, 16 Sep 2026)`；
4. **建议**（非必须）：题名改 `with negative controls defined a priori`（19 词，仍 ≤ 20），彻底消除歧义。

---

#### **P1-6｜主分析缺少多重性说明——但补上反而能加强论点**

**提出人：** R1

**事实：** Table 2 为 18 术语 × 4 药 ≈ 72 次比较，§2.4 与 §3 均未提多重性（§3.7 只为 SOC 全景声明了探索性）。

**本轮已代作者计算（可直接引用）：** 以 Woolf SE = 0.317 计，对瑞芬太尼 HYPERAESTHESIA（4.729，2.54–8.80）作 Bonferroni 校正：

| 校正范围 | m | 校正后 CI 下限 | 结论 |
|---|---|---|---|
| 18 术语 × 4 药 | 72 | **1.614** | 仍 > 1 |
| 仅 18 术语 | 18 | 1.832 | 仍 > 1 |
| 仅 14 个可检索术语 | 14 | 1.878 | 仍 > 1 |

**修改建议（加强项，非扣分项）：** 在 §3.3 或 §4.5 加一句：`Applying a Bonferroni correction across all 72 drug–term comparisons leaves the remifentanil HYPERAESTHESIA lower bound above 1 (1.61), so the corrected signal is not an artefact of multiplicity.` 一句话终结该质疑。

---

#### **P1-7｜局限称"JADER 与欧洲库均无法获取"，与第一轮记录及项目连通性日志冲突**

**提出人：** R4 + R5

**位置：** L179（§4.5）：`Neither JADER nor a European database could be retrieved, so cross-regional confirmation remains a planned extension…`

**证据：** 第一轮评审 C2 明确记载"稿件记忆中曾确认日本 JADER（info.pmda.go.jp）可达"；项目MEMORY同样记录 JADER 可达。因此"could not be retrieved"这一陈述**比项目自身记录更强**，且未给出不可获取的具体原因。

**修改要求（二选一）：**
- **（弱）** 把该句改为精确表述，例如 `JADER's downloadable files do not carry the English preferred-term and suspect-role fields this design requires, and EudraVigilance offers no bulk line-listing, so neither was usable here`——即说明"不可用"的**具体理由**；
- **（强，推荐）** 补做 JADER 作为第三库，仅复现"5 个零术语 + PAIN 低报方向"即可，把"two-database"升级为跨监管区三角验证。

---

#### **P1-8｜HYPERAESTHESIA 作为 OIH 代理的特异性未讨论，且跨药排序与临床预期相反**

**提出人：** R2（术语学）+ R3（临床）

**事实：**
1. **语义特异性：** MedDRA 中 HYPERAESTHESIA 指"对刺激的敏感性增高"，并非 OIH 的同义 PT；它与 OIH 之间是"最接近的可用 PT"关系，不是等价关系。稿件目前只说它"承载该概念"（carries the concept），未说明承载得有多松散。
2. **排序反转（关键）：** 实测 ROR 为 **吗啡 12.17 > 舒芬太尼 8.61 > 芬太尼 6.80 > 瑞芬太尼 4.73**。而临床文献的共识方向恰恰相反——瑞芬太尼被认为 OIH 风险最高（短效、快速耐受）。

**现稿件处理：** §4.1 仅含蓄写"瑞芬太尼的最弱"，未解释这个反向排序。审稿人几乎肯定会问：如果代理术语在吗啡上信号最强，它衡量的还是 OIH 吗？

**修改建议（这是加强而非削弱论点）：** 在 §4.2 或 §4.4 明确写：代理术语的跨药排序与 OIH 临床预期相反，说明 HYPERAESTHESIA 捕捉的更可能是**报告场景与编码习惯**（慢性疼痛场景下的吗啡报告更多感觉异常；而瑞芬太尼用于麻醉/镇静中的患者，无法主诉感觉过敏），而非 OIH 特异性。这恰恰**强化**了"术语学警示"这一主旨——即使找到了正确的 PT，它捕捉的仍然是报告背景。

---

### 3.3 P2（强烈建议）

| # | 位置 | 问题 | 建议 |
|---|---|---|---|
| **P2-1** | §3.3 | **DRUG TOLERANCE 未被提及**。它是 broad 组唯一可检索术语，瑞芬 **0 例**而芬太尼 278（ROR 9.94*）、吗啡 79（5.86*）——这是真实的、可解释的阴性结果，且与 OIH 概念相邻 | §3.3 补一句，与"瑞芬不报耐受"并列呈现 |
| **P2-2** | Table 2 | 只给瑞芬太尼的 `a`，三个对照药的 `a` 全缺，读者无法核验任何 OR | 增列四药 `a`，或移入新增 Table S5 |
| **P2-3** | L109 | `HYPERPATHIA and CHRONIC PAIN SYNDROME were too rare to estimate in either database` 不准确——它们在**对照药**中可估计且达信号（HYPERPATHIA 芬太尼 a=2 ROR 8.24*、舒芬 a=1 ROR 75.63*） | 改为 `too rare in the remifentanil cohort` |
| **P2-4** | §2.4 | A6 遗留：Woolf 独立性近似只作了定性说明 | 补一句量化（已代算）：共享背景的协方差约 4.8 × 10⁻⁸，占 Woolf 方差不足 **0.0001%**，且忽略它使 CI 偏宽（保守）。一句话终结 |
| **P2-5** | Ref [30] | 用于支撑"跨库编码差异"的 Vermeer 2013 实为**生物药可追溯性**研究，相关性偏弱 | 换成直接比较 FAERS/EudraVigilance 编码不一致的文献 |
| **P2-6** | §10 | 内部待办仍写 `S1–S3`（应为 S1–S4）；虽不随稿提交，但仓库一致性应保持 | 同步 |
| **P2-7** | Checklist L66 | 含 "521"，须与 P0-1 同步 | 改为 523 |

---

## 4. 必须补做的分析（非文字修改）

| # | 任务 | 关联 | 说明 |
|---|---|---|---|
| **C-1** | 把 5 个 proxy 加入 `04_sensitivity.py` 的 `PTS`，重跑严重报告限制分析 | P0-4 | openFDA：`search=serious:1 AND patient.drug.activesubstance.activesubstancename.exact:"REMIFENTANIL" AND patient.reaction.reactionmeddrapt.exact:"HYPERAESTHESIA"`，逐药逐术语取 `total` |
| **C-2** | 年份分层补 HYPERAESTHESIA；若不可行须显式说明 | P0-4 | a = 10，多数年份预计为 0 |
| **C-3** | 统一主分析与敏感性分析的信号判定规则并重跑 | P1-2 | 建议统一为 `a ≥ 3 且 CI 下限 > 1，或 PRR ≥ 2 且 χ² > 4` |
| **C-4** | 决定舒芬太尼头对头列的取舍 | P1-4 | 加列最透明 |
| **C-5** | （可选但推荐）JADER 第三库 | P1-7 | 仅需复现 5 零术语 + PAIN 方向 |

---

## 5. 门禁缺陷与加固要求（R5 专项）

**核心判断：** 现有 385 条断言全部通过，却同时容纳了 `521`（正文）与 `523`（Table S4 ↔ CSV）。这说明门禁存在**设计缺陷**：它把"正文必须包含某字符串"当作正确性证明，而这个字符串本身可能是错的。

| # | 缺陷 | 证据 | 加固要求 |
|---|---|---|---|
| **G-1** | **门禁自身断言互相矛盾**：`_check_consistency.py` L462 的 `TD_EXP` 把 Canada 值定为 **523**，而 L583 却把 `"521"` 列入**必须包含**的正文字符串 | 两行同处一个文件 | 删除 `"521"`，改为**禁止性断言** `"521" not in ms`；所有正文数字改为从源 CSV 读出后比对，不再硬编码"必须包含" |
| **G-2** | 未校验 Table 2/4A 的**星号** ⇔ 源 CSV 的 `*_signal` 布尔值 | P1-1（PRURITUS/芬太尼）漏网 | 新增逐格断言；星号改为脚本渲染 |
| **G-3** | 未校验"可估计年数" | P0-2 漏网 | 新增断言：Table 4B 中可估计年份数 == 正文中声明的年数 |
| **G-4** | 未校验 Table 4A 的**行集**是否等于 Table 2 的 18 术语 | P0-4 漏网 | 新增断言：`set(4A rows) == set(Table 2 rows)` |
| **G-5** | 未校验图注中的**数量词**与所列术语个数一致 | P1-3（"two" vs 三个）漏网 | 新增正则断言：图注中 `the (two|three|four|five) … terms` 的英文数词须与紧随括号内术语个数匹配 |
| **G-6** | 未校验 §3.2 的"四串表现相同"与 Table S4 的相邻 token 计数 | P0-3 漏网 | 新增断言：若正文称某组串 adjacent-token 为 0，须与 `10_term_dictionary.csv` 逐行比对 |

**原则性建议：** 把门禁的"必须包含固定字符串"类断言**整体降级**为"必须从源文件读出并与正文比对"。前者只能防抄错，且会把错误固化；后者才能防错。

---

## 6. 请作者保持、勿在修改中削弱的强项

- 第一轮 A2 的处理远超要求：不仅澄清了层级，还**让主结论服从证据**（从"结构性缺失"改为"术语不可检索"），并产品化为 `10_term_dictionary.csv` + Table S4。这是本稿最大的资产。
- 数字-源文件溯源（§9）与 385 条一致性断言的框架本身是对的——**本轮的问题是断言的写法，不是框架**（见 §5）。
- 双库设计、原生 27 SOC、suspect-role 限定、精确活性成分匹配（避免 apomorphine/海洛因污染）均保持完好。
- 对稀释与混杂的诚实呈现（route 归因缺陷、role-agnostic、无个案去重）优于多数同类投稿。
- 第一轮 P0 三条全部实质落实，`prespecified` 已全库清除。

---

## 7. 修改后须重跑的验证

```
_wordcount.py          （改摘要/正文后必须先跑，再回填声明值；余量仅 1 词，改动须先做减法）
_check_consistency.py  （须 PASS，且新增 G-1~G-6 断言后为 400+ 条）
_gen_table_s1.py       （幂等）
_build_submission.py → _verify_docx.py（须 PASS 59）
```

**提交前最后一道人工检查：** 确认 Data availability 中仓库 URL 可解析。

---

## 8. 编辑部必改清单（汇总）

### P0（4 项，不清零即退稿风险）
1. **521 → 523**（4 处）+ 门禁翻转断言
2. **"every year / ten calendar years" → "eight years"**（3 处）
3. **§3.2 "四串表现相同"** 改为承认 CHRONIC PAIN 相邻 token = 1
4. **把 5 个 proxy 补入敏感性分析**（Table 4A + 4B），重跑

### P1（8 项，必须修改）
5. 补上 DRUG WITHDRAWAL SYNDROME-舒芬太尼缺失的星号，星号改脚本渲染 + 门禁逐格比对
6. 统一信号判定规则，重跑 Table 4A
7. Figure 1 图注"two / 三个 / DRUG TOLERANCE"三错修正
8. 舒芬太尼头对头列：加列或说明理由
9. 摘要与 §2.3 披露代理术语为事后添加（含日期）；建议题名加 "negative"
10. 补一句 Bonferroni 校正后下限仍为 1.61（加强项）
11. "JADER 无法获取"改为给出具体理由，或补做第三库
12. 讨论 HYPERAESTHESIA 的跨药排序与临床预期相反及其含义

### P2（7 项，强烈建议）
13. 补 DRUG TOLERANCE 结果；14. Table 2 补对照组 a；15. "too rare in either database" → "in the remifentanil cohort"；16. Woolf 近似量化一句；17. 替换 Ref [30]；18. §10 与 checklist 同步；19. 门禁加固 G-1~G-6。

---

*本轮评审由编辑部组织 6 位专家（含新增 MedDRA 术语学与数据溯源审计两名）独立出具。所有质疑均已回到原始数据源逐条重算，其中 Canada 术语计数直接由 4 474 923 行原始文件重新统计验证。未发现任何数据捏造；问题集中于（a）修订过程中引入的数字漂移、（b）新主结局缺少稳健性检验、（c）门禁断言设计缺陷。*
