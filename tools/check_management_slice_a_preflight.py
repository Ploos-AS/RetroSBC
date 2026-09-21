#!/usr/bin/env python3
"""Preflight gate before writing Slice A into the native KiCad schematic."""
import csv
from pathlib import Path

root=Path("hardware/kicad/13_MANAGEMENT")
rows=list(csv.DictReader((root/"rp2354b-power-netlist.csv").open()))
by_ref={r["ref"]:r for r in rows}
required={
 "L_MGMT_CORE":("3.3uH","pad 64 VREG_LX","MGMT_1V1"),
 "C_MGMT_VREG_IN":("4.7uF","MGMT_3V3","GND"),
 "C_MGMT_VREG_OUT":("4.7uF","MGMT_1V1","GND"),
 "R_MGMT_VREG_AVDD":("33R","MGMT_3V3","VREG_AVDD"),
 "C_MGMT_VREG_AVDD":("4.7uF","VREG_AVDD","GND"),
}
for ref,expected in required.items():
 r=by_ref.get(ref)
 assert r, f"missing {ref}"
 assert (r["value_or_function"],r["from"],r["to"])==expected, f"{ref}: source mismatch"
 assert r["status"]=="REFERENCE_LOCK", f"{ref}: not reference locked"

sch=(root/"13_MANAGEMENT.kicad_sch").read_text()
assert "(kicad_sch " in sch
assert "(lib_symbols)" in sch, "preflight expects current scaffold with empty lib_symbols"
assert "(symbol (lib_id" not in sch, "native symbols already present; update preflight before proceeding"

sym=(root/"RetroSBC-management.kicad_sym").read_text()
assert 'symbol "RP2354B_QFN80"' in sym
for pin in ["61","62","63","64","65"]:
 assert f'(number "{pin}"' in sym, f"validated symbol missing pad {pin}"

fp=(root/"RP2354B_QFN80.kicad_mod").read_text()
for pad in ["61","62","63","64","65"]:
 assert f'(pad "{pad}"' in fp, f"validated footprint missing pad {pad}"

print("PASS: Slice A source, symbol, footprint and scaffold preflight")
