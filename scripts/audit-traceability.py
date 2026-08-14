#!/usr/bin/env python3
"""audit-traceability.py — machine-check that EVERY artifact resolves (the traceability gate).

Performance doctrine, rule "everything resolvable" (AGENTS.md §3.5 #21) applied to the DOC GRAPH:
every .md file (root, docs/, layers/, specs/, migration/) must be referenced by an index doc
(NAVIGATION.md, TRACEABILITY-MAP.md, specs/README.md, migration/README.md, etc.). Orphaned docs =
dangling references = the graph-explosion / lost-work failure mode. This is compute-on-write for docs.

Usage:
  python3 scripts/audit-traceability.py          # report + exit 0/1
  python3 scripts/audit-traceability.py --fix    # print the markdown rows to add (manual copy)
"""
import os, sys, glob, json

ROOT = "/mnt/HC_Volume_106427611/ip-graph"
INDEXES = ["NAVIGATION.md", "TRACEABILITY-MAP.md", "specs/README.md", "migration/README.md",
           "migration/v2/README.md", "LAB-REVIEW.md", "MASTER-KNOWLEDGE-BASE.md", "KERNELS-INDEX.md",
           "HANDOVER.md"]
SCAN_PATTERNS = ["*.md", "docs/*.md", "docs/vision/*.md", "docs/vision/beyond-patala/*.md",
                 "layers/*.md", "migration/*.md", "migration/v2/*.md", "specs/*.md"]

def main():
    blob = "\n".join(open(os.path.join(ROOT, f)).read() for f in INDEXES if os.path.exists(f))
    all_md = set()
    for pat in SCAN_PATTERNS:
        for f in glob.glob(os.path.join(ROOT, pat)):
            all_md.add(os.path.relpath(f, ROOT))
    def traced(f):
        b = os.path.basename(f)
        return (b in blob) or (f in blob)
    untraced = sorted(f for f in all_md if not traced(f))
    print(f"=== TRACEABILITY AUDIT ({len(all_md)} md files, {len(INDEXES)} index docs) ===")
    if untraced:
        print(f"ORPHANED ({len(untraced)}): resolve each in an index doc")
        for f in untraced:
            print(f"  MISSING: {f}")
        # machine form for the --fix path
        if "--fix" in sys.argv:
            print("\n--fix hint: add a row for each to an index doc:")
            for f in untraced:
                print(f"  | `{f}` | resolve to vision+layer |")
        sys.exit(1)
    else:
        print("OK — every .md resolves to an index doc. Nothing orphaned.")
        sys.exit(0)

if __name__ == "__main__":
    main()
