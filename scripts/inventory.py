#!/usr/bin/env python3
"""Inventory informationphilosopher corpus: categorize files by section + quality."""
import os, re, json, html as htmllib
from collections import Counter, defaultdict

ROOT = "/mnt/HC_Volume_106427611/CX-Train/informationphilosopher/www.informationphilosopher.com"

ERROR_MARKERS = ["Bad Request", "skybuilders", "Apache/2.4", "afrispa", "server could not understand",
                 "Your browser sent a request"]

def is_error_html(text):
    hits = sum(1 for m in ERROR_MARKERS if m.lower() in text.lower())
    return hits >= 1

def real_h1(text):
    m = re.search(r"<h1[^>]*>(.*?)</h1>", text, re.S)
    if not m: return None
    t = htmllib.unescape(re.sub(r"<[^>]+>", "", m.group(1))).strip()
    return t if len(t) >= 5 and "Bad Request" not in t else None

def body_text(text):
    m = re.search(r'<div class="bodycontent"[^>]*>(.*?)</div>', text, re.S)
    b = m.group(1) if m else text
    b = re.sub(r"<script.*?</script>", "", b, flags=re.S)
    b = re.sub(r"<style.*?</style>", "", b, flags=re.S)
    b = re.sub(r"<[^>]+>", " ", b)
    b = htmllib.unescape(b)
    b = re.sub(r"\s+", " ", b).strip()
    return b

def section_of(relpath):
    parts = relpath.split("/")
    return parts[0] if parts else "?"

stats = {"html_total": 0, "html_error": 0, "html_real": 0, "pdf_total": 0,
         "pdf_size": 0, "img_total": 0, "other_total": 0}
section_html = defaultdict(lambda: {"real": 0, "error": 0})
section_pdf = defaultdict(lambda: {"count": 0, "size": 0})
real_pages = []

for dirpath, dirnames, filenames in os.walk(ROOT):
    for fn in filenames:
        fp = os.path.join(dirpath, fn)
        rel = os.path.relpath(fp, ROOT)
        ext = os.path.splitext(fn)[1].lower()
        if ext == ".html" or fn.endswith(".html"):
            stats["html_total"] += 1
            try:
                text = open(fp, encoding="utf-8", errors="ignore").read()
            except Exception:
                continue
            sec = section_of(rel)
            if is_error_html(text):
                stats["html_error"] += 1
                section_html[sec]["error"] += 1
            else:
                title = real_h1(text)
                bt = len(body_text(text))
                stats["html_real"] += 1
                section_html[sec]["real"] += 1
                real_pages.append({"path": rel, "title": title, "body_len": bt, "section": sec})
        elif ext == ".pdf":
            stats["pdf_total"] += 1
            sz = os.path.getsize(fp)
            stats["pdf_size"] += sz
            section_pdf[section_of(rel)]["count"] += 1
            section_pdf[section_of(rel)]["size"] += sz
        elif ext in (".jpg", ".jpeg", ".png", ".gif", ".svg"):
            stats["img_total"] += 1
        else:
            stats["other_total"] += 1

print("=== TOTALS ===")
for k, v in stats.items():
    print(f"  {k}: {v if not isinstance(v,int) or 'size' not in k else v} "
          f"({'%.1fMB'%(v/1048576) if 'size' in k else ''})")

print("\n=== HTML BY SECTION ===")
for sec, c in sorted(section_html.items(), key=lambda x: -x[1]["real"]):
    if c["real"] or c["error"]:
        print(f"  {sec:20s} real={c['real']:4d} error={c['error']:5d}")

print("\n=== PDF BY SECTION ===")
for sec, c in sorted(section_pdf.items(), key=lambda x: -x[1]["size"]):
    print(f"  {sec:20s} count={c['count']:4d} size={'%.1fMB'%(c['size']/1048576):>8s}")

print("\n=== SAMPLE REAL PAGES (first 20) ===")
for p in sorted(real_pages, key=lambda x: -x["body_len"])[:20]:
    print(f"  [{p['section']:12s}] body={p['body_len']:6d}  {p['path']}  | {p['title']}")

out = {"stats": stats, "real_pages": real_pages}
with open("/tmp/opencode/ip_inventory.json", "w") as f:
    json.dump(out, f, indent=1)
print("\nsaved /tmp/opencode/ip_inventory.json")
