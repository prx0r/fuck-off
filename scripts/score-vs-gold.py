#!/usr/bin/env python3
"""scripts/score-vs-gold.py — score committed translation output against kārikā-level gold.

Closes the anti-theatre loop: for each gold verse, find the committed T1/L2 for that passage, concatenate
the output, and score agreement via TranslationVariant (mean pairwise Jaccard, 0..1). Honest — it reports
how many passages matched + the score for the matched ones (a passage that can't be mapped is not a silent
0; it's reported as unmatched).

Usage:
    python3 scripts/score-vs-gold.py --work kramasadbhava            # kramasadbhava gold_records vs committed T1
    python3 scripts/score-vs-gold.py --work tantraloka --gold dyczkowski   # Dyczkowski gold vs committed T1
"""
from __future__ import annotations

import argparse
import glob
import json
import os
import re
import sys

PATALA = "/root/projects/patala"
GOLD_RECORDS = f"{PATALA}/pipeline/gold_records"
DYCZKOWSKI = "/mnt/HC_Volume_106427611/ip-graph/data/tantraloka/dyczkowski-gold.json"


def _tokens(text) -> set[str]:
    if isinstance(text, (dict, list)):
        text = json.dumps(text, ensure_ascii=False)
    return set(re.findall(r"[a-zA-Zāīūṛṝḷḹṃñṅśṣṭḍḥṁṇ]+", (text or "").lower()))


def _jaccard(a, b) -> float:
    if not a and not b:
        return 1.0
    u = a | b
    if not u:
        return 0.0
    return round(len(a & b) / len(u), 3)


def load_gold(kind: str) -> list[dict]:
    if kind == "dyczkowski":
        d = json.load(open(DYCZKOWSKI))
        return [{"verse": v, "gold": g} for v, g in d["verses"].items()]
    # default: kramasadbhava gold_records
    out = []
    for f in glob.glob(f"{GOLD_RECORDS}/*.json"):
        d = json.load(open(f))
        st = d.get("stages", {})
        g = (st.get("T1") or {}).get("close_translation", "") or (st.get("T2") or {}).get("close_translation", "")
        loc = d.get("location", {})
        out.append({"verse": f"{loc.get('chapter','')}.{loc.get('verse','')}", "gold": g,
                    "passage": d.get("passage_id")})
    return out


def committed_t1(work: str) -> dict[str, str]:
    """Committed T1 for a work: {object_id -> concatenated gloss}. Streamed (low-RAM)."""
    sys.path.insert(0, f"{PATALA}/pipeline")
    import object_registry as R
    out = {}
    for oid in R.committed_ids("T1"):
        if not oid.startswith(work + ":"):
            continue
        cur = R.current("T1", oid)
        if not cur:
            continue
        p = cur.get("payload") or {}
        t = p.get("t1") or {}
        glosses = " ".join((x.get("gloss") or "") for x in (t.get("tokens") or []))
        out[oid] = glosses
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--work", default="kramasadbhava")
    ap.add_argument("--gold", default="kramasadbhava", help="kramasadbhava | dyczkowski")
    a = ap.parse_args()
    gold = load_gold(a.gold)
    committed = committed_t1(a.work)
    scores, matched, unmatched = [], 0, []
    for g in gold:
        # best-effort map: a committed object whose id contains the verse number
        num = str(g["verse"]).split(".")[-1]
        cand = ""
        for oid, gloss in committed.items():
            if oid.endswith(":" + num) or num in oid.rsplit(":", 1)[-1]:
                cand = gloss
                break
        if not cand:
            unmatched.append(g["verse"])
            continue
        matched += 1
        s = _jaccard(_tokens(g["gold"]), _tokens(cand))
        scores.append(s)
    mean = round(sum(scores) / len(scores), 3) if scores else None
    print(json.dumps({
        "work": a.work, "gold": a.gold, "gold_verses": len(gold),
        "committed_T1": len(committed), "matched": matched, "unmatched": len(unmatched),
        "unmatched_sample": unmatched[:10], "mean_jaccard": mean, "scores": scores[:20],
        "note": "score is Jaccard agreement of the matched passages; unmatched are not a silent 0",
    }, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    sys.exit(main())
