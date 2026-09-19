#!/usr/bin/env python3
"""Normalize the official Lattice ECP5UM-85 pinout CSV.

Usage:
  python3 tools/normalize_ecp5_pinout.py vendor.csv hardware/fpga/lfe5um85-bg381-vendor-normalized.csv

The script intentionally does not download vendor data. Keep the authoritative
Lattice source provenance outside generated output and review the detected
columns before using the result for physical binding.
"""
import csv, sys

if len(sys.argv) != 3:
    raise SystemExit("usage: normalize_ecp5_pinout.py INPUT.csv OUTPUT.csv")

src, dst = sys.argv[1:]
with open(src, newline="", encoding="utf-8-sig") as f:
    rows = list(csv.DictReader(f))
if not rows:
    raise SystemExit("input contains no data rows")

fields = list(rows[0])
def pick(*needles):
    for field in fields:
        low = field.lower().replace(" ", "").replace("_", "")
        if all(n in low for n in needles):
            return field
    return None

ball = pick("pin") or pick("ball")
bank = pick("bank")
name = pick("name") or pick("function") or pick("signal")
if not ball:
    raise SystemExit(f"cannot identify package pin/ball column; columns={fields!r}")

out=[]
for r in rows:
    b=(r.get(ball) or "").strip()
    if not b:
        continue
    out.append({
        "package_ball": b,
        "bank": (r.get(bank) or "").strip() if bank else "",
        "vendor_function": (r.get(name) or "").strip() if name else "",
        "source_row": str(len(out)+1),
    })

with open(dst,"w",newline="",encoding="utf-8") as f:
    w=csv.DictWriter(f,fieldnames=["package_ball","bank","vendor_function","source_row"])
    w.writeheader(); w.writerows(out)
print(f"normalized {len(out)} package rows -> {dst}")
