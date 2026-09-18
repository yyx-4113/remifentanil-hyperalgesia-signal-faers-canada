# REVIEW — Round 6 独立专家组（2026-09-18）

**稿件：** `I_正文_IMRaD_en.md`（v1.5.0，main @ `2fdfce5`，tag `v1.5.0` 已发布）
**目标刊：** *Anaesthesia*（Original Article，单作者）
**面板：** 4 位跨层独立专家 + 汇总层（本文件）
**独立性协议：** 见 `_PANEL_BRIEF.md`。四位专家均**未读取**任何 `REVIEW_*`/`RESPONSE_*`/`REVISION_*`/`SUBMISSION_MANIFEST.md`/`GITHUB_DEPOSIT_SOP.md`/`author_verification_statement.md`，且互不读取彼此文件；按"首次投稿"审读。独立性生效的证据：A2 与 A1 在**互不知情**下各自击中同一缺陷（§4.1/§4.6 的"setting, not drug"过强 → A1 Issue 3 / A2 Issue 3+4）。

**分文件：**
- `A1_domain.md`（领域层：麻醉/围术期/OIH，10 条）
- `A2_design.md`（设计层：药物流行病学/生物统计，11 条）
- `A3_implementation.md`（实现层：可复现/溯源审计，12 项核对 + 2 条）
- `A4_venue.md`（期刊/报告规范层，5 条）

---

## 一、汇总裁决

**结论：Major revision（大修）。** 不是格式问题——A4 明确判定"无 desk-reject 级格式硬伤"；大修来自**设计层与领域层的推论强度**，以及若干可独立验证的**硬错误/自相矛盾**。

**分层裁决（与 Round-5 同型）：**

| 层 | 代表 | 裁决 | 依据 |
|---|---|---|---|
| 实现层（算术/溯源） | A3 | **无阻塞性问题** | 12 项数值核查 11 项精确吻合、1 项差 5×10⁻⁴（纯舍入）；仅 2 处措辞不一致 |
| 领域层 | A1 | **Major** | 1 处药理学**说反**（line 139，与自引 ref 5 矛盾）+ 承重性 MedDRA 前提待证 + 解读过度 |
| 设计层 | A2 | **Major** | 核心结论 #2 过强；n=4 分层；MH 调整是 collider；术语选择使结论可反转 |
| 期刊/规范层 | A4 | **Minor（无硬伤）** | 字数/图件/AI 声明/标题/DOI 均合规；5 处 minor |

**关键事实：** 稿件**没有任何数值错误**（A3 逐格核对）、**没有任何格式硬伤**（A4），但**其两条头条结论的表述强于数据所支撑**（A1/A2），且存在**可独立验证的自相矛盾**（A3-F1、A2-6、A1-1）。这正是"绿门禁只认证算术与溯源，不认证设计"的再次体现——门禁 528/0、3996/4000、75/0 全绿，但设计级缺陷依然存在。

---

## 二、跨层综合：四条主题

**主题 A（承重最重）——"setting, not drug"结论过强，且与稿件自身承认的反转矛盾。**
A2 的 Issue 3/4/6 与 A1 的 Issue 3 指向同一处：结论 #2（瑞芬对 PAIN 低报 = 围术期报告设置的属性，非药物）依赖 (i) n=4 的 pain 分层（RORR 1.791，CI 0.184–17.397，信息量近乎为零）；(ii) MH"深度调整"——而报告条目数是设置的**后果**（中介/collider），不是前置混杂；(iii) §4.1/§4.6 称该结论"more robust"，**直接与 §4.4 承认的"INADEQUATE ANALGESIA 使方向反转"冲突**（line 163 vs line 143）。→ 表述必须从"setting, not drug"降为"attenuated, not eliminated"。

**主题 B——头条顺序效应：先给"四药全达信号"，再揭示其被单一重复病例污染。**
A1 Issue 8 与 A2 Issue 5 指向 Summary line 23 / §4.1 line 129 / §3.3 line 97：读者读到"met the signal criterion for all four opioids"即离场，而污染（一例九报；且 2024 年三臂的抬升同源）在后方。属**框定顺序**问题，非数据问题。

**主题 C——术语选择即结论：两个"发现"都随 PT 选择反转。**
A2 Issue 5/6：整个阳性术语集是观察到零值之后才选的（Amendment 1 已披露）；而 PAIN 低报在换成 INADEQUATE ANALGESIA 后**方向反转**（瑞芬 ROR 5.016 反超舒芬/吗啡）。即论文批判的"术语决定答案"反过来也适用于它自己的 PAIN 结论——A2 判定这削弱了"PAIN 低报更稳健"的主张。

**主题 D——"instrument, not drug"的阴性对照逻辑不成立。**
A2 Issue 9 与 A1 Issue 6：恶心/呕吐/瘙痒/便秘对瑞芬而言**本身就是真实的药理学/暴露差异**（瑞芬为术中短程静脉给药，对照臂含慢性口服/透皮用药），因此这些术语既测药物又测设置，不构成因果意义上的阴性对照；同理 DRUG INEFFECTIVE 的跨库反转（A1 Issue 2）恰是设置假设的**同义反复**，不能作为"反证非全局人为假象"的证据。

---

## 三、问题清单（合并去重、分级）

> 每条含：来源层 · 证据（`文件:行号`）· 裁决 · 具体修复。

### Tier 1 — 硬错误 / 自相矛盾（必须修；可独立验证）

**R6-01 ｜ 药理学表述说反 —— 与自引文献矛盾**
- 来源：A1 Issue 1
- 证据：`I_正文_IMRaD_en.md:139`："remifentanil's ultrashort half-life and lack of oral or transdermal formulation make true tolerance and withdrawal uncommon"；而 ref 5（Guignard 2000）恰恰是**急性阿片耐受**的奠基性证据，且 line 31 同一稿件用"context-insensitive half-time 3–4 min"解释 OIH 机制——快速消退是**触发**敏化，不是保护因素。
- 裁决：**成立（硬错误）**。这是全文唯一一处药物层面的机制性断言，方向相反。
- 修复（paste-ready）：
  > "For DRUG TOLERANCE and DRUG WITHDRAWAL SYNDROME the deficit may in part reflect pharmacology: remifentanil is given intravenously for short, supervised perioperative intervals and has no outpatient oral or transdermal formulation, so *chronic* physical dependence and withdrawal — the events captured in the fentanyl and morphine chronic-pain cohorts — are uncommon for it. This says nothing about *acute* intra-operative tolerance, which is well documented with remifentanil (Guignard et al., 2000) and is mechanistically linked to its rapid offset."

**R6-02 ｜ §3.3 与自身 Table S9 自相矛盾**
- 来源：A3-F1
- 证据：`I_正文_IMRaD_en.md:97`："each naming the same perioperative combination of remifentanil, sufentanil, fentanyl, hydromorphone, ketamine, oxycodone and propofol"（称 9 份**各自**含同一 7 药组合）vs `:657` Table S9 脚注："six of the nine name all seven products"；且首份报告 `24402565` 根本不含 fentanyl/sufentanil。
- 裁决：**成立（自相矛盾，低严重度）**。核心结论（一例九报）不受影响，但叙述与自身数据不符。
- 修复：`:97` 改为
  > "…each naming hydromorphone, ketamine, oxycodone, propofol and remifentanil, with six of the nine also naming fentanyl and sufentanil as part of the same perioperative combination…"

**R6-03 ｜ §4.6 稀有度范围低估**
- 来源：A3-F2
- 证据：`I_正文_IMRaD_en.md:157`："one report in 200 to 500, depending on the drug (Table 2)"；而 `:259` Table 2 脚注精确值为 remifentanil 1/538、fentanyl 1/387、sufentanil 1/296、morphine 1/216 → 实际范围 **216–538**，538 超出 500。
- 裁决：**成立（措辞不精确，低严重度）**。
- 修复：`:157` 改为 "one report in roughly 216 to 540, depending on the drug (Table 2)"。

**R6-04 ｜ "more robust" 与 §4.4 的反转承认冲突**
- 来源：A2 Issue 6
- 证据：`I_正文_IMRaD_en.md:163`（结论）："Remifentanil's low reporting of pain is **more robust** — large, stable, reproduced in Canada…"vs `:143`（§4.4）："The pain conclusion fails the same test: substituting INADEQUATE ANALGESIA **reverses it**"；`21_alternative_proxy_terms.csv`：INADEQUATE ANALGESIA 上瑞芬 ROR 5.016（信号），RORR vs 舒芬 1.334、vs 吗啡 1.403（点估计 >1）。
- 裁决：**成立（自相矛盾，中等严重度）**。删"more robust"并调和。
- 修复：`:163` 改为
  > "Remifentanil's low reporting of the generic term PAIN is large, stable across years, and reproduced in Canada, but — like the hyperalgesia finding — it is **term-dependent**: under INADEQUATE ANALGESIA the direction reverses (reporting odds ratio 5.02, above the sufentanil and morphine point estimates). The under-reporting of PAIN is therefore a property of how the reporting setting labels pain, not evidence about the drug."

**R6-05 ｜ READUS-PV"两项不适用"计数不准**
- 来源：A4 Issue 1
- 证据：`I_正文_IMRaD_en.md:451`："an explicit note on the **two items** that are not applicable (case-by-case analysis; protocol registration)"；但 `I_TableS2_READUS-PV_checklist.md` 将 case-by-case 映射到 **7d、10、2e**（三行），且 14d（注册）是"reported here rather than left blank"（line 76）——是**已述**而非不适用。
- 裁决：**成立（准确性，低严重度）**。
- 修复：`:451` 改为
  > "with explicit notes on the items that could not be addressed: case-by-case analysis and causality assessment were not performed (body items 7d and 10; abstract item 2e); prospective registration was absent and is stated rather than implied (body item 14d)."

**R6-06 ｜ 参考文献 32 作者未按 Wiley 体例截断**
- 来源：A4 Issue 2
- 证据：`I_正文_IMRaD_en.md:220`："Janiczak S, Tanveer S, Tom K, Zhang R, Ma Y, Wolf L, Muñoz MA."（7 位无 et al.）
- 裁决：**成立（体例，低严重度）**。
- 修复："Janiczak S, Tanveer S, Tom K, Zhang R, Ma Y, Wolf L, et al."

**R6-07 ｜ CITATION.cff 自引条目标题与稿件不一致**
- 来源：A4 Issue 4
- 证据：`CITATION.cff:3`（=稿件标题）"…an **observational head-to-head disproportionality analysis**" vs `CITATION.cff:47` "…a head-to-head disproportionality **study with a terminology caution**"。
- 裁决：**成立（一致性，低严重度）**。注意门禁"标题三处一致"未覆盖该**自引条目**，故漏网。
- 修复：将 `CITATION.cff:47` 标题改为与 `:3` 完全一致。

**R6-08 ｜ openFDA 访问日期两处不一致**
- 来源：A4 Issue 5
- 证据：`I_正文_IMRaD_en.md:47`："at extraction (**16 September 2026**)"；`:179`（Acknowledgements）："accessed **16 and 18 September 2026**"。
- 裁决：**成立（一致性，低严重度）**。READUS-PV 5b 要求单一明确的提取日期。
- 修复：统一为 "…corpus (20 692 687 reports) as of **16 September 2026**; the interface was queried on 16 and 18 September 2026."

**R6-09 ｜ 图件带 alpha（RGBA）通道**
- 来源：A4 Issue 3
- 证据：`05_figures.py` 未设白色 facecolor；PIL 报 `I_fig1_rorr_forest.tif` / `I_fig2_year_trend.tif` 为 **mode=RGBA**。*Anaesthesia* 线条图要求不透明白底。
- 裁决：**成立（格式，低严重度）**。
- 修复：`05_figures.py` 在 `plt.subplots(...)` 后加 `fig.patch.set_facecolor("white")` 与 `ax.set_facecolor("white")`（或保存前合成白底），重跑使 TIF/PDF 为不透明 RGB。

**R6-10 ｜ "四臂中三臂的年度抬升来自一例" 对芬太尼过度陈述**
- 来源：A2 Issue 10
- 证据：`I_正文_IMRaD_en.md:99` 与 `:344`："…all seven of the 2024 sufentanil HYPERAESTHESIA reports and **five of the seventeen** 2024 fentanyl reports come from it, so in three of the four cohorts the year's elevation is one patient's"；`20_2024cluster_membership.csv`：remi 8/8、su 7/7、fen **5/17**、mor 0/21 → 芬太尼 71% 的 2024 报告**不**来自该系列。
- 裁决：**成立（不精确，低严重度）**。瑞芬/舒芬结论稳固，芬太尼应限定。
- 修复：改为 "for remifentanil (8/8) and sufentanil (7/7) the 2024 elevation is entirely the case series; for fentanyl 5 of 17 are, so most of fentanyl's 2024 rise is independent of it; none of morphine's (0/21) is."

### Tier 2 — 框定过度（应修；提升可辩护性）

**R6-11 ｜ 核心结论 #2"setting, not drug"过强**
- 来源：A1 Issue 3 + A2 Issue 3 + A2 Issue 4（**两专家独立同击**）
- 证据：`I_正文_IMRaD_en.md:113`（"the deficit is no longer distinguishable from unity"）、`:139`、`:378`（Table 6 脚注"after holding reporting depth constant the deficit is no longer distinguishable from unity"）；Table 5 perioperative 分层 n=84 点估计仍 **0.399**（0.048–3.295）；pain 分层 n=4 → 1.791（0.184–17.397）；Table 6 MH vs 吗啡 0.978（**0.042–22.751**）。
- 裁决：**成立（Major）**。三处："moves to unity"依赖 n=4 分层；MH 是对 collider 的条件化；perioperative 层点估计仍 <1。
- 修复（三处同步）：
  1. `:113` 与 `:378` 将"no longer distinguishable from unity"改为 "attenuated towards, but not demonstrated to reach, unity"；
  2. Table 6 重标为 **sensitivity analysis for recording opportunity**（非 confounder adjustment），并加一句 collider 说明："reporting depth is a consequence of the reporting setting and is conditioned on only to show how much of the crude deficit is mechanical; it is not a control for confounding."；
  3. §4.3 将"setting, not drug"降为"consistent with a setting effect, but the data cannot establish that the drug contributes nothing."

**R6-12 ｜ 信号判据 a≥3 计"报告"非"患者"**
- 来源：A2 Issue 1
- 证据：`I_正文_IMRaD_en.md:259` 定义 "*a ≥ 3 and the lower bound of the 95% CI of the OR > 1"；瑞芬 HYPERAESTHESIA a=10 即两患者。
- 裁决：**成立（Major 之轻）**。判据本身不防重复病例。
- 修复：§2.4 加一句："the a ≥ 3 floor counts *reports*; because spontaneous reporting carries no patient identifier, a single case filed repeatedly can satisfy it."

**R6-13 ｜ 头条顺序：先"四药全达信号"**
- 来源：A1 Issue 8 + A2 Issue 5
- 证据：`I_正文_IMRaD_en.md:23`（Summary）、`:97`、`:129`。
- 裁决：**成立（Major 之轻）**。Summary line 23 已有"a term-level demonstration, not a signal"限定，但开头仍以"met the signal criterion for all four opioids"领起。
- 修复：Summary 与 §4.1 直接前置限定：
  > "HYPERAESTHESIA met the a ≥ 3 and LCI > 1 rule in the uncorrected counts for all four opioids, but the 2024 elevation in three of the four cohorts is supplied by a single duplicated reporter (§3.3, §3.7); once identified, no drug-specific signal remains."

**R6-14 ｜ 发生率免责应随结论同行**
- 来源：A1 Issue 7
- 证据：`I_正文_IMRaD_en.md:163` 结论句"a zero obtained from the clinical name alone is an artefact of terminology, not evidence of safety"；发生率免责仅见于 §4.5（`:147`）。
- 裁决：**成立（应修）**。
- 修复：结论句尾追加 "…not evidence of safety, and equally not evidence of harm: spontaneous reporting cannot address OIH incidence in either direction, which remains a question for prospective quantitative sensory testing."

**R6-15 ｜ "two patients" 是内容推断，非经验证的患者计数**
- 来源：A2 Issue 11
- 证据：`I_正文_IMRaD_en.md:97`："The ten reports therefore describe two patients"；FAERS 无患者键，`:657` 自承"only the content does"（仅靠内容判断）。
- 裁决：**成立（应修）**。
- 修复：改为 "appear to describe (at most) two patients"，并在 §2.2/§4.5 注明重复病例推断基于内容、非结论性。

**R6-16 ｜ DRUG INEFFECTIVE 反转的论证是循环的**
- 来源：A1 Issue 2
- 证据：`I_正文_IMRaD_en.md:105`／`:281` 以"反转"论证"against a uniform global reporting artefact"；但加拿大对照臂以慢性疼痛/透皮为主（Table S3），"drug ineffective"在慢性队列是自然报告、对术中输注不自然——恰由同一个 setting 轴解释。
- 裁决：**成立（应修）**。
- 修复：改为"the reversal shows the pattern is not invariant across databases, but it cannot be used as evidence against a reporting artefact, because the comparator cohorts are not indication-matched between the corpora."

**R6-17 ｜ 对照术语低报部分是药理学/暴露差异，非纯 setting**
- 来源：A1 Issue 6 + A2 Issue 9
- 证据：`I_正文_IMRaD_en.md:103`、§4.3 `:139`（归因"setting, not pharmacology"）；瑞芬为术中短程静脉给药，恶心/呕吐/瘙痒/便秘为剂量-暴露依赖的不良反应。
- 裁决：**成立（应修）**。属"special pleading"风险。
- 修复：§4.3 加 "We attribute the comparator-term deficit chiefly to the perioperative reporting setting, but acknowledge that remifentanil's brief intra-operative exposure also yields genuinely fewer of these events than the chronic morphine and transdermal fentanyl use that dominate the comparator cohorts; the two are not fully separable here."；并将"test the instrument, not the drug"改为"compatible with a setting artefact, but also compatible with genuine pharmacological differences…not negative controls in the causal sense."

**R6-18 ｜ "11/12"的多重性未处理**
- 来源：A2 Issue 8
- 证据：`I_正文_IMRaD_en.md:23`、`:259`（Table 2 脚注）；仅对 HYPERAESTHESIA 下界做了 Bonferroni（1.61），未对 PAIN/对照术语模式做校正。
- 裁决：**成立（应修）**。
- 修复：明示"11/12"为**描述性计数**而非统计结果（或补符号检验并声明族与相关性）；八年 PAIN 比值同样只作"directionally stable"表述。

### Tier 3 — 分析/验证缺口（需新工作或作者权限）

**R6-19 ｜ MedDRA v27.1 中是否存在独立 "Hyperalgesia" PT（承重前提）**
- 来源：A1 Issue 4
- 证据：`I_正文_IMRaD_en.md:63`、`:93`、Table S6（"the only term in the dictionary that carries the concept"）；公开 MedDRA 链接源无法确证 v27.1 是否有独立 PT "Hyperalgesia"（常见代号 10020566）。
- 裁决：**成立（Major，需作者核实）**。若该 PT 存在，"only term"不成立，主分析应纳入。
- 修复：在补充材料加 MedDRA v27.1 浏览器对字符串 "Hyperalgesia" 的**逐字输出**（LLT→PT 映射）；若存在独立 PT，纳入 18 术语集并同footing报告。

**R6-20 ｜ RORR 估计量：可考虑直接两药头对头**
- 来源：A2 Issue 2
- 证据：`I_正文_IMRaD_en.md:71`、`:604`、`:695`（A1.5）——稿件称两表"share neither an event column nor a drug column, so no term cancels algebraically"，**并已明示**"share the same corpus remainder and are therefore not independent"，且 `18_rorr_covariance.csv` 保留协方差重算全部 29 区间（移动在第三位小数）。
- 裁决：**部分成立，但 A2 的"虚假陈述"框定不成立——降级为可选精修**。稿件已诚实披露并校正共享余项协方差；A2 的"直接两药 2×2 / 年份条件 Poisson"是更强估计量，但非纠错。
- 修复（可选）：若采纳，在附录增列直接两药头对头作为主估计量，原边际-ROR 比值作为近似并明示受 29.3% 队列重叠上偏。

**R6-21 ｜ 去重叠的不对称 + "唯一 >1 比值塌陷"的定性**
- 来源：A2 Issue 7
- 证据：`I_正文_IMRaD_en.md:604`："the remifentanil arm is restricted to reports that do not name the comparator"（仅限制瑞芬臂）；`17_overlap_adjusted_rorr.csv`：PROCEDURAL PAIN vs 芬太尼 **1.962 → 0.981**。
- 裁决：**成立（可视作 Tier 2/3 之间）**。
- 修复：把去重改为**双臂对称**（两臂均排除共享报告）或明示不对称的理由；并直书"去共享后**无任何**头对头比值 >1；唯一曾 >1 者（PROCEDURAL PAIN vs 芬太尼）降至 0.98，故不作为发现。"

**R6-22 ｜ 缺 OIH 机制的一手文献**
- 来源：A1 Issue 5
- 证据：`I_正文_IMRaD_en.md:31` 机制句仅引 ref 1（2024 综述）、ref 2（2006 综述）；缺 Porreca/Vanderah/Ossipov 组的脊髓强啡肽与 RVM 下行易化的奠基性一手证据（Vanderah *J Neurosci* 2000/2001；Gardell *J Neurosci* 2001）。
- 裁决：**成立（must-cite，低严重度、高可信度收益）**。
- 修复：`:31` 在 [2] 后补一手引用并入 References。

**R6-23 ｜ PAIN 作为 OIH 代理的框定 + VAS 单位措辞**
- 来源：A1 Issue 9 + A1 Issue 10
- 证据：`I_正文_IMRaD_en.md:61`／§2.3（PAIN 既作代理又作探针）；`:33` "9.4 mm on a 100 mm scale"，而 Fletcher & Martinez 原文为 "9.4 cm on a 100 cm VAS"（比例相同）。
- 裁决：**成立（Minor）**。
- 修复：Abstract `:23` 与 §2.3 明确 PAIN 为 "a general reporting-burden probe, **not** an OIH proxy"；`:33` 补注原尺度。

---

## 四、分歧披露（必须显式记录）

1. **D1 — 实现层 vs 设计/领域层裁决相反。** A3：所有数值吻合、无错误；A1/A2：核心解释脆弱。**两者都对**——算术与溯源干净，设计级推论过度。与 Round-5 同型（分层裁决，不可取平均）。
2. **D2 — A4"无硬伤/5 处 minor" vs A1/A2"Major revision"。** 汇总层裁断：格式无硬伤**属实**；大修来自设计/领域层，非格式。**整体 = Major revision**。
3. **D3 — A2 Issue 2（RORR 估计量）被我降级。** A2 将 A1.5 句子判为"虚假陈述"；经核，hand稿**已披露**共享余项非独立并保留协方差重算（`18_rorr_covariance.csv`）→ 降为**可选精修**。这是汇总层对设计层意见的一次有据下调。
4. **D4 — MH 调整的定性。** A2 判为 collider 条件化（缺陷）；稿件 Table 6 脚注自承"the movement of the point estimate, not the interval, is what the table is for"（半承认）。裁断：**双方各半**——无需重算，但必须**重标为敏感性分析**并写明 collider 顾虑（R6-11）。
5. **D5 — 芬太尼归因口径。** A1 Issue 8 与 A2 Issue 10 均提"三臂"表述；裁断采用 A2 更精确的口径（5/17），因 A1 未点出芬太尼的 71% 反例。

---

## 五、站得住的点（未被推翻，需保留）

1. **术语层验证是真方法学贡献**（A2 #1）：HYPERALGESIA 是 LLT 非 PT、临床词零值是词典假象、Table S4 经验证两库可检索性——四位专家一致认可。
2. **leave-2024-out / 病例系列处理严谨诚实**（A2 #2、A1 #5）：`19`/`20` 两 CSV 与稿件两种读法（a=2, ROR 1.005；a=1, ROR 0.701）均可复现。
3. **双库设计构想合理**（A2 #3）：加拿大"suspect 角色 + 源端去重 + 原生 MedDRA"作为更干净的方向核验恰当，且已声明 111 例无功效。
4. **算术/溯源零缺陷**（A3）：12 项核查、含 2×2 重建、去重叠 11 行、病例系列 10 行、图-表同源——无一数值错误。
5. **格式/规范全部合规**（A4）：字数 3996/4000+296/300、图件 600 ppi 无图例框/边框/网格、AI 声明完整且不占正文字数、标题四处一致、33 条 DOI 可解析、READUS-PV 齐全。
6. **局限性章节异常充分**（A2 #5）：报告≠风险、版本/角色/重复约定、路径映射、唯一正比值在去重叠后塌陷——坦率度高于同类文献。

---

## 六、优先级行动清单

| 优先级 | 条目 | 性质 | 工作量 |
|---|---|---|---|
| **P0** | R6-01 药理学说反 | 硬错误 | 改 1 句 |
| **P0** | R6-04 "more robust" 自相矛盾 | 硬错误 | 改 1 句 |
| **P0** | R6-11 "setting, not drug" 过强（3 处 + Table 6 重标） | Major 框定 | 改 3–4 处 |
| **P1** | R6-02 §3.3 vs S9 矛盾 | 硬错误 | 改 1 句 |
| **P1** | R6-13 头条顺序（Summary/§4.1） | Major 框定 | 改 2 句 |
| **P1** | R6-16 DRUG INEFFECTIVE 循环论证 | 框定 | 改 1–2 句 |
| **P1** | R6-17 对照术语药理学贡献 | 框定 | 加 1–2 句 |
| **P1** | R6-19 MedDRA "Hyperalgesia" PT 核实 | 验证 | 需作者 MedDRA 权限 |
| **P2** | R6-03/05/06/07/08/09/10/12/14/15/18/22/23 | 措辞/格式/体例 | 逐条小改 |
| **P3** | R6-20 直接头对头、R6-21 对称去重叠 | 可选精修 | 新分析 |

**发布影响：** 采纳 P0+P1 将产生 **v1.6.0**（正文与表注变更）→ 须重跑三道门禁（一致性 528→或增；字数；docx 75）→ 本地重建投稿包 → amend 或新 commit → SSH 推送 → 新 tag/release。**R6-11/13/16/17 会改动 Summary 与结论句，字数口径需重算**（当前距 4000 上限仅 4 词，宜同步压缩）。

---

## 七、面板独立性证据

- A2 与 A1 在**互不读取**的前提下各自独立击中 §4.1/§4.6 的"setting, not drug"过强（A1 Issue 3 ↔ A2 Issue 3/4）——独立性生效的直接证据。
- 三位专家（A1、A2、A3）分别从领域、设计、实现层指向同一处病例系列处理（认可其诚实），同时 A2/A1 指出其后**框定**过度——跨层一致。
- 无专家读取任何前轮文件；`review_round6/` 内文件互不可见。
