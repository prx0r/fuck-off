#!/usr/bin/env python3
"""ingest-tantraloka-root.py — ingest the Sanskrit Tantrāloka root into the organism (P0 Mona Lisa).

Reads the GRETIL Sanskrit root (gretil_tantraloka.txt, the Kashmir Series 1918-38 edition via
Takashima) and produces a clean, machine-readable L0 ingestion: verse-by-verse kārikās with stable
`AbhT_x.y` references. This is the SOURCE + TOKENIZATION stage of the canonical Tantrāloka test.

Output:
  data/tantraloka/
    root-verses.json   every kārikā {ref, ahnika, text} from the Sanskrit root
    ahnika-1.json      the flagship āhnika (upāyas: reflexivity, the three means, recognition)
  The verses are the source of truth for TranslationProof (we translate from THIS, not Dyczkowski).

The Dyczkowski vols (vol{1..11}) are the VALIDATION reference for the later three-version comparison.
"""
import os, sys, json, re

ROOT = "/mnt/HC_Volume_106427611/ip-graph"
SRC = "/root/projects/tantraloka/texts-original/gretil_tantraloka.txt"
OUT = f"{ROOT}/data/tantraloka"

def main():
    os.makedirs(OUT, exist_ok=True)
    text = open(SRC).read()

    # split into lines, find the kārikā verses (AbhT_x.y references)
    verses = []
    # a verse line ends with a numeral reference like "AbhT_1.1" or "<num> AbhT_1.1"
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        m = re.search(r"AbhT_(\d+)\.(\d+)\s*$", line)
        if not m:
            continue
        ahnika, vno = int(m.group(1)), int(m.group(2))
        # the verse text is everything before the trailing ref number + AbhT_ ref
        body = re.sub(r"\s*\d*\s*AbhT_\d+\.\d+\s*$", "", line).strip()
        if body:
            verses.append({"ref": f"AbhT_{ahnika}.{vno}", "ahnika": ahnika, "verse": vno, "text": body})

    # dedupe by ref (GRETIL has some overlap with the commentary)
    seen = {}
    for v in verses:
        seen.setdefault(v["ref"], v)
    verses = [seen[k] for k in sorted(seen, key=lambda r: tuple(int(x) for x in re.findall(r"\d+", r)))]

    with open(f"{OUT}/root-verses.json", "w") as f:
        json.dump({"source": SRC, "count": len(verses), "verses": verses}, f, ensure_ascii=False, indent=1)

    # the flagship āhnika 1 (upāyas) for the from-scratch translation
    a1 = [v for v in verses if v["ahnika"] == 1]
    with open(f"{OUT}/ahnika-1.json", "w") as f:
        json.dump({"source": SRC, "count": len(a1), "verses": a1}, f, ensure_ascii=False, indent=1)

    print(f"=== TANTRĀLOKA ROOT INGESTED ===")
    print(f"  source: {SRC}")
    print(f"  total root kārikās: {len(verses)}")
    print(f"  āhnika 1 (upāyas): {len(a1)}")
    print(f"  sample verses:")
    for v in verses[:4]:
        print(f"    {v['ref']}: {v['text'][:60]}")

if __name__ == "__main__":
    main()
