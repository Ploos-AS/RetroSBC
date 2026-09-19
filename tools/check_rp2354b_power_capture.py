#!/usr/bin/env python3
import csv
from pathlib import Path

p=Path("hardware/kicad/13_MANAGEMENT/rp2354b-power-netlist.csv")
rows=list(csv.DictReader(p.open()))
assert rows, "empty power netlist"
text=p.read_text()
for token in ["MGMT_3V3","MGMT_1V1","MGMT_1V1_FB","VREG_LX","VREG_FB","VREG_PGND","ADC_AVDD","VREG_AVDD","VREG_VIN","EP"]:
    assert token in text, f"missing {token}"
assert "pad 64 VREG_LX,MGMT_1V1" in text
assert "pad 65 VREG_FB,MGMT_1V1_FB" in text
assert "VALUE_SOURCE_GATE" in text
assert "REFERENCE_TOPOLOGY_GATE" in text
print(f"PASS: {len(rows)} RP2354B power-capture rows validated")
