#!/usr/bin/env python3
from pathlib import Path
p=Path('hardware/kicad/13_MANAGEMENT/KICAD_REAL_POWER_CAPTURE.md')
text=p.read_text()
for token in ['U_MGMT','L_MGMT_CORE','3.3uH','C_MGMT_VREG_IN','4.7uF','C_MGMT_VREG_OUT','R_MGMT_VREG_AVDD','33R','C_MGMT_VREG_AVDD','VREG_LX pad 64','VREG_AVDD pad 61','VREG_VIN pad 63','VREG_PGND pad 62','VREG_FB pad 65','MGMT_3V3','MGMT_1V1','ERC']:
    assert token in text, f'real capture contract missing {token}'
assert 'No feedback divider is permitted.' in text
print('PASS: M3.7 real KiCad power-capture contract')
