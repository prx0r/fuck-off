"""lib/pushing_miner.py — wire the LOGICVID pushing sessions into the organism (the crux compass).

The audit found the 35 pushing-tantraloka sessions (deep human LOGICVID analysis of the cruxes) were
NEVER read by any experiment. They're the "crux compass" — the actual philosophical tensions the organism
should surface.

This kernel reads a pushing session markdown and mines it into structured crux/claim objects the organism
can use:
  - cruxes (the open tensions, e.g. "is determination a reflexive act?")
  - claims with their kārikā refs (TĀ 1/52-55)
  - objections (the hardest objections)
So the deep human analysis feeds the argument/crux/education layers — closing the biggest unused-asset gap.
"""
from __future__ import annotations
import os, re


class PushingCrux:
    """A crux mined from a pushing session."""
    def __init__(self, text, source_session, karika_refs=None, kind="tension"):
        self.text = text
        self.source = source_session
        self.karika_refs = karika_refs or []
        self.kind = kind


class PushingClaim:
    """A claim + its kārikā grounding mined from a pushing session."""
    def __init__(self, text, karika_ref, ceiling, source_session):
        self.text = text
        self.karika = karika_ref
        self.ceiling = ceiling
        self.source = source_session


class PushingMiner:
    """Mines a pushing session markdown into cruxes + claims + objections."""

    def __init__(self):
        self.cruxes = []
        self.claims = []
        self.objections = []
        self.session_count = 0

    # ---- read a pushing session file ----
    def mine_file(self, path):
        text = open(path).read()
        name = os.path.basename(path).replace(".md", "")
        self.session_count += 1

        # kārikā refs present (TĀ 1/52-55 style)
        refs = sorted(set(re.findall(r"(?:TĀ|T A|tantraloka)\s*1/(\d+)", text)))
        krefs = [f"TĀ 1/{r}" for r in refs]

        # cruxes: lines with "crux"/"tension"/"?" : the open tensions
        for line in text.splitlines():
            l = line.strip()
            # literal crux/tension markers
            if re.match(r"^(?:- |\*\*)?(?:CRUX|crux|THE CRUX|The crux|tension|TENSION)", l):
                self.cruxes.append(PushingCrux(l.strip("*- "), name, krefs))
            # the penetrating questions (ROUND headers + ?-lines that raise a real crux)
            elif re.match(r"^##?\s+ROUND\s+\d+.*\?", l) and len(l) < 160:
                self.cruxes.append(PushingCrux(l.split("—")[-1].strip(), name, krefs, "question"))
            elif l.endswith("?") and len(l) > 25 and len(l) < 160 and "why" in l.lower():
                self.cruxes.append(PushingCrux(l.strip("> "), name, krefs, "question"))

        # claims: the numbered steps ("1. ...") which are the text's argued positions
        for m in re.finditer(r"^\d+\.\s*(.+)", text, re.M):
            self.claims.append(PushingClaim(m.group(1).strip(), krefs[0] if krefs else "",
                                            "SCHOLARLY_CORROBORATED", name))

        # objections: "objection" sections
        if re.search(r"objection", text, re.I):
            for m in re.finditer(r"^(?:- |\*\*)?(?:Objection|objection|OBJECTION)[^:]*:\s*(.+)", text, re.M):
                self.objections.append(m.group(1).strip())
        return {"session": name, "karikas": krefs,
                "cruxes": len(self.cruxes), "claims": len(self.claims),
                "objections": len(self.objections)}

    # ---- mine a whole directory of sessions ----
    def mine_dir(self, dirpath):
        summary = {"sessions": 0, "cruxes": 0, "claims": 0, "objections": 0, "karikas": set()}
        for f in sorted(os.listdir(dirpath)):
            if f.endswith(".md"):
                r = self.mine_file(os.path.join(dirpath, f))
                summary["sessions"] += 1
                summary["cruxes"] += r["cruxes"]
                summary["claims"] += r["claims"]
                summary["objections"] += r["objections"]
                summary["karikas"].update(r["karikas"])
        summary["karikas"] = sorted(summary["karikas"])
        return summary

    # ---- the crux compass: the open tensions the organism should surface ----
    def crux_compass(self):
        return [{"text": c.text, "source": c.source, "karikas": c.karika_refs, "kind": c.kind}
                for c in self.cruxes]
