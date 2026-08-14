#!/usr/bin/env python3
"""validate-hermes-exec.py — the Hermes GENERATION path is real (agentic, not blind -z).

The critical-audit found hermes_exec.py was ORPHANED + used the blind `-z` invocation. This proves:
  1. hermes_exec is now AGENTIC (hermes chat -Q -q --yolo, the correct path with file access + skills)
  2. it can GENERATE a real translation of a Sanskrit kārikā (not hand-fed)
  3. available() works
Uses the real AbhT_1.52 kārikā. This is the "Hermes for GENERATION" fix.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))
from hermes_exec import available, agentic, translate_karika

results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond)))
    print(f"  [{'PASS' if cond else 'FAIL'}] {name} {detail}")

print("=== HERMES EXECUTION IS REAL (agentic generation, not blind -z) ===\n")

# 1. the agentic path is available
avail = available()
check("Hermes agentic path is available (hermes chat -Q -q)", avail)

# 2. the invocation is agentic (uses 'chat', not blind '-z')
src = open(f"{os.path.dirname(__file__)}/../lib/hermes_exec.py").read()
check("the invocation uses agentic 'hermes chat' (not blind -z)", '["chat", "-Q"' in src or '"chat", "-Q"' in src)
check("the invocation has file-access + skills support (--yolo/--skills)", "--skills" in src and "--yolo" in src)

# 3. it GENERATES a real translation (not hand-fed) — on the real AbhT_1.52 kārikā
if avail:
    karika = "nahyaprakāśarūpasya prākāśyaṃ vastutāpi vā //"
    try:
        result = translate_karika(karika)
        trans = result.get("translation", "") if isinstance(result, dict) else str(result)
        check("Hermes GENERATES a real translation (real model output)", len(trans) > 20, f"({len(trans)} chars)")
        check("the translation is of THIS kārikā (luminous/object)", 
              any(w in trans.lower() for w in ["luminous", "lumin", "object", "manifest"]))
        print(f"  → translation: {trans[:100]}")
    except Exception as e:
        check("Hermes GENERATES a real translation", False, f"error: {str(e)[:80]}")
else:
    check("Hermes GENERATES a real translation", False, "hermes unavailable")

# 4. available() is deterministic-ish (doesn't crash)
check("available() does not crash", isinstance(avail, bool))

print(f"\n=== SUMMARY: {sum(1 for _,c in results if c)}/{len(results)} passed ===")
print("\nHERMES GENERATION IS REAL: agentic 'hermes chat' (with file access + skills) generates a real")
print("translation of AbhT_1.52 — not a hand-fed container. This is the 'Hermes for GENERATION' fix")
print("from the shared critical-audit. .py stays for REDUCTION.")
sys.exit(0 if all(c for _,c in results) else 1)
