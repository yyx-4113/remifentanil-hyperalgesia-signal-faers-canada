# A3 — 实施 / 可复现性 / 数据溯源审计

**稿件：** `I_正文_IMRaD_en.md`（投稿 *Anaesthesia*，单作者，FAERS 主分析 + Canada Vigilance 对照）
**独立度：** 视为首次投稿，未读取 REVIEW_*/RESPONSE_*/REVISION_*/SUBMISSION_MANIFEST.md / author_verification_statement.md 及其他三位审稿人文件。
**审计方法：** 所有数值均从仓库内已抽取的 CSV 直接重算或交叉核对；未调用任何 API。ROR/RORR 由 2×2 单元格重建（分母取全库 20 692 687；各药队列规模取 `11_overlap_matrix.csv`）。

**总判断：** 稿件正文、Table 1–6、S1–S9、附录 A1 与仓库 CSV 之间**高度一致**；12 项核查中 11 项完全吻合，第 2 项（RORR 重算）吻合至 5×10⁻⁴ 以内。仅发现 2 处**细微的"叙述 vs 数据"措辞不一致**（均不构成数据错误，不改变结论）。

---

## 逐项核查（稿件值 / 来源值 / 是否一致）

### 1. Table 1 队列规模
- **FAERS 5 375 / 121 819 / 6 513 / 56 501** —— 来源 `11_overlap_matrix.csv`（cohort_n: REMI 5375, FEN 121819, SU 6513, MOR 56501）。✅ 一致（`:231`）。
- **Canada 111 / 4 881 / 63 / 7 675** —— 来源 `cv/cv_drug_totals.csv`（111 / 4881 / 63 / 7675）。✅ 一致（`:232`）。
- 全库总数：FAERS 20 692 687、Canada 1 154 017，正文与两表一致（`:89`,`:231`）。✅

### 2. Table 2 HYPERAESTHESIA（重算 ROR / RORR）
- 稿件：remi a=10 (ROR 4.73, 2.54–8.80)、fen a=315 (6.80)、su a=22 (8.61)、mor a=262 (12.17)；RORR vs fen 0.696、vs mor 0.389。
- 来源 `01_faers_results.csv:15` 同值。由 2×2 重建（以 N=20 692 687、PT_total=8161）：
  - ROR_remi = 10·(N−10−5365−8151)/(5365·8151) = **4.7288**（稿件 4.729）。
  - ROR_fen = 315·(N−315−121504−7846)/(121504·7846) = **6.795**（稿件 6.80 三位显示）。
  - RORR vs fen = 4.7288/6.795 = **0.6960**（稿件 0.696）。✅
  - RORR vs mor = 4.7288/12.166 = **0.3887 → 0.389**（稿件 0.389）。✅
  - vs su = 4.7288/8.611 = 0.549（Table S5 0.549）。✅
- 全表 13 个可估术语的 ROR 与 RORR（vs fen/su/mor）与重建值最大绝对差 **0.0005**（即纯舍入），无一处矛盾。✅

### 3. Table 3 跨库关键术语
- **PAIN**：FAERS remi a=23，RORR 0.066/0.046（`01_faers_results.csv`/`Table S5:510`）；Canada remi a=2，RORR 0.235/0.146（`cv/cv_indication_strata.csv` All PAIN 行）。✅ 与 `:267` 一致。
- **VOMITING**：FAERS remi a=64，RORR 0.409/0.185（`Table S5:518`）；Canada remi a=3，RORR 1.066/0.392（`cv/cv_indication_strata.csv` All VOMITING 行）。✅ 与 `:278` 一致。
- **HYPERAESTHESIA Canada a=0**；`:273` 一致，`cv/cv_indication_strata.csv` All HYPERAESTHESIA 行 a_remi=0。✅

### 4. Table 4C 年份计数
- **2024 remi a=8，ROR 72.856** —— `04_sensitivity_year_hyperaesthesia.csv:11`（REMIFENTANIL_a=8, REMIFENTANIL_ROR=72.856）。✅ 与 `:338` 一致。
- **"remifentanil 列合计为 9"**：表内 remi a 列 = 2021(1)+2024(8)=9；2025-03-25 那一份（25115900）receivedate 在窗口外、不入表，即"一份无可用的 receivedate"。✅ 与 `:340` 一致。
- 2024 RORR vs fen = 72.856/29.199 = **2.494→2.495**；vs mor = 72.856/20.845 = **3.495**（`:338`）。✅
- 2021 行 ROR 8.374、RORR 0.511/0.571 亦与年份文件吻合。✅

### 5. Table S8 重叠与"去共享后 RORR"
- **1 575 / 5 375 = 29.3%** 同时命名 fentanyl；483 (9.0%) 命名 sufentanil；323 (6.0%) 命名 morphine —— `11_overlap_matrix.csv`（REMIFENTANIL 行：overlap_fentanyl 1575，overlap_sufentanil 483，overlap_morphine 323）。✅ 与 `:597`、`:602` 一致。
- 4×4 重叠矩阵（Panel A）与 `11_overlap_matrix.csv` 完全对称吻合（含 Fen–Su 299、Fen–Mor 6185、Su–Mor 596）。✅
- Panel B 的"去共享后 RORR"逐行对照 `17_overlap_adjusted_rorr.csv`：HYPERAESTHESIA 0.696→0.278（vs fen，n_remi_and_fen=6）、→0.110（vs su，n=8）、→0.389（vs mor，n=0）；PROCEDURAL PAIN 1.962→0.981；PAIN 0.066→0.040；VOMITING 0.409→0.268；PRURITUS 0.833→0.488；CONSTIPATION 0.122→0.022；等共 11 行全部逐格吻合。✅ 与 `:606`–`:617` 一致，无任何出入。

### 6. Table S9 病例系列
- 10 份报告：9 份为美国 76 岁男性（8 份 2024 年、1 份 2025-03-25），1 份为日本 45 岁女性（2021-08-13）—— 与 `13_report_series_hyperaesthesia.csv`（10 行：19700005 JP/F/45/2021-08-13；其余 9 份 US/M/76，其中 24402565–24727039 为 2024 年 8 份、25115900 为 2025-03-25）完全一致。✅ 与 Panel A（`:631`–`:640`）一致。
- Panel B 的"每报告命名哪些 7 种产品"逐格与 CSV 的 `all_medicinal_products` 字段核对：19700005（Fen/Ket/Methadone/Oxy/Remi）、24402565（APAP/Bupi/Lido/Hydro/Ket/Oxy/Prop/Remi）等均一致。✅

### 7. Table S5 分子列（comparator a：fen/su/mor）vs Table 2
- HYPERAESTHESIA：S5 为 315/22/262（`:521`）；Table 2 同行为 FEN 315、SU 22、MOR 262（`:247`）。✅
- 其余各术语（PAIN 7349/98/4794；VOMITING 3483/80/3432；NAUSEA 4928/109/4527；PRURITUS 1117/38/1291；CONSTIPATION 2011/63/1786；DRUG INEFFECTIVE 8062/318/4450；PROCEDURAL PAIN 162/8/167；DRUG WITHDRAWAL SYNDROME 3274/42/865；ALLODYNIA 48/0/30）在 S5 与 Table 2 及 `01_faers_results.csv` 三者间完全一致。✅

### 8. §3.7 簇声明（8/8 remi、7/7 su、5/17 fen 的 2024 HYPERAESTHESIA 来自同一系列）
- `20_2024cluster_membership.csv`：remifentanil_with_term_2024=8、sufentanil_with_term_2024=7（_also_remifentanil=7）、fentanyl_with_term_2024=17（_also_remifentanil=5）、morphine_with_term_2024=21（_also_remifentanil=0）。
- 即 8/8 remi、7/7 su、5/17 fen、0/21 mor。✅ 与 `:344` 及 §3.3（"all seven of the 2024 sufentanil… and five of the seventeen 2024 fentanyl"）完全一致。
- 另：Table 4C 2024 行 Fen a=17、Mor a=21（`:338`）与年份文件 `fentanyl_with_term_2024=17`、`morphine_with_term_2024=21` 吻合。✅

### 9. 去 2024（附录 A1.8）
- 移除 2024：a=2、cohort 4 927、term_total 7 824、corpus 19 373 581、ROR 1.0051 (0.2513–4.0209) —— `19_leave2024_hyperaesthesia.csv:2`。重建：ROR=2·(19373581−2−4925−7822)/(4925·7822)=**1.0051**。✅ 与 "ROR 1.01 (0.25–4.02)"（`:342`）一致。
- 限制至 2015–2023：a=1、cohort 3 798、ROR 0.7009 (0.0987–4.9778)、RORR vs fen 0.106 (0.015–0.758) —— `19_leave2024_hyperaesthesia.csv:3`。✅ 与 "0.701 (0.099–4.978)"（`:342`,`:705`）一致。
- 注：移除 2024 后 corpus 19 373 581 = 20 692 687 − 1 319 106，而 `04_sensitivity_year_pain.csv:11` 2024 N_year=1 319 106，可相互印证。✅

### 10. Table 3 中 VOMITING 行（近期插入）的内部一致性
- FAERS 侧：Table 2 VOMITING remi a=64、ROR 0.527、FEN a=3483、SU a=80、MOR a=3432（`:255`）；Table 3 VOMITING RORR 0.409/0.185（`:278`）= Table S5 `:518`。✅
- Canada 侧：Table 3 VOMITING Canada a=3，RORR 1.066/0.392（`:278`）= `cv/cv_indication_strata.csv` All VOMITING 行（a_remi 3，RORR_fen 1.066，RORR_mor 0.392）＝ Table 5 All VOMITING（remi a=3, fen a=124, mor a=508, `:352`）。✅
- `cv/cv_whole_corpus_pt_counts.csv` 给出 VOMITING 加拿大反应行 39 131、HYPERAESTHESIA 523、PROCEDURAL PAIN 1527、DRUG WITHDRAWAL SYNDROME 1667，与 Table 3 脚注列举的"523/1527/1667"一致。✅ 该行"Confirmed: no (direction reversed versus fentanyl)"准确（FAERS vs fen 0.409<1，Canada 1.066>1）。✅
- **结论：VOMITING 行与 Table 2、Table 5、cv 两份 CSV 完全自洽，是一处干净插入。**

### 11. Figure 1 vs Table S5
- `05_figures.py` 在运行期从 `01_faers_results.csv` 逐格读取 `RORR_REMI_vs_FENTANYL/SUFENTANIL/MORPHINE`（`:113`–`:125`），不手填常量。SHOWN 列表（`:93`）含 9 个术语，顺序与图注（`:727`）一致。
- 其打印值即 `01_faers_results.csv` 中的 RORR，与 Table S5（`:506`–`:525`）逐格相同：HYPERAESTHESIA 0.696/0.549/0.389、PROCEDURAL PAIN 1.962/2.124/0.878、PAIN 0.066/0.281/0.046、VOMITING 0.409/0.969/0.185、PRURITUS 0.833/1.310/0.328 等。✅ 图与表一致，且图源即表源，无"图≠表"风险。

### 12. 表格语法 / 舍入 / 叙述-表格矛盾
- **表格语法**：Table 1–6、S1–S9、A1 各表分隔符与列数匹配，未发现错位或断行 markdown 错误。✅
- **双重舍入**：第 2 项全表重算最大差 0.0005，所有 RORR 均由未舍入 2×2 计算后三位显示，无"先舍入再运算"痕迹。✅
- **§3.6 "mean 1.69 reaction terms for remifentanil" vs Table 6 "Share of cohort reaction rows 1.064%"**：二者度量不同（前者是每报告平均反应条目数，后者是 PAIN 占队列反应行的百分比），并非同一指标，不构成矛盾；且 1.69/3.90/4.11/6.50 在 §3.6（`:113`）与 Table 6 脚注（`:378`）两处一致。Table 6 的 share ratio（PAIN 0.573/0.618、VOMITING 2.449/1.568、DRUG INEFFECTIVE 2.796/5.931）经 1.064/1.855、1.596/0.652 等重算吻合。✅ 无矛盾。
- **§3.3 "each naming the same perioperative combination of remifentanil, sufentanil, fentanyl, hydromorphone, ketamine, oxycodone and propofol"**：见下方 F1。
- **§4.6 "one report in 200 to 500"**：见下方 F2。
- 其余叙述-表格数值（§3.2 的 8 161/523；§3.3 的 315/6.80、278/9.94、79/5.86、18 fen/30 mor；§3.4 的 0.066/0.281/0.046、1.310；§3.6 的 102/111、0.399、1.791、0.640/0.978、12 104/2.25、328 048/2.69、257 029/4.55；§3.7 的 11 882 968、5 270/98.0%、4.309、0.014–0.168、0.019–0.097、2.495/3.495；§4.1 的 4.73/2.54–8.80）均与其对应表/CSV 一致。✅

---

## 发现的问题（按四段式）

### F1（低严重度）§3.3 称 9 份报告"each naming the same [7 药] combination"与实际数据不符

- 【Problem】 §3.3 写 9 份美国报告"各自命名了相同的围手术期组合（remifentanil、sufentanil、fentanyl、hydromorphone、ketamine、oxycodone、propofol）"，但稿件自己 Table S9 Panel B 显示只有 6/9 命名全部 7 种药，且首份报告（24402565）根本不含 fentanyl/sufentanil。
- 【Evidence】 `I_正文_IMRaD_en.md:97`（"each naming the same perioperative combination of remifentanil, sufentanil, fentanyl, hydromorphone, ketamine, oxycodone and propofol"）对比 `13_report_series_hyperaesthesia.csv:4`（24402565 的 products = ACETAMINOPHEN, BUPIVACAINE;LIDOCAINE, HYDROMORPHONE, KETAMINE, OXYCODONE, PROPOFOL, REMIFENTANIL，无 fentanyl、无 sufentanil）以及 Table S9 Panel B 脚注（`:657`："all nine name hydromorphone, ketamine, oxycodone, propofol and remifentanil, and six of the nine name all seven products"）。
- 【Why it matters】 核心结论（9 份=1 名患者、共 2 名患者）仍由人口学/日期/产品高度重叠支撑，不受影响；但"每份都含同一 7 药组合"是过度陈述，且与稿件自身 Panel B 的"6/9"自相矛盾，细心的审稿人/统计学编辑会发现此不一致，削弱叙述可信度。
- 【Specific fix】 将 `:97` 改为与 Panel B 一致的表述，例如："nine reports that all name hydromorphone, ketamine, oxycodone, propofol and remifentanil, with six of the nine also naming fentanyl and sufentanil as part of the same perioperative combination"，并保留"only the content, not the identifier, links them"的限定。

### F2（低严重度）§4.6 "one report in 200 to 500" 范围低估

- 【Problem】 §4.6 称 HYPERAESTHESIA"one report in 200 to 500, depending on the drug (Table 2)"，但 Table 2 脚注给出的各药实际比率为 remifentanil 1/538、fentanyl 1/387、sufentanil 1/296、morphine 1/216，跨药范围为 216–538，其中 remifentanil 的 538 超出 500。
- 【Evidence】 `I_正文_IMRaD_en.md:157`（"one report in 200 to 500"）对比同稿 `:259` Table 2 脚注（"one report in 538 for remifentanil, one in 387 for fentanyl, one in 296 for sufentanil and one in 216 for morphine"）。重建：5375/10=537.5≈538、121819/315=386.7≈387、6513/22=296.0、56501/262=215.6≈216，均与表注吻合。
- 【Why it matters】 属措辞性不精确而非数据错误；但"200 to 500"与稿件自身 Table 2 注的精确值不一致，且会轻微低估 remifentanil 的稀有度（538>500）。不影响任何统计结论。
- 【Specific fix】 将 `:157` 改为 "one report in roughly 216 to 540, depending on the drug (Table 2)" 或 "one report per 200–540 reports"，或明确写成 "remifentanil 1 in 538 … morphine 1 in 216"。

### （补充说明，非问题）Bonferroni 下界 1.61 可复现
Table 2 脚注"with a Bonferroni correction across all 72 drug–term comparisons the lower bound … remains above one (1.61)" 经重建可复现：HYPERAESTHESIA remi ROR=4.7288，log=1.5541；SE≈√(1/10+1/5365+1/8151)=0.3167；72 次比较 Bonferroni 双尾临界 z=Φ⁻¹(1−0.05/(2·72))=3.396；下界 log=1.5541−3.396·0.3167=0.4785，exp=1.613≈1.61。✅ 该声明可溯源、可复现，不构成问题。

---

## § Stands up（稿件站得住的点）

1. **所有队列规模、分子计数、ROR/RORR 均与源 CSV 数值级吻合**：FAERS/Canada 队列（Table 1）、HYPERAESTHESIA 的 ROR 4.73 与 RORR 0.696/0.389（第 2 项由 2×2 重建至 4 位小数一致）、以及 Table S5 的 comparator a 列与 Table 2 完全对应——证明稿件未手改、未搬错数字。
2. **跨库与敏感性分析自洽**：Table 3 的 PAIN/VOMITING/HYPERAESTHESIA 加拿大值逐一等于 `cv/cv_indication_strata.csv`；Table 4C 的 2024 a=8/ROR 72.856、去 2024（a=2, ROR 1.005）与限制 2015–2023（a=1, ROR 0.701）精确对应 `04_sensitivity_year_hyperaesthesia.csv` 与 `19_leave2024_hyperaesthesia.csv`；§3.7 簇声明精确对应 `20_2024cluster_membership.csv`（8/8、7/7、5/17、0/21）。
3. **重叠/病例系列/图-表一致性无懈可击**：Table S8 Panel A 重叠矩阵与 `11_overlap_matrix.csv` 完全吻合，Panel B 的"去共享后 RORR"11 行逐格等于 `17_overlap_adjusted_rorr.csv`；Table S9 的 10 份报告与 `13_report_series_hyperaesthesia.csv` 逐格一致；Figure 1 运行期读取 `01_faers_results.csv`，其打印值即 Table S5 值，图与表同源、无漂移风险。

---

## § Questions for the authors

1. §3.3 与 Table S9 Panel B 对"9 份报告共享的产品组合"的描述不一致（见 F1）：是否同意将正文改为"all nine name hydromorphone, ketamine, oxycodone, propofol and remifentanil; six of nine name all seven"，以与数据一致？
2. §4.6 的"200 to 500"是否应据 Table 2 脚注改为"216 to 538"（见 F2）？
3. Table 6 的 Mantel–Haenszel RORR（如 VOMITING vs fentanyl 3.765、PAIN 0.640/0.978）依赖按反应条目数分层的 band 级数据，仓库中未提供可直接复算的 band CSV——能否在补充材料中给出 band 级 2×2 以便独立复现 MH 估计？
4. §3.5 "Of the comparator terms only vomiting could be tested in Canada; the others were empty" 中，NAUSEA/PRURITUS/CONSTIPATION 在加拿大 remifentanil 的 a 是否确实为 0（即 Table 3 未列出它们是因为 a=0 而非遗漏）？建议确认 Table 3 已覆盖全部 18 个术语（当前缺失 NAUSEA、PRURITUS、CONSTIPATION 的加拿大行——若其 a=0，建议在脚注统一说明"其余 comparator 术语在加拿大 remifentanil 队列 a=0，未单列"）。

---

## § What I actually checked（文件、命令、每个重算值 vs 稿件、是否发现差异）

**读取并核对的源文件（均来自仓库，未调用 API）：**
- `01_faers_results.csv`（18 术语 × 4 药的 a / ROR / PRR / IC / RORR，全表）
- `11_overlap_matrix.csv`、`17_overlap_adjusted_rorr.csv`、`13_report_series_hyperaesthesia.csv`、`19_leave2024_hyperaesthesia.csv`、`20_2024cluster_membership.csv`
- `04_sensitivity_year_pain.csv`、`04_sensitivity_year_hyperaesthesia.csv`、`16_year_trend.csv`
- `cv/cv_drug_totals.csv`、`cv/cv_whole_corpus_pt_counts.csv`、`cv/cv_indication_strata.csv`、`cv/cv_reaction_onset_completeness.csv`
- `05_figures.py`（图 1/图 2 取值逻辑）
- 稿件 `I_正文_IMRaD_en.md` 全文（含 Table 1–6、S1–S9、附录 A1、图注）

**运行的重算命令（Python，N=20 692 687，cohort 取 `11_overlap_matrix.csv`）：**
1. 由 2×2 重建每个术语、每个药的 ROR = a·d/(b·c)，再算 RORR = ROR_remi / ROR_comp，并与 `01_faers_results.csv` 存储值比较：13 个可估术语的 ROR_remi、RORR_fen/su/mor 最大绝对差 **0.0005**（即纯舍入），例如 HYPERAESTHESIA ROR_remi 重算 4.7288 vs 存储 4.729、RORR_fen 0.6960 vs 0.696、RORR_mor 0.3887→0.389；PRURITUS vs su 1.3098→1.310。→ **无差异**。
2. 重建 HYPERAESTHESIA RORR vs fen=0.696、vs mor=0.389（第 2 项要求）。→ **与稿件一致**。
3. 重建去 2024 的 ROR = 2·(19 373 581−2−4925−7822)/(4925·7822)=**1.0051**（稿件 1.01）；限制 2015–2023 的 ROR=**0.7009**（稿件 0.701）。→ **与 `19_leave2024_hyperaesthesia.csv` 一致**。
4. 重建 2024 HYPERAESTHESIA RORR vs fen=72.856/29.199=**2.495**、vs mor=72.856/20.845=**3.495**（Table 4C `:338`）。→ **一致**。
5. 重建 Table S8 Panel A 百分比：1575/5375=29.3%、483/5375=9.0%、323/5375=6.0%（`:602`）。→ **与 `11_overlap_matrix.csv` 一致**。
6. 逐行对照 `17_overlap_adjusted_rorr.csv` 与 Table S8 Panel B 的"去共享后 RORR"（11 行全部逐格相等）。→ **无差异**。
7. 逐行对照 `cv/cv_indication_strata.csv` 与 Table 3 / Table 5 的 PAIN、VOMITING、HYPERAESTHESIA、DRUG INEFFECTIVE（All / Perioperative / Pain 三层）的 a 与 RORR（如 All PAIN 0.235/0.146、Perioperative PAIN 0.399/0.161、Pain-indication PAIN 1.791/1.416、All VOMITING 1.066/0.392）。→ **无差异**。
8. 对照 `13_report_series_hyperaesthesia.csv` 与 Table S9 Panel A/B（10 份报告的 ID/日期/国家/年龄/性别/产品全字段一致）。→ **无差异**。
9. 对照 `20_2024cluster_membership.csv` 与 §3.3/§3.7/Table 4C 的簇声明与年份 a（8/8、7/7、5/17、0/21；2024 Fen a=17、Mor a=21）。→ **无差异**。
10. 对照 `16_year_trend.csv` 与 §3.7 的 Poisson 趋势（remi 4.0385 (p≈0)、fen 1.1375 (p≈0)、su 1.0691 (p=0.52465)、mor 1.0423 (p=0.09853) → 稿件 "4.04 / 1.14 / 1.07 / 1.04" 与 "p<10⁻⁴, p<10⁻⁴, p=0.53, p=0.10"）。→ **一致**。
11. 对照 `cv/cv_reaction_onset_completeness.csv` 与附录 A1.9（Hyperaesthesia 13/523、Procedural pain 57/1527、Pain 1196/49260）。→ **一致**。
12. 复核 Figure 1：确认 `05_figures.py` 运行期读取 `01_faers_results.csv` 的 RORR 列，其值与 Table S5 逐格相同。→ **图=表，无漂移**。
13. 复核 Bonferroni 下界 1.61（Table 2 脚注）可由 72 次比较、SE≈0.3167 重建（exp(1.5541−3.396·0.3167)=1.613）。→ **可复现**。
14. 表语法/列对齐扫描（Table 1–6、S1–S9）：分隔符与列数匹配。→ **无断表/错位**。
15. Table 6 share ratio 重算（PAIN 1.064/1.855=0.573、1.064/1.721=0.618 等）吻合；mean 1.69 在 §3.6 与 Table 6 脚注一致。→ **无矛盾**。

**差异汇总：** 仅 F1（§3.3 措辞过度陈述，与自身 Table S9 Panel B 的"6/9"矛盾）与 F2（§4.6 "200 to 500" 应为 216–538）两处低严重度叙述-数据措辞不一致；**未发现任何数值性（数字对错、搬错、双重舍入、表间矛盾）差异**。
