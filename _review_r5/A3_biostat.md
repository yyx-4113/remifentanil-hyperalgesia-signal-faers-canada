# Round-5 独立审稿 — A3_biostat 生物统计学家

## 0. 审稿人身份与总体结论

**审稿人自述。** 我从事药物警戒统计方法研究，专长是稀疏计数数据的区间估计（Woolf/精确条件/中位数无偏近似）、多重比较的错误率控制、时间序列与变点分析、以及跨库失衡分析的 Meta 合并。我按本刊 Original Article 的标准审读，并把稿件中每一个可核验的数字在我自己的环境下重算了一遍（§6）。

**Verdict: Major Revision**

**理由（5 句）。**
1. 稿件把一个只用 1 例支撑的 Wald（Woolf）区间当作可展示的结果印在正文与 Table 2 中：我重算 ALLODYNIA 的 Woolf 下界为 0.488，而精确条件区间下界是 0.088（相差 5.6 倍），加 0.5 校正更会把一个 1 例术语的下界推到 1.05——三种方法在同一个 2×2 上给出互相矛盾的区间，而稿件只报了最"好看"的那一个（M1）。
2. 所谓 "leave-2024-out 敏感性分析"在原始 CSV 里实际是"限定 2015–2023"，它同时丢弃了 1 129 份 2015 年前的瑞芬太尼报告；真正的"全库剔除 2024"应得 ROR 0.94 (0.24–3.77)，而不是稿件写的 0.70 (0.10–4.98)，且该区间的上界包含合并估计 4.73，因此"signal 消失"是功效不足而非效应不存在（M2）。
3. 年份分层用的是各年相互独立的 2×2 RORR，不是任何时间模型；`ratio_2024_to_pooled` 是一个没有分布、没有区间、分子分母还互相包含的比值，却承担了"2024 是全体位移"的因果式论断（M3）。
4. Table 2 脚注的 Bonferroni（1.61）我可以复现（双侧 α=0.05、k=72、z=3.392 → 下界 1.615），但它是把"通过 α 校正"偷换成"结论稳健"，而本稿真正的威胁从来不是假阳性率，是 2024 单年聚集（P1-1）。
5. 与此相对，稿件在方法层面有若干真正规范的做法（预先定义的信号判据、阴性对照与特异性探针、对不可检索串拒绝解释、严重报告子集同步重算参照集），这些应当保留（§4）。

---

## 1. 重大问题（Major）

### M1. 稀疏计数下 Woolf 区间失效，而稿件把最不可靠的那个区间印了出来

**【问题】** 稿件在 §2.4 声明 CI 用 "the log scale with the sum of the reciprocal cell counts (Woolf approximation)"，并在 §3.3 与 Table 2 展示 a=1 的 ALLODYNIA 区间 "3.47 (0.49–24.67)"。对 a=1 的格子，Wald 型对数区间不成立：其下界被 1/a 主导且系统性偏高，方向是**反保守**（把"可能有信号"说成"没有"）。

**【证据】** 我用稿件自己的 2×2（a=1, b=5374, c=1109, d=20686203；`01_核心FAERS失衡分析.py:110` 定义 d=N−a−b−c）独立重算（§6 PART 1）：

| 方法 | 点估计 | 95% CI |
|---|---|---|
| Woolf（稿件，z=1.96） | 3.471 | **0.488 – 24.668**（与稿件 0.49–24.67 一致，复现成功） |
| Haldane 加 0.5 | 5.204 | **1.049 – 25.816**（下界越过 1） |
| 精确条件 MLE（Fisher 非中心超几何） | 3.471 | **0.088 – 19.387** |
| mid-P 条件 | 3.471 | **0.173 – 17.153** |

对 a = 0,1,2,7,10,23 在 ALLODYNIA 框架下的系统比较（§6 补充）：

```
   a      ROR               Woolf         Haldane+0.5          exact cond
   0    0.000     undefined (1/0)         0.108-27.72         0.000-12.82
   1    3.471         0.488-24.67         1.049-25.82         0.088-19.39
   2    6.950         1.735-27.83         2.509-30.04         0.840-25.18
   7   24.456        11.626-51.45        12.765-53.73         9.805-50.59
  10   35.052        18.796-65.37        20.021-67.59        16.752-64.76
  23   81.783        54.067-123.71        55.451-125.78        51.575-123.49
```

即：a=0 时 Woolf 直接无定义；a=1 时 Woolf 下界是精确下界的 5.56 倍；a=2 时是 2.07 倍；即使 a=10，Woolf 下界（在 HYPERAESTHESIA 上是 2.542）仍比精确下界（2.265）高 12%。可信的下界从 a≈7 起才稳定（比值 1.19 → 1.05）。

**【为什么重要】** (i) 对 ALLODYNIA，"no signal" 的**结论**没错（各法下界都 <1，且 a=1<3 不满足处 a≥3 的前置条件），但**显示出来的区间是错的**：读者会看到"0.49"，以为下界接近 0.5、距 1 不远，实际上精确下界只有 0.088。这是会被统计审稿人直接抓住的问题。(ii) 更危险的是方法方向本身——对 a=1 使用加 0.5 校正会让下界变成 1.049 > 1，一个单报告术语会"看起来产生信号"。稿件没有意识到 a=1 情境下三种区间法给出发散答案。(iii) §3.3 已正确地写了 "not estimable … the only defensible fact is the absence of a signal, not its direction"，但正文/表格同时印出一个看似精确的区间，两者自相矛盾。

**【具体修改建议】**
(1) 在 §2.4 增加方法分级句，并在全稿对所有 a<5 的格子改用精确/中位数无偏区间：
> "Log-scale Wald intervals require at least about five observed events; below that the lower bound is dominated by 1/a and is anticonservative. For cells with fewer than five events we therefore report the exact conditional (or mid-P) interval, computed by inverting Fisher's noncentral hypergeometric distribution, and we treat any cell with a = 0 as not estimable rather than as a zero."
(2) Table 2 ALLODYNIA 行改为：`1 | 3.47 (exact 95% CI 0.09–19.39; Woolf not reported: a=1) | …`，脚注删去 "Remifentanil counts of fewer than 3 reports give unstable estimates" 这类泛泛的话，换成 "for a < 5 the interval is exact conditional; a Wald interval is not reported because it is anticonservative"。必须给出精确区间数值，不能只写一句说明。

---

### M2. "leave-2024-out" 实际算的不是剔除 2024；"signal 消失"混淆了"估计不稳定"与"效应不存在"

**【问题】** 稿件的 Summary、§3.8、§4.1、§5 与 `04_sensitivity_leave2024_hyperaesthesia.csv` 都称之为 "leave-2024-out"，并写 "disappears when 2024 is excluded (**a = 1**)"。但全库 a=10、其中 2024 年 8 例，真正的"全库剔除 2024"应当得到 **a = 2**。a=1 的来源是该脚本把分析限定在 **2015–2023 窗口**（`_round4_leave2024.py:41-42, 47-51`），它同时丢弃了 1 129 份 2015 年以前的瑞芬太尼报告，并把背景从 20 692 687 换成 12 401 440。

**【证据】**（§6 PART 4）

```
sum(N_year 2015-2024)= 13720546   sum(H_year)= 4995   sum(remi cohort)= 4246
remifentanil reports OUTSIDE 2015-2024 = 1129
as implemented (2015-2023 窗口): N=12401440 H=4658 cohort=3798 a=1 -> ROR=0.701 (0.099-4.978)  [CSV 0.701 (0.099-4.978)]
TRUE whole-corpus leave-2024-out (a=10-8=2, 全 5375 队列): ROR=0.943 (0.236-3.774)
whole corpus with a=1 only                                 : ROR=0.472 (0.066-3.349)
pooled ROR 4.729 inside the as-implemented leave-out CI? True
exact conditional CI of the as-implemented leave-out: 0.018-3.909
RORR vs fentanyl = 0.1064 (0.0149-0.7585)   [CSV 0.106 (0.015-0.758)]
```

三点统计事实：
- **(i) 判别力。** 该 "敏感性分析" 只剩 1 例（无论按哪种定义都 ≤2 例），它没有判别力。其 CI 上界 **4.98 > 合并估计 4.73**——也就是说，剔除 2024 后的数据**并未排除**原来的效应量；下界 0.10 只说明"什么都不能排除"。同时 RORR vs 芬太尼 = 0.11 (0.02–0.76) 的**上界 0.76 < 1**，这不是"无信号"，而是"在 2015–2023 窗口内瑞芬太尼相对芬太尼**显著低报**"——只是这个"信号"方向与主分析相反、且只由芬太尼臂（249 例）驱动。
- **(ii) 推理跳跃。** 作者据此写 "so the pooled estimate is a single-year cluster, not a stable finding"。前半句（池化估计由 2024 承载）成立且正确；但由此暗示"剔除后效应不存在"就把 **"估计不稳定"** 当成了 **"效应不存在"**。正确的统计结论是：主分析关于 HYPERAESTHESIA 的 ROR 是**不可识别的**（uninformative），不是阴性的。
- **(iii) 标签错误。** 由于实际口径是 2015–2023，任何按字面"全库剔除 2024"重算的读者会得到 0.94 (0.24–3.77)，与稿件 0.70 (0.10–4.98) 明显不同；这属于无法用文字搪塞的口径不一致。

**【为什么重要】** 这一句是全文摘要、结论三处重复的核心论断。若不动它，(a) 任何复算者都会发现"leave-2024-out"的 a 值对不上；(b) "signal 消失"会被读成"瑞芬太尼没有报告失衡"，而这与同一段里 RORR 显著 <1 的事实冲突，读者会认为作者在为自己的结论选措辞。

**【具体修改建议】** 用下面这段替换 §3.8 的对应句（并同步改 Summary 与 §5）：
> "Restricting the hyperaesthesia analysis to 2015–2023 (remifentanil cohort 3 798 of its 5 375 reports; background 12 401 440 reports; a = 1) gave a reporting odds ratio of 0.70 (95% CI 0.10–4.98) and a ratio against fentanyl of 0.11 (0.02–0.76). This interval is wide and still contains the pooled estimate of 4.73, so the analysis is uninformative for the presence of the signal rather than evidence that it is absent; the pre-2024 ratio against fentanyl indicates that the pooled remifentanil-versus-fentanyl difference was confined to 2024. For transparency, a whole-corpus analysis that removes only the 2024 reports (a = 2) gives 0.94 (0.24–3.77)."
同时把 CSV 列名与正文中的 "leave-2024-out" 改为 "2015–2023 window"，或补一列真正剔除 2024 的结果。

---

### M3. 年份分层不是时间模型；`ratio_2024_to_pooled` 没有分布却被用作跨药比较的证据

**【问题】** §3.8 与 Table 4B/4C 逐年各做一次独立 2×2，得到各年 RORR；作者以"八个可估计年份无一反向"作为"稳定"的证据，又以 `ratio_2024_to_pooled`（瑞芬 15.41、芬 4.30、舒 4.90、吗 1.71）论证"2024 是全体位移而非瑞芬特有"。前者没有趋势检验或异质性检验，后者既无区间也无检验，且**分子分母互相包含**（合并 ROR 里含 2024）。

**【证据】**（§6 PART 5）
- `ratio_2024_to_pooled` 是 **ROR_2024 / ROR_pooled** 的比值（`_round4_leave2024.py:74-89`）。分子用 2024 年 2×2（d≈1.32×10⁶），分母用合并 2×2（d≈2.07×10⁷）——**参照人群不同**；且分母**包含**分子，两者不独立。我按 delta 法（假定独立，因而**高估**方差）给出区间：瑞芬 **15.41 (6.01–39.49)**、芬 **4.30 (2.60–7.10)**、舒 **4.90 (2.07–11.59)**、吗 **1.71 (1.08–2.71)**。瑞芬与芬太尼的区间**大幅重叠**，因此"四个药都在 2024 抬升"这一**方向**可陈述，但"15.41 与 4.30 属于同一类位移"这一**量级**论断没有统计支持。
- 全库 HYPERAESTHESIA 的**报告率并不升反降**：2015→2024 为 54.4、47.9、46.9、40.1、30.5、32.8、30.9、31.9、29.2、**25.5**（每 10 万报告）。所以 2024 的 ROR 抬升不可能来自"全库事件率上升"，只能来自各药队列内部的编码份额变化或队列构成变化（例如芬太尼队列从 2015 年 10 017 份降到 2024 年 2 412 份）。稿件把这称为 "a 2024 coding or reporting shift" 只是**一种**未检验的解释。
- Table 4B 的 PAIN 结论 "no reversal in the eight estimable years" 同样是不可反证的：各年瑞芬 a 只有 0–3（`04_sensitivity_year_pain.csv` 的 REMIFENTANIL_a = 2,1,1,0,0,2,1,1,2,3），8 个可估计年的 RORR 点估计落在 0.014–0.168、上界最高 0.53，任何真实的反向都会被这层宽区间淹没；而且逐年独立 2×2 之间没有共同参照系，把年份当作互斥的重复实验本身不是时间模型。

**【为什么重要】** 这是本稿唯一"支持性证据"的形式化来源（PAIN 的跨年稳定、2024 的全体性）。如果只用逐点比较，它经不起"没有趋势检验/没有交互检验"的追问；而 `ratio_2024_to_pooled` 恰好是全文最容易在统计上被推翻的一步，因为它连区间都没有。

**【具体修改建议】** 把年份分析升级为真正的计数模型，并把描述性比值降级。模型形式（可直接照抄）：

> "Year effects were estimated with a Poisson generalised linear model with a log link and the drug-year report total as offset: log E[Y_{d,y}] = log R_{d,y} + μ + α_drug + γ_year + δ_{drug×year}. Y is the number of reports carrying the preferred term for drug d in year y and R the number of reports in that drug-year cell. Over-dispersion was assessed and, where the dispersion statistic exceeded 2, a negative-binomial model was fitted. The 2024 cluster was tested by a likelihood-ratio test of δ_REMIFENTANIL,2024 = 0 and the shared-shift hypothesis by a likelihood-ratio test of δ_ = 0 for all four drugs jointly. Trend was tested by replacing γ_year with a linear (and, as a sensitivity, restricted cubic-spline) term in year and testing the drug×year interaction."

输出列（新 Table 4D）建议固定为：`PT | drug | comparator | model | β(interaction, log) | SE | 95% CI | LRT p (drug×year) | p for linear trend | n events | n reports | dispersion φ`。

对 `ratio_2024_to_pooled` 的处置：
> "The 2024-to-pooled ratio is a descriptive quantity without a sampling distribution; because the pooled estimate contains the 2024 data the numerator and denominator are dependent, and the two use different reference populations. It is reported with a delta-method interval (calculated assuming independence and therefore conservative) and no cross-drug claim is made from it unless the drug×year interaction test supports one."

即：要么补区间 + 交互检验，要么把这一句删成纯描述（"all four point estimates exceeded one"），不得保留"rather than a remifentanil-specific event"这种由未检验比值推出的结论性短语。

---

## 2. 重要问题（P1）

### P1-1. Bonferroni 脚注：数值可复现，但它在偷换概念

**【问题】** Table 2 脚注写 "with a Bonferroni correction across all 72 drug–term comparisons the lower bound of the remifentanil HYPERAESTHESIA interval remains above one (1.61)"。这被隐含用来支持"结论稳健"，但多重性校正解决的是假阳性率，而本结果真正的脆弱点是 **2024 单年聚集**（M2/M3）——α 校正再多也治不了它。

**【证据】**（§6 PART 3）我独立复现：ROR=4.7288，log=1.553675，Woolf se=0.316716；`k=72` 双侧 α=0.05 → `z=3.39176` → 下界 **1.6152（≈1.61）**。因此：**72 = 18 术语 × 4 药**，校正的是**双侧** α（单侧 k=72 会给 1.718，不是 1.61；k=54 给 1.656；k=216 给 1.473；k=440 给 1.393）。复现成功。

三处概念问题：
1. **家族规模被低估**：除 Table 2 的 18×4=72，还有 Table S5 的 RORR 18×3=54、Table 4A 18×4=72、年份表 10×4×2=80、加拿大 SOC 27×3=81、FAERS SOC 27×3=81，可辩护的家族 ≥ 440（此时下界 1.39，仍 >1——所以这不是"翻不翻盘"的问题，而是"报少了"的问题）。
2. **未计入"事后选词"**：HYPERAESTHESIA 是在 5 个先验术语返回 0 之后才补入的（ANALYSIS_PLAN.md §Amendment 1），这一类**自适应选择**造成的多重性远大于 72，Bonferroni 覆盖不到。
3. **内部不一致**：§3.7 明确写 SOC 分析 "with no multiplicity correction"，而 Table 2 又单独做了一次校正，全稿没有统一的错误率框架。

**【为什么重要】** 脚注的修辞效果是"作者已经做了多重性校正，所以这个信号可信"。但一个 1.61 的下界同时存在于一个 a=1 的邻近术语（ALLODYNIA）之上，恰恰说明**下界 >1 不等于结果可重复**。审稿人读到 M2 的 a=1 之后，会把这个脚注读成"选择性使用统计工具"。

**【具体修改建议】** 删除脚注最后一句，替换为：
> "No family-wise error rate was controlled in this table. For orientation only, a two-sided Bonferroni correction over the 72 drug–term odds ratios in this table leaves the lower bound of the remifentanil HYPERAESTHESIA interval above one (1.62). This correction does not address the post hoc selection of HYPERAESTHESIA after the a priori terms returned zero, nor the concentration of that term in a single year (§3.8); the reader should therefore treat the surviving lower bound as evidence against a family-wise false positive, not as evidence of a stable signal. The family of comparisons across this study is much larger than 72 (Tables S5, 4A, 4B, 4C and S1) and no study-wide correction is claimed."

---

### P1-2. "份额参照 d 的协方差可忽略"以及"比较药特异项相消"两处声明需要修正

**【问题】** §2.4 写 "Both ratios share the same background reference, **so comparator-specific terms cancel** … treating the two ratios as independent although they share the background reference d; with 20 692 687 background reports the ignored covariance is under 0.001% of the variance, so it is conservative."

**【证据】**（§6 PART 2）按作者实际做法（`04_sensitivity.py:101`，se² = 逐格倒数和、含两个 d）：
- **协方差项是否真的 <0.001%？** 被忽略的量 = 1/d_瑞芬 + 1/d_芬太尼；占总方差的比例：

```
term                          d_remi     d_fen     V_used     ignored    % of V
HYPERAESTHESIA              20679161  20563022   0.103619    9.70e-08  0.00009%
ALLODYNIA                   20686203  20569806   1.022871    9.70e-08  0.00001%
PAIN                        20080159  19971041   0.043813    9.99e-08  0.00023%
DRUG INEFFECTIVE            19388242  19279652   0.005136    1.03e-07  0.00201%   <-- 超过 0.001%
NAUSEA                      19908817  19797250   0.020010    1.01e-07  0.00050%
VOMITING                    20224713  20111688   0.016113    9.92e-08  0.00062%
PRURITUS                    20314412  20199044   0.025487    9.87e-08  0.00039%
CONSTIPATION                20473787  20359343   0.091611    9.80e-08  0.00011%
```

  对我的问题中的口径澄清：**d 不是 20 692 687**。源码 `01_核心FAERS失衡分析.py:110` 定义 `d = N - a - b - c`，即"全库减去本药、再减去本术语（并加回 a）"；HYPERAESTHESIA 的 d 是 20 679 161（瑞芬）与 20 563 022（芬太尼），N=20 692 687 只高出 0.07–1.6%。结论的**数量级**成立（2/N = 9.7×10⁻⁸，与 2/d 同级），但"under 0.001%"这个具体阈值对高计数术语（DRUG INEFFECTIVE 0.0020%、VOMITING 0.0006%）**不成立**。
- **"comparator-specific terms cancel" 不成立。** 因为两个 d 数值不同，RORR = (a₁d₁/b₁c₁)/(a₂d₂/b₂c₂) 里 d 并不会相消。按作者做法与"共享同一 d"的代数式之差：

```
HYPERAESTHESIA    d_r/d_f=1.005648  implemented=0.6960  shared-d=0.6921  diff=+0.565%
ALLODYNIA         d_r/d_f=1.005659  implemented=0.4546  shared-d=0.4521  diff=+0.566%
PAIN              d_r/d_f=1.005464  implemented=0.0665  shared-d=0.0661  diff=+0.546%
DRUG INEFFECTIVE  d_r/d_f=1.005632  implemented=0.5678  shared-d=0.5646  diff=+0.563%
```

  系统性偏高约 0.55–0.57%（不是随机噪声，而是由两个队列规模差决定的偏差）。

**【为什么重要】** 这是 §2.4 中唯一一处"数学上正确性"的声明，而它是错的（d 不相消）或过宽（<0.001% 不普遍成立）。这类声明会被复算审稿人当成"作者对自己的公式没算过"的证据，连带削弱其余声明的可信度。好在实际数值影响很小（≤0.002%），所以是 P1 而不是 M。

**【具体修改建议】** 改为：
> "Each ratio uses its own remainder cell d, so the background terms do not cancel exactly; the resulting deviation in the ratio of reporting odds ratios is below 0.6% for every comparison reported here (for HYPERAESTHESIA, 0.696 as computed versus 0.692 under a common remainder). Confidence intervals were computed on the log scale from the sum of the reciprocal cell counts of the two 2×2 tables. This ignores the positive correlation induced by the shared corpus, which inflates the variance by 1/d₁ + 1/d₂ — for HYPERAESTHESIA 0.0001% of the variance and at most 0.002% across all terms in Table 2 — so the intervals are, if anything, conservative."

---

### P1-3. 加拿大库的功效：0.19%，"neither confirms nor refutes" 是正确但不充分的表述

**【问题】** §3.3/§5 写 "111 reports have no power for a term this rare, so Canada neither confirms nor refutes the FAERS signal"。这句话方向正确，但把一个"几乎零功效"的阴性结果说成了"中性的验证结果"，读者会高估加拿大库的信息量。

**【证据】**（§6 PART 6）加拿大 111 份瑞芬太尼报告、全库 HYPERAESTHESIA 523 行，背景率 p₀ = 523/(1 154 017−111) = 4.532×10⁻⁴。在"a≥3 且下界>1"的判据下（a≥3 是必要条件）：

```
  true ROR=  1.00 E[a]=0.0503  P(a>=3)=0.000020
  true ROR=  2.00 E[a]=0.1006  P(a>=3)=0.000157
  true ROR=  4.73 E[a]=0.2376  P(a>=3)=0.001872   <-- 主分析量级：功效 0.19%
  true ROR= 10.00 E[a]=0.5011  P(a>=3)=0.014468
  true ROR= 20.00 E[a]=0.9976  P(a>=3)=0.079862
  true ROR= 50.00 E[a]=2.4608  P(a>=3)=0.446105
  true ROR=100.00 E[a]=4.8149  P(a>=3)=0.858872
最小可检出 ROR（80% 功效）= 88.4
```

即：加拿大库要以 80% 功效检出效应，需要真实 ROR ≈ 88；对主分析的 4.73，功效约 **0.19%**（且加严到"下界>1"只会更低）。此外，加拿大的 523 是**反应行**计数而队列 111 是**报告**计数，二者量纲不同，直接相除会略微高估背景率——用更保守的报告级背景率只会让功效更低。

**【为什么重要】** 这是"跨库验证"这一整块结论的效力边界。稿件目前会让读者以为"两个库结论不一致"，实际上第二个库根本没有能力产生除了 0 以外的任何结果；若换成"power"语言，反而**支持**作者"不能证伪"的立场，是免费的加分。

**【具体修改建议】** 用带功效数字的句子替换：
> "With 111 remifentanil reports and a background preferred-term frequency of 4.5 per 1 000 reports, the Canadian cohort had a power of about 0.2% to detect an effect of the magnitude seen in FAERS (reporting odds ratio 4.7), and a reporting odds ratio of roughly 88 would have been needed for 80% power. The absence of a Canadian remifentanil report of this term is therefore uninformative rather than discordant, and Canada can neither confirm nor refute the FAERS signal for a term this rare."

---

### P1-4. 全稿缺少可执行的多重性框架

**【问题】** 全稿约 18 术语 × 4 药 ×（全库/严重/年份）加上两套 SOC（各 27 类 × 3 比较）的比较，作者只在 Table 2 提了一句 Bonferroni，其余一律"exploratory"。既没有分层，也没有 FDR，也没有预先声明主/次要终点。

**【证据】** 家族规模核算（§6 PART 7）：Table 2 OR 18×4=72；Table S5 RORR 18×3=54；Table 4A 18×4=72；年份表 10×4×2=80；加拿大 SOC 27×3=81；FAERS SOC 27×3=81 → ≥440。阴性对照部分是"11/12 个比值 <1"，其单侧二项概率 P(≥11 of 12 | p=0.5) = **0.00317**——方向性证据其实不弱，但作者既没给这个数，也没说明它是否属于某个家族。

**【为什么重要】** 不声明主/次要终点，读者无法判断哪些对比是"结论"、哪些只是"探索"。这对 *Anaesthesia* 这类临床刊尤其敏感，因为审稿人最怕的是"从大量比较里挑一个显著的讲成结论"——而本稿恰恰是从 5 个先验术语返回 0 之后**换了一个术语**继续分析。

**【具体修改建议】** 在 §2.4 加一段固定框架，并落到表格脚注：
> "Endpoints were analysed in a pre-ordered hierarchy. (i) The two a priori narrow terms (HYPERALGESIA, ALLODYNIA) are the primary endpoints, tested two-sided at α = 0.05. (ii) The five dictionary proxies are secondary; because they were added after the a priori terms returned zero, they are tested only if a primary endpoint rejects, using a fixed-sequence gate, and their p values are reported with Benjamini–Hochberg false-discovery-rate control at q = 0.05 within the 18-term × 3-comparator family (54 tests). (iii) Negative controls and the specificity probe, the serious-report and year-stratified analyses, and both system-organ-class panels are descriptive and hypothesis-generating; no p value in those panels is to be read as confirmatory, all CIs are reported, and no comparison is selected on the basis of its p value or its asterisk."
并在每张表脚注写明该表属于哪一层、家族内共几次比较。**必须改的一句**是 Table 2 脚注里 "No multiplicity correction was applied to this table; with a Bonferroni correction … (1.61)"——它与新增的分层框架冲突，应按 P1-1 的替换句重写。

---

## 3. 次要问题（P2）

### P2-1. 方法段说 z 用 1.96，但这会让部分表格数字无法逐位复现

**【问题】** 源码 `01_核心FAERS失衡分析.py:105` 与 `04_sensitivity.py:76` 都硬编码 `1.96`，而稿件没有说明这一点。用 1.96 还是 1.959964，在 a=1 时会让末位差 0.001–0.01，在 Bonferroni 段落则直接决定报 1.61 还是 1.62。
**【证据】** 我对 ALLODYNIA 分别用两个 z 计算：z=1.96 → 0.488–24.668；z=1.95996 → 0.488–24.667（稿件写 0.49–24.67，与 z=1.96 同源）。HYPERAESTHESIA 在 k=72 下我算 1.6152，稿件写 1.61（1.6148 才四舍五入到 1.61）。
**【为什么重要】** 读者若用 z=1.959964 复算会得到不一致的末位，容易误判为造数。**建议**：在 §2.4 明确 "two-sided 95% intervals used z = 1.96"，并统一脚本与成文；Bonferroni 句给出 z 值。

### P2-2. §3.7 与 Table 2 的错误率声明需要统一
**【问题】** §3.7 声明 SOC 分析 "with no multiplicity correction"，Table 2 却单独做了一次 Bonferroni；同稿两种口径。
**【证据】** §3.7 原文 vs Table 2 脚注末句。**建议**：按 P1-4 的框架统一表述，SOC 面板明确标注为"description only, no inference"。

### P2-3. 阴性对照的"11/12"应当给出概率
**【问题】** "eleven of the twelve computable ratios were below 1" 未附任何概率，读者无法判断这是否超出偶然。
**【证据】** P(≥11 of 12, p=0.5) = 0.00317（§6 PART 7）。**建议**：加一句 "under a null of no directional difference this count has a one-sided binomial probability of 0.003"。

### P2-4. 加拿大 HYPERAESTHESIA "523" 的量纲
**【问题】** 稿件把加拿大 523 称为 "reaction rows"，而队列 111 是 **reports**（`cv/cv_drug_totals.csv`）；用行数做事件计数、报告数做分母会轻微高估背景率。
**【证据】** Table S4 写 "Canada reaction rows"；`cv_summary.md` 的 111/4 881/7 675 为 suspect **reports**。**建议**：说明或改用报告级计数重算这一处背景率。

---

## 4. 我认为稿件站得住的地方（附证据）

1. **信号判据是显式、可复现的，并且对稀疏数据加了计数下限。** §2.4 与 ANALYSIS_PLAN.md 一致地写 "a ≥ 3 and the lower bound of the 95% CI of the ROR > 1, or PRR ≥ 2 with χ² > 4, or IC025 > 0"。我在 a=1 的极端情形下验证了这个 a≥3 前置条件正是阻止"单报告假信号"的关键机制——例如加 0.5 校正会把 ALLODYNIA 的下界推到 1.049 > 1，但 a≥3 仍然正确地把它挡在信号之外（§6 PART 1）。这个设计是对的。
2. **四算法交叉验证而非单指标。** `01_faers_results.csv` 同时给出 ROR/PRR/IC025/EBGM；我核对 HYPERAESTHESIA 一行，四者方向一致（ROR 4.729、PRR 4.722、IC025 1.342、EBGM 4.972），与之相对 DRUG WITHDRAWAL SYNDROME 的 ROR 0.307 与 IC025 −2.769 也一致。这种一致性是失衡分析的规范做法。
3. **拒绝把不可检索串解释成"零事件"——本稿最扎实的一步。** §2.3、§3.2 与 Table S4 明确：HYPERALGESIA 不是 PT，串查询为 0 是构造性的；我用 `10_term_dictionary.csv` 复核，HYPERALGESIA 在两库均为 0，而相邻词元查询也为 0、HYPERAESTHESIA 为 8 161/523，与稿件完全一致。而且稿件主动声明"五个代理术语不是独立验证，因为它们共享语料且是因原始串为 0 才被选中"（§2.3 末），这是很难得的自我限制。
4. **严重报告子集的做法正确。** §2.6/§3.8 对 `serious:1` 同时限制了分子与参照集（`04_sensitivity.py:71,112-126`），不是只换分子。我核对 Table 4A：N_ser=11 882 968，瑞芬 5 270/5 375=98.0%，HYPERAESTHESIA 的 10 例全部落在该子集，ROR 由 4.729 变为 4.309——数字自洽。这是敏感性分析应有的做法。
5. **可估计年份数由机器写死，不由人写。** `04_sensitivity_estimable_years.json` 固定 {PAIN: 8, HYPERAESTHESIA: 2}，脚本还在摘要里写了"不得写 'every year' 或 'ten years'"的门禁。这类把结论数字从文本中抽出的做法应被鼓励。
6. **对 a=1 的 RORR 主动加了 † 号并声明不可估。** Table 2 把 ALLODYNIA 的 RORR 标为 "not estimable (n = 1)"，Figure 1 图注也明说不画 ALLODYNIA。这说明作者对稀疏性有意识——M1 的问题在于区间怎么算、而不是在于作者想掩盖。

---

## 5. 需要作者明确澄清的事实性问题

1. **"leave-2024-out" 的确切口径**：是"全库剔除 2024"（应为 a=2、ROR 0.94）还是"限定 2015–2023"（a=1、ROR 0.70）？若是后者，1 129 份 2015 年前的瑞芬太尼报告为何被一并丢弃，为何正文与摘要都写 "a = 1"？
2. **d 的定义**：§2.4 说 "with 20 692 687 background reports"，但源码用的是 `d = N − a − b − c` = 20 679 161（瑞芬）与 20 563 022（芬太尼）。请确认协方差百分比是按 N 还是按各自的 d 计算。
3. **"72" 的构成与临界值**：是否确为 18 术语 × 4 药？校正的是双侧还是单侧 α？我复现 1.61 需要双侧、k=72、z≈3.39；请确认脚本里用的 z。
4. **年份分层的参照集**：各年 ROR 是否以"该年全库 N_year"为参照？若是，请说明为何可以把不同年份的 ROR 相除（`ratio_2024_to_pooled`）而没有量纲问题。
5. **2024 的可能机制**：全库 HYPERAESTHESIA 报告率在 2015–2024 单调下降（54.4→25.5 每 10 万），因此不存在"全库事件率上升"；作者是否核查过 2024 年 clusster 是否来自某一段 receivedate、某个国家/报告者类型或某批重复报告？
6. **加拿大 523 的量纲**：是 reaction rows 还是 reports？若是 rows，背景率 p₀ 应如何按报告级重算？
7. **ALLODYNIA 那 1 例**：其 receivedate、serious 标志、是否与 HYPERAESTHESIA 的 10 例重合、是否为重复报告？这决定 a=1 是否还是 1。
8. **openFDA 去重**：稿件称 openFDA 不做法案级去重（§2.1/§4.5）。那么年份表里 `N_year` 是否也含重复？重复若集中在 2024，会不会本身就是"2024 聚集"的来源？

---

## 6. 我实际做的独立核查

环境：`python 3.13.14`（与稿件 §2.4 声明一致）、numpy 2.5.2、scipy 1.18.1（statsmodels 不可用，未使用）。脚本写在 `_review_r5/_a3_analysis2.py`、`_review_r5/_a3_addendum.py`，输出落在 `_review_r5/_a3_out.txt`、`_review_r5/_a3_add.txt`。**读过的源文件**：`I_正文_IMRaD_en.md`（全文）、`ANALYSIS_PLAN.md`、`01_faers_results.csv`、`04_sensitivity_leave2024_hyperaesthesia.csv`、`04_sensitivity_2024cluster_hyperaesthesia.csv`、`04_sensitivity_year_hyperaesthesia.csv`、`04_sensitivity_year_pain.csv`、`04_sensitivity_ps_only.csv`、`04_sensitivity_estimable_years.json`、`10_term_dictionary.csv`、`cv/cv_drug_totals.csv`、`cv/cv_pt_summary.csv`、`cv/cv_summary.md`、`_faers_cache.json`，以及**分析脚本** `01_核心FAERS失衡分析.py`、`04_sensitivity.py`、`_round4_leave2024.py`（用于确定 d 的定义、z 的取值与 leave-2024 的实际口径）。

命令（截断）：
```bash
cd "…/瑞芬太尼"
"C:/Users/Administrator/.workbuddy/binaries/python/versions/3.13.12/python.exe" -u _review_r5/_a3_analysis2.py > _review_r5/_a3_out.txt 2>&1
"C:/Users/Administrator/.workbuddy/binaries/python/versions/3.13.12/python.exe" -u _review_r5/_a3_addendum.py > _review_r5/_a3_add.txt 2>&1
```

关键代码：
```python
def cells(pt, drug, Ntot=N):            # 与 01_核心FAERS失衡分析.py:110 一致
    a = A[pt][drug]; b = DRUG_N[drug]-a; c = PT_N[pt]-a
    return a, b, c, Ntot-a-b-c

def ror_woolf(a,b,c,d,z=1.96):          # 稿件方法
    ror=(a*d)/(b*c); se=math.sqrt(1/a+1/b+1/c+1/d)
    return ror, math.exp(math.log(ror)-z*se), math.exp(math.log(ror)+z*se), se

def ror_haldane(a,b,c,d):               # 加 0.5 连续性校正
    a,b,c,d = a+.5,b+.5,c+.5,d+.5
    ...

odds_ratio(np.array([[a,b],[c,d]]), kind="conditional")   # 精确条件 MLE + CI
# mid-P：直接对 Fisher 非中心超几何 pmf ∝ C(n1,k)C(n0,m1−k)ψ^k 做归一化并反解 ψ
```

### 6.1 复核出的数值（我算 vs 稿件）

| 量 | 稿件 | 我的复算 | 判定 |
|---|---|---|---|
| ALLODYNIA 瑞芬 ROR (Woolf) | 3.47 (0.49–24.67) | 3.471 (0.488–24.668) | 复现成功 |
| ALLODYNIA 精确条件 CI | — | 0.088–19.387 | 新增：下界为 Woolf 的 1/5.6 |
| ALLODYNIA mid-P CI | — | 0.173–17.153 | 新增 |
| ALLODYNIA Haldane +0.5 | — | 1.049–25.816 | 新增：下界越 1，方向性伪信号 |
| HYPERAESTHESIA 瑞芬 ROR | 4.73 (2.54–8.80) | 4.729 (2.542–8.797)；精确 2.265–8.708 | 复现成功 |
| RORR vs 芬太尼 | 0.696 (0.37–1.31) | 0.6960（共享 d 应为 0.6921，+0.57%） | 复现，但"相消"声明有误 |
| 忽略协方差占方差比 | "< 0.001%" | HYPERAESTHESIA 0.00009%；DRUG INEFFECTIVE 0.00201% | 阈值不普遍成立 |
| Bonferroni 下界 | 1.61（72 比较） | k=72 双侧 z=3.392 → 1.6152 | 复现（四舍五入差 0.005） |
| leave-2024-out ROR | 0.70 (0.10–4.98) | 0.701 (0.099–4.978) | 数字复现，但口径是 2015–2023 |
| 真·全库剔 2024（a=2） | — | 0.943 (0.236–3.774) | 新增：与稿件口径不符 |
| leave-out RORR vs 芬太尼 | 0.11 (0.02–0.76) | 0.1064 (0.0149–0.7585) | 复现 |
| 合并 ROR 4.73 是否落在 leave-out CI 内 | 稿件未提 | 是（0.099–4.978） | 新增：剔除 2024 不排除合并效应 |
| ratio_2024_to_pooled | 15.4 / 4.3 / 4.9 / 1.7（无 CI） | 15.41 (6.01–39.49)、4.30 (2.60–7.10)、4.90 (2.07–11.59)、1.71 (1.08–2.71) | 新增：区间大幅重叠 |
| 加拿大功效 @ROR 4.73 | "no power" | E[a]=0.238，功效 0.19%；80% 功效需 ROR≈88 | 新增 |
| 阴性对照 11/12 | 只给计数 | 单侧 P = 0.00317 | 新增 |
| 全库 HYPERAESTHESIA 年率 | 未报 | 54.4→25.5 /10 万（2015→2024，单调下降） | 新增：与"2024 全库位移"叙事不符 |

### 6.2 与源数据不一致或需澄清之处（已在 §5 列出）

- `04_sensitivity_leave2024_hyperaesthesia.csv` 的列名 `cohort_excl2024 = 3798` 与"剔除 2024"不符：全库瑞芬 5 375，2015–2024 只有 4 246，故 2015 年前的 1 129 份被一并排除。
- Table S4 的加拿大 523 为 reaction rows，而队列为 reports。
- Table 2 脚注 "72" 未说明其构成与校正侧别；我按"18×4、双侧"才复现出 1.61。
- §2.4 的 "20 692 687 background reports" 与源码 `d = N − a − b − c`（20 679 161 / 20 563 022）不是同一个量。
- 稿件 §2.4 说 "All computations used Python 3.13.14"，与运行环境一致（无问题，此点经核查无问题）。

---

## 统计学必改清单（≤7 条）

| # | 事项 | 类别 | 具体动作 |
|---|---|---|---|
| 1 | 稀疏格子改用精确/中位数无偏区间 | **必须补算** | 对全稿 a<5 的格子（ALLODYNIA、逐年 PAIN/HYPERAESTHESIA、加拿大可估计项）改用精确条件或 mid-P 区间；Table 2 的 ALLODYNIA 行给出精确 CI 0.09–19.39，并在 §2.4 写明 Wald 区间在 a<5 时反保守、a=0 时不报告 |
| 2 | 更正 leave-2024-out 口径与结论 | **必须改写** | 将 "leave-2024-out (a = 1, 0.70 [0.10–4.98])" 更正为 "2015–2023 窗口"，或补真正剔除 2024 的 0.94 (0.24–3.77)；删去"signal 消失"的措辞，改为"区间仍包含 4.73，故不具判别力" |
| 3 | 年份分析升级为计数模型 | **必须补算** | 加 Poisson/负二项 GLM：`log E[Y_{dy}] = log R_{dy} + μ + α_d + γ_y + δ_{d×y}`，报告交互 LRT、线性趋势 p，输出列见 M3；据此重写 Table 4B/4C 的"稳定"表述 |
| 4 | `ratio_2024_to_pooled` 补区间或降级 | **必须改写** | 至少给出 delta/自助区间（15.41 [6.01–39.49] 等）并声明分子分母不独立、参照人群不同；在交互检验支持前不得写 "rather than a remifentanil-specific event" |
| 5 | 修正 §2.4 的 d 相消与协方差声明 | **必须改写** | 改为 P1-2 给出的替换句：d 不相消（偏差 <0.6%），忽略的协方差占方差 0.0001%（最高 0.002%），属于保守方向 |
| 6 | 统一多重性框架，重写 Table 2 脚注 | **必须改写 + 可选补算** | 按 P1-4 建立"主终点—固定序列门控—次级 BH-FDR—探索性描述"分层；Table 2 脚注删去"survives Bonferroni = 稳健"的暗示；SOC 面板统一标为描述性（可选：补 BH-FDR 结果作为敏感性） |
| 7 | 加拿大功效与阴性对照概率 | **可选** | 在 §3.3/§4.5 加入功效 0.19%、最小可检出 ROR≈88；在 §3.4 加入 11/12 的单侧二项概率 0.003；说明 523 为反应行的量纲问题 |
