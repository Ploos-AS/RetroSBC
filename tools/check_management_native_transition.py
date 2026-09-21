#!/usr/bin/env python3
"""Guard the transition from scaffold to native KiCad Slice A capture.

This checker encodes the exact native objects that the next generator/edit must
produce. It intentionally does not manufacture KiCad syntax itself.
"""
from pathlib import Path

root = Path("hardware/kicad/13_MANAGEMENT")
sch = (root / "13_MANAGEMENT.kicad_sch").read_text()
contract = (root / "KICAD_REAL_POWER_CAPTURE.md").read_text()

# Current file must remain parseable scaffold until native materialization lands.
assert "(kicad_sch " in sch
assert "(lib_symbols)" in sch

required = {
    "U_MGMT": "RP2354B_QFN80",
    "L_MGMT_CORE": "3.3uH",
    "C_MGMT_VREG_IN": "4.7uF",
    "C_MGMT_VREG_OUT": "4.7uF",
    "R_MGMT_VREG_AVDD": "33R",
    "C_MGMT_VREG_AVDD": "4.7uF",
}
for ref, value in required.items():
    assert ref in contract, f"capture contract missing {ref}"
    assert value in contract, f"capture contract missing locked value {value}"

for net in ("MGMT_3V3", "MGMT_1V1", "VREG_AVDD", "GND"):
    assert net in contract, f"capture contract missing net {net}"

for forbidden in ("MGMT_1V1_FB", "feedback divider"):
    assert forbidden not in contract.lower(), f"obsolete topology remains in contract: {forbidden}"

print("PASS: native Slice A transition contract")
