#!/usr/bin/env python3
"""Post-capture validator for the first native KiCad Slice A netlist."""
import sys
from pathlib import Path

p = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("/tmp/retrosbc-kicad/13_MANAGEMENT.net")
text = p.read_text()

required_refs = (
    "U_MGMT",
    "L_MGMT_CORE",
    "C_MGMT_VREG_IN",
    "C_MGMT_VREG_OUT",
    "R_MGMT_VREG_AVDD",
    "C_MGMT_VREG_AVDD",
)
required_values = ("RP2354B_QFN80", "3.3uH", "4.7uF", "33R")
required_nets = ("MGMT_3V3", "MGMT_1V1", "VREG_AVDD", "GND")

for token in required_refs:
    assert token in text, f"native netlist missing component {token}"
for token in required_values:
    assert token in text, f"native netlist missing locked value {token}"
for token in required_nets:
    assert token in text, f"native netlist missing required net {token}"

assert "MGMT_1V1_FB" not in text, "obsolete feedback net returned"
assert "FB_MGMT_CORE" not in text, "obsolete feedback component returned"

print("PASS: native Slice A components, locked values and named nets are present")
