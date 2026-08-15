#!/usr/bin/env python3
"""scripts/compile-translation-status.py — LIGHTWEIGHT compile-on-commit for the translation projection.

Rebuilds ONLY site/openpatala/translation.json (per-work translation status) from the live ledger +
registries — fast, streaming, low-RAM. This is the compile-on-commit step: run it after a factory commit
so the served projection is live (no whole-site rebuild).

Usage:
    python3 scripts/compile-translation-status.py [--out PATH]

Writes the SAME shape as build-static-site.compile_translation_status (the Atlas API reads it unchanged).
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys

# the ip-graph site dir (same default the Atlas API reads)
OUT = os.environ.get("OUT", "/mnt/HC_Volume_106427611/ip-graph/site/openpatala")
PATALA = "/root/projects/patala"


def sha(b): return hashlib.sha256(b.encode() if isinstance(b, str) else b).hexdigest()[:16]


def compile(out: str) -> dict:
    sys.path.insert(0, os.path.join(PATALA, "pipeline"))
    import object_registry as R

    ledger_path = os.path.join(PATALA, "data/corpus/downloads/translation-state-ledger.json")
    layers = ["T1", "ARGMAP", "L0", "L2", "L200", "C1"]

    # streamed per-work committed counts
    counts: dict[str, dict] = {}
    for layer in layers:
        for oid in R.committed_ids(layer):
            wid = oid.split(":", 1)[0]
            d = counts.setdefault(wid, {})
            d[layer] = d.get(layer, 0) + 1

    works = []
    if os.path.exists(ledger_path):
        with open(ledger_path, encoding="utf-8") as f:
            ledger = json.load(f)
        for wid, rec in (ledger.get("works") or {}).items():
            tr = rec.get("translation") or {}
            na = rec.get("next_action") or {}
            works.append({"work_id": wid,
                          "t1": tr.get("t1", "UNKNOWN"),
                          "l2": tr.get("l2", "UNKNOWN"),
                          "c1": tr.get("c1", "UNKNOWN"),
                          "next_action": na.get("action", ""),
                          "eligible_for_agent3": bool(na.get("eligible_for_agent3")),
                          "committed": counts.get(wid, {})})
    works.sort(key=lambda w: w["work_id"])
    proj = {"generated": True, "count": len(works), "surface": "translation-status", "works": works}

    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "translation.json"), "w", encoding="utf-8") as f:
        json.dump(proj, f, ensure_ascii=False, indent=1)

    # also write the sha for the registry manifest (content-address)
    with open(os.path.join(out, "translation.sha256"), "w") as f:
        f.write(sha(json.dumps({"layer": "TRANSLATION", "count": len(works)})))
    return proj


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=OUT)
    a = ap.parse_args()
    proj = compile(a.out)
    print(json.dumps({"compiled": True, "count": proj["count"], "out": os.path.join(a.out, "translation.json")}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
