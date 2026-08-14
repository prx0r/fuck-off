#!/usr/bin/env python3
"""validate-pushing-miner.py — wire the LOGICVID pushing sessions into the organism (crux compass).

The audit's #1 unused asset: the 35 pushing-tantraloka sessions (deep human LOGICVID crux analysis) were
never read. This mines them into structured cruxes + claims grounded in kārikās, so the deep human work
feeds the argument/crux/education layers. Real data, read from disk.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))
from pushing_miner import PushingMiner

ROOT = "/mnt/HC_Volume_106427611/ip-graph"
PUSHING = "/root/projects/research-library/recognition/pushing-tantraloka"
results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond)))
    print(f"  [{'PASS' if cond else 'FAIL'}] {name} {detail}")

print("=== WIRE THE PUSHING SESSIONS (the crux compass, finally read) ===\n")

m = PushingMiner()
# confirm the sessions exist on disk
n_sessions = len([f for f in os.listdir(PUSHING) if f.endswith(".md")])
check("the pushing sessions exist (real human LOGICVID analysis)", n_sessions >= 30, f"({n_sessions} files)")

summary = m.mine_dir(PUSHING)
check("mined the sessions (cruxes + claims + objections extracted)", summary["sessions"] == n_sessions)
check("mined cruxes (the tensions)", summary["cruxes"] > 0, f"({summary['cruxes']})")
check("mined claims (the text's argued positions)", summary["claims"] > 0, f"({summary['claims']})")
check("grounded in real kārikā refs (TĀ 1/52-55 reflexivity)", "TĀ 1/52" in summary["karikas"])

# the Q1 reflexivity session specifically → the flagship crux
compass = m.crux_compass()
check("the crux compass surfaces real tensions",
      any("manifest" in c["text"] or "reflex" in c["text"] for c in compass[:20]))

# the cruxes ground to kārikās (the organism can use them)
grounded = [c for c in compass if c["karikas"]]
check("cruxes carry kārikā grounding (usable by the argument layer)",
      len(grounded) > 0, f"({len(grounded)} grounded)")

print(f"\n=== SUMMARY: {sum(1 for _,c in results if c)}/{len(results)} passed ===")
print("\nTHE PUSHING SESSIONS ARE NOW WIRED: 35 deep human LOGICVID analyses become structured")
print("cruxes + claims grounded in kārikās (TĀ 1/52-55). The crux compass finally feeds the organism.")
print(f"\n  {summary['sessions']} sessions → {summary['cruxes']} cruxes, {summary['claims']} claims, "
      f"{summary['objections']} objections, across {len(summary['karikas'])} kārikās")
sys.exit(0 if all(c for _,c in results) else 1)
