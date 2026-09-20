#!/usr/bin/env python3
"""Generate the M3.7 management power-capture fragment from the locked CSV.

This deliberately generates a deterministic, reviewable KiCad-source fragment
before it is inserted into the complete schematic. It prevents hand-copying
locked RP2354B regulator values and nets into the electrical capture.
"""
import csv
from pathlib import Path

ROOT = Path("hardware/kicad/13_MANAGEMENT")
SRC = ROOT / "rp2354b-power-netlist.csv"
OUT = ROOT / "generated-management-power.kicad_sexpr"

rows = list(csv.DictReader(SRC.open()))
locked = {r["ref"]: r for r in rows}

required = {
    "L_MGMT_CORE": ("3.3uH", "REFERENCE_LOCK"),
    "C_MGMT_VREG_IN": ("4.7uF", "REFERENCE_LOCK"),
    "C_MGMT_VREG_OUT": ("4.7uF", "REFERENCE_LOCK"),
    "R_MGMT_VREG_AVDD": ("33R", "REFERENCE_LOCK"),
    "C_MGMT_VREG_AVDD": ("4.7uF", "REFERENCE_LOCK"),
}
for ref, (value, status) in required.items():
    row = locked.get(ref)
    assert row, f"missing {ref}"
    assert row["value_or_function"] == value, f"{ref}: expected {value}"
    assert row["status"] == status, f"{ref}: expected {status}"

lines = [
    "; RetroSBC M3.7 generated management-power capture fragment",
    "; GENERATED from rp2354b-power-netlist.csv — do not hand edit",
    "(management_power_capture",
]
for row in rows:
    fields = " ".join(
        f'({key} "{row[key]}")'
        for key in ("ref", "value_or_function", "from", "to", "status")
    )
    lines.append(f"  (connection {fields})")
lines.append(")")
OUT.write_text("\n".join(lines) + "\n")
print(f"generated {OUT} with {len(rows)} connections")
