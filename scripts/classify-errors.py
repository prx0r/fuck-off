#!/usr/bin/env python3
"""Classify extracted md files: flag TRUE boilerplate error pages (vs false positives).

A page is a real error page if the error marker dominates its content (is the body),
not just mentioned once in a citation/link.
"""
import os, re, glob

MD_ROOT = "/mnt/HC_Volume_106427611/ip-graph/data/extracted_md"

# Error pages have these as the MAJORITY of a SHORT body
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
    # must be short-ish (error pages are) and contain 2+ distinct error markers
    hits = [p for p in ERROR_PATTERNS if re.search(p, text, re.I)]
    if len(hits) >= 2:
        return True
    # or a single dominant marker with 'could not be found' phrasing
    if re.search(r"could not be found|could not understand|does not exist on this server", text, re.I) \
       and len(text) < 3000:
        return True
    return False

flagged = []
for f in glob.glob(os.path.join(MD_ROOT, "**", "*.md"), recursive=True):
    text = open(f, encoding="utf-8", errors="ignore").read()
    if is_error_page(text):
        flagged.append(f)

print(f"=== TRUE ERROR PAGES: {len(flagged)} ===")
for f in sorted(flagged):
    rel = os.path.relpath(f, MD_ROOT)
    print("  ", rel)
