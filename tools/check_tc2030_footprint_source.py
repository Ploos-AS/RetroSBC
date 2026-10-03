#!/usr/bin/env python3
import csv
from pathlib import Path

p=Path("hardware/kicad/13_MANAGEMENT/tc2030-footprint-source-lock.csv")
rows={r["item"]:r for r in csv.DictReader(p.open())}
required={
 "FOOTPRINT":"TC2030-IDC-FP legged",
 "CONTACT_PAD_DIAMETER":"0.787 mm +/- 0.076",
 "ALIGNMENT_HOLE_DIAMETER":"0.991 mm +/- 0.076",
 "LEG_LATCH_HOLE_DIAMETER":"2.375 mm +/- 0.076",
 "CONTACT_PITCH":"1.270 mm",
 "LEG_PITCH":"2.540 mm",
 "CONTACT_ROW_SPAN":"5.080 mm",
}
for k,v in required.items():
    if k not in rows: raise SystemExit(f"missing source-lock row: {k}")
    if rows[k]["value"] != v: raise SystemExit(f"{k}: expected {v!r}, got {rows[k]['value']!r}")
    if rows[k]["status"] != "REFERENCE_LOCK": raise SystemExit(f"{k}: not REFERENCE_LOCK")
for k in ("KEEP_OUT","CONTACT_CLEARANCE","SOLDER_PASTE","FINGER_ACCESS","BOM_LOAD"):
    if k not in rows or rows[k]["status"]!="REFERENCE_LOCK":
        raise SystemExit(f"{k}: missing reference lock")
print("TC2030 footprint source lock: PASS")
