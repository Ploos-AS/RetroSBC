#!/usr/bin/env python3
import csv
from pathlib import Path

p=Path("hardware/kicad/13_MANAGEMENT/rp2354b-power-netlist.csv")
rows=list(csv.DictReader(p.open()))
assert rows, "empty power netlist"
text=p.read_text()
for token in ["MGMT_3V3","MGMT_1V1","VREG_LX","VREG_FB","VREG_PGND","ADC_AVDD","VREG_AVDD","VREG_VIN","EP"]:
    assert token in text, f"missing {token}"

# Locked RP235x reference regulator topology.
assert "L_MGMT_CORE,3.3uH,pad 64 VREG_LX,MGMT_1V1,REFERENCE_LOCK" in text
assert "U_MGMT,RP2354B,pad 65 VREG_FB,MGMT_1V1,REFERENCE_LOCK" in text
assert "C_MGMT_VREG_IN,4.7uF,MGMT_3V3,GND,REFERENCE_LOCK" in text
assert "C_MGMT_VREG_OUT,4.7uF,MGMT_1V1,GND,REFERENCE_LOCK" in text
assert "R_MGMT_VREG_AVDD,33R,MGMT_3V3,VREG_AVDD,REFERENCE_LOCK" in text
assert "C_MGMT_VREG_AVDD,4.7uF,VREG_AVDD,GND,REFERENCE_LOCK" in text

# Old provisional gates must not survive once the official reference is locked.
assert "MGMT_1V1_FB" not in text
assert "VALUE_SOURCE_GATE" not in text
assert "REFERENCE_TOPOLOGY_GATE" not in text

print(f"PASS: {len(rows)} RP2354B power-capture rows validated; regulator reference locked")
