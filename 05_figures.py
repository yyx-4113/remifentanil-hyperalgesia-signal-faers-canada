# -*- coding: utf-8 -*-
"""I 步：生成稿件图（matplotlib, Agg 后端）—— 目标期刊 *Anaesthesia* 规格

规格依据（*Anaesthesia* Guidance for Authors，2026-09-16 核对）：
  - 图件须为**单独文件**，接受 .pdf / .jpg / .tiff / .pptx；**不接受** Word 内嵌。
  - 分辨率：照片 300 ppi；**线条图或线条+照片组合 600 ppi**。本图为纯线条图 → 600 ppi。
  - 单文件 ≤ 10 MB。
  - 图内**不得**有标题、绘图边框、网格线或图例框；符号与误差线在图注中说明。
  - 字体尽量用 Avenir LT Pro；本环境无该字体，改用 **Arial**（同为无衬线、期刊通用）。
  - 版面宽度：双栏 180 mm（7.09 in），单栏 85 mm（3.35 in）。本图信息量较大 → 双栏。

输出（每图 3 种格式，均为单独文件）：
  I_fig1_rorr_forest.{tif,pdf,png}
  I_fig2_year_trend.{tif,pdf,png}
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))

DPI = 600                 # 线条图 600 ppi
W_DOUBLE_IN = 180 / 25.4  # 180 mm 双栏

# 全局样式：无衬线字体、可编辑矢量文本、无网格
plt.rcParams.update({
    "font.family": "sans-serif",
    "font.sans-serif": ["Arial", "DejaVu Sans"],
    "font.size": 8,
    "axes.labelsize": 8,
    "xtick.labelsize": 8,
    "ytick.labelsize": 8,
    "legend.fontsize": 8,
    "axes.linewidth": 0.8,
    "xtick.major.width": 0.8,
    "ytick.major.width": 0.8,
    "xtick.direction": "out",
    "ytick.direction": "out",
    "pdf.fonttype": 42,   # TrueType，保证文字可编辑、字体不乱码
    "ps.fonttype": 42,
    "savefig.bbox": None,  # 用 subplots_adjust 精确控版面，不用 tight（否则物理尺寸不可控）
    "figure.dpi": DPI,
})

C_FEN = "#1f4e9c"   # 深蓝（与红色在灰度下亦可由实心/空心 + 线型区分）
C_MOR = "#b5121b"   # 深红
C_REF = "#333333"

OUT = [
    ("I_fig1_rorr_forest", "tif"),
    ("I_fig1_rorr_forest", "pdf"),
    ("I_fig1_rorr_forest", "png"),
    ("I_fig2_year_trend", "tif"),
    ("I_fig2_year_trend", "pdf"),
    ("I_fig2_year_trend", "png"),
]


def clean_axes(ax, keep=("left", "bottom")):
    """去掉绘图边框（只保留必要的坐标轴脊线），并关闭网格。"""
    for s in ("top", "right", "left", "bottom"):
        ax.spines[s].set_visible(s in keep)
    ax.grid(False)
    ax.set_axisbelow(True)


def save_all(fig, stem):
    for name, ext in OUT:
        if name != stem:
            continue
        path = os.path.join(HERE, f"{name}.{ext}")
        if ext == "tif":
            fig.savefig(path, dpi=DPI, pil_kwargs={"compression": "tiff_lzw"})
        else:
            fig.savefig(path, dpi=DPI)
        print(f"  wrote {os.path.basename(path)}")


# =========================================================================
# Fig 1: 头对头 RORR 森林图（FAERS 主分析）
# =========================================================================
# 取值来源：01_faers_results.csv（逐格读取，勿手改）。
# 分组自上而下：承载 hyperalgesia 概念的 PT 与其最近的可估计姊妹项 /
#              代理项 PAIN / 四个阴性对照 / 特异性探针。
# 不可估计者（HYPERALGESIA 等五个无报告字符串、HYPERPATHIA、
# CHRONIC PAIN SYNDROME 在瑞芬队列 a=0、ALLODYNIA 瑞芬 a=1）不入图，
# 在图注中说明。
# 逐格从 01_faers_results.csv 读取（第二轮评审 P1-4：舒芬太尼头对头此前被计算却不展示）
import csv as _csv

# 入图的顺序与分组；左为 CSV 中的 PT，右为图上标签
SHOWN = [
    ("HYPERAESTHESIA", "HYPERAESTHESIA"),
    ("PROCEDURAL PAIN", "PROCEDURAL PAIN"),
    ("DRUG WITHDRAWAL SYNDROME", "DRUG WITHDRAWAL SYND."),
    ("PAIN", "PAIN"),
    ("NAUSEA", "NAUSEA"),
    ("VOMITING", "VOMITING"),
    ("PRURITUS", "PRURITUS"),
    ("CONSTIPATION", "CONSTIPATION"),
    ("DRUG INEFFECTIVE", "DRUG INEFFECTIVE"),
]
C_SUF = "#1a7f5a"   # 深绿（舒芬太尼，第三组）

def _ci(s):
    s = (s or "").strip()
    if not s:
        return None
    lo, hi = s.replace("\u2013", "-").split("-")
    return float(lo), float(hi)

_src = {r["PT"]: r for r in _csv.DictReader(
    open(os.path.join(HERE, "01_faers_results.csv"), encoding="utf-8-sig"))}

def _triplet(pt, comp):
    r = _src[pt]
    est = r[f"RORR_REMI_vs_{comp}"]
    if est in ("", None):
        return None
    lo, hi = _ci(r[f"RORR_CI_{comp}"])
    return (float(est), lo, hi)

data = [(label, _triplet(pt, "FENTANYL"), _triplet(pt, "SUFENTANIL"),
         _triplet(pt, "MORPHINE")) for pt, label in SHOWN]
for lbl, f, s, m in data:
    if None in (f, s, m):
        raise SystemExit(f"figure 1: {lbl} has a missing comparator value; check the source file")

SERIES = [  # (数据下标, 颜色, 标记, 是否空心, 纵向偏移, 图例名)
    (1, C_FEN, "o", False, +0.30, "Remifentanil vs fentanyl"),
    (2, C_SUF, "^", True,  0.00, "Remifentanil vs sufentanil"),
    (3, C_MOR, "s", True, -0.30, "Remifentanil vs morphine"),
]
ROW = 3  # 每个术语占 3 个单位行距

fig, ax = plt.subplots(figsize=(W_DOUBLE_IN, 6.6))
fig.subplots_adjust(left=0.275, right=0.975, top=0.978, bottom=0.105)

ax.axvline(1.0, color=C_REF, lw=0.9, ls="--", zorder=1)

for i, (pt, _f, _s, _m) in enumerate(data):
    yi = ROW * i
    for idx, col, mk, hollow, off, _lab in SERIES:
        est, lo, hi = data[i][idx]
        ax.errorbar(est, yi + off,
                    xerr=[[est - lo], [hi - est]],
                    fmt=mk, mfc="none" if hollow else col,
                    mec=col, color=col, ecolor=col, elinewidth=0.9,
                    capsize=2.2, capthick=0.9, ms=4.0,
                    mew=0.9 if hollow else 0.0, zorder=3)
    ax.text(-0.012, yi, pt, ha="right", va="center", fontsize=8,
            transform=ax.get_yaxis_transform())

ax.set_yticks([])
ax.set_xscale("log")
ax.set_xlim(0.012, 7.0)
ax.set_ylim(-1.0, ROW * len(data) - 0.4)
ax.set_xticks([0.02, 0.05, 0.1, 0.2, 0.5, 1, 2, 5])
ax.set_xticklabels(["0.02", "0.05", "0.1", "0.2", "0.5", "1", "2", "5"])
ax.set_xlabel("Head-to-head RORR (95% CI), log scale")
clean_axes(ax, keep=("bottom",))

# 图例（无边框）
handles = []
for idx, col, mk, hollow, _off, lab in SERIES:
    handles.append(ax.errorbar([], [], fmt=mk, mfc="none" if hollow else col,
                               mec=col, color=col, ms=4.0, mew=0.9 if hollow else 0.0,
                               label=lab))
ax.legend(handles=handles, loc="upper left", frameon=False,
          handletextpad=0.5, borderaxespad=0.4)
save_all(fig, "I_fig1_rorr_forest")
plt.close(fig)

# =========================================================================
# Fig 2: PAIN 头对头 RORR 年份趋势（FAERS 2015–2024）
# =========================================================================
years = [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]
fen = [(0.093, 0.02, 0.37), (0.039, 0.01, 0.28), (0.051, 0.01, 0.36), None, None,
       (0.044, 0.01, 0.18), (0.014, 0.00, 0.10), (0.016, 0.00, 0.11),
       (0.112, 0.03, 0.45), (0.168, 0.05, 0.53)]
mor = [(0.097, 0.02, 0.39), (0.038, 0.01, 0.27), (0.032, 0.00, 0.23), None, None,
       (0.037, 0.01, 0.15), (0.019, 0.00, 0.14), (0.022, 0.00, 0.16),
       (0.052, 0.01, 0.21), (0.066, 0.02, 0.21)]
overall_fen, overall_mor = 0.066, 0.046

fig, ax = plt.subplots(figsize=(W_DOUBLE_IN, 3.55))
fig.subplots_adjust(left=0.105, right=0.975, top=0.965, bottom=0.195)

xf = [years[i] for i, v in enumerate(fen) if v]
yf = [v[0] for v in fen if v]
lf = [[v[0] - v[1] for v in fen if v], [v[2] - v[0] for v in fen if v]]
xm = [years[i] for i, v in enumerate(mor) if v]
ym = [v[0] for v in mor if v]
lm = [[v[0] - v[1] for v in mor if v], [v[2] - v[0] for v in mor if v]]

ax.axhline(1.0, color=C_REF, ls="--", lw=0.9, zorder=1)
h1 = ax.errorbar(xf, yf, xerr=lf, fmt="o", color=C_FEN, ecolor=C_FEN,
                 elinewidth=0.9, capsize=2.5, capthick=0.9, ms=4.2,
                 label="Remifentanil vs fentanyl", zorder=3)
h2 = ax.errorbar(xm, ym, xerr=lm, fmt="s", mfc="none", mec=C_MOR, color=C_MOR,
                 ecolor=C_MOR, elinewidth=0.9, capsize=2.5, capthick=0.9,
                 ms=4.2, mew=0.9, label="Remifentanil vs morphine", zorder=3)

# 全库总体 RORR 参考线（虚线，图注中说明）
ax.axhline(overall_fen, color=C_FEN, ls=":", lw=0.9, alpha=0.8, zorder=2)
ax.axhline(overall_mor, color=C_MOR, ls=":", lw=0.9, alpha=0.8, zorder=2)

ax.set_yscale("log")
ax.set_ylim(0.008, 2.0)
ax.set_xlim(2014.5, 2024.5)
ax.set_xticks(years)
ax.set_xticklabels([str(y) for y in years])
ax.set_xlabel("Report year")
ax.set_ylabel("RORR for PAIN (95% CI), log scale")
clean_axes(ax, keep=("left", "bottom"))

# 无边框图例（含虚线参考线的说明）
from matplotlib.lines import Line2D
h3 = Line2D([], [], color=C_REF, ls=":", lw=0.9, label="Pooled RORR (whole corpus)")
ax.legend(handles=[h1, h2, h3], loc="lower left", frameon=False,
          handletextpad=0.6, borderaxespad=0.4, ncol=1)
save_all(fig, "I_fig2_year_trend")
plt.close(fig)

print("Figures written (Anaesthesia spec: separate files, line art @ 600 ppi, "
      "no in-figure title / border / grid / legend box):")
print("  I_fig1_rorr_forest.tif | .pdf | .png")
print("  I_fig2_year_trend.tif | .pdf | .png")
