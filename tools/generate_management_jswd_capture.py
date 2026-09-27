#!/usr/bin/env python3
"""Generate the source-locked native J_SWD capture fragment.

This generator deliberately emits a standalone KiCad S-expression fragment.
Insertion into 13_MANAGEMENT.kicad_sch is a separate, parser-gated transition.
"""
from pathlib import Path

OUT = Path("hardware/kicad/13_MANAGEMENT/generated-jswd-capture.kicad_sexpr")
PROJECT = "RetroSBC-13-MANAGEMENT"
ROOT = "7a5d3d51-9e2f-4d31-b7cb-9fbd10b8c301"
UUID = "8a111111-1111-4111-8111-811111111111"

pins = [
    ("1", "81000001-2222-4222-8222-811111111111"),
    ("2", "81000002-2222-4222-8222-811111111111"),
    ("3", "81000003-2222-4222-8222-811111111111"),
    ("4", "81000004-2222-4222-8222-811111111111"),
    ("5", "81000005-2222-4222-8222-811111111111"),
    ("6", "81000006-2222-4222-8222-811111111111"),
]

s = [
'(symbol "RetroSBC-management:TC2030_CTX_SWD"',
'  (pin_names (offset 1.016))',
'  (exclude_from_sim no) (in_bom no) (on_board yes)',
'  (property "Reference" "J" (at 0 10.16 0) (effects (font (size 1.27 1.27))))',
'  (property "Value" "TC2030-CTX SWD" (at 0 7.62 0) (effects (font (size 1.27 1.27))))',
'  (property "Footprint" "RetroSBC:TC2030-IDC-FP" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))',
'  (property "Datasheet" "Tag-Connect TC2030-CTX" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))',
'  (property "Description" "DNL TC2030 Cortex SWD target contact pattern" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))',
'  (symbol "TC2030_CTX_SWD_0_1"',
'    (rectangle (start -7.62 6.35) (end 7.62 -6.35) (stroke (width 0) (type default)) (fill (type background)))',
'  )',
'  (symbol "TC2030_CTX_SWD_1_1"',
]
for n, name, y in [
    ("1","VTREF",5.08), ("2","SWDIO",2.54), ("3","nRESET",0),
    ("4","SWCLK",-2.54), ("5","GND",-5.08), ("6","SWO", -7.62)
]:
    s.append(f'    (pin passive line (at -12.7 {y} 0) (length 5.08) (name "{name}" (effects (font (size 1.0 1.0)))) (number "{n}" (effects (font (size 1.0 1.0)))))')
s += ['  )',')','',
'(symbol (lib_id "RetroSBC-management:TC2030_CTX_SWD") (at 205 80 0) (unit 1)',
'  (exclude_from_sim no) (in_bom no) (on_board yes)',
f'  (uuid {UUID})',
'  (property "Reference" "J_SWD" (at 205 68 0) (effects (font (size 1.27 1.27))))',
'  (property "Value" "TC2030-CTX SWD" (at 205 71 0) (effects (font (size 1.27 1.27))))',
'  (property "Footprint" "RetroSBC:TC2030-IDC-FP" (at 205 80 0) (effects (font (size 1.27 1.27)) hide))',
'  (property "Datasheet" "Tag-Connect TC2030-CTX" (at 205 80 0) (effects (font (size 1.27 1.27)) hide))',
'  (property "Description" "DNL TC2030 Cortex SWD target contact pattern" (at 205 80 0) (effects (font (size 1.27 1.27)) hide))',
]
for n,u in pins:
    s.append(f'  (pin "{n}" (uuid {u}))')
s += [
f'  (instances (project "{PROJECT}" (path "/{ROOT}/{UUID}" (reference "J_SWD") (unit 1))))',
')','',
'# net contract: 1=MGMT_3V3 2=MGMT_SWDIO 3=MGMT_RUN 4=MGMT_SWCLK 5=GND 6=SWO_RESERVED',
]
OUT.write_text("\n".join(s)+"\n")
print(OUT)
