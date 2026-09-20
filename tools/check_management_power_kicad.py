#!/usr/bin/env python3
from pathlib import Path
import subprocess
import sys

out = Path("hardware/kicad/13_MANAGEMENT/generated-management-power.kicad_sexpr")
subprocess.run([sys.executable, "tools/generate_management_power_kicad.py"], check=True)
text = out.read_text()
for token in [
    'L_MGMT_CORE', '3.3uH', 'C_MGMT_VREG_IN', 'C_MGMT_VREG_OUT',
    'R_MGMT_VREG_AVDD', '33R', 'C_MGMT_VREG_AVDD',
    'MGMT_3V3', 'MGMT_1V1', 'VREG_LX', 'VREG_FB', 'VREG_AVDD', 'GND',
    'REFERENCE_LOCK'
]:
    assert token in text, f"generated capture missing {token}"
assert "VALUE_SOURCE_GATE" not in text
assert "REFERENCE_TOPOLOGY_GATE" not in text
print("PASS: deterministic management-power KiCad capture fragment")
