#!/usr/bin/env python3
"""scripts/build-dyczkowski-gold.py — key the Dyczkowski Tantrāloka verses into kārikā gold.

Reads the RAW ahnika structured text (site/public/texts-structured/ahnika/NN.txt) and produces a
kārikā-keyed gold JSON: { "ref": "AbhT_<ahnika>.<verse>", "gold": "<the verse's English translation>" }.

Parsing (verified on AbhT 1.52): within an ahnika, a verse's translation ends on a line whose content ends
in `(N)` (e.g. `(vastutā). (52)`). We accumulate the text since the previous verse marker, filter obvious
apparatus (footnotes/references), and key it to AbhT_<ahnika>.<N>. Best-effort — enough kārikā-level gold
(>=300 verses) to score T1/L2 against.

Usage:
    python3 scripts/build-dyczkowski-gold.py --out data/tantraloka/dyczkowski-gold.json
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys

RAW_DIR = "/root/projects/tantraloka/site/public/texts-structured/ahnika"
OUT = "/mnt/HC_Volume_106427611/ip-graph/data/tantraloka/dyczkowski-gold.json"

# apparatus cues: lines that are footnotes/references, not the verse translation
APPARATUS = re.compile(
    r"(see\s|ibid|dyczkowski|jayaratha|k[sS]emar|note\s|below\s|above\s|quoted\s|transliterat|sanskrit\s|"
    r"^\s*[A-Za-z]*\s*\d+/\d+|p\.\s?\d+|f\.\s?f|the\s+vyomavy|abbreviations)", re.I)


def key_ahnika(path: str, ahnika: int) -> dict:
    out: dict[str, str] = {}
    buffer: list[str] = []
    for line in open(path, encoding="utf-8"):
        s = line.strip()
        if not s or s.startswith("----"):
            continue
        m = re.search(r"\((\d{1,3})\)\s*$", s)  # a verse-terminating marker
        if m and buffer:
            num = int(m.group(1))
            verse_lines = [ln for ln in buffer if not APPARATUS.search(ln)]
            gold = re.sub(r"\s+", " ", " ".join(verse_lines)).strip()
            # keep the last line (which carries the tail + marker) and the real verse body
            gold = re.sub(r"\s*\(\d{1,3}\)\s*$", "", gold).strip()
            if len(gold) > 40:  # skip headers/apparatus stubs
                out[f"AbhT_{ahnika}.{num}"] = gold
            buffer = []
            continue
        if s.upper() in ("TANTRĀLOKA", "CHAPTER") or s.upper().startswith("CHAPTER"):
            buffer = []
            continue
        buffer.append(s)
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=OUT)
    a = ap.parse_args()
    gold: dict[str, str] = {}
    for fn in sorted(os.listdir(RAW_DIR)):
        m = re.match(r"(\d+)\.txt$", fn)
        if not m:
            continue
        gold.update(key_ahnika(os.path.join(RAW_DIR, fn), int(m.group(1))))
    os.makedirs(os.path.dirname(a.out), exist_ok=True)
    with open(a.out, "w", encoding="utf-8") as f:
        json.dump({"schema": "dyczkowski-tantraloka-gold.v2", "granularity": "karika",
                   "count": len(gold), "verses": gold}, f, ensure_ascii=False, indent=1)
    print(json.dumps({"gold_verses": len(gold), "has_1.52": "AbhT_1.52" in gold,
                      "sample_refs": sorted(gold)[:3]}, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
