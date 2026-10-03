#!/usr/bin/env python3
from pathlib import Path
p=Path("hardware/kicad/13_MANAGEMENT/TC2030-IDC-FP.kicad_mod")
t=p.read_text()
for n in "123456":
 if f'(pad "{n}" smd circle' not in t: raise SystemExit(f"missing contact pad {n}")
if t.count('(size 0.787 0.787)') != 6: raise SystemExit("contact pad diameter/count mismatch")
if t.count('(size 0.991 0.991)') != 3: raise SystemExit("alignment-hole count/diameter mismatch")
if t.count('(size 2.375 2.375)') != 2: raise SystemExit("latch-hole count/diameter mismatch")
if '"F.Paste"' in t: raise SystemExit("contact footprint must not expose F.Paste")
if "exclude_from_bom" not in t: raise SystemExit("footprint must be DNL/excluded from BOM")
print("TC2030 generated footprint structural gate: PASS")
