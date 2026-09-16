# -*- coding: utf-8 -*-
"""03 D: 27 SOC 全景（openFDA 聚合层，复用氯胺酮 soc_rules v4）— 稳健版

改动说明（相对初版）：
  * 进度写入 03_soc_run.log（每条 flush），避免管道缓冲盲区；后台运行可读日志监控。
  * 全局 top-1000 查询省略空 search 参数（openFDA 不接受 search= 空串）。
  * 收紧退避：tries=5，退避 5+i*3 秒；count 端点实测可用（HTTP 200 ~1-5s）。
  * 缓存复用：N 与四药分母已在 _faers_cache.json（302 键），仅 5 次真实调用。

方法、局限见文件头初版注释；本版仅加固执行层。
"""
import urllib.request, urllib.parse, json, time, os, csv, sys
from soc_rules import SOC_RULES, SOC_LIST, NSOC, map_soc
from _fda_auth import add_key, get_key

BASE = "https://api.fda.gov/drug/event.json"
HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(HERE, "_faers_cache.json")
LOG = os.path.join(HERE, "03_soc_run.log")
cache = json.load(open(CACHE, encoding="utf-8")) if os.path.exists(CACHE) else {}

logf = open(LOG, "w", encoding="utf-8")
def log(*a):
    s = " ".join(str(x) for x in a)
    print(s, flush=True)
    logf.write(s + "\n"); logf.flush()

def save():
    json.dump(cache, open(CACHE, "w", encoding="utf-8"))

def build_url(search, count=None, limit=None, no_search=False):
    params = {}
    if not no_search and search:
        params["search"] = search
    if count:
        params["count"] = count
    if limit:
        params["limit"] = str(limit)
    params = add_key(params)   # 若配置 OPENFDA_API_KEY / openfda_key.txt，则加入 api_key
    return f"{BASE}?{urllib.parse.urlencode(params)}"

def api_count_top(search, limit=1000, tries=8, no_search=False):
    key = f"__TOP__{search}__{limit}"
    if key in cache and cache[key]:
        log(f"  [cache] TOP {search[:40]} len={len(cache[key])}")
        return cache[key]
    q = build_url(search, "patient.reaction.reactionmeddrapt.exact", limit, no_search)
    for i in range(tries):
        try:
            with urllib.request.urlopen(q, timeout=60) as r:
                res = json.load(r).get("results", [])
            cache[key] = res; save()
            log(f"  [ok] TOP {search[:40]} len={len(res)} ({i+1}次)")
            time.sleep(12.0); return res   # 错峰：成功后再等 12s，规避突发限流
        except urllib.error.HTTPError as e:
            body = ""
            try:
                body = e.read().decode("utf-8", "ignore")
            except Exception:
                pass
            # count 端点的 API_KEY_MISSING 是"要 key"而非限流，重试无益 → 立刻中止
            if "API_KEY_MISSING" in body:
                log("  [!] count 返回 API_KEY_MISSING → 立即中止（非限流，重试无用）")
                return []
            if e.code in (403, 429):
                log(f"  [{e.code}] count 退避{i+1} 等{30+i*20}s"); time.sleep(30 + i*20); continue
            log("count err", e.code, body[:100]); return []
        except Exception as e:
            log("count err", e); time.sleep(5)
    cache[key] = []; save(); return []

def api_total(search, tries=5):
    if search in cache and cache[search] is not None:
        return cache[search]
    q = build_url(search, None, "1")
    for i in range(tries):
        try:
            with urllib.request.urlopen(q, timeout=30) as r:
                t = json.load(r).get("meta", {}).get("results", {}).get("total", 0)
            cache[search] = t; save()
            log(f"  [ok] TOTAL {search[:40]} = {t}")
            time.sleep(0.6); return t
        except urllib.error.HTTPError as e:
            if e.code == 404:
                cache[search] = 0; save(); return 0
            if e.code in (403, 429):
                time.sleep(5 + i*3); continue
            time.sleep(3)
        except Exception:
            time.sleep(3)
    cache[search] = None; save(); return None

DRUGS = {
 "REMIFENTANIL":'patient.drug.activesubstance.activesubstancename.exact:("REMIFENTANIL" "REMIFENTANIL HYDROCHLORIDE")',
 "FENTANYL":'patient.drug.activesubstance.activesubstancename.exact:("FENTANYL")',
 "SUFENTANIL":'patient.drug.activesubstance.activesubstancename.exact:("SUFENTANIL" "SUFENTANIL CITRATE")',
 "MORPHINE":'patient.drug.activesubstance.activesubstancename.exact:("MORPHINE")',
}

log("=== 03 SOC 开始 ===", time.strftime("%H:%M:%S"))
_k = get_key()
log("API key:", (f"已配置(掩码 {_k[:6]}…{_k[-4:]})" if _k else "未配置 → count 端点可能报 API_KEY_MISSING"))
N = api_total('patient.reaction.reactionmeddrapt:[* TO *]')
log("N(全库 reaction) =", N)
drug_tot = {k: api_total(v) for k, v in DRUGS.items()}
log("drug_tot:", drug_tot)

soc_reports = {name: [0] * NSOC for name in DRUGS}
soc_npt = {name: [0] * NSOC for name in DRUGS}
cov = {}
unmapped_top = {name: [] for name in DRUGS}
for name, s in DRUGS.items():
    log(f"-- 取 {name} top-1000 --")
    top = api_count_top(s, 500)
    s_total = drug_tot[name]
    mapped = 0; tot = 0; unm = {}
    for x in top:
        pt = x["term"]; c = x["count"]; tot += c
        soc = map_soc(pt)
        if soc is None:
            unm[pt] = c; continue
        si = SOC_LIST.index(soc)
        soc_reports[name][si] += c
        soc_npt[name][si] += 1
        mapped += c
    cov[name] = round(100 * mapped / tot, 1) if tot else 0
    unmapped_top[name] = sorted(unm.items(), key=lambda kv: -kv[1])[:10]
    log(f"  {name}: events={tot}, mapped={mapped}, map_cov={cov[name]}%")
    log(f"    unmapped_top={unmapped_top[name][:3]}")

log("-- 取 全局 top-500 (no_search) --")
time.sleep(12.0)
glob = api_count_top("", 500, no_search=True)
soc_all = [0] * NSOC
glob_mapped = 0; glob_total = sum(x["count"] for x in glob) if glob else 0
for x in glob:
    soc = map_soc(x["term"])
    if soc:
        soc_all[SOC_LIST.index(soc)] += x["count"]; glob_mapped += x["count"]
log(f"全局: total_events={glob_total}, mapped={glob_mapped}, "
    f"map_cov={(100*glob_mapped/glob_total if glob_total else 0):.1f}%")

def soc_ror(name, si):
    a = soc_reports[name][si]; dn = drug_tot[name]; c = soc_all[si]
    if None in (a, dn, c, N):
        return None
    b = dn - a; d = N - c
    if min(a, b, c, d) <= 0:
        return None
    return (a * d) / (b * c)

log("\n== 27 SOC 全景 ==")
rows = []
for si in range(NSOC):
    soc = SOC_LIST[si]
    row = {"SOC": soc}
    for name in DRUGS:
        a = soc_reports[name][si]
        row[f"{name}_reports"] = a
        row[f"{name}_pct"] = round(100 * a / drug_tot[name], 2) if drug_tot[name] else 0
    r_remi = soc_ror("REMIFENTANIL", si)
    row["REMI_ROR"] = round(r_remi, 3) if r_remi else ""
    for comp in ["FENTANYL", "MORPHINE"]:
        r_c = soc_ror(comp, si)
        if r_remi and r_c:
            row[f"RORR_REMI_vs_{comp}"] = round(r_remi / r_c, 3)
        else:
            row[f"RORR_REMI_vs_{comp}"] = ""
    rows.append(row)
    log(f"  {soc:45s} REMI_rep={soc_reports['REMIFENTANIL'][si]:>6} "
        f"({100*soc_reports['REMIFENTANIL'][si]/drug_tot['REMIFENTANIL']:.1f}%) "
        f"ROR={r_remi}  RORR_FEN={row.get('RORR_REMI_vs_FENTANYL','')} RORR_MOR={row.get('RORR_REMI_vs_MORPHINE','')}")

out = os.path.join(HERE, "03_soc_27.csv")
with open(out, "w", newline="", encoding="utf-8-sig") as f:
    w = csv.writer(f)
    w.writerow(["## 27 SOC 全景（openFDA 聚合层 · **事件级近似**）"])
    w.writerow(["## 方法：各药取 count 端点 top-500 PT → 本地 soc_rules v4 映射到 27 SOC"])
    w.writerow(["## 警告：本表为事件级（PT 计数之和），同一报告含多个同 SOC 的 PT 会被重复计数；"])
    w.writerow(["##       报告级原生 SOC 以 Canada Vigilance 表（cv/cv_soc_27.csv）为准，本表仅作定性互证。"])
    w.writerow(["## 免 key 说明：count+search 在 limit=500 可免 key；limit=1000 报 API_KEY_MISSING。"])
    w.writerow(["N_total_reactions", N])
    w.writerow(["Drug", "Total_reports", "Top500_PT_mapping_coverage%"])
    for name in DRUGS:
        w.writerow([name, drug_tot[name], cov[name]])
    w.writerow(["Global_top500_mapping_coverage%",
                round(100 * glob_mapped / glob_total, 1) if glob_total else ""])
    w.writerow([])
    w.writerow(["SOC"] + [f"{n}_reports" for n in DRUGS] + [f"{n}_pct" for n in DRUGS]
               + ["REMI_ROR", "RORR_vs_FEN", "RORR_vs_MOR"])
    for row in rows:
        w.writerow([row["SOC"]] + [row[f"{n}_reports"] for n in DRUGS]
                   + [row[f"{n}_pct"] for n in DRUGS]
                   + [row.get("REMI_ROR", ""), row.get("RORR_REMI_vs_FENTANYL", ""), row.get("RORR_REMI_vs_MORPHINE", "")])
    w.writerow([])
    w.writerow(["Unmapped_top_REMI"] + [f"{pt}:{c}" for pt, c in unmapped_top["REMIFENTANIL"][:10]])
    w.writerow(["Unmapped_top_FEN"] + [f"{pt}:{c}" for pt, c in unmapped_top["FENTANYL"][:10]])
    w.writerow(["Unmapped_top_MOR"] + [f"{pt}:{c}" for pt, c in unmapped_top["MORPHINE"][:10]])
log("\n写出:", out, "完成")
logf.close()
