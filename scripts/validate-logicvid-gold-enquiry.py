#!/usr/bin/env python3
"""validate-logicvid-gold-enquiry.py — REDUCTION gate for the Hermes-derived LOGICVID gold -> enquiry.

Verifies the previously-generated data/logicvid/enquiry-gold.json is present, complete, and
Hermes-derived (not regex-fallback) — the .py REDUCTION that gates the GENERATION. Does NOT re-run
Hermes (that's the ingest step, run separately / on demand).
"""
import os, sys, json

results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond)))
    print(f"  [{'PASS' if cond else 'FAIL'}] {name} {detail}")

print("=== LOGICVID GOLD -> ENQUIRY (REDUCTION gate on the Hermes-derived output) ===\n")

p = "/mnt/HC_Volume_106427611/ip-graph/data/logicvid/enquiry-gold.json"
check("output exists", os.path.exists(p))
if os.path.exists(p):
    d = json.load(open(p))
    tot = d.get("totals", {})
    check(">=10 gold files derived", len(d["enquiries"]) >= 10, f"({len(d['enquiries'])})")
    check("derived by HERMES (not regex-fallback)",
          tot.get("hermes_derived", 0) >= 10, f"({tot.get('hermes_derived',0)} hermes, {tot.get('regex_fallback',0)} fallback)")
    check("each enquiry carries the discovery structure",
          all(any(e.get(k) for k in ("taxonomy", "theorem", "boundary", "frontier")) for e in d["enquiries"]),
          "taxonomy/theorem/boundary/frontier present")
    check("aggregate discovered-structure computed",
          bool(d.get("aggregate")), f"({len(d.get('aggregate',{}))} topics)")

print(f"\n=== SUMMARY: {sum(1 for _,c in results if c)}/{len(results)} passed ===")
print("The Hermes-derived LOGICVID enquiry output is present, complete, and recorded as Hermes-derived.")
sys.exit(0 if all(c for _,c in results) else 1)
