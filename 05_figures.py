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
    # The journal accepts .pdf, .jpg, .tiff or .pptx only, and requires line art at
    # 600 ppi in a separate file, so no .png is written (round-5 revision, T3-13).
    ("I_fig1_rorr_forest", "tif"),
    ("I_fig1_rorr_forest", "pdf"),
    ("I_fig2_year_trend", "tif"),
    ("I_fig2_year_trend", "pdf"),
]


def clean_axes(ax, keep=("left", "bottom")):
    """去掉绘图边框（只保留必要的坐标轴脊线），并关闭网格。"""
    for s in ("top", "right", "left", "bottom"):
        ax.spines[s].set_visible(s in keep)
    ax.grid(False)
    ax.set_axisbelow(True)


def flatten_alpha(path):
    """Matplotlib's TIFF writer emits RGBA whatever the facecolour, and the
    journal asks for opacity in line art (Round-6 A4 issue 3).  Composite onto
    white and rewrite as RGB, keeping the 600 ppi metadata: the manuscript
    checks that dpi, and a figure with an alpha channel can print or convert
    with a black or transparent background."""
    from PIL import Image
    im = Image.open(path)
    if im.mode == "RGB":
        return False
    rgba = im.convert("RGBA")
    flat = Image.new("RGB", rgba.size, (255, 255, 255))
    flat.paste(rgba, mask=rgba.split()[-1])
    flat.save(path, format="TIFF", compression="tiff_lzw",
              dpi=im.info.get("dpi", (DPI, DPI)))
    return True


def save_all(fig, stem):
    for name, ext in OUT:
        if name != stem:
            continue
        path = os.path.join(HERE, f"{name}.{ext}")
        if ext == "tif":
            fig.savefig(path, dpi=DPI, facecolor="white",
                        pil_kwargs={"compression": "tiff_lzw"})
            if flatten_alpha(path):
                print(f"  flattened alpha to opaque RGB: {os.path.basename(path)}")
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
# SHOWN is ordered most-important-first (HYPERAESTHESIA at i = 0). matplotlib puts
# y = 0 at the *bottom*, so without this inversion the figure reads bottom-up and
# contradicts both the panel ordering and the legend. Inverting makes i = 0 the
# top row, which is what the comment above SHOWN has always claimed.
ax.invert_yaxis()
ax.set_xticks([0.02, 0.05, 0.1, 0.2, 0.5, 1, 2, 5])
ax.set_xticklabels(["0.02", "0.05", "0.1", "0.2", "0.5", "1", "2", "5"])
ax.set_xlabel("Head-to-head RORR (95% CI), log scale")
clean_axes(ax, keep=("bottom",))

# 图例已删除（第五轮评审 P0-8：本刊明确要求图内无 legend box；
# 符号说明全部移入图注，见 I_正文_IMRaD_en.md 的 Figure 1 legend）。
save_all(fig, "I_fig1_rorr_forest")
plt.close(fig)

# =========================================================================
# Fig 2: PAIN 头对头 RORR 年份趋势（FAERS 2015–2024）
# =========================================================================
# 取值来源：04_sensitivity_year_pain.csv 与 01_faers_results.csv，逐格在运行期读取。
# 第五轮评审 P4：本图此前把 RORR 与 CI 写成手写常量，与 AI 声明中
# "every reported value is a direct read of the analysis output files" 不符；
# 现改为运行期读取，声明与实物一致。
def _pair(s):
    """'0.02-0.37' -> (0.02, 0.37); '' -> None."""
    s = (s or "").strip().replace("\u2013", "-")
    if not s:
        return None
    lo, hi = s.split("-")
    return (float(lo), float(hi))

with open(os.path.join(HERE, "04_sensitivity_year_pain.csv"), encoding="utf-8-sig") as fh:
    _yr = list(_csv.DictReader(fh))

def _series(comp):
    out = []
    for r in _yr:
        est = (r["RORR_REMI_vs_%s" % comp] or "").strip()
        ci = _pair(r["RORR_CI_%s" % comp])
        if not est or ci is None:
            continue
        out.append((int(r["Year"]), float(est), ci[0], ci[1]))
    return out

_ser_fen = _series("FENTANYL")
_ser_mor = _series("MORPHINE")
years = [int(r["Year"]) for r in _yr]
overall_fen = float(_src["PAIN"]["RORR_REMI_vs_FENTANYL"])
overall_mor = float(_src["PAIN"]["RORR_REMI_vs_MORPHINE"])

fig, ax = plt.subplots(figsize=(W_DOUBLE_IN, 3.55))
fig.subplots_adjust(left=0.105, right=0.975, top=0.965, bottom=0.195)

xf = [v[0] for v in _ser_fen]
yf = [v[1] for v in _ser_fen]
lf = [[v[1] - v[2] for v in _ser_fen], [v[3] - v[1] for v in _ser_fen]]
xm = [v[0] for v in _ser_mor]
ym = [v[1] for v in _ser_mor]
lm = [[v[1] - v[2] for v in _ser_mor], [v[3] - v[1] for v in _ser_mor]]

ax.axhline(1.0, color=C_REF, ls="--", lw=0.9, zorder=1)
ax.errorbar(xf, yf, xerr=lf, fmt="o", color=C_FEN, ecolor=C_FEN,
            elinewidth=0.9, capsize=2.5, capthick=0.9, ms=4.2, zorder=3)
ax.errorbar(xm, ym, xerr=lm, fmt="s", mfc="none", mec=C_MOR, color=C_MOR,
            ecolor=C_MOR, elinewidth=0.9, capsize=2.5, capthick=0.9,
            ms=4.2, mew=0.9, zorder=3)

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

# 图例已删除（第五轮评审 P0-8）：符号说明在图注中。
save_all(fig, "I_fig2_year_trend")
plt.close(fig)

print("Figures written (Anaesthesia spec: separate files, line art @ 600 ppi, "
      "no in-figure title / border / grid / legend box):")
print("  I_fig1_rorr_forest.tif | .pdf")
print("  I_fig2_year_trend.tif | .pdf")
