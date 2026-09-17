# 专家修改意见书（第四轮 · Major Revision）

**对象稿件：** `I_正文_IMRaD_en.md`（v1.3.0，*Anaesthesia* Original Article）
**依据：** `REVIEW_round4_2026-09-17.md`（重新编排专家阵容、不带前三轮预设结论，结论 Major Revision）
**性质：** 本文件只给**可落地的修改意见**，不改动稿件。每条均附具体行号、拟改措辞或需补做的分析。
**门禁现状：** 一致性 422/0、字数 4000/297、docx 61/0 全绿——但门禁只认证算术，不认证研究设计，本轮 Major 项恰是门禁抓不到的一类。

---

## 0. 两个需要您拍板的决策点（先决）

| 决策 | 选项 A | 选项 B | 专家建议 |
|---|---|---|---|
| **M1 框架** | 保留 Original Article，把"主分析无结果、信号为事后"写进方法学声明 | 降级为 **Commentary / Correspondence**，以"术语学警示"为唯一卖点 | 若 M1/M2 落实，**A 可成立**；核心贡献（a-priori 阴性对照 + 特异性探针 + 双库框架）对 OIH 文献确有增量 |
| **M3 栏目** | 维持 Original Article（同上） | 转投 *Anaesthesia* 的 Commentary 或 *Regional Anesthesia & Pain Medicine* / *Therap Adv Drug Saf* 的方法学短文 | 取决于 M1 落地的诚实度；若标题仍暗示"确认信号"，**必须转 B** |

> 下面 M1/M2 的改写意见默认您选 A；若选 B，则 §1/§5/标题需进一步压缩为"警示"基调，但数据层改动一致。

---

## 1. M1 — 主分析未产生结果，阳性信号是事后补入的

**问题本质：** 预设的原发性超敏术语（HYPERALGESIA、ALLODYNIA）全部不可解读（非 PT / n=1）。唯一瑞芬太尼阳性信号（HYPERAESTHESIA ROR 4.73）来自"看到零之后"补入的代理 PT。标题与摘要把"a priori 阴性对照"作为诚信锚点，却未同等披露**超敏主结局是事后 rescued**。

**具体改写（方法学声明，§2.3 / §3.1 附近，建议新增一段）：**

> *Proposed.* "The two prespecified hyperalgesia outcomes were non-estimable: HYPERALGESIA is a lowest-level term (parent preferred term HYPERAESTHESIA) and returned zero by construction, and ALLODYNIA yielded a single remifentanil report (n = 1), below the signal threshold. No prespecified hyperalgesia term therefore produced a result. The analysis became hypothesis-generating; the five dictionary proxies were introduced by dated Amendment 1 (16 September 2026) after the zeros were observed and are reported as exploratory, not as confirmatory outcomes."

**标题修改（去掉会误导的 a-priori 暗示，或显式诚实）：**
- 候选 1（保留 Original Article）：`Remifentanil and hyperalgesia reporting in two pharmacovigilance databases: a head-to-head disproportionality study with a terminology caution`
- 候选 2（最诚实）：`What a clinical name misses: a two-database pharmacovigilance caution on remifentanil and opioid-induced hyperalgesia`
- 避免：继续用 "with negative controls defined a priori" 作为标题卖点——它真实（对照确为 a priori），却掩盖主结局的事后性（评审已两次点名）。

**摘要 Results 同步：** 在 "remifentanil included (4.73, 95% CI 2.54–8.80)" 后补："**added a posteriori as a dictionary proxy after the prespecified terms returned structurally uninterpretable zeros**"。

---

## 2. M2 — 信号几乎完全由 2024 单年簇驱动（硬结论，必须补做并改写）

**数据事实（已核验 `04_sensitivity_year_hyperaesthesia.csv`）：**
- 瑞芬太尼 HYPERAESTHESIA 共 **a=10**：2024 年 **8 例**、2021 年 **1 例**、**1 例无可用日期**；2015–2020、2022–2023 共 8 个年份 **a=0**。
- **2024 年是唯一方向翻转的年份**：当年 RORR vs 芬太尼 = **2.495 (1.06–5.90)**、vs 吗啡 = **3.495 (1.52–8.05)**——即该年瑞芬太尼**过度**报告 HYPERAESTHESIA，与其余所有术语"低报"的模式相反；而 2021 年（唯一另一年有计数）RORR vs 芬 = 0.511 (<1)。
- **leave-2024-out 实测：** 去掉 2024 后瑞芬 a = 2（2021:1 + 无日期:1），**低于信号阈值 a≥3，信号消失**。

**必须补做的分析（落到新产物，进 §3.8 + 表 4C 脚注 + 门禁）：**
1. **Leave-2024-out 敏感性**：重算瑞芬 HYPERAESTHESIA 排除 2024 后的 a/ROR/是否达信号——预期 a=2、不达标。产物 `04_sensitivity_leave2024_hyperaesthesia.csv`，并在 §9 溯源表补一行。
2. **2024 簇调查（brief）**：核查 2024 是否伴随 (a) MedDRA 版本切换、(b) 某篇高引文献/标签事件、(c) 其他阿片在 2024 是否同步激增。若仅瑞芬 2024 激增，提示报告簇而非药理；若多药同步，提示编码/监测年效应。无论结论如何，须在 §4.5 或 §3.8 写 2–3 句。
3. **年度异质性陈述**：在摘要与 §4.4 明示"the pooled estimate (4.73) is driven by a single-year cluster; excluding 2024 leaves two reports and no signal"。

**具体改写（摘要 Results 末尾 / §3.3 / §5）：**
> *Proposed §3.3.* "Eight of the ten remifentanil HYPERAESTHESIA reports fall in 2024, where remifentanil's reporting odds ratio ratio exceeded 1 against both comparators (2.50 versus fentanyl, 3.50 versus morphine); the only other estimable year (2021, n = 1) was below 1. Excluding 2024 leaves two reports and no signal, so the pooled estimate reflects a single-year cluster rather than a stable across-time finding."

> *Proposed §5.* 将 "Remifentanil's signal is the weakest of the four, rests on ten reports, eight of them in a single year" 强化为："**rests on ten reports, eight concentrated in 2024, where the direction reverses; excluding that year leaves no estimable signal**"。

---

## 3. M3 — 期刊契合度

若 M1/M2 按上落实（信号降级为探索性、披露事后性与单年脆弱性），Original Article 可成立——因为 a-priori 阴性对照 + 特异性探针 + 双库方向复现的方法学框架对 OIH 文献有真实增量，且结论"术语选择决定答案"本身是一条可发表的警示。

若您**不愿**在标题/框架上做 M1 的诚实化，则信号式叙事与"无法下结论"的临床结论不匹配，应转 **Commentary / Letter**（*Anaesthesia* 或 *RA & PM*）。评审未强制，但给出此岔路以免返修循环。

---

## 4. P1 — 四项框架性措辞

**P1-1 零值/信号的认知不对称。** 稿件把临床名零值正确判为"非安全证据"，却把代理信号当作"信号"头条。建议两端同标准：HYPERAESTHESIA 信号在摘要与 §4.4 一律加 "exploratory / fragile / 2024-driven" 限定，不再作为正面发现头条。

**P1-2 "weakest-of-four" 双刃。** §4.4 与 §5 的"瑞芬最弱"可被读作"更少超敏"（安慰）或"低报假象"（ artefact）。建议明确归因为低报：*"its lowest of the four RORs is most parsimoniously explained by the same under-reporting that affects every other term, not by a genuinely lower hyperalgesia burden"*。

**P1-3 计数驱动的选择偏差。** 5 个代理因 5 个字符串为零而补入，属数据驱动选择，可能抬高信号。建议 §2.3/§4.5 加一句局限：*"the proxies are not independent confirmations of the prespecified strings; they share the same corpora and were selected because the originals returned zero, so they cannot be counted as separate evidence."*

**P1-4 特异性探针过度解读。** DRUG INEFFECTIVE 跨库方向反转被解为"术语特异性低报"，但反转同样可能源自库间差异。建议 §4.4 改为：*"the probe's reversal is consistent with term-specific reporting but is also compatible with database differences, so it narrows rather than settles the interpretation."*

---

## 5. P2 — 四项细修

| 项 | 位置 | 修正 |
|---|---|---|
| P2-1（真实 bug） | §9 L540 | 溯源表该行末尾多一个 `\| \|`：`...hyperaesthesia.csv` \| \|` → 删掉尾随空管，改为 `\| 04_sensitivity_year_hyperaesthesia.csv \|` |
| P2-2（已核验无需改） | §9 L534 | `01_faers_summary.md` §2/§8 确含不可检索性论述，**保留**，勿误改 |
| P2-3 | 摘要 Methods | "the proxies were added after the zeros and dated in the plan" 已诚实，但 Results 头条代理信号未带该限定——见 M1/M2 同步 |
| P2-4（建议增） | §1 或 §5 开头 | 加一句期望管理：*"This study makes no clinical safety claim and issues no prevention recommendation; it examines how reporting responds to term choice."* |

---

## 6. 优先级执行清单（建议顺序）

1. **[M2] 跑 `04_sensitivity_leave2024_hyperaesthesia.csv`** + 2024 簇 brief 调查 → 落 §3.8/§4.4/§5 + §9 溯源行 + 门禁 G-10（leave-2024-out 断言）+ 字数回填。
2. **[M1] 方法学声明段 + 标题候选 + 摘要 Results 同步** → 门禁加"声明须含 a posteriori / 2024-driven"字符串断言。
3. **[P1-1~4]** 四处措辞收敛（同标准对待零值与信号）。
4. **[P2-1]** 修 §9 L540 尾随管；**[P2-4]** 加期望管理句。
5. 三道门禁重跑 + 重建 docx + 写 `RESPONSE_round4` + commit/tag v1.4.0 + SSH 推送。

> 门禁纪律提醒：任何"信号消失/2024 驱动"的新论断，必须同时写进产物 CSV、稿件、§9 溯源表与一致性门禁断言，避免再次"绿码放行矛盾"（参见 G-9 教训）。

---

*本意见书由重新编排的专家阵容（方法学 / 生物统计 / 药物警戒 / 临床麻醉 / 期刊契合 / 溯源审计）独立给出，未带入前三轮 Minor Revision 预设。*
