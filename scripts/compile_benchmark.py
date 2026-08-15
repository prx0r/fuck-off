#!/usr/bin/env python3
"""scripts/compile_benchmark.py — compute-on-write projection of the translation-progress registry.

Reads the translation-progress JSONL registry (pipeline/translation_db.py) and writes the BENCHMARK
projection the dashboard reads:
  - web/static/benchmark.json   (what the Astro dashboard page consumes)
  - site/openpatala/benchmark.json (the compiled read-plane, content-addressed, per perf doctrine)

Projection: per-model leaderboard (n, avg_s, avg_calls, avg_raw, avg_c1, avg_quality), per-work progress,
totals. Static bytes, compute-on-write, ETag/304 — the perf doctrine.

Usage:
  python3 scripts/compile_benchmark.py            # write both projections
"""
from __future__ import annotations
import json, os, sys
from pathlib import Path

sys.path.insert(0, "/root/projects/patala/pipeline")
from translation_db import ProgressRegistry

WEB = Path("/root/projects/patala/web/static")
SITE = Path("/mnt/HC_Volume_106427611/ip-graph/site/openpatala")


def build_projection() -> dict:
    pr = ProgressRegistry()
    recs = pr.stream()
    agg_m, agg_w = {}, {}
    for r in recs:
        m = agg_m.setdefault(r["model"], {"n": 0, "s": 0, "mc": 0, "raw": 0, "c1": 0, "q": [], "qs": 0.0})
        m["n"] += 1; m["s"] += r.get("total_s", 0); m["mc"] += r.get("api_calls", 0)
        m["raw"] += r.get("raw_len", 0); m["c1"] += r.get("c1_len", 0)
        q = r.get("quality_score")
        if q is not None:
            m["qs"] += q; m["q"].append(q)
        w = agg_w.setdefault(r["work"], {"n": 0, "s": 0, "c1": 0})
        w["n"] += 1; w["s"] += r.get("total_s", 0); w["c1"] += r.get("c1_len", 0)
    models = []
    for name, m in agg_m.items():
        models.append({
            "model": name, "n": m["n"],
            "avg_s": round(m["s"] / max(1, m["n"]), 1),
            "avg_calls": round(m["mc"] / max(1, m["n"]), 2),
            "avg_raw": round(m["raw"] / max(1, m["n"]), 1),
            "avg_c1": round(m["c1"] / max(1, m["n"]), 1),
            "avg_quality": round(m["qs"] / len(m["q"]), 3) if m["q"] else None,
        })
    models.sort(key=lambda x: (x["avg_quality"] is None, -(x["avg_quality"] or 0)))
    works = [{"work": w, **agg_w[w], "avg_s": round(agg_w[w]["s"] / max(1, agg_w[w]["n"]), 1)}
             for w in agg_w]
    works.sort(key=lambda x: -x["n"])
    # per-layer aggregation (avg time + calls + committed from every verse's layer detail)
    agg_l = {}
    for r in recs:
        for lay in r.get("layers", []):
            L = agg_l.setdefault(lay["layer"], {"n": 0, "s": 0.0, "mc": 0, "c": 0})
            L["n"] += 1; L["s"] += lay.get("time_s", 0); L["mc"] += lay.get("api_calls", 0)
            L["c"] += lay.get("committed", 0)
    layers = [{"layer": k, "n": v["n"], "avg_s": round(v["s"] / max(1, v["n"]), 1),
               "calls": v["mc"], "committed": v["c"]} for k, v in agg_l.items()]
    layers.sort(key=lambda x: -x["avg_s"])
    return {
        "schema": "patala.translation-benchmark.v1",
        "generated": __import__("time").strftime("%Y-%m-%dT%H:%M:%S"),
        "totals": {"n": len(recs),
                   "total_s": round(sum(r.get("total_s", 0) for r in recs), 1),
                   "model_calls": sum(r.get("api_calls", 0) for r in recs),
                   "c1_chars": sum(r.get("c1_len", 0) for r in recs)},
        "models": models,
        "works": works,
        "layers": layers,
    }


def main() -> int:
    proj = build_projection()
    WEB.mkdir(parents=True, exist_ok=True)
    SITE.mkdir(parents=True, exist_ok=True)
    for p in (WEB / "benchmark.json", SITE / "benchmark.json"):
        p.write_text(json.dumps(proj, indent=1, ensure_ascii=False))
        print(f"wrote {p} ({p.stat().st_size} bytes)")
    t = proj["totals"]
    print(f"projection: {t['n']} translations, {t['model_calls']} calls, {len(proj['models'])} models")
    return 0


if __name__ == "__main__":
    sys.exit(main())
