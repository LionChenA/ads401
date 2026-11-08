#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Inferential / significance analysis on the tidy survey_long.csv, merged with the
descriptive summary, then injected into results2_template.html -> results-2.html.

Computes (all EXPLORATORY given n≈27):
  * Wilson 95% CI for key proportions (funnel, adoption, Q9, Q11/Q18 categories)
  * Spearman correlation matrix: PU / PEOU / Trust / Q12 / Q15  (current users)
  * Spearman: AI experience (Q6) vs adoption rank (all)
  * Paired Wilcoxon signed-rank: Q11a vs Q18b usefulness (per activity, "Both" users)
  * Sign test (binomial): Q19 direction per dimension
  * Mann-Whitney U: AI experience, current users vs others
"""
import csv
import json
import math
import os

BASE = os.path.dirname(os.path.abspath(__file__))
LONG = os.path.join(BASE, "survey_long.csv")
SUM = os.path.join(BASE, "summary.json")
TPL = os.path.join(BASE, "results2_template.html")
OUT_HTML = os.path.join(BASE, "..", "results-2.html")

# ---------------- math helpers ---------------------------------------------
def norm_cdf(z):
    t = 1.0 / (1.0 + 0.2316419 * abs(z))
    d = 0.3989422804014327 * math.exp(-z * z / 2.0)
    p = d * t * ((((1.330274429 * t - 1.821255978) * t + 1.781477937) * t - 0.356563782) * t + 0.319381530)
    return 1.0 - p if z >= 0 else p

def _betacf(a, b, x):
    ITMAX, EPS, FPMIN = 200, 3e-7, 1e-30
    qab, qap, qam = a + b, a + 1.0, a - 1.0
    c = 1.0
    d = 1.0 - qab * x / qap
    if abs(d) < FPMIN: d = FPMIN
    d = 1.0 / d
    h = d
    for m in range(1, ITMAX + 1):
        m2 = 2 * m
        aa = m * (b - m) * x / ((qam + m2) * (a + m2))
        d = 1.0 + aa * d
        if abs(d) < FPMIN: d = FPMIN
        c = 1.0 + aa / c
        if abs(c) < FPMIN: c = FPMIN
        d = 1.0 / d
        h *= d * c
        aa = -(a + m) * (qab + m) * x / ((a + m2) * (qap + m2))
        d = 1.0 + aa * d
        if abs(d) < FPMIN: d = FPMIN
        c = 1.0 + aa / c
        if abs(c) < FPMIN: c = FPMIN
        d = 1.0 / d
        delta = d * c
        h *= delta
        if abs(delta - 1.0) < EPS:
            break
    return h

def betai(a, b, x):
    if x <= 0: return 0.0
    if x >= 1: return 1.0
    bt = math.exp(math.lgamma(a + b) - math.lgamma(a) - math.lgamma(b)
                  + a * math.log(x) + b * math.log(1 - x))
    if x < (a + 1) / (a + b + 2):
        return bt * _betacf(a, b, x) / a
    return 1.0 - bt * _betacf(b, a, 1 - x) / b

def t_two_sided_p(t, df):
    if df <= 0:
        return 1.0
    return betai(df / 2.0, 0.5, df / (df + t * t))

def rankdata(vals):
    n = len(vals)
    order = sorted(range(n), key=lambda i: vals[i])
    ranks = [0.0] * n
    i = 0
    while i < n:
        j = i
        while j + 1 < n and vals[order[j + 1]] == vals[order[i]]:
            j += 1
        avg = (i + 1 + j + 1) / 2.0
        for k in range(i, j + 1):
            ranks[order[k]] = avg
        i = j + 1
    return ranks

def wilson(count, n, z=1.96):
    if n <= 0:
        return (0.0, 0.0)
    p = count / n
    denom = 1 + z * z / n
    center = (p + z * z / (2 * n)) / denom
    half = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / denom
    return (max(0.0, center - half), min(1.0, center + half))

def wilcoxon_signed_rank(diffs):
    n = len(diffs)
    if n == 0:
        return None
    absd = [abs(d) for d in diffs]
    ranks = rankdata(absd)
    Wp = sum(ranks[i] for i in range(n) if diffs[i] > 0)
    Wn = sum(ranks[i] for i in range(n) if diffs[i] < 0)
    W = min(Wp, Wn)
    mean = n * (n + 1) / 4.0
    # tie correction for variance
    from collections import Counter
    tcounts = Counter(absd)
    tie_corr = sum((t ** 3 - t) for t in tcounts.values()) / 48.0
    var = n * (n + 1) * (2 * n + 1) / 24.0 - tie_corr
    if var <= 0:
        var = 1e-9
    z = (W - mean) / math.sqrt(var)
    p = 2 * (1 - norm_cdf(abs(z)))
    r = z / math.sqrt(n)
    return {"n": n, "W+": round(Wp, 2), "W-": round(Wn, 2), "W": round(W, 2),
            "z": round(z, 3), "p": round(p, 4), "r": round(r, 3)}

def spearman(x, y):
    n = len(x)
    if n < 3:
        return None
    rx, ry = rankdata(x), rankdata(y)
    mx, my = sum(rx) / n, sum(ry) / n
    cov = sum((rx[i] - mx) * (ry[i] - my) for i in range(n))
    sx = math.sqrt(sum((rx[i] - mx) ** 2 for i in range(n)))
    sy = math.sqrt(sum((ry[i] - my) ** 2 for i in range(n)))
    if sx == 0 or sy == 0:
        return None
    r = cov / (sx * sy)
    r = max(-1.0, min(1.0, r))
    if abs(r) >= 1.0:
        p = 0.0
        t = float("inf") if r > 0 else float("-inf")
    else:
        t = r * math.sqrt((n - 2) / (1 - r * r))
        p = t_two_sided_p(abs(t), n - 2)
    return {"r": round(r, 3), "p": round(p, 4), "n": n, "t": round(t, 3)}

def sign_test(xjtu, ext):
    n = xjtu + ext
    if n == 0:
        return None
    m = max(xjtu, ext)
    tail = sum(math.comb(n, k) for k in range(m, n + 1)) * (0.5 ** n)
    p = min(1.0, 2 * tail)
    return {"n": n, "xjtu": xjtu, "ext": ext, "p": round(p, 4)}

def mann_whitney(x, y):
    nx, ny = len(x), len(y)
    if nx == 0 or ny == 0:
        return None
    allv = x + y
    ranks = rankdata(allv)
    Rx = sum(ranks[:nx])
    Ux = Rx - nx * (nx + 1) / 2.0
    U = min(Ux, nx * ny - Ux)
    mean = nx * ny / 2.0
    var = nx * ny * (nx + ny + 1) / 12.0
    if var <= 0:
        var = 1e-9
    z = (U - mean) / math.sqrt(var)
    p = 2 * (1 - norm_cdf(abs(z)))
    r = z / math.sqrt(nx + ny)
    return {"U": round(U, 2), "z": round(z, 3), "p": round(p, 4),
            "r": round(r, 3), "n1": nx, "n2": ny}

# ---------------- load tidy data -------------------------------------------
rows = list(csv.DictReader(open(LONG, encoding="utf-8-sig")))

def to_int(s):
    try:
        return int(s)
    except (TypeError, ValueError):
        return None

resp = {}
for r in rows:
    key = (r["survey_language"], r["submission_id"])
    d = resp.setdefault(key, {"single": {}, "matrix": {}, "multi": {}})
    qid, rt = r["question_id"], r["response_type"]
    if rt in ("single_nominal", "single_ordinal"):
        d["single"][qid] = (r["response"], r["response_code"])
    elif rt in ("matrix_agreement", "matrix_usefulness", "matrix_comparison"):
        d["matrix"][(qid, r["item_id"])] = (r["response"], r["response_code"])
    elif rt == "multi":
        if r["item_id"] == "other_text":
            continue
        d["multi"][(qid, r["item_id"])] = (r["response"], int(r["selected"]))

respondents = list(resp.values())
n_total = len(respondents)

def code(d, qid, item=None):
    if item is None:
        v = d["single"].get(qid)
        return to_int(v[1]) if v else None
    v = d["matrix"].get((qid, item))
    return to_int(v[1]) if v else None

def label(d, qid):
    v = d["single"].get(qid)
    return v[0] if v else ""

def q9_is_current(d):
    return label(d, "Q9") in ("Both XJTLU AI and External AI", "XJTLU AI only (no External AI)")

# ---------------- descriptive (from summary.json) --------------------------
summary = json.load(open(SUM, encoding="utf-8"))

def add_ci_prop(obj):
    for it in obj:
        lo, hi = wilson(it["count"], it["n"])
        it["ci_lo"] = round(lo * 100, 1)
        it["ci_hi"] = round(hi * 100, 1)
    return obj

# funnel CI
funnel = summary["funnel"]
for f in funnel:
    lo, hi = wilson(f["count"], n_total)
    f["ci_lo"] = round(lo * 100, 1)
    f["ci_hi"] = round(hi * 100, 1)

# q9 CI
for c in summary["q9"]["categories"]:
    lo, hi = wilson(c["count"], summary["q9"]["n"])
    c["ci_lo"] = round(lo * 100, 1)
    c["ci_hi"] = round(hi * 100, 1)

# q11 / q18 category CI
for key in ("q11", "q18"):
    items = summary[key]
    out = {"labels": items["labels"], "n": items["n"]}
    for k in ("xjtu", "external"):
        if k in items:
            out[k] = [{"count": c, "pct": round(100.0 * c / items["n"], 1),
                       "ci_lo": round(wilson(c, items["n"])[0] * 100, 1),
                       "ci_hi": round(wilson(c, items["n"])[1] * 100, 1)}
                      for c in items[k]]
    summary[key] = out

# adoption CI
for a in summary["adoption"]:
    lo, hi = wilson(a["count"], n_total)
    a["ci_lo"] = round(lo * 100, 1)
    a["ci_hi"] = round(hi * 100, 1)

# ---------------- derived variables ----------------------------------------
ACT = ["campus", "within", "beyond", "policy", "prod"]
ACT_LABEL = {"campus": "Campus resources", "within": "In-course content",
             "beyond": "Beyond-course support", "policy": "ADS401 policy",
             "prod": "Coursework production"}

def construct_mean(d, slugs):
    vals = [code(d, "Q13", s) for s in slugs if code(d, "Q13", s) is not None]
    return sum(vals) / len(vals) if vals else None

def adoption_rank(d):
    q7, q8, q9, q10 = label(d, "Q7"), label(d, "Q8"), label(d, "Q9"), label(d, "Q10")
    if q7 == "Had not heard of them":
        return 0
    if q8 == "No":
        return 1
    if q9 in ("External AI only (no XJTLU AI)", "Neither XJTLU AI nor External AI"):
        return 2
    if q9 in ("Both XJTLU AI and External AI", "XJTLU AI only (no External AI)"):
        if q10 == "1–4 times in total (at most once a week on average)":
            return 3
        if q10 in ("5–8 times in total (about 1–2 times a week on average)",
                   "9–12 times in total (about 2–3 times a week on average)",
                   "More than 12 times in total (more than 3 times a week on average)"):
            return 4
        return 3
    return None

# ---------------- inferential results --------------------------------------
# 1) Spearman correlation matrix (current users)
cur = [d for d in respondents if q9_is_current(d)]
VARS = [("PU", lambda d: construct_mean(d, ["pu1", "pu2"])),
        ("PEOU", lambda d: construct_mean(d, ["peou1", "peou2"])),
        ("Trust", lambda d: construct_mean(d, ["trust1", "trust2"])),
        ("Verif(Q12)", lambda d: code(d, "Q12")),
        ("Continue(Q15)", lambda d: code(d, "Q15"))]
labels = [v[0] for v in VARS]
Rmat = [[None] * len(VARS) for _ in VARS]
Pmat = [[None] * len(VARS) for _ in VARS]
Nmat = [[None] * len(VARS) for _ in VARS]
for i in range(len(VARS)):
    for j in range(len(VARS)):
        if i == j:
            Rmat[i][j], Pmat[i][j], Nmat[i][j] = 1.0, None, None
            continue
        xs, ys = [], []
        for d in cur:
            a = VARS[i][1](d); b = VARS[j][1](d)
            if a is not None and b is not None:
                xs.append(a); ys.append(b)
        res = spearman(xs, ys)
        if res:
            Rmat[i][j], Pmat[i][j], Nmat[i][j] = res["r"], res["p"], res["n"]
corr = {"labels": labels, "r": Rmat, "p": Pmat, "n": Nmat}

# 2) Q6 vs adoption rank (all)
q6 = [code(d, "Q6") for d in respondents]
adr = [adoption_rank(d) for d in respondents]
pairs = [(a, b) for a, b in zip(q6, adr) if a is not None and b is not None]
q6_adr = spearman([a for a, b in pairs], [b for a, b in pairs])

# 3) Paired Wilcoxon Q11a vs Q18b (per activity, Both users)
both = [d for d in respondents if label(d, "Q9") == "Both XJTLU AI and External AI"]
paired = []
for c in ACT:
    diffs, xs, ys = [], [], []
    for d in both:
        a = code(d, "Q11a", c); b = code(d, "Q18b", c)
        if a is not None and b is not None:
            diffs.append(a - b); xs.append(a); ys.append(b)
    w = wilcoxon_signed_rank([x for x in diffs if x != 0])
    entry = {"category": c, "label": ACT_LABEL[c], "n_pairs": len(xs),
             "mean_xjtu": round(sum(xs) / len(xs), 2) if xs else None,
             "mean_ext": round(sum(ys) / len(ys), 2) if ys else None,
             "median_diff": round(sorted(diffs)[len(diffs) // 2], 2) if diffs else None}
    if w:
        entry.update(w)
        entry["sig"] = w["p"] < 0.05
    paired.append(entry)

# 4) Sign test Q19 per dimension
q19_items = [("campus", "Campus resources"), ("within", "In-course content"),
             ("beyond", "Beyond-course support"), ("policy", "ADS401 policy"),
             ("prod", "Coursework production"), ("other", "Other activity"),
             ("overall", "Overall preference")]
sign_q19 = []
for it, lab in q19_items:
    xjtu = sum(1 for d in both if code(d, "Q19", it) == 1)
    same = sum(1 for d in both if code(d, "Q19", it) == 2)
    ext = sum(1 for d in both if code(d, "Q19", it) == 3)
    unable = sum(1 for d in both if code(d, "Q19", it) is None and (("Q19", it) in d["matrix"]))
    st = sign_test(xjtu, ext)
    sign_q19.append({"dimension": it, "label": lab, "xjtu": xjtu, "same": same,
                     "ext": ext, "unable": unable,
                     "p": st["p"] if st else None, "n": (st["n"] if st else 0),
                     "sig": (st["p"] < 0.05) if st else False})

# 5) Mann-Whitney: Q6 experience, current users vs others
cur_q6 = [code(d, "Q6") for d in respondents if q9_is_current(d) and code(d, "Q6") is not None]
oth_q6 = [code(d, "Q6") for d in respondents if (not q9_is_current(d)) and code(d, "Q6") is not None]
mw = mann_whitney(cur_q6, oth_q6)

# ---------------- assemble tests table -------------------------------------
tests = []

def fmt_p(p):
    if p is None:
        return "—"
    return f"{p:.3f}" if p >= 0.001 else "<0.001"

# correlations -> table rows (upper triangle, off-diagonal)
for i in range(len(VARS)):
    for j in range(i + 1, len(VARS)):
        r, p, n = Rmat[i][j], Pmat[i][j], Nmat[i][j]
        if r is None:
            continue
        tests.append({"id": f"corr_{i}_{j}", "test": "Spearman ρ",
                      "comparison": f"{labels[i]} × {labels[j]}",
                      "n": n, "statistic": f"ρ={r:.3f}",
                      "p": p, "effect": "rho", "effect_size": r,
                      "sig": p < 0.05,
                      "note": "当前用户（n 见左）"})

if q6_adr:
    tests.append({"id": "q6_adr", "test": "Spearman ρ",
                  "comparison": "AI 经验(Q6) × 采纳等级",
                  "n": q6_adr["n"], "statistic": f"ρ={q6_adr['r']:.3f}",
                  "p": q6_adr["p"], "effect": "rho", "effect_size": q6_adr["r"],
                  "sig": q6_adr["p"] < 0.05, "note": "全体受访者"})

for e in paired:
    if e.get("p") is not None:
        tests.append({"id": f"pair_{e['category']}", "test": "Wilcoxon 配对",
                      "comparison": f"Q11a vs Q18b · {e['label']}",
                      "n": e["n"], "statistic": f"W={e['W']}, z={e['z']}",
                      "p": e["p"], "effect": "r", "effect_size": e["r"],
                      "sig": e["p"] < 0.05, "note": "仅「两者都用」者"})

for s in sign_q19:
    if s["p"] is not None:
        tests.append({"id": f"sign_{s['dimension']}", "test": "符号检验（二项）",
                      "comparison": f"Q19 · {s['label']}",
                      "n": s["n"], "statistic": f"西浦={s['xjtu']} vs 外部={s['ext']}",
                      "p": s["p"], "effect": "方向", "effect_size": (s["xjtu"] - s["ext"]),
                      "sig": s["p"] < 0.05, "note": "忽略「差不多/无法比较」"})

if mw:
    tests.append({"id": "mw_q6", "test": "Mann-Whitney U",
                  "comparison": "AI 经验(Q6) · 当前用户 vs 其他",
                  "n": f"{mw['n1']}+{mw['n2']}", "statistic": f"U={mw['U']}, z={mw['z']}",
                  "p": mw["p"], "effect": "r", "effect_size": mw["r"],
                  "sig": mw["p"] < 0.05, "note": "秩和检验"})

payload = dict(summary)
payload["paired"] = paired
payload["sign_q19"] = sign_q19
payload["corr"] = corr
payload["q6_adr"] = q6_adr
payload["q6_adr_scatter"] = [{"q6": a, "adr": b} for a, b in pairs]
payload["tests"] = tests
payload["n_sig"] = sum(1 for t in tests if t["sig"])

with open(os.path.join(BASE, "results.json"), "w", encoding="utf-8") as f:
    json.dump(payload, f, ensure_ascii=False, indent=2)

tpl = open(TPL, encoding="utf-8").read()
html = tpl.replace("/*__DATA__*/", json.dumps(payload, ensure_ascii=False))
with open(OUT_HTML, "w", encoding="utf-8") as f:
    f.write(html)

print("=== ANALYSIS DONE ===")
print("n_total:", n_total, "| current users:", len(cur), "| both:", len(both))
print("corr labels:", labels)
for i in range(len(labels)):
    for j in range(i + 1, len(labels)):
        if Rmat[i][j] is not None:
            print(f"  ρ({labels[i]}, {labels[j]}) = {Rmat[i][j]}, p={Pmat[i][j]}, n={Nmat[i][j]}")
print("Q6 × adoption rank:", q6_adr)
print("paired:")
for e in paired:
    print(f"  {e['label']}: n={e['n_pairs']}, meanX={e['mean_xjtu']}, meanE={e['mean_ext']}, p={e.get('p')}, r={e.get('r')}")
print("sign_q19:")
for s in sign_q19:
    print(f"  {s['label']}: xjtu={s['xjtu']}, ext={s['ext']}, p={s['p']}")
print("MWU Q6:", mw)
print("n significant tests (p<.05):", payload["n_sig"])
print("HTML ->", OUT_HTML)
