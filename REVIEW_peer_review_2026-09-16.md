# 同行评审意见汇总（编辑部决策信 + 专家审稿报告）

**稿件标题：** Remifentanil and hyperalgesia reporting in two national pharmacovilance databases: a head-to-head disproportionality study with prespecified controls
**目标期刊：** *Anaesthesia* (Wiley / Association of Anaesthetists)
**审理方式：** 编辑部组织 4 位学组专家（方法学与药物警戒统计 / 临床麻醉与 OIH 证据 / 药物流行病学与数据库及报告规范 / 学术英语与发表规范）独立审稿
**编辑部决定：** **Major Revision（重大修改后复审）**

---

## 0. 编辑部总体评价（Handling Editor's Overview）

这是一项设计精巧、透明度很高的药物警戒研究。其核心贡献不在"瑞芬太尼是否致痛觉过敏"这一临床问题，而在于一个**方法学警示**：自发报告系统缺乏编码 OIH 的优先术语（PT），且瑞芬太尼的低报完全由报告场景（严重、围术期、医护上报）驱动，因此一类"阴性"药物警戒研究在 OIH 领域实质上是**结构性的非信息性结果**。这一论点经双库独立复现、内部一致性校验、完整溯源与 AI 使用声明，论证链条相当扎实，且复现包已公开（MIT、含 v1.0.0 资产）。

但稿件在**诚信呈现、核心论断的稳健性、数据库角色分配、摘要措辞、期刊契合度**五处存在必须修改的硬伤，另有若干提升项。若修改到位，本稿适合以 *Anaesthesia* 的 **Original Article** 或 **Special Article（方法学警示类）** 形式发表；若仅做表面润色而回避下述 P0/P1，将被拒。

---

## 1. 审稿人 A —— 方法学与药物警戒统计

### 主要意见（Major）

**A1. "预先设定（prespecified）"的诚信问题（最严重）。**
稿件在摘要、引言、方法、讨论反复使用 "prespecified negative controls / specificity probe / prespecified set of hyperalgesia terms"。但复现包（含 README、分析脚本、数据提取日期 16 Sep 2026）是**分析完成后才建立**的，没有任何前瞻性注册（preregistration）或带时间戳、早于数据提取/结果解读的分析计划。READUS-PV 清单也将 "protocol registration" 标记为 N/A。
- 问题：整个"诊断性零结果"的论证（阴性对照 + 特异性探针）取决于对照是否**真正**预先设定；若对照是事后为合理化零结果而选，论证即崩塌。审稿人必然质疑。
- **修改要求：** 在仓库中存入一份**标注定稿日期的分析计划**（明确写清："本计划在数据提取后、任何结果解读前定稿，未做前瞻性注册"），并将正文 "prespecified" 改为 "defined a priori in the analytical plan"（并在方法学局限中坦承未前瞻性注册）。切勿继续使用暗示前瞻性注册的 "prespecified" 一词。

**A2. 5 个"零术语"必须证明为 MedDRA PT 级，而非查询假象（潜在致命弱点）。**
稿件核心论断"HYPERALGESIA / PAIN INCREASED / POSTOPERATIVE PAIN / CHRONIC PAIN / OPIOID WITHDRAWAL SYNDROME 在全库为零"是"结构性缺失"结论的基石。该结论有两个未澄清的前提：
- 这些术语是否真的是 **PT（preferred term）级**、且会出现在 `patient.reaction.reactionmeddrapt` 字段？若某个术语实际只作为 **LLT（lowest level term）** 存在，则 `.exact` 查询天然匹配不到——此时"全库为零"是**查询假象，而非报告现实**。POSTOPERATIVE PAIN、CHRONIC PAIN 确为 PT，但 HYPERALGESIA 在部分 MedDRA 版本中层级需核实。
- 必须明确声明所用的 **MedDRA 版本**（openFDA 与 Canada 各自的版本可能不同）。
- **修改要求：** 在方法 §2.3 与补充材料中（a）声明 MedDRA 版本；（b）逐条确认这 5 个术语为 PT 级、可被 `reactionmeddrapt.exact` 命中；（c）若 HYPERALGESIA 仅为 LLT，须如实改成"该术语在 PT 层不可查"，并弱化"结构性缺失"的措辞。§3.2 已用常见疼痛术语验证查询路径未断，这很好，但**不能替代 PT/LLT 层级的澄清**。

**A3. ALLODYNIA 的"方向相反"结论建立在 n=1 上，不应作方向性论断。**
瑞芬太尼 ALLODYNIA a=1（ROR 3.47, 95% CI 0.49–24.67），头对头 RORR 0.455/0.342 均建立在这个单例之上。稿件虽在 §3.3 加注"估计不稳定"，但仍称其为"唯一可分析的痛觉过敏相关术语"并得出"方向与研究假设相反"的论断。
- **修改要求：** 将 ALLODYNIA 头对头严格标记为 **"not estimable / uninformative due to a single remifentanil report"**，删除任何方向性结论；其价值仅在于"瑞芬太尼无信号"这一阴性事实，而非"方向如何"。

**A4. "主分析 / 验证"分配与数据质量倒置。**
FAERS 臂是报告级、role-agnostic（不区分可疑药物）、无 FDA 个案级去重、route 字段存在严重归因缺陷（§4.6，route 计数累加达 184%）；Canada Vigilance 臂则是 suspect-role 限定、源头去重、原生 27 SOC、原生 MedDRA。稿件自己也在 §3.7、§4.6 称 Canada 为"权威（authoritative）"。然而稿件却把较弱、假设更多的 FAERS 标为 **primary analysis**，把更强、更严谨的 Canada 标为 **confirmation**。
- **修改要求：** 要么将 Canada 改为主分析、FAERS 改为验证（并相应调整摘要/引言表述），要么在方法 §2.1 用一整段**明确论证为何以 FAERS 为主**（例如体量、覆盖年份），承认这是对"数据质量 vs 体量"的权衡，而非默认。

**A5. SOC 全景（27 类）是探索性 fishing，却被当作"发现"呈现；"免疫类阳性对照"是事后观察。**
§3.7 与 §3.9 对 27 个 SOC 做全景比较、并提出"免疫类（过敏性休克）阳性对照证明仪器能检出信号"。这实质是（a）多重比较的探索性分析，未做任何多重性校正；（b）"阳性对照"是**事后**发现的，并非预先设定。
- **修改要求：** 将 §3.7 的 SOC 全景明确标注为 **exploratory / hypothesis-generating**；将 §3.9 的"阳性对照"措辞弱化为"a post hoc demonstration that the pipeline detects signals when present"，并把其作为支持"方法非缺陷"的**辅助证据**而非正式对照。

### 次要意见（Minor）
- **A6.** 头对头 RORR 的 CI 用 Woolf 倒数单元格求和，但两个 ROR 共享同一背景参照 'd'，存在轻微相关未校正；属常规忽略，建议在 §2.4 加一句说明此近似。
- **A7.** 信号判定规则（a≥3 且 ROR 的 95% CI 下限 >1，或 PRR≥2 且 χ²>4）是标准做法，建议补一句引用 van Puijenbroek 2002 之外的关于阈值选择的文献。

---

## 2. 审稿人 B —— 临床麻醉与 OIH 临床证据

### 主要意见（Major）

**B1. 期刊契合与文章类型：本稿的真正贡献是方法学，而非临床。**
标题与框架以"瑞芬太尼痛觉过敏报告"这一临床实体为锚点，但结论明确表示自发报告**无法**回答该临床问题（"spontaneous reporting is structurally unable to detect it"）。真正的贡献是一条**方法学通约**：OIH 类阴性药物警戒研究是结构性非信息性的。*Anaesthesia* 可能更欢迎将其作为 **Special Article / Methods** 或 **Editorial-style caution**，而非以 Original Article 呈现临床发现。
- **修改要求：** 在投稿信与引言中明确这一定位（"a methodological caution, not a clinical trial of remifentanil"），并考虑在讨论开头用一段把"临床问题 vs 方法学贡献"的边界讲清，避免读者误以为是"瑞芬太尼安全的证据"。

**B2. "PAIN 是任何痛觉过敏叙事必经的唯一高频术语"这一推论桥缺乏支撑。**
§2.3 与 §3.4 把 PAIN 当作痛觉过敏的**替代指标（surrogate）**，理由是"任何痛觉过敏叙事都必须经过 PAIN 这一术语"。但 PAIN 在术后极普遍、可由无数与 OIH 无关的原因触发；该桥接断言**无引用支撑**，且恰好是审稿人会攻击的点。
- **修改要求：** 为这一 surrogate 选择补引（如 OIH 测量中为何以疼痛术语为代理的相关文献），或明确将其弱化为"a pragmatic, necessarily imperfect proxy"并在局限中说明 PAIN 低报完全可由场景解释、不能反向推断 OIH 缺失。

**B3. 适应症混杂的论证存在循环风险。**
稿件的核心解释（§4.3）是：瑞芬太尼低报一切，是因为其报告场景（围术期、严重、医护上报）不同于 comparator。但 comparator 本身也不"干净"——吗啡 FAERS 队列由慢性疼痛与消费者上报主导、芬太尼由透皮/门诊主导。于是"瑞芬太尼低报 PAIN"很大程度是**把一种围术期药物与慢性疼痛场景的阿片对比**所致，而这恰恰就是稿件点名的适应症混杂。换言之，研究设计在 comparator 处于根本不同照护场景时，**本就无法分离"药物特异性信号"与"场景特异性报告"**。
- **修改要求：** 在 §4.3/§4.6 更直白地写明：头对头比较受场景混杂限制，本研究只能检测**报告差异**；在报告由场景主导的前提下，真实的（若有）药物效应不可分离。当前稿件大体诚实，但摘要/结论的"head-to-head"措辞可能让读者高估其为"药物层面的检验"。

### 次要意见（Minor）
- **B4.** 参考文献偏少（仅 20 篇）。作为 Original Article，建议扩充至更能支撑方法学贡献的规模（补充：OIH 关键实验论文、关于"自发报告对综合征级现象局限性"的药物流行病学文献、FAERS vs EudraVigilance 比较文献）。注意参考文献 [5] 与 [19] 为同一前 4 作者（Kim SH 等）的两篇高度相似系统综述，建议合并取舍、避免冗余。
- **B5.** 新颖性表述可更克制：结论"stream of null studies is otherwise likely to be read as accumulating evidence of safety"很有价值，建议在摘要 Discussion 中更早点出，作为本稿的"so what"。

---

## 3. 审稿人 C —— 药物流行病学、数据库与报告规范（READUS-PV）

### 主要意见（Major）

**C1. FAERS 个案级数据"不可达"使主分析臂最弱，须直面并合理定位（与 A4 呼应）。**
稿件称 FDA 个案级/药物记录级文件"本环境无法获取"，导致 FAERS 臂 role-agnostic、无法去重、无法 route 归因。这是**环境性限制**而非方法性选择，却实质性削弱了被标为 primary 的 FAERS 臂。
- **修改要求：** 除按 A4 重新定位主/验证外，在 §4.6 补一句：FAERS 臂的关键结论（PAIN 低报、阴性对照一致）**已由 Canada 的 suspect-role 限定分析独立复现**，因此即便 FAERS 臂有稀释，结论方向不被推翻——把"局限"转化为"已被交叉验证缓解"。

**C2. 两个数据库均为北美、英语报告文化、重叠药品市场——"独立"成色有限；强烈建议加入第三库。**
FAERS（美国）与 Canada Vigilance（加拿大）同属北美自发报告体系、MedDRA 编码相近，"地理/文化独立"被高估。稿件记忆中曾确认日本 JADER（info.pmda.go.jp）可达。
- **修改要求（强建议）：** 增加 **JADER** 作为第三、跨大陆验证库（哪怕只复现 PAIN 低报方向与 5 零术语）。这将把"two-database confirmation"升级为真正的跨监管区三角验证，显著提升说服力；若时间不允许，至少须在局限中明确"两个库均为北美体系，跨大陆验证留待后续"。

**C3. READUS-PV 中 "protocol registration" 标 N/A，将与被 A1 的 prespecified 主张冲突。**
READUS-PV 要求说明分析计划；稿件把"方案注册"标为不适用，却又满篇 "prespecified"。两者并置会被审稿人视为不一致。
- **修改要求：** 随 A1 一并处理——在分析计划文件中说明未注册的原因，并在 READUS-PV 清单对应项注明"no prospective registration; analytical plan archived post hoc with date"，保持与正文措辞一致。

### 次要意见（Minor）
- **C4.** 伦理/数据使用声明：建议补一句"分析符合各数据库的使用条款（Canada Open Government Licence; openFDA 公开访问）"，比单纯"无需伦理审批"更完整。
- **C5.** AI 使用声明（§Acknowledgements）整体合规且详尽，但"language, clarity and style editing of the manuscript text"与"Generative AI was not the primary source of any text"之间张力需在定稿时自洽——鉴于已做多轮去 AI，文本现已基本人工定稿，建议加一句"all AI-assisted output was substantially rewritten by the author"以强化责任归属。

---

## 4. 审稿人 D —— 学术英语与发表规范（*Anaesthesia*）

### 主要意见（Major）

**D1. 摘要与结论高估了"特异性探针方向反转"。**
Summary（第 25 行）与 Conclusion（第 205 行）均写 "a specificity probe that reversed direction"。但数据事实是：在 **FAERS 主库**，DRUG INEFFECTIVE 被瑞芬太尼**低报**（ROR 0.60；RORR 0.568/0.470）——即它与一切**同方向**，并未反转；仅在 **Canada** 库反转（1.277/1.703，医师-only 更达 5.921/10.604）。正文 §3.4/§3.5/Table 3 是准确的（Table 3 标 "no (direction reversed)"），但摘要/结论的概括过度。
- **修改要求：** 摘要与结论改为 "a specificity probe whose direction reversed in the confirmation database but not in the primary analysis"，或弱化为 "a specificity probe that behaved inconsistently between databases, arguing against a uniform global artefact"。

**D2. "structurally unable to detect" 表述过强。**
§4.4/§5 称自发报告"对于 OIH 结构性无法检测"。更精确的说法是：该**特定 PT** 在自发报告中不被使用，综合征只能通过通用疼痛术语（PAIN 等）间接观察，而这些术语本身受场景混杂。直接说"无法检测"易被误解为"该方法对 OIH 完全失明"，过度。
- **修改要求：** 改为 "structurally unable to detect OIH *via its specific preferred term*; the syndrome is only indirectly observable through generic pain terms, which are themselves confounded by reporting setting"。

### 次要意见（Minor）
- **D3.** Figure 1 说明称 5 个零术语"cannot be plotted and are omitted"——建议在图中以 "not estimable" 占位或于图注列出，避免读者误以为这些术语被遗漏。
- **D4.** 语言总体已很干净（无弯引号、无散文破折号、无套路词）。仅 §4.5 一句较长，可考虑再断一句以提升可读性（非必须）。
- **D5.** 标题 19 词、≤20、未下结论；running head ≤60 字符；关键词 3–5；Summary 293 词结构化无缩略语无引用——均符合 *Anaesthesia*。继续保持。

---

## 5. 编辑部必改清单（Editor's Required Revisions）

### P0（不修改即退稿风险）
1. **A1 / C3：** 仓库内存入带日期的分析计划，正文 "prespecified" → "defined a priori in the analytical plan"，并坦白未前瞻性注册。
2. **A2：** 方法 §2.3 + 补充材料澄清 5 零术语确为 **PT 级**、所用 **MedDRA 版本**，排除 LLT 查询假象；若 HYPERALGESIA 仅为 LLT，据实弱化"结构性缺失"措辞。
3. **D1：** 摘要（Summary/Conclusion）修正特异性探针"方向反转"的过度概括，与正文/Table 3 一致。

### P1（必须修改）
4. **A3：** ALLODYNIA 头对头改为 "not estimable (n=1)"，删除方向性结论。
5. **A4 / C1：** 重新定位主/验证（建议 Canada 为主、FAERS 为验证），或在 §2.1 论证并保持与全文一致；§4.6 补"FAERS 结论已被 Canada suspect-role 分析交叉验证"。
6. **A5：** §3.7 SOC 全景标注 exploratory；§3.9 "阳性对照"弱化为 post hoc demonstration。
7. **B3：** 在 §4.3/§4.6 直白说明头对头受场景混杂限制，只能检测报告差异、药物效应不可分离。
8. **B1：** 投稿信与引言明确"方法学警示"定位，避免被读作"瑞芬太尼安全证据"。

### P2（强烈建议，提升接受率）
9. **C2：** 加入 JADER 第三库做跨大陆三角验证（或于局限中明确仅为北美体系）。
10. **B2：** 为 PAIN 作为 surrogate 补引或弱化。
11. **B4：** 扩充参考文献（现 20 篇偏少），合并 [5]/[19] 冗余。
12. **D2：** 弱化 "structurally unable to detect" 为 "via its specific preferred term"。
13. **A6 / C4 / C5 / D3：** 统计近似说明、数据使用条款、AI 声明自洽、Figure 1 占位。

---

## 6. 稿件已具备的强项（供作者保持、勿在修改中削弱）
- 双主权库独立复现、内部一致性校验（211 条断言）、完整数字-源文件溯源（§9）、AI 使用声明详尽且符合 *Anaesthesia* 政策。
- 结构性缺失用"常见疼痛术语同路径返回大计数"做查询完整性反证（§3.2）——方法上聪明且令人信服。
- 稀释/混杂的诚实呈现（route 缺陷 184% 归因、role-agnostic、去重缺失）远优于多数同类投稿。
- 格式已通过 *Anaesthesia* Author Guidelines 合规审计（docx 零嵌入图、表/图注/补充置于正文后）。

---

*本审稿意见由编辑部基于稿件全文与底层数据文件（01_faers_results.csv、02_route_stratified.csv、cv/cv_soc_27.csv、cv/cv_pt_summary.csv、04_sensitivity_ps_only.csv、04_sensitivity_year_pain.csv）逐格核对后组织专家出具。所有对被引数字的质疑均已回到源文件验证，未发现数据捏造；意见集中于诚信呈现、论断稳健性与期刊契合度。*
