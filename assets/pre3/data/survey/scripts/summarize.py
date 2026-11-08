#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Aggregate the tidy survey_long.csv into summary tables + a JSON payload, then
inject that payload into chart_template.html to produce preliminary_results.html.

Outputs (pre3/data/):
  summary_categorical.csv   frequencies for nominal single + multi-select questions
  summary_scale.csv         distribution (per level) for ordinal/Likert items
  summary_scale_stats.csv   n_valid / mean / median / sd per ordinal/Likert item
  summary_constructs.csv    per-respondent derived variables (adoption status, PU/PEOU/Trust)
  summary_adoption.csv      adoption-status + adoption-funnel counts
  summary.json              the same numbers as JSON (for the d3 page)
And (pre3/):
  preliminary_results.html  self-contained d3.js preview
"""
import csv
import json
import os
import statistics

BASE = os.path.dirname(os.path.abspath(__file__))
LONG = os.path.join(BASE, "survey_long.csv")
TPL = os.path.join(BASE, "chart_template.html")
OUT_HTML = os.path.join(BASE, "..", "preliminary_results.html")

rows = list(csv.DictReader(open(LONG, encoding="utf-8-sig")))

NOMINAL = ["Q1", "Q2", "Q3", "Q4", "Q7", "Q8", "Q9", "Q23"]
ORDINAL = ["Q5", "Q6", "Q10", "Q12", "Q15", "Q17", "Q18a"]
MULTI = ["Q11", "Q14", "Q16", "Q18", "Q20", "Q21"]
MATRIX = ["Q11a", "Q13", "Q18b", "Q19"]

SHORT = {
    "campus": "Campus resources", "within": "In-course content",
    "beyond": "Beyond-course support", "policy": "ADS401 policy",
    "prod": "Coursework production", "other": "Other activity",
    "overall": "Overall preference",
    "pu1": "Helps complete tasks more effectively",
    "pu2": "Helps complete tasks more efficiently",
    "peou1": "Easy to learn how to use",
    "peou2": "Easy to use for ADS401 tasks",
    "trust1": "Usually provides reliable information",
    "trust2": "I generally trust its explanations",
}

# --- per-respondent store ----------------------------------------------------
resp = {}
for r in rows:
    key = (r["survey_language"], r["submission_id"])
    d = resp.setdefault(key, {
        "survey_language": r["survey_language"],
        "submission_id": r["submission_id"],
        "respondent_id": r["respondent_id"],
        "submitted_at": r["submitted_at"],
        "single": {}, "matrix": {}, "multi": {}, "other_text": {},
    })
    qid = r["question_id"]
    rt = r["response_type"]
    if rt in ("single_nominal", "single_ordinal"):
        d["single"][qid] = (r["response"], r["response_code"])
    elif rt in ("matrix_agreement", "matrix_usefulness", "matrix_comparison"):
        d["matrix"][(qid, r["item_id"])] = (r["response"], r["response_code"])
    elif rt == "multi":
        if r["item_id"] == "other_text":
            d["other_text"][qid] = r["response"]
        else:
            d["multi"][(qid, r["item_id"])] = (r["response"], int(r["selected"]))

respondents = list(resp.values())
n_total = len(respondents)

def pct(c, n):
    return round(100.0 * c / n, 1) if n else 0.0

def to_int(s):
    try:
        return int(s)
    except (TypeError, ValueError):
        return None

# =============================================================================
# 1. summary_categorical.csv
# =============================================================================
cat_rows = []
for qid in NOMINAL:
    counts = {}
    for d in respondents:
        if qid in d["single"]:
            lab = d["single"][qid][0]
            counts[lab] = counts.get(lab, 0) + 1
    n = sum(counts.values())
    for lab in sorted(counts, key=lambda k: -counts[k]):
        cat_rows.append(dict(question_id=qid, item_id="", item_text_en="",
                             category=lab, code="", count=counts[lab],
                             pct=pct(counts[lab], n), n=n))

for qid in MULTI:
    labels, sel_counts = {}, {}
    for d in respondents:
        for (q, item), (lab, sel) in d["multi"].items():
            if q == qid:
                labels.setdefault(item, lab)
                sel_counts[item] = sel_counts.get(item, 0) + sel
    n = sum(1 for d in respondents if any(q == qid for q, _ in d["multi"]))
    for item in sorted(labels, key=lambda k: -sel_counts.get(k, 0)):
        cat_rows.append(dict(question_id=qid, item_id=item,
                             item_text_en=SHORT.get(item, labels[item]),
                             category="selected", code="",
                             count=sel_counts.get(item, 0),
                             pct=pct(sel_counts.get(item, 0), n), n=n))

with open(os.path.join(BASE, "summary_categorical.csv"), "w", encoding="utf-8-sig", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["question_id", "item_id", "item_text_en",
                                      "category", "code", "count", "pct", "n"])
    w.writeheader()
    w.writerows(cat_rows)

# =============================================================================
# 2. summary_scale.csv  +  3. summary_scale_stats.csv
# =============================================================================
scale_rows, stats_rows = [], []

def item_rows(qid, item_id, label, entries):
    dist = {}
    for lab, code in entries:
        dist[lab] = dist.get(lab, 0) + 1
    n = sum(dist.values())
    codes = [c for _, c in entries if c is not None]
    n_valid = len(codes)
    n_na = n - n_valid
    code_of = {lab: c for lab, c in entries if c is not None}
    for lab in sorted(dist, key=lambda k: -dist[k]):
        scale_rows.append(dict(question_id=qid, item_id=item_id, item_text_en=label,
                               level=(code_of.get(lab, "")), label_en=lab,
                               count=dist[lab], pct=pct(dist[lab], n), n=n))
    if n_valid:
        mean = round(sum(codes) / n_valid, 2)
        median = round(statistics.median(codes), 2)
        sd = round(statistics.pstdev(codes), 2) if n_valid > 1 else 0.0
    else:
        mean = median = sd = ""
    stats_rows.append(dict(question_id=qid, item_id=item_id, item_text_en=label,
                           n_valid=n_valid, mean=mean, median=median, sd=sd, n_na=n_na))

for qid in ORDINAL:
    entries = []
    for d in respondents:
        if qid in d["single"]:
            lab, code = d["single"][qid]
            entries.append((lab, to_int(code)))
    item_rows(qid, "", "", entries)

for qid in MATRIX:
    labels = {}
    for d in respondents:
        for (q, item), (lab, code) in d["matrix"].items():
            if q == qid:
                labels[item] = lab
    for item in sorted(labels):
        entries = [(d["matrix"][(qid, item)][0], to_int(d["matrix"][(qid, item)][1]))
                   for d in respondents if (qid, item) in d["matrix"]]
        if entries:
            item_rows(qid, item, SHORT.get(item, item), entries)

with open(os.path.join(BASE, "summary_scale.csv"), "w", encoding="utf-8-sig", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["question_id", "item_id", "item_text_en",
                                      "level", "label_en", "count", "pct", "n"])
    w.writeheader()
    w.writerows(scale_rows)

with open(os.path.join(BASE, "summary_scale_stats.csv"), "w", encoding="utf-8-sig", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["question_id", "item_id", "item_text_en",
                                      "n_valid", "mean", "median", "sd", "n_na"])
    w.writeheader()
    w.writerows(stats_rows)

# =============================================================================
# 4. summary_constructs.csv
# =============================================================================
def q13_mean(d, slugs):
    vals = [to_int(d["matrix"][("Q13", s)][1]) for s in slugs
            if ("Q13", s) in d["matrix"] and to_int(d["matrix"][("Q13", s)][1]) is not None]
    return round(sum(vals) / len(vals), 2) if vals else ""

def adoption_status(d):
    q7 = d["single"].get("Q7", ("", ""))[0]
    q8 = d["single"].get("Q8", ("", ""))[0]
    q9 = d["single"].get("Q9", ("", ""))[0]
    q10 = d["single"].get("Q10", ("", ""))[0]
    if q7 == "Had not heard of them":
        return "Unaware"
    if q7 == "Unsure whether known services were XJTLU-provided":
        return "Uncertain (awareness)"
    if q8 == "No":
        return "Aware non-user"
    if q8 == "Not sure":
        return "Uncertain (ever-used)"
    if q9 in ("Both XJTLU AI and External AI", "XJTLU AI only (no External AI)"):
        if q10 == "1–4 times in total (at most once a week on average)":
            return "Occasional user"
        if q10 in ("5–8 times in total (about 1–2 times a week on average)",
                   "9–12 times in total (about 2–3 times a week on average)",
                   "More than 12 times in total (more than 3 times a week on average)"):
            return "Frequent user"
        return "Current user (frequency unknown)"
    if q9 in ("External AI only (no XJTLU AI)", "Neither XJTLU AI nor External AI"):
        return "Ex-user (not current)"
    return "Other"

con_rows = []
for d in respondents:
    con_rows.append(dict(
        survey_language=d["survey_language"], submission_id=d["submission_id"],
        respondent_id=d["respondent_id"], submitted_at=d["submitted_at"],
        q7=d["single"].get("Q7", ("", ""))[0],
        q8=d["single"].get("Q8", ("", ""))[0],
        q9=d["single"].get("Q9", ("", ""))[0],
        q10=d["single"].get("Q10", ("", ""))[0],
        adoption_status=adoption_status(d),
        pu_mean=q13_mean(d, ["pu1", "pu2"]),
        peou_mean=q13_mean(d, ["peou1", "peou2"]),
        trust_mean=q13_mean(d, ["trust1", "trust2"]),
    ))

with open(os.path.join(BASE, "summary_constructs.csv"), "w", encoding="utf-8-sig", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(con_rows[0].keys()))
    w.writeheader()
    w.writerows(con_rows)

# =============================================================================
# 5. summary_adoption.csv  (status + funnel)
# =============================================================================
status_counts = {}
for d in respondents:
    st = adoption_status(d)
    status_counts[st] = status_counts.get(st, 0) + 1
STATUS_ORDER = ["Unaware", "Uncertain (awareness)", "Aware non-user",
                "Uncertain (ever-used)", "Ex-user (not current)",
                "Occasional user", "Current user (frequency unknown)", "Frequent user"]

def heard(d):
    return d["single"].get("Q7", ("", ""))[0] in (
        "Heard of them and knew some functions", "Heard of them but knew little")

def ever_used(d):
    return d["single"].get("Q8", ("", ""))[0] == "Yes"

def used_past4(d):
    return d["single"].get("Q9", ("", ""))[0] in (
        "Both XJTLU AI and External AI", "XJTLU AI only (no External AI)")

def frequent(d):
    return used_past4(d) and d["single"].get("Q10", ("", ""))[0] in (
        "5–8 times in total (about 1–2 times a week on average)",
        "9–12 times in total (about 2–3 times a week on average)",
        "More than 12 times in total (more than 3 times a week on average)")

funnel_def = [
    ("All participants (consented)", lambda d: True),
    ("Heard of XJTLU AI", heard),
    ("Ever used XJTLU AI", ever_used),
    ("Used XJTLU AI in past 4 weeks", used_past4),
    ("Frequent use (5+ times)", frequent),
]
funnel_vals = []
for idx, (stage, fn) in enumerate(funnel_def):
    c = sum(1 for d in respondents if fn(d))
    prev_c = funnel_vals[-1]["count"] if funnel_vals else n_total
    funnel_vals.append(dict(stage=stage, count=c, pct_total=pct(c, n_total),
                            pct_prev=pct(c, prev_c)))

adopt_rows = []
for st in STATUS_ORDER:
    if st in status_counts:
        adopt_rows.append(dict(metric="adoption_status", category=st,
                               count=status_counts[st],
                               pct=pct(status_counts[st], n_total), n=n_total))
for st in sorted(status_counts):
    if st not in STATUS_ORDER:
        adopt_rows.append(dict(metric="adoption_status", category=st,
                               count=status_counts[st],
                               pct=pct(status_counts[st], n_total), n=n_total))
for fv in funnel_vals:
    adopt_rows.append(dict(metric="funnel", category=fv["stage"], count=fv["count"],
                           pct=fv["pct_total"], n=n_total))

with open(os.path.join(BASE, "summary_adoption.csv"), "w", encoding="utf-8-sig", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["metric", "category", "count", "pct", "n"])
    w.writeheader()
    w.writerows(adopt_rows)

# =============================================================================
# JSON payload for the d3 page
# =============================================================================
def single_freq(qid):
    counts = {}
    for d in respondents:
        if qid in d["single"]:
            lab = d["single"][qid][0]
            counts[lab] = counts.get(lab, 0) + 1
    n = sum(counts.values())
    return {"categories": [{"label": k, "count": v, "pct": pct(v, n)}
                           for k, v in sorted(counts.items(), key=lambda x: -x[1])], "n": n}

def multi_freq(qid):
    labels, counts = {}, {}
    for d in respondents:
        for (q, item), (lab, sel) in d["multi"].items():
            if q == qid:
                labels.setdefault(item, lab)
                counts[item] = counts.get(item, 0) + sel
    n = sum(1 for d in respondents if any(q == qid for q, _ in d["multi"]))
    return {"items": [{"item": i, "label": SHORT.get(i, labels[i]),
                       "count": counts.get(i, 0), "pct": pct(counts.get(i, 0), n)}
                      for i in sorted(labels, key=lambda k: -counts.get(k, 0))], "n": n}

def matrix_freq(qid, item, na_key="na", n_levels=5):
    levels, n_na, codes = {}, 0, []
    for d in respondents:
        if (qid, item) in d["matrix"]:
            lab, code = d["matrix"][(qid, item)]
            c = to_int(code)
            if c is not None:
                levels[str(c)] = levels.get(str(c), 0) + 1
                codes.append(c)
            else:
                n_na += 1
    mean = round(sum(codes) / len(codes), 2) if codes else None
    out = {str(k): levels.get(str(k), 0) for k in range(1, n_levels + 1)}
    out[na_key] = n_na
    return {"levels": out, "mean": mean, "n_valid": len(codes)}

q13_items = [("pu1", "Helps complete tasks more effectively"),
             ("pu2", "Helps complete tasks more efficiently"),
             ("peou1", "Easy to learn how to use"),
             ("peou2", "Easy to use for ADS401 tasks"),
             ("trust1", "Usually provides reliable information"),
             ("trust2", "I generally trust its explanations")]
q19_items = [("campus", "Campus resources"), ("within", "In-course content"),
             ("beyond", "Beyond-course support"), ("policy", "ADS401 policy"),
             ("prod", "Coursework production"), ("other", "Other activity"),
             ("overall", "Overall preference")]

def order_multi(mf, order):
    m = {i["item"]: i for i in mf["items"]}
    return [m[a] for a in order if a in m]

q11 = multi_freq("Q11")
q18 = multi_freq("Q18")
act_order = ["campus", "within", "beyond", "policy", "prod"]
q11o = order_multi(q11, act_order)
q18o = order_multi(q18, act_order)

constructs = []
for name, slugs in [("PU", ["pu1", "pu2"]), ("PEOU", ["peou1", "peou2"]),
                    ("Trust", ["trust1", "trust2"])]:
    vals = [q13_mean(d, slugs) for d in respondents]
    vals = [v for v in vals if v != ""]
    constructs.append({"name": name,
                       "mean": round(sum(vals) / len(vals), 2) if vals else None,
                       "n": len(vals)})

payload = {
    "meta": {"n_total": n_total,
             "n_en": sum(1 for d in respondents if d["survey_language"] == "EN"),
             "n_zh": sum(1 for d in respondents if d["survey_language"] == "ZH")},
    "q9": single_freq("Q9"),
    "q7": single_freq("Q7"),
    "q8": single_freq("Q8"),
    "adoption": [dict(state=st, count=status_counts.get(st, 0),
                      pct=pct(status_counts.get(st, 0), n_total))
                 for st in STATUS_ORDER if st in status_counts],
    "funnel": funnel_vals,
    "q11": {"labels": [i["label"] for i in q11o], "xjtu": [i["count"] for i in q11o], "n": q11["n"]},
    "q18": {"labels": [i["label"] for i in q18o], "external": [i["count"] for i in q18o], "n": q18["n"]},
    "q13": [dict(item=i, label=lab, **matrix_freq("Q13", i)) for i, lab in q13_items],
    "q19": [dict(item=i, label=lab, **matrix_freq("Q19", i, na_key="unable", n_levels=3)) for i, lab in q19_items],
    "constructs": constructs,
    "q14": multi_freq("Q14"),
    "q16": multi_freq("Q16"),
    "q20": multi_freq("Q20"),
    "q21": multi_freq("Q21"),
}

with open(os.path.join(BASE, "summary.json"), "w", encoding="utf-8") as f:
    json.dump(payload, f, ensure_ascii=False, indent=2)

tpl = open(TPL, encoding="utf-8").read()
html = tpl.replace("/*__DATA__*/", json.dumps(payload, ensure_ascii=False))
with open(OUT_HTML, "w", encoding="utf-8") as f:
    f.write(html)

print("=== SUMMARY DONE ===")
print("respondents:", n_total, "(EN", payload["meta"]["n_en"], "/ ZH", payload["meta"]["n_zh"], ")")
print("categorical rows:", len(cat_rows), "| scale rows:", len(scale_rows),
      "| stats rows:", len(stats_rows), "| construct rows:", len(con_rows))
print("adoption status:", status_counts)
print("funnel:", [(fv["stage"], fv["count"]) for fv in funnel_vals])
print("HTML ->", OUT_HTML)
