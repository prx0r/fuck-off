#!/usr/bin/env python3
"""Move the 26 true HTML error pages out of the active corpus into 02_extracted_md/_errors/.
Also drop them from corpus.jsonl so the machine corpus is clean.
"""
import os, re, glob, json, shutil

MD_ROOT = "/mnt/HC_Volume_106427611/ip-graph/data/extracted_md"
JSONL = "/mnt/HC_Volume_106427611/ip-graph/data/corpus.jsonl"
ERR_DIR = os.path.join(MD_ROOT, "_errors")

ERROR_PATTERNS = [
    r"Multiple Choices",
    r"could not be found on this server",
    r"Your browser sent a request that this server could not understand",
    r"The document name you requested",
    r"Available documents:",
    r"Apache/2\.4",
    r"skybuilders",
]
def is_error_page(text):
    hits = [p for p in ERROR_PATTERNS if re.search(p, text, re.I)]
    if len(hits) >= 2: return True
    if re.search(r"could not be found|could not understand|does not exist on this server", text, re.I) \
       and len(text) < 3000: return True
    return False

os.makedirs(ERR_DIR, exist_ok=True)
moved = []
for f in glob.glob(os.path.join(MD_ROOT, "**", "*.md"), recursive=True):
    if "_errors" in f: continue
    if is_error_page(open(f, encoding="utf-8", errors="ignore").read()):
        rel = os.path.relpath(f, MD_ROOT)
        dest = os.path.join(ERR_DIR, os.path.basename(f))
        shutil.move(f, dest)
        moved.append(rel)

# rebuild corpus.jsonl excluding the error docs (match by docname)
moved_basenames = set(os.path.splitext(os.path.basename(m))[0] for m in moved)
records = []
with open(JSONL) as f:
    for line in f:
        r = json.loads(line)
        if r["docname"] not in moved_basenames:
            records.append(r)

with open(JSONL, "w") as f:
    for r in records:
        f.write(json.dumps(r) + "\n")

print(f"moved {len(moved)} error pages to _errors/")
print(f"corpus.jsonl now: {len(records)} clean records ({os.path.getsize(JSONL)/1048576:.1f}MB)")
print("active md files:", len(glob.glob(os.path.join(MD_ROOT, "**", "*.md"), recursive=True)) - len(glob.glob(os.path.join(ERR_DIR, "*.md"))))
