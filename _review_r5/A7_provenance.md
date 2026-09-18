# Round-5 独立审稿 — A7_provenance 数据溯源与计算审计员

## 0. 审稿人身份与总体结论

我自己做药物警戒失衡分析的方法学与统计复现工作十余年，主要工作是"拿别人的结果文件按 2×2 表重算一遍"，因此本轮只做一件事：**独立重算与逐格比对**。我不评价写作风格。

**Verdict: Minor Revision**

理由（具体到本稿）：

1. **表格与源数据的吻合度极高。** 我把 Table 2、Table 3、Table 4A/4B/4C、Table S1（Panel A 与 Panel B）、Table S3、Table S4、Table S5 中每一个数字都解析出来与源 CSV 逐格比对，共约 **1 196 格**，只有 **2 格**对不上——Table S3 的两个百分比（吗啡 18–64 岁组写 54.4，正确 54.3；芬太尼 Female 写 43.2，正确 43.1），且都由"先把 CSV 的两位小数再四舍五入到一位"的双重舍入造成。ROR 由 a、PT_total、N 独立重算的最大相对误差 9.0×10⁻⁴，全部落在三位小数显示精度内。加拿大侧更进一步：我不使用作者的任何中间文件，直接用字节级流式解析原始 line-listing（合计约 2.1 GB、近 1 000 万行）重建队列，把 `cv_soc_27.csv` 与 `cv_pt_summary.csv` **端到端复现，逐格不一致 = 0**。

2. **但"RORR"这个统计量在两库里不是同一个定义，而稿件只描述了其中一个。** FAERS 侧实现为"各自 c、d 的 ROR 相除"，加拿大侧实现为"共享 c、d 的 ROR 相除"；§2.4 的"Both ratios share the same background reference, so comparator-specific terms cancel"只对加拿大侧成立。按 §2.4 的文字与 Table S5 脚注承诺的方式（"可由计数重算"）用计数直推，HYPERAESTHESIA vs fentanyl 得 **0.719**，稿件是 **0.696**（差 3.3%）——偏偏差在全文最核心的那个数上。

3. **结论里有一句与自己的源数据直接矛盾。** §5 说"the four negative controls … could not be tested in Canada"。但 `cv/cv_pt_summary.csv` 的 VOMITING 行有 remifentanil a = 3（芬太尼 124、舒芬 1、吗啡 508），加拿大侧**可算**：RORR vs fentanyl = **1.066**、vs morphine = 0.392。这是四个阴性对照里唯一可算的一个，而且它对芬太尼的方向与 FAERS（0.409）相反。稿件既没报告、又在结论里说"无法检验"。**这一判定我不依赖作者的中间文件**：我直接流式解析加拿大原始 line-listing（`reactions.txt` 4 474 923 行、`report_drug.txt` 5 066 837 行）重建队列后重算，VOMITING 四药计数 3 / 124 / 1 / 508、全库 c = 38 452，与 CSV 完全相同；同一条独立管线把加拿大侧 27 SOC 表与 PT 表 100% 复现（逐格不一致 = 0）。

4. 其余为可文字修补的问题：§2.4 的协方差量级（"under 0.001%"）经重算应为 0.12–0.25%，差约 100 倍；Table 4C 题注"the table holds nine rows"与表实际十行不符；Figure 1 图注说"from the top"而图上顺序是自下而上；§9 溯源表漏了三个结果文件的映射，且第 539 行少一个竖线导致 Markdown 表格断裂。

5. 这些都不推翻任何方向性结论：PAIN 低报、阴性对照低报、加拿大库复现、2024 年聚集——我逐项独立算过，全部成立。

---

## 1. 重大问题（Major）

### M1 【结论第 5 节称"四个阴性对照在加拿大无法检验"，但其中 VOMITING 可算，且方向与 FAERS 相反】

**【问题】** §5 最后一段把加拿大侧的"不可检验"扩大到了全部四个阴性对照。源数据里 VOMITING 在加拿大**完全可算**，稿件既未报告、又据此宣称该部分"untested"。

**【证据】**
- `cv/cv_pt_summary.csv` 第 12 行：`VOMITING,negctrl,3,124,1,508,0.806,1.066,0.392`，即 REMIFENTANIL = 3、FENTANYL = 124、SUFENTANIL = 1、MORPHINE = 508，`RORR_REMI_vs_FEN = 1.066`、`RORR_REMI_vs_MOR = 0.392`。
- 我用两组计数独立重算（`cv/cv_pt_summary.csv` 口径 RORR = a_R·b_C /(b_R·a_C)，共享 c、d）：
  - vs fentanyl：(3×4757)/(108×124) = **1.065636** → 1.066 ✓
  - vs morphine：(3×7167)/(108×508) = **0.391896** → 0.392 ✓
- **该判定不依赖作者任何中间文件**：我以字节级流式解析直接重读加拿大原始 line-listing（`reactions.txt` 742 MB / 4 474 923 行、`report_drug.txt` 953 MB、`drug_product_ingredients.txt`），自己建立"活性成分 → 药品 → Suspect 报告"与"报告 → PT"两条链路，独立得到 VOMITING 全库报告数 c = **38 452**、四药 a = **3 / 124 / 1 / 508**，与 `cv/cv_pt_summary.csv` 逐格相同（脚本 `_review_r5/_a7_scratch/a7_cv_soc_full.py`，输出见 §6.6）。也就是说，"VOMITING 在加拿大可算"是原始数据层面的结论，不是对作者产物的二次引用。
- 对照稿件原文（`I_正文_IMRaD_en.md:193`）："the four negative controls are stable within FAERS but could not be tested in Canada, whose cohorts were too small"。
- 另三个阴性对照在加拿大的 remifentanil a 均为 0（NAUSEA 0、PRURITUS 0、CONSTIPATION 0，见 `cv/cv_pt_summary.csv` 第 11、13、14 行），确实不可算；**只有 VOMITING 例外**。我重算的全库 c 分别为 NAUSEA 63 311、VOMITING 38 452、PRURITUS 45 744、CONSTIPATION 13 366——四个对照在全库里都有几百到几千条报告，所以"加拿大队列太小"这一理由只在**暴露侧**（remifentanil a = 0）成立，不在分母侧成立；稿件把它写成四个对照整体不可检验，是把一个暴露侧的稀疏性说成了整组的不可能性。
- 该对比的结果方向：FAERS 侧 VOMITING RORR vs fentanyl = 0.409（<1），加拿大 = 1.066（>1）；vs morphine 两侧均 <1（0.185 / 0.392）。也就是说，报告出来会是"12 个低于 1 之外的另一处例外"。
- 注意稿件自己的信号阈值是 a ≥ 3（§2.4），VOMITING 的 a = 3 恰好等于阈值，按作者自己的规则没有理由排除。

**【为什么重要】** 这不只是措辞：稿件 §3.4 的论证支点之一是"阴性对照全线同向低报，说明不是全局报告假象"，§4.1 与 §5 都重复了这一点，并在 §4.5 用"加拿大阴性对照 too small"为"untested rather than confirmed"辩护。实际存在的唯一加拿大阴性对照检验结果与 FAERS 相反（对芬太尼），把它写成"无法检验"会同时触发两个问题：结论句与源数据不符，以及**选择性省略了一个不支持叙事的数据点**。审稿人一旦自己打开 `cv/cv_pt_summary.csv`（10 秒的事），对全文数值可信度的评价会立即下调——而这篇稿件的全部卖点就是数值可核查。

**【具体修改建议】**
1) §5 结论句改为（可直接粘贴）：
> "Its low reporting of pain, by contrast, is large, stable and reproduced in Canada (§4.1). Of the four negative controls only vomiting could be tested in Canada — three remifentanil reports, ratio 1.07 (95% CI not estimable with three reports) versus fentanyl and 0.39 versus morphine — while nausea, pruritus and constipation could not be tested, the remifentanil cell being empty in each; the Canadian vomiting comparison therefore neither confirms nor refutes the FAERS direction."
2) §3.4 末补一句并把表补全：
> "In Canada Vigilance only vomiting had a non-zero remifentanil cell (3 reports); the ratio was 1.07 versus fentanyl and 0.39 versus morphine, so the Canadian data neither reproduce nor contradict the FAERS direction for this control."
3) Table 3 增加一行 `VOMITING | 64 | 0.409 / 0.185 | 3 | 1.066 / 0.392 | no (direction reversed versus fentanyl)`，并在图注/正文注明加拿大侧该比值的 CI 不可估计（a = 3）。
4) §4.5 limitation 句由"too small for most ratios to be computed"改为精确表述："of the four negative controls only vomiting had a non-zero remifentanil cell (3 reports); the remaining three were untestable."

---

### M2 【"RORR"在 FAERS 与加拿大两库用的是两个不同定义；§2.4 的描述与 FAERS 实现不符，Table S5 的"可由计数重算"承诺不成立】

**【问题】** §2.4 声明两根 ROR"共用同一背景参考、对照特异项相消"，因此 RORR 可由计数直接重算。FAERS 侧的实现并非如此（每个药的对照列 c 与背景列 d 各不相同）；加拿大侧才是共享 c、d。于是同一个名为 RORR 的量，在两库里定义不同，而稿件只描述了一种。

**【证据】**
- 我用 `_faers_cache.json` 的 N 与队列数、`01_faers_results.csv` 的 a 与 PT_total 反推 2×2，并按"各自 c、d"重算（脚本 `_review_r5/_a7_scratch/a7_task1_rerun_ror2.py`）：
  - HYPERAESTHESIA vs fentanyl：CSV = **0.696**，我按"各自 c、d"算 = **0.695975**（完全吻合）；按"计数直推 (a_R·b_C)/(b_R·a_C)"算 = **0.718969**（差 **3.30%**）。
  - DRUG WITHDRAWAL SYNDROME vs fentanyl：CSV = 0.046，各自 c、d = 0.045705 ✓；计数直推 = 0.047216（差 2.64%）。
  - PAIN vs fentanyl：CSV = 0.066，各自 c、d = 0.066492 ✓；计数直推 = 0.066938（差 1.42%）。
  - 差异来源可解析：以 HYPERAESTHESIA 为例，c_R = 8161−10 = 8151，c_F = 8161−315 = 7846，d_R = 20 679 161，d_F = 20 563 022，修正因子 (d_R·c_F)/(d_F·c_R) = 0.9680。§2.4 说"对照特异项相消"在 c 上不成立（8151 vs 7846，差 3.9%）。
  - 全部 12 个 RORR 的两种口径偏差：HYPERAESTHESIA 3.30%/0.17%/2.85%（fen/suf/mor），PAIN 1.42%/0.11%/0.76%，PROCEDURAL PAIN 0.04%/0.03%/0.33%，DRUG WITHDRAWAL SYNDROME 2.64%/0.04%/1.05%。
- 加拿大侧 `cv/cv_process.py:218-226` 中 `c = len(global_pt[p])` 对所有药取同一值，同一 `N-c` 也相同，因此加拿大 RORR ≡ 计数直推口径。我用该口径独立重算：PAIN 0.235361 / 0.145593，DRUG INEFFECTIVE 1.277142 / 1.703140，VOMITING 1.065636 / 0.391896——与 `cv/cv_pt_summary.csv` 完全一致。
- Table S5 脚注（`I_正文_IMRaD_en.md:493`）承诺："The last column gives the numerator for each comparator, so that every ratio printed here and in Table 2 can be recomputed from the counts alone." 按这句话去算，第 3 行（HYPERAESTHESIA）会得到 0.719 而不是 0.696。

**【为什么重要】** §2.5 明说加拿大侧"ratios were computed as in §2.4"，而 §2.4 的文字只在加拿大成立；Table 3 的全部意义就是跨库比较，读者会默认两侧的 RORR 是同一统计量。偏差量级不大（≤3.3%），方向与结论都不会翻，但这是**方法学描述与代码实现不一致**，在一篇以"术语与数值可核查"为卖点的稿件里是不能留下的。它还有第二层后果：Table S5 是作者提供的"自查入口"，脚注承诺的复算路径给出不同的数，等于把审稿人引到一个假阳性差异上。

**【具体修改建议】**
1) §2.4 第三段改为（可直接粘贴）：
> "Head-to-head comparison used the ratio of reporting odds ratios (RORR), remifentanil divided by the comparator. Each ratio was computed in its own 2×2 table, in which c is the whole-corpus count of the term minus that drug's own count and d is all remaining reports, so the two ratios do not share their event column exactly and no term cancels algebraically; with 20 692 687 background reports the two d values differ by under 0.6% and the two c values by the term's own frequency in the cohort."
2) Table S5 脚注末句改为：
> "The last column gives the numerator for each comparator; together with the cohort sizes in Table 1, the whole-corpus term totals in the analysis output files and the 2×2 convention in §2.4, every ratio printed here and in Table 2 can be recomputed."
3) 在 §2.5 加拿大段补一句明确两侧口径一致或不同的说明。**若能改代码，最干净的修法是把加拿大侧也改成"各自 c、d"，使两侧定义完全统一**——但请注意这不是"数字不变"的改动：我按两种口径都算了一遍，Table 3 的四个加拿大比值里**有两个会在三位小数上发生变化**：
   - PAIN vs fentanyl：共享 0.235361 → 各自 0.234587（仍印 **0.235**，不变）
   - PAIN vs morphine：共享 0.145593 → 各自 0.143880（**0.146 → 0.144，要改**）
   - DRUG INEFFECTIVE vs fentanyl：共享 1.277142 → 各自 1.276901（仍印 **1.277**，不变）
   - DRUG INEFFECTIVE vs morphine：共享 1.703140 → 各自 1.705693（**1.703 → 1.706，要改**）
   共同因子为 (d_R·c_C)/(d_C·c_R)，在 PAIN vs morphine 上等于 0.9882，即 −1.18%——因为加拿大队列只有 111 人，`b_R` 很小，而 `c` 又是全库级的大数，"共享 c、d"与"各自 c、d"不再近似相等。所以两条路只能选一条：要么统一口径并同步更新 Table 3 的这两格，要么保留现状并在题注明说两库口径不同。**不要只改文字不改数**。
   附带说明：加拿大侧两种口径的差异（最大 1.18%）比 FAERS 侧（最大 3.30%，见上）小，但仍足以跨过第三位小数，因此不能以"量级可忽略"为由省略说明。

---

### M3 【Table 4C 题注"the table holds nine rows"与表的十行结构不符】

**【问题】** 题注把"九份带日期报告"说成"表里有九行"。Table 4C 是按年分行的表，2015–2024 共 **10 行**；九份报告分布在 2021（1 份）与 2024（8 份）两个年份行上。

**【证据】**
- 稿件原文（`I_正文_IMRaD_en.md:366`）："nine reports carry a usable receivedate in 2015–2024 (eight in 2024; the tenth omitted), so the table holds nine rows."
- Table 4C 表体从 2015 到 2024，逐行列出，共 10 行。
- `04_sensitivity_year_hyperaesthesia.csv` 的 `REMIFENTANIL_a` 列：10 个年度值依次为 0,0,0,0,0,0,1,0,0,8，**合计 = 9**，与"nine reports carry a usable receivedate"完全一致。
- 我独立核对 §3.3 的 8 + 1 + 1：`01_faers_results.csv` 的 HYPERAESTHESIA `REMIFENTANIL_a = 10`；2024 年 8 份（次年表）+ 2021 年 1 份（次年表）+ 无日期 1 份 = 10 ✓，与 `04_sensitivity_leave2024_hyperaesthesia.csv` 的 `a_excl2024 = 1, cohort_excl2024 = 3798` 也自洽（5375 − 8 − 1 = 5366；再扣除 2024 年队列后剩 3798——两者口径不同，见下条澄清）。**8+1+1 与 9 的关系本身没有问题**，错的是"nine rows"这四个字。

**【为什么重要】** 这是"读者一眼能数出来"的错。稿件通篇强调每个数都对得上源文件，而这里稿件与自己的表体（10 行）直接冲突；审稿人不需要任何工具就能发现，会直接质疑 §9"每个数字都可溯源"的强声明。

**【具体修改建议】** 题注末句改为：
> "Nine of the ten reports carry a receivedate in 2015–2024 (eight in 2024 and one in 2021; the tenth is undated and falls outside the table), so the remifentanil column of this table sums to nine."

---

### M4 【Table S3 两个百分比是双重舍入的产物，与"该药队列的百分比"不符】

**【问题】** Table S3 题注定义括号内为"该药队列的百分比"，但两格是把源 CSV 的两位小数再舍入到一位，导致与 n/队列 的正确一位小数不一致。

**【证据】**（脚本 `_review_r5/_a7_scratch/a7_task_s3_pct.py`，逐格独立算 `100×n/队列`）
- **Age 18–64 years / Morphine**：n = 4171，队列 7675 → 100×4171/7675 = **54.3453%**，正确一位小数 = **54.3**；稿件写 **54.4**。源 `cv/cv_subgroups.csv` 存的是 2 位 54.35，54.35 →（半进位）54.4 是双重舍入。
- **Female / Fentanyl**：n = 2106，队列 4881 → **43.1469%**，正确一位 = **43.1**；稿件写 **43.2**。源存 43.15。
- 同表其余 46 个百分比格全部正确（例如 Remifentanil 的 "Age not stated 49 (44.1)"——49/111 = 44.1441% → 44.1 ✓；"Serious report 102 (91.9)"——91.8919% → 91.9 ✓），全部 108/108 个 Table S3 计数格也都与 `cv/cv_subgroups.csv` 一致。

**【为什么重要】** 影响面很小（0.1 个百分点，不触及任何结论），但它是同类错误的一个实例：只要有一处是"对已舍入值再舍入"，就说明百分比不是逐个从计数算的，而这正是 Table S3 题注所承诺的算法。审稿人若在 `_review_r5` 之外自己抽查，会得到"表格百分比不可全信"的印象。

**【具体修改建议】** Table S3 两格改为 `4 171 (54.3)` 与 `2 106 (43.1)`；并在题注补一句：
> "Proportions are computed from the counts and the cohort size and then rounded to one decimal place, not rounded from a previously rounded value."

---

### M5 【Figure 1 图注说术语"from the top"自上而下排列，图上是自下而上】

**【问题】** 图注描述的分组顺序与图内实际纵向顺序相反（图是上下翻转的）。

**【证据】**
- 图注（`I_正文_IMRaD_en.md:522`）："Terms are grouped from the top: the preferred term carrying the hyperalgesia concept (HYPERAESTHESIA) and the two nearest retrievable siblings (PROCEDURAL PAIN, DRUG WITHDRAWAL SYNDROME); the pragmatic proxy PAIN; the four negative controls (NAUSEA, VOMITING, PRURITUS, CONSTIPATION); and the specificity probe DRUG INEFFECTIVE."
- 我读 `I_fig1_rorr_forest.png`（4 251 × 3 960 px，600 ppi，180 mm 双栏）：**纵轴自上而下**依次是 DRUG INEFFECTIVE、CONSTIPATION、PRURITUS、VOMITING、NAUSEA、PAIN、DRUG WITHDRAWAL SYND.、PROCEDURAL PAIN、HYPERAESTHESIA——与图注所述顺序完全颠倒。
- 代码成因可定位：`05_figures.py:94-103` 的 `SHOWN` 列表把 HYPERAESTHESIA 排在首位，`05_figures.py:142-143` 用 `yi = ROW*i` 绘图且未 `invert_yaxis()`，matplotlib 的 y 轴向上递增，于是列表首项落在图底。
- 图内数值我逐个核对无误：HYPERAESTHESIA 0.696/0.549/0.389、PROCEDURAL PAIN 1.962/2.124/0.878、DRUG WITHDRAWAL SYNDROME 0.046/0.201/0.083、PAIN 0.066/0.281/0.046、NAUSEA 0.227/0.563/0.110、VOMITING 0.409/0.969/0.185、PRURITUS 0.833/1.310/0.328、CONSTIPATION 0.122/0.210/0.062、DRUG INEFFECTIVE 0.568/0.784/0.470，与 `01_faers_results.csv`（= Table S5）一致；`05_figures.py:113-125` 确为逐格读 CSV，无硬编码。

**【为什么重要】** 图注是读者读图的唯一指引。现在读者按"from the top"去找 HYPERAESTHESIA，会在最底部才找到，且会把 DRUG INEFFECTIVE 误认为 OIH 相关术语——恰好与全文"术语选择决定结论"的主旨相冲突，观感极差。

**【具体修改建议】** 二选一，必须与图一致：
- 改图注：把 "Terms are grouped from the top:" 改为 "Terms are grouped from the bottom:"；
- 或改代码：在 `05_figures.py` 的 `clean_axes(ax, keep=("bottom",))` 之后加 `ax.invert_yaxis()`（或把 `SHOWN` 列表反向），重出 tif/pdf/png 三个文件，并保留图注原文。

---

## 2. 重要问题（P1）

### P1-1 【§2.4 关于"被忽略的协方差不足方差 0.001%"的量化声明经重算差约 100 倍】

**【问题】** §2.4 用"背景报告数高达 20 692 687，故被忽略的协方差不到方差的 0.001%"为"把两根 ROR 当独立处理"辩护。按标准多项分布协方差重算，该比例约为 **0.12%–0.25%**，比声明大两个数量级。

**【证据】** 以 HYPERAESTHESIA vs fentanyl 的两个 2×2 为例（a_R=10, b_R=5365, c_R=8151, d_R=20 679 161；a_F=315, b_F=121 504, c_F=7846, d_F=20 563 022）：
- 稿件的独立近似：Var(log RORR) = 1/10 + 1/5365 + 1/8151 + 1/20 679 161 + 1/315 + 1/121 504 + 1/7846 + 1/20 563 022 = 0.1003091 + 0.0033103 = **0.1036194**（SE = 0.32190，与 `01_faers_results.csv` 印出的 0.37–1.31 完全一致，说明 CI 就是按这个算的）。
- 共享成分的量级：主控项来自"事件列中扣除本药后的报告数"（c_R 与 c_F 的重叠部分约 7 836 份），Cov(log ROR_R, log ROR_F) ≈ −1/7836 ≈ **−1.28×10⁻⁴**（按多项分布 Cov(log n_A, log n_B) ≈ (δ_AB/μ_B − 1)/N 逐项展开，非对角元相消后仅剩该量级；若按 §2.4 文字所述"共享同一 c、d"，则需要计入 Var(log c − log d) ≈ 1/8151 + 1/20 679 161 ≈ **1.23×10⁻⁴**）。
- 因此 |2Cov| / Var = 2.55×10⁻⁴ / 0.1036 ≈ **0.25%**（共享 c 口径下约 0.12%），而 0.001% × 0.1036 = 1.04×10⁻⁶。声明偏小约 **120–250 倍**。
- 方向上，Cov < 0，忽略它会使区间变宽（保守），所以"so it is conservative"这句结论本身站得住；站不住的只有"under 0.001%"这个量。

**【为什么重要】** 这是 §2.4 里唯一一个"看起来像被算过"的量化量，而它恰好没算对。对一个把"数字都可核查"写进 AI 声明与 §9 的稿件，一个偏小 100 倍的界反而比不说更危险：生物统计审稿人会直接把它当成"数量级直觉缺失"的证据，进而重查全部方法学段落。

**【具体修改建议】** 删除这个界，或改成经得起推敲的表述（可直接粘贴）：
> "Confidence intervals used the log scale with the sum of the reciprocal cell counts (Woolf approximation), treating the two ratios as independent. The two 2×2 tables are not strictly independent — the event column and the background column overlap in the reports of the other drugs — but the overlap involves on the order of 1/c reports, so the ignored covariance is of order 10⁻⁴ against a log-scale variance of 0.10, i.e. about 0.1% of the variance, and its sign makes the intervals slightly wider than the true ones."

### P1-2 【§2.3 称两个先验术语"produced no estimable result"，但 Table 2 给出了 ALLODYNIA 的 OR 与区间】

**【问题】** §2.3 用"两个先验痛觉过敏术语均无可估计结果"作为"本研究是假说生成而非验证性"的依据；实际 ALLODYNIA 在瑞芬队列 a = 1，2×2 无空格，OR 与 CI 都能算，稿件自己也印出来了。

**【证据】**
- §2.3（`I_正文_IMRaD_en.md:67`）："Consequently the two a priori hyperalgesia outcomes (HYPERALGESIA, ALLODYNIA) produced no estimable result, so the study is reported as hypothesis-generating rather than confirmatory."
- Table 2 第 2 行：`ALLODYNIA | narrow | 1 | 3.47 (0.49–24.67) | … | 0.455† (0.06–3.30) | 0.342† (0.05–2.51)`；`01_faers_results.csv` 第 3 行为 `ALLODYNIA,…,1110,1,3.471,0.49-24.67,…,0.455,0.06-3.30,,,0.342,0.05-2.51`。四个格 (1, 5374, 1109, 20 686 203) 均非零，ROR 与 RORR 都可估计——我按 2×2 独立重算得 3.4713 / 0.4552 / 0.3421，与 CSV 一致。
- 稿件在别处的表述更准确：§3.3 "ALLODYNIA … is not estimable for remifentanil, which contributed a single report (a = 1); the only defensible fact is the absence of a signal"。可见"not estimable"被当成了"a < 3、不可信"的同义词。
- 一个统计量在 2×2 无空格时是**可估**的，"达不到信号阈值（a ≥ 3）"是另一回事。

**【为什么重要】** 稿件的自我定位（hypothesis-generating 而非 confirmatory）建立在"先验结局一个都没算出来"之上。这个前提实际上只对 HYPERALGESIA 成立。作者若坚持这句，等于用一个不准确的统计表述支撑全文定位；审稿人（尤其统计背景的）会立刻指出"a = 1 不是不可估计，只是不稳定"，并要求重述。另外，全文主题就是"术语与用词的精确性"，这里却把"不可估计"和"不可信"混用，自相矛盾。

**【具体修改建议】** 改为：
> "Consequently neither a priori hyperalgesia outcome met the signal criterion: HYPERALGESIA returned no report in either corpus, and ALLODYNIA contributed a single remifentanil report, so its estimate is uninterpretable (Table 2). The study is therefore reported as hypothesis-generating rather than confirmatory."
并在 §3.3、Table 2 脚注中统一把 "not estimable" 改为 "not interpretable (a < 3)"，只对真正出现空 2×2 格的情形保留 "not estimable"。

### P1-3 【§3.4 首句即被同句后半段自我否定】

**【问题】** "The same pattern held for every negative control across all three comparators" 与紧随其后的 "eleven of the twelve … the exception being pruritus versus sufentanil" 直接冲突。

**【证据】** `I_正文_IMRaD_en.md:117`。我从 `01_faers_results.csv` 逐格数了 4 个阴性对照 × 3 个对照药 = 12 个 RORR：NAUSEA 0.227/0.563/0.110、VOMITING 0.409/0.969/0.185、PRURITUS 0.833/**1.310**/0.328、CONSTIPATION 0.122/0.210/0.062，确为 **11 个 < 1、1 个 > 1**——后半段的算术完全正确，错的是前半段的"every"。

**【为什么重要】** 这种"总述与细节同句互斥"的写法在方法学论文里会被直接引用为"作者对自己数据的概括不严谨"。数量与结论都没错，是措辞把关不严。

**【具体修改建议】** 首句改为：
> "The same direction held for the negative controls against both fentanyl and morphine, and for nausea, vomiting and constipation against sufentanil: eleven of the twelve computable ratios were below 1, the exception being pruritus versus sufentanil (1.310, 0.84–2.04), whose interval includes one."

### P1-4 【§9 溯源表漏映射三个结果文件，且有一行 Markdown 结构损坏；"FAERS cohort sizes"指到了不含队列数的文件】

**【问题】** 稿件的强声明是"每个数字都可溯源到源文件"，而 §9 表既漏项，又有一行少一个竖线（表格会断），且把队列规模指向了实际不含队列规模的 CSV。

**【证据】**（对 `I_正文_IMRaD_en.md:528-547` 逐行统计竖线数）
- 第 539 行 `| Year-stratified PAIN (FAERS) | 04_sensitivity_year_pain.csv` 只有 **2 个竖线**（其余 16 行均为 3 个），Markdown 渲染时该行会被吞掉或错位。
- 缺映射的正文数字（我逐个在全部源结果文件中检索）：
  - **11 882 968**（§3.8 "Restricting FAERS to serious reports (11 882 968)"）与 **5 270**（"remifentanil contributed 5 270 of 5 375 reports (98.0%)"）：`04_sensitivity_ps_only.csv`（§9 指定的文件）**不含**这两个数（该 CSV 表头无任何分母/队列列）；它们的唯一出处是 `_faers_cache.json` 的 `serious:1 = 11882968` 与 `…("REMIFENTANIL" "REMIFENTANIL HYDROCHLORIDE") AND serious:1 = 5270`（另有 `04_sensitivity_run.log` 记录）。
  - **15.4 / 4.3 / 4.9 / 1.7**（§3.8 的 year-to-pooled 比值）：只出自 `04_sensitivity_2024cluster_hyperaesthesia.csv`（`ratio_2024_to_pooled` = 15.41 / 4.30 / 4.90 / 1.71），而 §9 **完全没有这一文件的行**。
  - **300 / 4 000**（首页 Word count）与 `04_sensitivity_estimable_years.json`（"8 of the ten years"的依据）同样不在 §9。
  - §9 首行把 "FAERS cohort sizes" 指向 `01_faers_results.csv`，但该 CSV 只有 PT 级 a 与统计量，**没有 5 375 / 121 819 / 6 513 / 56 501**；这四个数只在 `_faers_cache.json`。
  - **1.61**（Table 2 脚注的 Bonferroni 下界）不是任何文件的存储值，需由 `01_faers_results.csv` 的 4.729 与 4 个格反推（我复算：z(0.05/72) = 3.3955，exp(ln4.7288 − 3.3955×0.31672) = **1.6132** → 1.61 ✓，算式本身无误，但属"派生量"而非"直接读取"）。

**【为什么重要】** §9 与 AI 声明里的 "each number in the manuscript is traceable to its source file" 是作者对期刊的正式承诺。现在有三处数字在 §9 指定的文件里找不到，其中两处（11 882 968、5 270）需要打开一个 §9 只用来解释"总 N"的文件才能找到，另有一处（15.4 系列）连文件都没列。再叠加一行坏的 Markdown，审稿人完全有理由把"可溯源"降级为"大体可溯源"。

**【具体修改建议】**
1) 修第 539 行末尾补 ` |`。
2) §9 增加三行（可直接粘贴）：

| Reported quantity | Source file |
|---|---|
| Serious-report subset size and per-cohort serious counts (11 882 968; 5 270 / 97 881 / 6 412 / 49 058) | `_faers_cache.json` (`serious:1` keys); `04_sensitivity_run.log` |
| Year-to-pooled odds-ratio ratios for the 2024 cluster (15.41 / 4.30 / 4.90 / 1.71) | `04_sensitivity_2024cluster_hyperaesthesia.csv` |
| Number of estimable years by term, and word counts | `04_sensitivity_estimable_years.json`; `_wordcount.py` |

3) 首行拆成两行：`FAERS cohort sizes | _faers_cache.json`；`FAERS preferred-term a, OR, PRR, IC, EBGM, RORR | 01_faers_results.csv`。
4) 在 Table 2 脚注注明 1.61 为派生量："the bound is obtained by replacing 1.96 with the two-sided 0.05/72 normal quantile (3.396) in the Woolf interval of the remifentanil HYPERAESTHESIA odds ratio."

### P1-5 【"main text 4 000 words"与可复算的字数不符】

**【问题】** 首页声明 "Summary 300 words; main text 4 000 words"，并注明"Verified with `_wordcount.py`"。我按多口径独立统计，正文（Introduction→Conclusion）在 3 789–3 951 之间，取不到 4 000。

**【证据】** 我独立分词统计（脚本见 §6）：
- Summary：299 词（与"300"相符，且落在期刊 250–300 的限内）。
- 正文 Introduction→Conclusion：**不含**节标题 = 3 820（数字作分词计）／3 789（"20 692 687" 记为 1 词）；**含**节标题 = **3 951**／3 920。
- 分节：Introduction 371、Methods 1 196、Results 1 090、Discussion 1 045、Conclusion 172。

**【为什么重要】** 数字本身没超限（3 000–4 000 内），风险为零，但它是"稿件首页自己给的数"，而 §9 没有它的源。审稿人看到 `Verified with _wordcount.py` 却算不出同一个数，会追问计数规则（是否含节标题、数字/连字符如何计）。

**【具体修改建议】** 改为实测值并写明口径，例如：
> "Word count: Summary 299 words; main text 3 951 words (Introduction to Conclusion, section headings and in-text citation numbers included, multi-word numerals counted as one). Tables: 1–3 and 4A–4C (six table objects) plus 5 supplementary. Figures: 2."

---

## 3. 次要问题（P2）

### P2-1 【首页 "Tables: 4 (Table 4 in three panels)" 与实际表对象数不符】
**【问题】** 正文实际有 Table 1、2、3、4A、4B、4C 共 6 个表对象，声明写"4"。
**【证据】** `I_正文_IMRaD_en.md:13`："**Tables:** 4 (Table 4 in three panels) plus 5 supplementary."表体实际为 `### Table 1.`、`### Table 2.`、`### Table 3.`、`### Table 4A.`、`### Table 4B.`、`### Table 4C.`。
**【为什么重要】** 投稿系统与生产环节会按声明核对表数量；报少了容易在排版阶段被退回。
**【具体修改建议】** 改为 "Tables: 1–3 and 4A–4C (six table objects) plus 5 supplementary."

### P2-2 【Table 3 "Confirmed" 列对 DRUG TOLERANCE、HYPERPATHIA 的语义与题注不一致】
**【问题】** 这两行写 "yes (zero in both)"，但指的是"瑞芬太尼在两地均为 0"，而不是"该术语在两地都不可检索"（这两个词其实都可检索，对照药在两库都有计数）。
**【证据】** `I_正文_IMRaD_en.md:299、301`；`cv/cv_pt_summary.csv`：DRUG TOLERANCE = 0/25/0/30、HYPERPATHIA = 0/0/0/0；`01_faers_results.csv`：DRUG TOLERANCE 芬太尼 a = 278、吗啡 a = 79，HYPERPATHIA 芬太尼 a = 2、舒芬 a = 1。题注只解释了"五个不可检索字符串"的零（`I_正文_IMRaD_en.md:307`），没覆盖这两行。
- **我用原始 `reactions.txt` 数出了这两个词在加拿大全库的报告数 c**：DRUG TOLERANCE c = **386**、HYPERPATHIA c = **0**。也就是说两行的"zero in both"含义**互不相同**：DRUG TOLERANCE 在加拿大真实存在（386 份报告，只是没有一份归在瑞芬太尼名下），而 HYPERPATHIA 在加拿大整个语料库中确实一次都没出现。同一个短语同时承载两种截然不同的情形，读者无从分辨。
- 同样的歧义也波及 Table 3 的其余 "yes (zero in both)" 行。我把全部 14 行的加拿大侧 a 与全库 c 都独立算了：
  `HYPERALGESIA` a=0 / c=0；`ALLODYNIA` a=0 / c=**29**；`PAIN` a=2 / c=48 267；`PAIN INCREASED` a=0 / c=0；`POSTOPERATIVE PAIN` a=0 / c=0；`CHRONIC PAIN` a=0 / c=0；`OPIOID WITHDRAWAL SYNDROME` a=0 / c=0；`DRUG TOLERANCE` a=0 / c=386；`HYPERAESTHESIA` a=0 / c=**521**；`HYPERPATHIA` a=0 / c=0；`PROCEDURAL PAIN` a=0 / c=**1 510**；`CHRONIC PAIN SYNDROME` a=0 / c=0；`DRUG WITHDRAWAL SYNDROME` a=0 / c=**1 664**；`DRUG INEFFECTIVE` a=25 / c=205 227。
  其中 5 个术语（ALLODYNIA、DRUG TOLERANCE、HYPERAESTHESIA、PROCEDURAL PAIN、DRUG WITHDRAWAL SYNDROME）在加拿大有 29–1 664 份报告，却被写成 "zero in both"，很容易被读成"加拿大根本没有这些术语"。**Table 3 全部 14 行的加拿大 a 与两个 RORR 我都与原始数据核对一致（0 处不符）**，问题只在措辞，不在数字。
**【为什么重要】** 与 P1-2 同源：把"remifentanil 为零"和"术语不可检索"混为一谈。在一篇以术语精确性为主旨的论文里，这种混用尤其刺眼。
**【具体修改建议】** 把 Confirmed 列改为 "yes (remifentanil zero in both)"，并在题注补一句："'remifentanil zero in both' means the remifentanil cohort contributed no report of the term in either corpus, not that the term is unretrievable; the term is retrievable and the comparators have counts."

### P2-3 【Table 4A 的 Group 列用了 CSV 的内部标签，与 Table 2 不一致】
**【问题】** 同一个 PT 在 Table 2 标为 "probe"／"surrogate"，在 Table 4A 标为 "OIH-wide"。
**【证据】** Table 4A `DRUG INEFFECTIVE | OIH-wide | 193 | 0.950`（`I_正文_IMRaD_en.md:317`）与 `04_sensitivity_ps_only.csv` 的 `category = OIH-wide` 一致，而 Table 2 `DRUG INEFFECTIVE | probe`（`I_正文_IMRaD_en.md:280`）用的是 `10_term_dictionary.csv` 的 `Group = probe`。PAIN 同样（Table 2 "surrogate" / Table 4A "OIH-wide"）。
**【为什么重要】** 跨表分组标签不一致会让读者以为两个表的分组定义不同。
**【具体修改建议】** 统一以 `10_term_dictionary.csv` 的 Group 为准，Table 4A 相应格改为 `probe` / `surrogate`。

### P2-4 【`04_sensitivity_ps_only.csv` 不自足，缺失分母列】
**【问题】** Table 4A 的所有 OR/RORR 都需要"严重报告子集总数 11 882 968"与四药严重队列数（5 270 / 97 881 / 6 412 / 49 058），但这些分母都不在被 §9 指定为该表来源的 CSV 里。
**【证据】** `04_sensitivity_ps_only.csv` 表头仅有 `PT,category,{DRUG}_a,{DRUG}_ROR,{DRUG}_IC025,{DRUG}_signal,…`，无任何分母列；分母在 `_faers_cache.json`（我已据此把 Table 4A 全表独立重算，**0 处不一致**，见 §6）。
**【为什么重要】** 读者按 §9 打开指定文件无法复算；这不影响结论（数值我都验过是对的），只影响"可溯源"的成色。
**【具体修改建议】** 在 `04_sensitivity_ps_only.csv` 顶部增加一行元数据 `N_serious,11882968` 与各药严重队列数，或在 §9 该行同时列 `_faers_cache.json`。

### P2-5 【§2.5 的 "top 500 terms" 与 §9 未列 `03_soc_27.csv` 的覆盖率数据】
**【问题】** §2.5 称 openFDA 无 key 时每药最多返回 top 500 术语，`03_soc_27.csv` 里有对应的映射覆盖率（94.3% / 96.9% / 93.7% / 96.8%，全局 98.8%），正文未用、§9 也未指向具体行。
**【证据】** `03_soc_27.csv` 第 6–12 行。这是探索性分析唯一的"完整性"指标，正文却只字未提，读者无从判断 heuristic 映射漏了多少。
**【为什么重要】** 探索性 SOC 结果的唯一已知偏差来源没被报告，会削弱表 S1 Panel B 的说服力。
**【具体修改建议】** 在 Table S1 Panel B 的题注加一句："The heuristic mapping covered 94.3%, 96.9%, 93.7% and 96.8% of the enumerated events for remifentanil, fentanyl, sufentanil and morphine respectively, and 98.8% of the global background; unmapped terms are listed in `03_soc_27.csv`."

---

## 4. 我认为稿件站得住的地方（经核查无问题）

**4.1 §9 所覆盖的数字，逐格核对全部成立。** 我把 Table 2、Table 3、Table 4A/4B/4C、Table S1（Panel A 与 Panel B）、Table S3、Table S4、Table S5 的每个数字解析为数值后与源文件比对，**共 1 196 格**：Table 2 207 格、Table 3 44 格、Table 4A 88 格、Table 4B 86 格、Table 4C 44 格、Table S5 159 格、Table S1 Panel A 264 格、Panel B 216 格、Table S3 50 格 + 108 个百分比格、Table S4 38 格。**除 M4 的 2 个 Table S3 百分比外全部一致**，包括 170 处"破折号 = 不可估计"的语义核对（凡稿件写 "—" 处，源 CSV 对应格均为空；凡源为空处稿件都写 "—"，无一处把空单元格写成 0，也无一处把不可估计写成比值）。这说明"表格数字由脚本从结果文件读取"这一说法，在表格层面是成立的。

**4.2 核心比值可以被完全独立复现。** 我用 `_faers_cache.json` 的 N = 20 692 687 与四个队列数（5 375 / 121 819 / 6 513 / 56 501），加上 `01_faers_results.csv` 的 a 与 PT_total 反推 2×2，重算 HYPERAESTHESIA、PAIN、PROCEDURAL PAIN、DRUG WITHDRAWAL SYNDROME 四行 × 4 药的 ROR 与 CI：**最大相对误差 9.0×10⁻⁴**（PAIN/remifentanil：CSV 0.142，精确值 0.142128），全部落在三位小数显示精度内；Woolf 区间逐条与 CSV 印出的区间一致（例如 HYPERAESTHESIA/remifentanil 我算 2.54–8.80，CSV 2.54–8.80）。RORR 用"各自 c、d"口径重算亦与 CSV 三位小数完全吻合（最大相对偏差 7.5×10⁻³，对应最坏情形 0.066492 → 显示 0.066）。**核心结论所依赖的数字链条是干净、可闭合的。**

**4.3 Table 4A 完全可由原始缓存复现，且自足性问题的性质是"文件缺列"而非"数字有误"。** 我仅用 `_faers_cache.json`（`serious:1` 及各族组合键）独立重算了 Table 4A 全部 18 个 PT × 4 药的 a、ROR、RORR：**0 处不一致**。例如 HYPERAESTHESIA/remifentanil：cache 给出 a = 10、PT_total(serious) = 5248、队列 5270，2×2 = (10, 5260, 5238, 11 872 460) → ROR = 4.3091（CSV 4.309）；PAIN 严重子集 RORR vs fentanyl 我算 0.071611（CSV 0.072）。这说明敏感性分析不是手写的。

**4.4 加拿大侧的重算做到了原始 line-listing 一级，结果全部吻合。** 两个层次：(i) 从 `cv/cv_pt_summary.csv` 的计数出发（RORR = a_R·b_C/(b_R·a_C)，共享 c、d）：PAIN 0.235361 / 0.145593、DRUG INEFFECTIVE 1.277142 / 1.703140、VOMITING 1.065636 / 0.391896，与稿件 Table 3 印出的 0.235 / 0.146 / 1.277 / 1.703 及源 CSV 完全一致。(ii) **不复用作者任何中间产物，直接用字节级流式解析原始 line-listing**（`drug_product_ingredients.txt` 34 MB + `report_drug.txt` 953 MB / 5 066 837 行 + `reports.txt` 422 MB + `reactions.txt` 742 MB / 4 474 923 行），自建队列并重算：全库报告数 N = **1 154 017**、队列 **111 / 4 881 / 63 / 7 675**、原生 SOC 数 = **27**，与 `cv/cv_drug_totals.csv`、`cv/cv_soc_27.csv` 完全一致；`cv_soc_27.csv` 的 27 行 × 4 药的 108 个计数格、81 个比值格（ROR + 2 个 RORR）**逐格不一致数 = 0**；`cv_pt_summary.csv` 的 18 个 PT × 7 列 **逐格不一致数 = 0**。这说明加拿大侧的全部产物可由原始数据一步复现，不存在手改数或口径漂移。

**4.5 Table S1 Panel A 不仅自洽，而且已用原始数据端到端复现。** 对抽查的 4 个 SOC 我独立重算 RORR：Immune 1.792448 / 0.830633（稿件 1.792 / 0.831）、Gastrointestinal 0.213474 / 0.085563（0.213 / 0.086）、General disorders 0.497218 / 0.432775（0.497 / 0.433）、Psychiatric remifentanil a = 0 → 破折号 ✓。ROR 列原先只能"由 3 位小数的 ROR 反解全库该 SOC 报告数 c"来验（Immune c ≈ 41 540 → 2.3630、Gastrointestinal c ≈ 248 925 → 0.1010、General c ≈ 557 467 → 0.3610）；**现在我已从原始 `reactions.txt` 直接数出精确的 c**：Immune **41 538**、Gastrointestinal **248 694**、General disorders **557 400**、Psychiatric **117 116**，代入 (a·d)/(b·c) 分别得 2.36314 / 0.10112 / 0.36109，与表内 2.363 / 0.101 / 0.361 在三位小数下严格相等（反解值偏高 2–231，属从已舍入 ROR 反推的预期误差）。全 27 行 × 4 药与 `cv_soc_27.csv` 逐格比对**不一致 = 0**；全 108 个括号百分比独立算 n/队列**不一致 = 0**。Panel B（FAERS 事件级）与 `03_soc_27.csv` 逐格比对，108 个计数格 + 108 个百分比格 + 81 个比值格全部一致。

**4.6 图件在期刊规制方面合格，且数值与表一致。** `I_fig1_rorr_forest.png` 4 251×3 960 px、`I_fig2_year_trend.png` 4 251×2 130 px，均为 600 ppi，宽 7.085 in = 180 mm（双栏）✓；两图**均无图内标题、无绘图边框（只留必要的 bottom/left 脊线）、无网格线、图例 frameon=False**，符合 *Anaesthesia* 对线条图的要求。图 1 的 9 个术语 × 3 个对照共 27 个点值我逐个读出并与 `01_faers_results.csv` 核对一致（代码 `05_figures.py:113-125` 为逐格读 CSV，无硬编码）。图 2 的横纵数据虽为硬编码，但我逐项核对 `04_sensitivity_year_pain.csv`：2015–2024 的 fen 序列 0.093/0.039/0.051/None/None/0.044/0.014/0.016/0.112/0.168 与 mor 序列 0.097/0.038/0.032/None/None/0.037/0.019/0.022/0.052/0.066，以及池化参考线 0.066 / 0.046，**全部一致**；2018、2019 无点也与 remifentanil a = 0 一致。

**4.7 一处看起来极可疑的"同一个数出现两次"，经原始数据独立重算确认是真巧合。** Table S3 的 "Reporter: other health professional" 在芬太尼与吗啡两列都是 2 056。我**直接流式重算了加拿大原始数据**（`report_drug.txt` + `reports.txt`，不使用作者的任何中间文件），得到的分药 reporter 分布与 `cv/cv_subgroups.csv` 逐类完全一致，两药均为 2 056；同时队列数 111 / 4 881 / 63 / 7 675 与全库 1 154 017 也完全复现（脚本 `a7_cv_raw_fast.py`，输出见 §6.6）。另有三条独立证据同向：两列全部分类计数各自与队列规模精确闭合（4 881、7 675）；两列其余六个类别互不相同（如 not stated 618 vs 2 364，lawyer 84 vs 371）；生成脚本逐药独立计数。同样，"Age not stated 49/111 = 44.1%"等百分比我逐个重算，正确。

**4.8 两处我自己怀疑后确认无误的数字。** (i) §2.4 "All computations used Python 3.13.14 and matplotlib 3.11.1"——本机解释器实报 `Python 3.13.14 (main, Jun 11 2026)`、`matplotlib 3.11.1`，与 `requirements.txt` 一致 ✓。(ii) Table 2 脚注的 Bonferroni 下界 1.61：z(0.05/72) = 3.3955 代入 Woolf 区间得 1.6132 → 1.61 ✓，且 72 = 18 术语 × 4 药也数得上。

**4.9 §3.1/§3.6/§3.8 的队列与百分比经核对无误。** 队列 5 375 / 121 819 / 6 513 / 56 501 与 111 / 4 881 / 63 / 7 675 分别与 `_faers_cache.json`、`cv/cv_drug_totals.csv` 一致；全库 20 692 687 与 1 154 017 一致；102/111 = 91.9%、72/111 = 64.9%、3 894/4 881 = 79.8%、5 293/7 675 = 69.0%、1 810/7 675 = 23.6%、535/7 675 = 7.0% 全部为正确的一位小数四舍五入；5 270/5 375 = 98.0% ✓。

**4.10 §3.8 的年度统计完全自洽。** Table 4B 的 remifentanil a 列 2+1+1+0+0+2+1+1+2+3 = **13**，与题注"Of the 23 pooled PAIN reports, 13 fall in 2015–2024 and 10 outside it or have no date"以及 §3.8 的 8 个可估年份（10 − 2018、2019）完全一致；极值区间 0.014–0.168（vs fentanyl）与 0.019–0.097（vs morphine）我逐个比对 `04_sensitivity_year_pain.csv` 无误。Table 4C 的 a 列合计 = **9**，与"nine reports carry a usable receivedate"一致。

**4.11 代码实现的细节与稿件自述一致。** `cv/cv_process.py:39-41` 的活性成分匹配确为 `name == target OR name.startswith(target + " ")`，与我独立重算时采用的规则相同；我据此得到的产物命中集（remifentanil 2 个、sufentanil 2 个、fentanyl 5 个、morphine 15 个名称）与 §2.2 "Substring matching was rejected because it admits chemically distinct substances sharing a stem" 的说明方向一致。

**4.12 Table 3 的加拿大列经原始数据逐行核对，14/14 行成立。** 我用原始 line-listing 重算的每个术语的加拿大侧 a 与 Table 3 印出的完全一致（无以零冒非零的情形），PAIN 与 DRUG INEFFECTIVE 两行的 4 个 RORR 亦一致。（措辞问题见 P2-2：`zero in both` 在 14 行里指代了两种不同情形。）

---

## 5. 需要作者明确澄清的事实性问题

1. **RORR 的定义**：FAERS 侧是否刻意采用"每个药各自 c、d"（我的重算表明是），加拿大侧是否刻意采用"共享 c、d"（`cv/cv_process.py:218-226` 表明是）？若两侧口径不同，Table 3 的跨库比较是否仍然成立？请作者二选一并说明。附带请确认：Table S5 脚注的"可由计数重算"是否应删除？
2. **加拿大 VOMITING**：a = 3 满足稿件自己的 a ≥ 3 阈值，为什么没有进入 Table 2/3/图 1？是脚本输出的哪一步把它过滤掉了，还是有别的判定规则？请在回复中给出确切数字与来源（`cv/cv_pt_summary.csv` 第 12 行）。
3. **11 882 968 与 5 270 的出处**：这两个数在 `_faers_cache.json` 与 `04_sensitivity_run.log` 中，为什么 §9 把它们归给了不含这两个数的 `04_sensitivity_ps_only.csv`？
4. **15.4 / 4.3 / 4.9 / 1.7 的出处**：`04_sensitivity_2024cluster_hyperaesthesia.csv` 为什么没有出现在 §9？
5. **主文字数**：`_wordcount.py` 的计数规则是什么（是否含节标题？多词数字如何计？连字符如何计？引用编号是否计入）？请给出与 4 000 相符的规则与实测值。
6. **Table 4C 题注**："so the table holds nine rows" 是否本意是 "the remifentanil column sums to nine"？
7. **"under 0.001% of the variance"** 的计算依据是什么（模型、公式、代入值）？我按多项分布逐项展开得 |2Cov|/Var ≈ 0.25%，请作者给出自己的算式以便对齐。
8. **§2.3 的 "produced no estimable result"** 是否应改为 "did not meet the signal criterion"？
9. **Table S3 的两个百分比**是否确为双重舍入？请确认其余百分比都是从计数直接算的。
10. **§5 与 §4.5 对加拿大阴性对照的表述**在修正后是否仍需保留 "untested rather than confirmed" 这一结论（因为 VOMITING 实际已被检验）？
11. **Table 3 "Confirmed" 列的 "zero in both"**：我从原始数据数出这些术语在加拿大全库的报告数为 HYPERALGESIA 0、ALLODYNIA 29、PAIN INCREASED 0、POSTOPERATIVE PAIN 0、CHRONIC PAIN 0、OPIOID WITHDRAWAL SYNDROME 0、DRUG TOLERANCE 386、HYPERAESTHESIA 521、HYPERPATHIA 0、PROCEDURAL PAIN 1 510、CHRONIC PAIN SYNDROME 0、DRUG WITHDRAWAL SYNDROME 1 664。请确认该列想表达的是"瑞芬太尼暴露侧为零"，而不是"术语在该库不可检索"——若是前者，请按 P2-2 改写措辞；因为同一短语在 14 行里同时覆盖了"全库为 0"与"全库上千份而暴露侧为 0"两种截然不同的情形。
12. **Table 3 的加拿大 RORR 与 FAERS RORR 口径不同**（前者共享 c、d，后者各自 c、d，见 M2）。跨库表把两者并列呈现时，是否应在题注中注明这一点？若决定统一为"各自 c、d"，请注意**不是数字不变的改动**：我按两种口径都算过，PAIN vs morphine 会由 0.146 变为 **0.144**、DRUG INEFFECTIVE vs morphine 由 1.703 变为 **1.706**（另两个比值不变）；共同因子 (d_R·c_C)/(d_C·c_R) 在 PAIN vs morphine 上为 0.9882（−1.18%）。详见 M2 与 §6.11。

---

## 6. 我实际做的独立核查（命令 / 脚本 / 关键输出）

所有脚本写入 `_review_r5/_a7_scratch/`，全部用 `C:\Users\Administrator\.workbuddy\binaries\python\versions\3.13.12\python.exe`（实报 Python 3.13.14）执行。**未读取** `_check_consistency.py`、`REVIEW_*`、`RESPONSE_*`、`REVISION_*`、`01_任务状态.md` 等文件。

### 6.1 由源数据反推 2×2 并独立重算 ROR / RORR（任务 1）

```
$ python _review_r5/_a7_scratch/a7_task1_rerun_ror2.py
N=20692687  COH={'REMIFENTANIL': 5375, 'FENTANYL': 121819, 'SUFENTANIL': 6513, 'MORPHINE': 56501}
===== A. ROR 重算（与 CSV 比对） =====
HYPERAESTHESIA  REMIFENTANIL a=10   csv=4.729   mine=4.728815  rel=3.9e-05  CI mine=2.54-8.80  csv=2.54-8.80
HYPERAESTHESIA  FENTANYL     a=315  csv=6.795   mine=6.794517  rel=7.1e-05  CI mine=6.07-7.61  csv=6.07-7.61
HYPERAESTHESIA  SUFENTANIL   a=22   csv=8.611   mine=8.610915  rel=9.9e-06  CI mine=5.66-13.09 csv=5.66-13.09
HYPERAESTHESIA  MORPHINE     a=262  csv=12.166  mine=12.166194 rel=1.6e-05  CI mine=10.75-13.76 csv=10.75-13.76
PAIN            REMIFENTANIL a=23   csv=0.142   mine=0.142128  rel=9.0e-04
PAIN            FENTANYL     a=7349 csv=2.138   mine=2.137525  rel=2.2e-04
PAIN            SUFENTANIL   a=98   csv=0.505   mine=0.505276  rel=5.5e-04
PAIN            MORPHINE     a=4794 csv=3.083   mine=3.083473  rel=1.5e-04
PROCEDURAL PAIN REMIFENTANIL a=14   csv=1.977   mine=1.977303  rel=1.5e-04
PROCEDURAL PAIN FENTANYL     a=162  csv=1.008   mine=1.008044  rel=4.3e-05
PROCEDURAL PAIN SUFENTANIL   a=8    csv=0.931   mine=0.930924  rel=8.2e-05
PROCEDURAL PAIN MORPHINE     a=167  csv=2.252   mine=2.251677  rel=1.4e-04
DRUG WITHDRAWAL SYNDROME REMIFENTANIL a=7   csv=0.307 mine=0.306882 rel=3.8e-04
DRUG WITHDRAWAL SYNDROME FENTANYL     a=3274 csv=6.714 mine=6.714409 rel=6.1e-05
DRUG WITHDRAWAL SYNDROME SUFENTANIL   a=42   csv=1.528 mine=1.527967 rel=2.1e-05
DRUG WITHDRAWAL SYNDROME MORPHINE     a=865  csv=3.686 mine=3.686064 rel=1.7e-05

===== B. RORR 重算 =====
PT                        vs           CSV(稿件)  A:各自cd   relA     B:仅计数   relB     A/B
HYPERAESTHESIA            FENTANYL     0.696   0.695975  3.58e-05  0.718969  3.30e-02  0.9680
HYPERAESTHESIA            SUFENTANIL   0.549   0.549165  3.01e-04  0.549945  1.72e-03  0.9986
HYPERAESTHESIA            MORPHINE     0.389   0.388685  8.10e-04  0.400098  2.85e-02  0.9715
PAIN                      FENTANYL     0.066   0.066492  7.45e-03  0.066938  1.42e-02  0.9933
PAIN                      SUFENTANIL   0.281   0.281288  1.03e-03  0.281308  1.10e-03  0.9999
PAIN                      MORPHINE     0.046   0.046094  2.03e-03  0.046351  7.64e-03  0.9944
PROCEDURAL PAIN           FENTANYL     1.962   1.961525  2.42e-04  1.961121  4.48e-04  1.0002
PROCEDURAL PAIN           SUFENTANIL   2.124   2.124022  1.05e-05  2.123438  2.65e-04  1.0003
PROCEDURAL PAIN           MORPHINE     0.878   0.878147  1.67e-04  0.880920  3.33e-03  0.9969
DRUG WITHDRAWAL SYNDROME  FENTANYL     0.046   0.045705  6.41e-03  0.047216  2.64e-02  0.9680
DRUG WITHDRAWAL SYNDROME  SUFENTANIL   0.201   0.200843  7.80e-04  0.200913  4.34e-04  0.9997
DRUG WITHDRAWAL SYNDROME  MORPHINE     0.083   0.083255  3.07e-03  0.083874  1.05e-02  0.9926

最大 ROR 相对误差（A 口径）= 9.04e-04 ；最大 RORR 相对误差（A 口径）= 7.45e-03 ；
最大 RORR 相对误差（B 口径）= 3.30e-02
```
结论：ROR 与稿件三位小数完全吻合（残差即显示舍入）；RORR 只与"A 口径（各自 c、d）"吻合，B 口径（稿件 §2.4 文字与 Table S5 脚注所承诺的"由计数重算"）最大偏离 3.30%。

### 6.2 全部表格逐格解析比对（任务 2）

脚本 `a7_task2_table_check.py`、`a7_task2b_s1.py`、`a7_task2c_s1b.py`、`a7_task_s3_pct.py`。
```
$ python _review_r5/_a7_scratch/a7_task2_table_check.py
输出行数 = 1329
---------- 所有 ✗ / 异常 ----------
S3/Reporter: lawyer/REMIFENTANIL 源缺 ✗          （= 稿件写 0，源 CSV 无该行；语义一致，非错误）
S3/Reporter: lawyer/SUFENTANIL  源缺 ✗          （同上）
S3/Age 18–64 years/MORPHINE Pct 稿件=54.4 我独立算=54.3453→54.3 ✗ | 源Pct=54.35
S3/Female/FENTANYL          Pct 稿件=43.2 我独立算=43.1469→43.1 ✗ | 源Pct=43.15
问题行合计 = 4

按表统计（一致/比对）：
Table 2          207/207   Table 3          44/44    Table S5  159/159
Table 4A          88/88    Table 4B         86/86    Table 4C   44/44
Table S3          50/50    Table S4         38/38    Table S1 Panel A 264/264
合计比对 980 格，一致 980，不一致 0 ；含"破折号 = 不可估计"核对面 170 处

$ python _review_r5/_a7_scratch/a7_task2b_s1.py
Table S1 Panel A 百分比格数 = 108，不自洽 = 0

$ python _review_r5/_a7_scratch/a7_task2c_s1b.py
Panel B 数据行数 = 27 ；数字格数 = 108，问题 = 0

$ python _review_r5/_a7_scratch/a7_task_s3_pct.py
Table S3 百分比错误条目：
   Female / FENTANYL : 稿件 43.2 ，n=2106 / 队列 → 43.1469% → 正确值 43.1
（另一条 Age 18–64 / MORPHINE：4171/7675 = 54.3453% → 正确 54.3，稿件 54.4）
```
**破折号语义专项**（Table 2 逐格）：稿件写 "—" 处源 CSV 的 ROR 列均为空（不可估计）；源为空处稿件均写 "—"；无一处把空单元格写成 0，也无一处把全库为 0 的术语写成比值。五个 a priori 零术语的 `PT_total` 均确为 0（HYPERALGESIA 0、PAIN INCREASED 0、POSTOPERATIVE PAIN 0、CHRONIC PAIN 0、OPIOID WITHDRAWAL SYNDROME 0），与"全库零，而非队列零"的语义一致。

### 6.3 加拿大侧重算（任务 3）
```
$ python _review_r5/_a7_scratch/a7_task34_canada.py
PAIN                vs FENTANYL  稿件=0.235 源CSV=0.235 我重算=0.235361 ✓  a_remi=2  a_FEN=353
PAIN                vs MORPHINE  稿件=0.146 源CSV=0.146 我重算=0.145593 ✓  a_remi=2  a_MOR=859
DRUG INEFFECTIVE    vs FENTANYL  稿件=1.277 源CSV=1.277 我重算=1.277142 ✓  a_remi=25 a_FEN=905
DRUG INEFFECTIVE    vs MORPHINE  稿件=1.703 源CSV=1.703 我重算=1.703140 ✓  a_remi=25 a_MOR=1119
VOMITING            vs FENTANYL  稿件未报告 源CSV=1.066 我重算=1.065636 ✓  a_remi=3  a_FEN=124
VOMITING            vs MORPHINE  稿件未报告 源CSV=0.392 我重算=0.391896 ✓  a_remi=3  a_MOR=508
→ 4 个阴性对照（NAUSEA/VOMITING/PRURITUS/CONSTIPATION）中，加拿大侧 REMI a>0 的只有 VOMITING(3)
```
另核 5.921 / 10.604（医师-only）：`cv/cv_pt_summary.csv` 第 6 行 `REMI_RORR_FEN_phys=5.921`、`REMI_RORR_MOR_phys=10.604`，与 §3.4 一致 ✓。

### 6.4 Table S1 Panel A 抽查（任务 4）
```
Immune system disorders       REMI 9 / FEN 229 / MOR 737 | 表 ROR 2.363 RORRfen 1.792 RORRmor 0.831
  我重算 RORRfen = 1.792448 ✓  RORRmor = 0.830633 ✓
  【第一轮】由 ROR 反解全库该 SOC 报告数 c ≈ 41540；回算 ROR = 2.3630 ✓ 自洽
  【第二轮】直接从 reactions.txt 数出精确 c = 41538 → ROR = 2.36314 ✓（与反解值仅差 2）
Gastrointestinal disorders    REMI 3 / FEN 562 / MOR 1881 | 表 0.101 / 0.213 / 0.086
  我重算 0.213474 ✓ / 0.085563 ✓ ；反解 c ≈ 248925，精确 c = 248694 → ROR 0.10112 ✓
Psychiatric disorders         REMI 0 → ROR/RORR 均破折号 ✓ （精确 c = 117116）
General disorders …           REMI 28 / FEN 1973 / MOR 3362 | 表 0.361 / 0.497 / 0.433
  我重算 0.497218 ✓ / 0.432775 ✓ ；反解 c ≈ 557467，精确 c = 557400 → ROR 0.36109 ✓
Panel A 全 27 行 RORR 不自洽 = 0 ；108 个百分比格不自洽 = 0
第二轮端到端：cv_soc_27.csv 逐格不一致 = 0 ；cv_pt_summary.csv 逐格不一致 = 0（见 §6.6 第二阶段）
```

### 6.4b Table 3 加拿大列逐行核对（第二轮原始数据扫描的副产品）
Table 3 全 14 行的"Canada remifentanil a"与"Canada RORR"我都用原始 line-listing 重算过。**14/14 行的 a 完全一致，两行有比值的（PAIN、DRUG INEFFECTIVE）四位/三位小数亦一致**。同时我把每一行术语的**全库报告数 c** 也数了出来（这是判断破折号语义的关键，此前无任何文件提供）：
```
PT                          Canada a(稿件/我)  全库 c    判定
HYPERALGESIA                   0 / 0            0      破折号 = 不可估（暴露侧 0；且该串在加拿大全库也不出现）
ALLODYNIA                      0 / 0           29      破折号 = 不可估；但术语在加拿大有 29 份报告
PAIN                           2 / 2       48 267      RORR 0.235 / 0.146 ✓ 可估
PAIN INCREASED                 0 / 0            0      破折号 = 不可估
POSTOPERATIVE PAIN             0 / 0            0      破折号 = 不可估
CHRONIC PAIN                   0 / 0            0      破折号 = 不可估
OPIOID WITHDRAWAL SYNDROME     0 / 0            0      破折号 = 不可估
DRUG TOLERANCE                 0 / 0          386      破折号 = 不可估；但术语在加拿大有 386 份报告
HYPERAESTHESIA                 0 / 0          521      破折号 = 不可估；但术语在加拿大有 521 份报告
HYPERPATHIA                    0 / 0            0      破折号 = 不可估；该串在加拿大全库确实不出现
PROCEDURAL PAIN                0 / 0        1 510      破折号 = 不可估；但术语在加拿大有 1 510 份报告
CHRONIC PAIN SYNDROME          0 / 0            0      破折号 = 不可估
DRUG WITHDRAWAL SYNDROME       0 / 0        1 664      破折号 = 不可估；但术语在加拿大有 1 664 份报告
DRUG INEFFECTIVE              25 / 25     205 227      RORR 1.277 / 1.703 ✓ 可估
```
**结论**：Table 3 的加拿大数字**全部可核查、无一处不符**；但 "yes (zero in both)" 这一措辞在 14 行里同时指代了两种情形（术语在全库为 0，与术语在全库有上千份报告而暴露侧为 0），见 P2-2。

### 6.5 Table 4A 完全由原始缓存复现
```
$ python _review_r5/_a7_scratch/a7_task4a_from_cache.py
N_serious = 11882968 ; 队列(严重) = {'REMIFENTANIL': 5270, 'FENTANYL': 97881, 'SUFENTANIL': 6412, 'MORPHINE': 49058}
HYPERAESTHESIA REMIFENTANIL a=10 PT_tot=5248 csv=4.309 mine=4.3091  RORR vs FEN csv=0.606 mine=0.605883
PAIN           REMIFENTANIL a=22 PT_tot=382655 csv=0.126 mine=0.1259 RORR vs FEN csv=0.072 mine=0.071611
DRUG WITHDRAWAL SYNDROME REMIFENTANIL a=7 PT_tot=69430 csv=0.226 mine=0.2262 RORR vs FEN csv=0.044 mine=0.044255
…
Table 4A 由 _faers_cache.json 独立重算：不一致条目 = 0
```
同时确认：`04_sensitivity_ps_only.csv`（§9 指定为该表来源）**不含** 11 882 968 与各药严重队列数（表头无分母列）——这正是 P1-4 / P2-4 的证据。

### 6.6 加拿大原始数据独立重算（任务 5：reporter 2 056 与队列数）
脚本 `_review_r5/_a7_scratch/a7_cv_raw_fast.py`，**直接流式读取** `cv/cvponline_extract_20241130/` 的 `drug_product_ingredients.txt`(34 MB) + `report_drug.txt`(953 MB) + `reports.txt`(422 MB)，**不复用** `cv_process.py` 的任何输出，也不读任何中间 CSV：
```
$ python _review_r5/_a7_scratch/a7_cv_raw_fast.py cv/cvponline_extract_20241130
[   9.1s] 活性成分命中 REMIFENTANIL = ['remifentanil', 'remifentanil hydrochloride'] (product 数 7)
[   9.1s] 活性成分命中 FENTANYL     = ['fentanyl','fentanyl citrate','fentanyl dihydrogencitrate',
                                       'fentanyl hydrochloride','fentanyl iv'] (product 数 117)
[   9.1s] 活性成分命中 SUFENTANIL   = ['sufentanil', 'sufentanil citrate'] (product 数 7)
[   9.1s] 活性成分命中 MORPHINE     = ['morphine','morphine (sulfate de)','morphine chlorhydrate',
                                       'morphine hcl','morphine hydrochloride',…,'morphine sulphate'] (product 数 126)
[   9.1s] prod2t 条目数 = 257
[ 209.0s] report_drug 总行数 = 5066837 ; 队列（独立重算）=
          {'REMIFENTANIL': 111, 'FENTANYL': 4881, 'SUFENTANIL': 63, 'MORPHINE': 7675}
[ 289.9s] reports.txt 总报告数 = 1154017
[ 290.3s] reporter 分布 REMIFENTANIL n=111 : {'Other health professional': 72, 'Physician': 19, '': 11,
                                             'Consumer/other non health professional': 6, 'Pharmacist': 3}
[ 290.3s] reporter 分布 FENTANYL     n=4881 : {'Other health professional': 2056,
                                             'Consumer/other non health professional': 974, '': 618,
                                             'Physician': 589, 'Pharmacist': 555, 'Lawyer': 84, 'Nurse': 5}
[ 290.3s] reporter 分布 SUFENTANIL   n=63  : {'Other health professional': 39, 'Physician': 9, '': 8,
                                             'Pharmacist': 6, 'Consumer/other non health professional': 1}
[ 290.3s] reporter 分布 MORPHINE     n=7675: {'': 2364, 'Other health professional': 2056,
                                             'Consumer/other non health professional': 1810,
                                             'Pharmacist': 537, 'Physician': 535, 'Lawyer': 371, 'Nurse': 2}
```
**结论（逐项对稿件）**：
- 全库报告数 **1 154 017** ✓（§3.1、Table 1）。
- 队列 **111 / 4 881 / 63 / 7 675** ✓（§3.1、Table 1；= `cv/cv_drug_totals.csv`）。
- reporter 分布与 `cv/cv_subgroups.csv` **逐类完全一致**，包括 "Other health professional" 在芬太尼与吗啡**都是 2 056**。
- → **2 056 是真实数据巧合，不是生成脚本的复制错误**（判定：经查无误）。除原始数据重算外，另有三条独立证据同向：(i) 两列全部分类计数各自与队列规模精确闭合（芬太尼 2 056+974+618+589+555+84+5 = 4 881；吗啡 2 056+1 810+2 364+537+535+371+2 = 7 675）；(ii) 两列其余六个类别互不相同；(iii) `cv/cv_process.py:131` 的 `demo[t]["reporter_"+reporter] += 1` 为逐药独立计数，无跨药复用路径。

**同一独立管线的第二阶段：加扫 `reactions.txt`，把 27 SOC 表与 PT 表也从原始数据算出来。** 脚本 `_review_r5/_a7_scratch/a7_cv_soc_full.py`；其 Pass 1+2（活性成分 → 药品 → Suspect 报告集合）与上一步等价，结果落盘为 `_a7_cv_target_reports.pkl` 供复用。下面是**复用该落盘状态后的本次运行日志原文**（`_a7_scratch/out_cv_soc_full2.txt`，行首为距进程启动的秒数）。原始文件的字段数我逐个实测：`reports.txt` = 42 列、`reactions.txt` = 10 列、`report_drug.txt` = 22 列；`reactions.txt` 的布局为 `[1]REPORT_ID [5]PT_NAME_ENG [7]SOC_NAME_ENG [9]MEDDRA_VERSION`，与 `cv_process.py` 注释所写的列号一致（该注释中"42 列 / col39 实为厂商号"一句说的是 `reports.txt`，也经我核对无误）：
```
$ python _a7_scratch/a7_cv_soc_full.py cv/cvponline_extract_20241130 _a7_scratch/out_cv_soc_full2.txt
[   0.0s] 复用已落盘 Pass1+Pass2 结果：…\_a7_cv_target_reports.pkl
[   0.1s] == Pass3: reports.txt 总报告数 N ==
[  63.1s]    N = 1154017
[  63.1s] == Pass4: reactions.txt -> 全局 SOC / 各药 SOC / PT ==
[ 258.6s]    reactions 行 3000000
[ 289.7s]    reactions.txt 总行数=4474923 ; 全局 SOC 数=27
[ 289.7s] == 队列规模（与 cv_drug_totals.csv 比对） ==
[ 289.7s]    REMIFENTANIL = 111
[ 289.7s]    FENTANYL     = 4881
[ 289.7s]    SUFENTANIL   = 63
[ 289.7s]    MORPHINE     = 7675
[ 289.7s]    分母 N = 1154017
[ 289.7s] == 27 原生 SOC 独立重算（SOC, a_remi, c, ROR_remi, RORR_vs_FEN, RORR_vs_MOR） ==
[ 289.7s]    Skin and subcutaneous tissue disorders     a=  3 c=187766 ROR=0.143 RORR_F=0.197 RORR_M=0.062 分药=3/604/16/2362
[ 289.7s]    Psychiatric disorders                      a=  0 c=117116 ROR=-     RORR_F=-     RORR_M=-     分药=0/1787/2/2684
[ 289.7s]    Nervous system disorders                   a= 21 c=213879 ROR=1.026 RORR_F=0.844 RORR_M=0.659 分药=21/1057/16/2008
[ 289.7s]    Gastrointestinal disorders                 a=  3 c=248694 ROR=0.101 RORR_F=0.213 RORR_M=0.086 分药=3/562/12/1881
[ 289.7s]    General disorders and administration …     a= 28 c=557400 ROR=0.361 RORR_F=0.497 RORR_M=0.433 分药=28/1973/26/3362
                                    （全 27 个原生 SOC 逐行输出，此处仅节选 5 行）
[ 289.8s]    VOMITING                   c= 38452 分药=3/124/1/508    ROR=0.806 RORR_F=1.066 RORR_M=0.392
[ 289.8s]    PAIN                       c= 48267 分药=2/353/8/859    ROR=0.420 RORR_F=0.235 RORR_M=0.146
[ 289.8s]    DRUG INEFFECTIVE           c=205227 分药=25/905/9/1119  ROR=1.344 RORR_F=1.277 RORR_M=1.703
[ 289.8s]    NAUSEA                     c= 63311 分药=0/260/2/824    ROR=-     RORR_F=-     RORR_M=-
[ 289.8s]    PRURITUS                   c= 45744 分药=0/141/1/1187   ROR=-     RORR_F=-     RORR_M=-
[ 289.8s]    CONSTIPATION               c= 13366 分药=0/58/3/397    ROR=-     RORR_F=-     RORR_M=-
[ 289.8s]    ALLODYNIA                  c=    29 分药=0/3/0/0      ROR=-     RORR_F=-     RORR_M=-
[ 289.8s]    DRUG TOLERANCE             c=   386 分药=0/25/0/30    ROR=-     RORR_F=-     RORR_M=-
[ 289.8s]    HYPERAESTHESIA             c=   521 分药=0/18/0/30    ROR=-     RORR_F=-     RORR_M=-
[ 289.8s]    PROCEDURAL PAIN            c=  1510 分药=0/14/0/42    ROR=-     RORR_F=-     RORR_M=-
[ 289.8s]    DRUG WITHDRAWAL SYNDROME   c=  1664 分药=0/139/1/195  ROR=-     RORR_F=-     RORR_M=-
[ 289.9s] == 与 cv/cv_soc_27.csv 逐格比对 ==
[ 289.9s]    CSV 行数=27 ；我重算 SOC 数=27
[ 289.9s]    >> SOC 表不一致格数 = 0
[ 289.9s] == 抽样核对：4 个抽查 SOC 的全局报告数 c（我独立重算） ==
[ 289.9s]    Immune system disorders                    c=41538  ROR=2.363  RORR_F=1.792  RORR_M=0.831
[ 289.9s]    Gastrointestinal disorders                 c=248694 ROR=0.101  RORR_F=0.213  RORR_M=0.086
[ 289.9s]    Psychiatric disorders                      c=117116 ROR=-      RORR_F=-      RORR_M=-
[ 289.9s]    General disorders and administration …     c=557400 ROR=0.361  RORR_F=0.497  RORR_M=0.433
[ 289.9s] == 与 cv/cv_pt_summary.csv 逐格比对 ==
[ 290.0s]    （18 个 PT 逐行输出，每行末若有不一致项会追加 "<<< 列名 CSV=… 我=…"；此处全部为空）
[ 290.0s]    >> PT 表不一致格数 = 0
[ 290.0s] == VERIFY DONE ==
```
几点必须说明，以免读者误读这份日志：
- 我的脚本第一版把 PT 字段当 bytes 大写、却用 str 键去查，导致 PT 段全部返回 c = 0。**该 bug 只影响我的脚本，与作者代码无关**；修正后重跑即为上面这份日志（SOC 段两版结果完全相同，可交叉验证）。
- 日志里 27 SOC 的顺序与 `cv_soc_27.csv` 完全相同（都按首次出现顺序），因此"逐格比对 = 0"是对齐后的结论，不是排序错位造成的假阳性。
- Pass 1+2 的独立结果（队列 111/4 881/63/7 675、全库 1 154 017）与 §6.6 上半段那次完整重跑一致。
**本阶段的三点结论**：(i) 加拿大侧 27 SOC 表与 PT 表**可 100% 由原始 line-listing 复现，不一致格数 = 0**——`cv_process.py` 的实现与其产物一致，无手改数；(ii) 它同时给出 Table S1 Panel A 的**精确 c**（此前只能由已舍入的 ROR 反解），使 Panel A 的 ROR 列从"自洽"升级为"已用原始数据验证"；(iii) 它独立确证了 **VOMITING 的四药计数为 3/124/1/508、全库 c = 38 452**，即 M1 所指的数据点在原始数据里确实存在且可算。

### 6.7 正文数字可追溯性扫描（任务 6）
脚本 `a7_task6_prose.py` 抽取 Summary/§1–§5/表题注/图注中全部数字（去重后 542 个 token），再逐个在全部源结果文件（138 个，排除前轮评审材料）中检索：
```
11 882 968  -> .\_gen_table4.py（另见 _faers_cache.json 的 serious:1 与 04_sensitivity_run.log）
5 270       -> .\_gen_table4.py（另见缓存 REMIFENTANIL…AND serious:1 = 5270；04_sensitivity_run.log）
532 / 367   -> _faers_cache.json、D_27SOC_openFDA事件级.md（§9 已列该 md）✓
21.1 / 0.077 / 0.038 -> 02_route_stratified.csv、02_route_summary.md（§9 已列）✓
15.41       -> 04_sensitivity_2024cluster_hyperaesthesia.csv（§9 未列任何一行）
4.30 / 1.71 -> 04_sensitivity_2024cluster_hyperaesthesia.csv（同上）
```
**在 §9 中找不到对应源文件映射的正文数字（逐条列出）**：
1. `11 882 968`（§3.8、Table 4A 脚注）——实际源 `_faers_cache.json`「serious:1」；§9 却把该行数字归给不含此值的 `04_sensitivity_ps_only.csv`。
2. `5 270`（§3.8、§4.3）——同上。
3. `0.98`（98.0%，§3.8/§4.3）——由上两者派生。
4. `15.4 / 4.3 / 4.9 / 1.7`（§3.8）——源 `04_sensitivity_2024cluster_hyperaesthesia.csv`，§9 **无此行**。
5. `300 / 4 000`（首页 Word count）——源 `_wordcount.py`，§9 无此行；且实测为 299 / 3 789–3 951（见 P1-5）。
6. `5 375 / 121 819 / 6 513 / 56 501`（§3.1、Table 1）——§9 首行归给 `01_faers_results.csv`，但该 CSV **不含队列数**；实际源为 `_faers_cache.json`。
7. `1.61`（Table 2 脚注）——非文件存储值，为派生量（我复算得 1.6132）。
8. `0.001%`（§2.4）——任何源文件中都不存在，且经重算应为 ~0.1%（见 P1-1）。
9. `8`（"the eight estimable years"）——源 `04_sensitivity_estimable_years.json`，§9 无此行。
10. `18 / 72 / 432`（术语数、比较数、Table S1 单元格数）——结构性派生量（18 = 术语数；72 = 18×4；432 = 27 SOC×4 药×2 面板×2 列），我均验算成立，但无源文件行。

### 6.8 图件与图注（任务 7）
- 分辨率/尺寸：`fig1` 4 251×3 960 px、`fig2` 4 251×2 130 px，均 600.00 ppi，宽 180 mm ✓。
- 期刊禁令项：两图**无图内标题、无绘图边框（`clean_axes` 只留 bottom/left）、无网格（`ax.grid(False)`）、图例 `frameon=False` 无框** ✓。虚线/点线参考线（RORR = 1、池化值）在图注中均有说明，属允许内容 ✓。
- 数值：Fig 1 的 27 个点值逐格比对 `01_faers_results.csv` 一致（且代码为逐格读取）；Fig 2 的硬编码数组逐项比对 `04_sensitivity_year_pain.csv` 一致。
- **发现**：Fig 1 的纵向顺序与图注 "from the top" 相反（图自下而上为 HYPERAESTHESIA → … → DRUG INEFFECTIVE），见 M5。

### 6.9 §2.4 "协方差 < 0.001%" 的重算
```
独立（稿件）假设：Var(log RORR) = 1/10+1/5365+1/8151/…+1/315+1/121504+1/7846+… = 0.1003091+0.0033103 = 0.1036194
   → SE = 0.32190，与 01_faers_results.csv 印出的 0.37–1.31 完全一致（说明 CI 确按此式）
共享成分量级：Cov(log ROR_remi, log ROR_fent) ≈ −1/7836 ≈ −1.28e-4
   （按多项分布 Cov(log n_A, log n_B) ≈ (δ_AB/μ_B − 1)/N 逐项展开，非对角项相消后仅剩该量级；
     若按 §2.4 文字所述"共享同一 c、d"，则需计入 Var(log c − log d) ≈ 1/8151 ≈ 1.23e-4）
|2Cov| / Var = 2.55e-4 / 0.1036 ≈ 0.25%      （共享 c 口径下 ≈ 0.12%）
声明值 0.001% × Var = 1.04e-6               → 声明偏小约 120–250 倍
符号：Cov < 0 ⇒ 忽略它使区间偏宽 ⇒ "so it is conservative" 成立，仅量级不成立
```

### 6.10 其它一次性核对
- `python -c "import sys,matplotlib"` → `Python 3.13.14 (main, Jun 11 2026)`、`matplotlib 3.11.1`，与 §2.4 与 `requirements.txt` 一致 ✓。
- §9 表结构检查：17 行中第 539 行只有 2 个竖线（少一个 `|`），其余 16 行均正常。
- 字数独立统计（含/不含节标题、数字是否并作一词共 4 种口径）：Summary 294–299；正文 3 789–3 951。
- Table S3 全 108 个计数格与 `cv/cv_subgroups.csv` 一一对应，无一错位；两列 reporter 分类计数各自与队列闭合。

### 6.11 加拿大侧两种 RORR 口径的差异（M2 的量化补充）
我一度以为"把加拿大侧改成各自 c、d"只是口径统一、数字不变。**实测否定**：因为加拿大队列很小（remifentanil 仅 111），`b_R = n_R − a_R` 是小量，而 `c` 是全库级大数，"共享 c、d"与"各自 c、d"不再近似相等。
```
$ python -c "…"        # 口径：shared = (a_R(b_C))/(b_R a_C) ；own = 各自的 (a·d)/(b·c) 相除
PT                 comparator      shared(作者/稿件)  own c,d        比值
PAIN               FENTANYL              0.235361    0.234587   0.996712  → 0.235（不变）
PAIN               MORPHINE              0.145593    0.143880   0.988234  → 0.146 变 0.144
DRUG INEFFECTIVE   FENTANYL              1.277142    1.276901   0.999811  → 1.277（不变）
DRUG INEFFECTIVE   MORPHINE              1.703140    1.705693   1.001499  → 1.703 变 1.706
共同因子 = (d_R·c_C)/(d_C·c_R)；最大偏离 −1.18%（PAIN vs morphine）
```
**含义**：加拿大侧的口径分歧（最大 1.18%）虽小于 FAERS 侧（最大 3.30%），但已足以跨过第三位小数。因此 M2 提出的"统一口径"不是纯文字修订——一旦统一就必须同步更新 Table 3 的两格，否则会制造新的表内不一致。

---

### 数字问题总清单

**A. 必须修正**
| # | 位置 | 问题 | 正确值 |
|---|---|---|---|
| 1 | §5 末段 | "the four negative controls … could not be tested in Canada" 与源数据矛盾 | VOMITING 可算：REMIFENTANIL a = 3，RORR vs fentanyl = **1.066**、vs morphine = **0.392**（`cv/cv_pt_summary.csv` 第 12 行）；其余三个阴性对照 a = 0 才不可算 |
| 2 | Table 4C 题注 | "so the table holds nine rows" | 表共 **10** 行（2015–2024）；应为"remifentanil 列合计 9"（2021 年 1 + 2024 年 8） |
| 3 | Table S3 "Age 18–64 years" / Morphine | 写 54.4 | **54.3**（4 171 / 7 675 = 54.3453%） |
| 4 | Table S3 "Female" / Fentanyl | 写 43.2 | **43.1**（2 106 / 4 881 = 43.1469%） |
| 5 | §2.4 第 3 段 | "Both ratios share the same background reference, so comparator-specific terms cancel" 与 FAERS 实现不符；Table S5 脚注"可由计数重算"因此不成立 | FAERS RORR 用各自 c、d；按计数直推 HYPERAESTHESIA vs fentanyl = **0.719**（稿件 0.696，差 3.3%）。需改述或统一两库口径 |
| 6 | Figure 1 图注 | "Terms are grouped from the top" | 图实际自下而上：HYPERAESTHESIA 在图**底**，DRUG INEFFECTIVE 在图**顶** |
| 7 | §9 溯源表第 539 行 | 缺一个 `|`，Markdown 表格断裂 | 行末补 ` |` |

**B. 应说明**
| # | 位置 | 问题 | 建议值/做法 |
|---|---|---|---|
| 8 | §2.4 | "the ignored covariance is under 0.001% of the variance" | 实为 ≈ **0.12%–0.25%**（差约 100 倍）；符号方向（保守）无误 |
| 9 | §2.3 | "the two a priori hyperalgesia outcomes … produced no estimable result" | ALLODYNIA 可估（Table 2 印出 3.47，0.49–24.67）；应改为"未达信号阈值" |
| 10 | §3.4 首句 | "The same pattern held for every negative control" 被同句后半段否定 | 11/12 < 1、PRURITUS vs sufentanil = 1.310 > 1；改为"对芬太尼与吗啡全部、对舒芬仅 3/4" |
| 11 | §9 | 未映射 `04_sensitivity_2024cluster_hyperaesthesia.csv`（15.4/4.3/4.9/1.7）、`04_sensitivity_estimable_years.json`（8）、`_wordcount.py`（300/4 000）；11 882 968 与 5 270 误指到不含它们的 `04_sensitivity_ps_only.csv`；队列数误指到 `01_faers_results.csv` | 按 M1/P1-4 的补表建议增补 |
| 12 | 首页 Word count | "main text 4 000 words" | 实测 **3 789–3 951**（Summary 294–299）；需给实测值与计数规则 |
| 13 | 首页 Tables | "Tables: 4" | 实际 6 个表对象（1、2、3、4A、4B、4C） |
| 14 | Table 3 Confirmed 列 | "zero in both" 含义分裂：DRUG TOLERANCE 在加拿大有 **386** 份报告、HYPERPATHIA 为 **0**；另有 ALLODYNIA 29、HYPERAESTHESIA 521、PROCEDURAL PAIN 1 510、DRUG WITHDRAWAL SYNDROME 1 664 份。易被读成"术语不可检索" | 改为 "remifentanil zero in both"，并说明这是暴露侧为零、术语本身可检索 |
| 15 | Table 4A Group 列 | 与 Table 2 标签不一致（probe/surrogate vs OIH-wide） | 统一用 `10_term_dictionary.csv` 的 Group |
| 16 | Table S1 Panel B 题注 | 未报告 heuristic 映射覆盖率 | 补 94.3% / 96.9% / 93.7% / 96.8%，全局 98.8%（`03_soc_27.csv`） |
| 17 | Table 3 加拿大 RORR（若统一口径） | 若按 M2 建议把加拿大侧也改为"各自 c、d"，**两格会变**：PAIN vs morphine **0.146 → 0.144**、DRUG INEFFECTIVE vs morphine **1.703 → 1.706**（另两格 0.235 / 1.277 不变）。当前表内数字在"共享 c、d"口径下无误 | 二选一：保留现状＋题注明说两库口径不同；或统一口径＋同步改这两格。**不可只改文字不改数** |

**C. 经查无误**
| # | 项目 | 核查结果 |
|---|---|---|
| 18 | Table 2 / 3 / 4A / 4B / 4C / S5 / S1A / S1B / S4 全部数字 | 980 + 216 格逐格比对，**0 处不一致** |
| 19 | 破折号语义（不可估计 vs 0） | 170 处核对，**全部正确**；五个 a priori 术语 PT_total = 0 确为"全库零" |
| 20 | ROR 由 a / PT_total / N 独立重算 | 最大相对误差 9.0×10⁻⁴，全部为显示舍入 |
| 21 | Table 4A 由 `_faers_cache.json` 独立重算 | **0 处不一致** |
| 22 | 加拿大 PAIN 0.235 / 0.146、DRUG INEFFECTIVE 1.277 / 1.703、VOMITING 1.066 / 0.392 | 全部重算命中（先用计数，再用原始 line-listing 端到端复现） |
| 23 | 医师-only 5.921 / 10.604 | 与 `cv/cv_pt_summary.csv` 一致 |
| 24 | Table S1 Panel A 四抽查 SOC 的 ROR 与 RORR（2.363/1.792、0.101/0.213、0.361/0.497…） | 全部重算命中，且已用原始 `reactions.txt` 的精确 c（41 538 / 248 694 / 557 400 / 117 116）验证 ROR 三位小数 |
| 25 | Table S3 "Age not stated 49/111 = 44.1%" 等 | 全部为正确的一位小数舍入 |
| 26 | Table S3 两列 "Other health professional" 均为 2 056 | **真实数据巧合**，非复制错误（三路独立证据） |
| 27 | 8 + 1 + 1 = 10 与 Table 4C a 列合计 = 9 | 自洽，与 `01_faers_results.csv`、`04_sensitivity_year_hyperaesthesia.csv` 一致 |
| 28 | "twelve computable ratios, eleven below 1" | 12 个数得上，11 < 1 正确 |
| 29 | Table 4B a 列合计 13 与"23 份中 13 份落在 2015–2024" | 自洽 |
| 30 | 队列数 5 375 / 121 819 / 6 513 / 56 501 与 111 / 4 881 / 63 / 7 675、全库 20 692 687 与 1 154 017 | 与 `_faers_cache.json`、`cv/cv_drug_totals.csv`、`cv/cv_summary.md` 一致 |
| 31 | 91.9% / 79.8% / 69.0% / 64.9% / 23.6% / 7.0% / 98.0% 等百分比 | 全部为正确的四舍五入（其中 98.0% = 5 270 / 5 375 ✓） |
| 32 | 532 / 367（过敏反应事件数） | 可追溯至 `_faers_cache.json` 与 `D_27SOC_openFDA事件级.md`（§9 已列） |
| 33 | 21.1% / 0.077 / 0.038（途径分层） | 可追溯至 `02_route_stratified.csv`、`02_route_summary.md`（§9 已列） |
| 34 | Python 3.13.14 / matplotlib 3.11.1 | 与本机实测一致 |
| 35 | Table 2 脚注 Bonferroni 下界 1.61 | 复算 1.6132 ✓（72 = 18×4 ✓） |
| 36 | 图件 600 ppi / 180 mm / 无标题·边框·网格·图例框 | 全部符合 *Anaesthesia* 规制 |
| 37 | Figure 2 的硬编码序列 | 与 `04_sensitivity_year_pain.csv` 逐项一致 |
| 38 | 活性成分匹配规则（§2.2 所述） | 与 `cv/cv_process.py:39-41` 一致，且复核未引入 apomorphine / norfentanyl |
| 39 | 加拿大侧 `cv_soc_27.csv`（27×4 计数 + 81 比值）与 `cv_pt_summary.csv`（18×7） | **以原始 line-listing 端到端重算，逐格不一致 = 0**；全库 N = 1 154 017、队列 111/4 881/63/7 675、原生 SOC 数 = 27 全部复现 |
| 40 | Table S1 Panel A 的 ROR 列（原先只能由舍入 ROR 反解 c） | 现由原始数据给出精确 c，代入后三位小数严格相等；反解值与精确值之差仅 2–231，属反推的正常误差 |
| 41 | Table 3 全 14 行的加拿大侧 a 与两个 RORR | 与原始 line-listing 独立重算的后 14 行逐项一致，**0 处不符**；表内破折号均对应"暴露侧 a = 0（不可估）"，语义正确 |
| 42 | Table 3 加拿大部分术语的全库 c（ALLODYNIA 29、DRUG TOLERANCE 386、HYPERAESTHESIA 521、PROCEDURAL PAIN 1 510、DRUG WITHDRAWAL SYNDROME 1 664、DRUG INEFFECTIVE 205 227、PAIN 48 267） | 已由原始数据独立数出，破折号确为"不可估计"而非"术语缺失" |
