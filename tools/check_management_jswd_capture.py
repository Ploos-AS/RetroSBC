#!/usr/bin/env python3
from pathlib import Path
import re, sys

p=Path("hardware/kicad/13_MANAGEMENT/generated-jswd-capture.kicad_sexpr")
s=p.read_text()
required=[
    'RetroSBC-management:TC2030_CTX_SWD',
    'Reference" "J1"',
    'Value" "TC2030-CTX SWD"',
    '(reference "J1")',
    'Footprint" "RetroSBC:TC2030-IDC-FP"',
    '1=MGMT_3V3','2=MGMT_SWDIO','3=MGMT_RUN',
    '4=MGMT_SWCLK','5=GND','6=SWO_RESERVED',
]
missing=[x for x in required if x not in s]
if missing:
    sys.exit("J_SWD capture missing: "+", ".join(missing))
for pin in range(1,7):
    if len(re.findall(rf'\(pin "{pin}" ',s)) != 1:
        sys.exit(f"J_SWD instance pin {pin} missing or duplicated")
if s.count('(pin passive line') != 6:
    sys.exit("J_SWD library symbol must expose exactly six passive pins")
print("J_SWD generated capture contract: PASS")
