#!/usr/bin/env python3
"""Generate the project-local RP2354B QFN-80 KiCad symbol from validated CSV."""
import csv,sys
from pathlib import Path
KTYPE={"bidirectional":"bidirectional","input":"input","output":"output","power_in":"power_in","power_out":"power_out"}
def main(src,dst):
 rows=list(csv.DictReader(Path(src).open(encoding="utf-8",newline="")))
 if len(rows)!=80: raise SystemExit("expected 80 package pads")
 # Four 20-pin sides. Geometry is deterministic and intentionally roomy.
 groups=[rows[0:20],rows[20:40],rows[40:60],rows[60:80]]
 out=['(kicad_symbol_lib (version 20231120) (generator retrosbc_rp2354b_symbol_gen)',
 '  (symbol "RP2354B_QFN80"',
 '    (pin_names (offset 1.016))',
 '    (exclude_from_sim no)','    (in_bom yes)','    (on_board yes)',
 '    (property "Reference" "U" (at 0 30.48 0) (effects (font (size 1.27 1.27))))',
 '    (property "Value" "RP2354B_QFN80" (at 0 27.94 0) (effects (font (size 1.27 1.27))))',
 '    (property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))',
 '    (property "Datasheet" "RP2350 datasheet" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))',
 '    (property "Description" "RP2354B management MCU, QFN-80 B package; generated from validated RetroSBC package table." (at 0 0 0) (effects (font (size 1.27 1.27)) hide))',
 '    (symbol "RP2354B_QFN80_0_1"',
 '      (rectangle (start -20.32 25.4) (end 20.32 -25.4) (stroke (width 0) (type default)) (fill (type background)))','    )',
 '    (symbol "RP2354B_QFN80_1_1"']
 def pin(r,x,y,rot):
  t=KTYPE[r["pin_type"]]
  return f'      (pin {t} line (at {x} {y} {rot}) (length 5.08) (name "{r["pin_name"]}" (effects (font (size 1.0 1.0)))) (number "{r["pad"]}" (effects (font (size 1.0 1.0)))))'
 # left 1..20, bottom 21..40, right 41..60, top 61..80
 for i,r in enumerate(groups[0]): out.append(pin(r,-25.4,24.13-i*2.54,0))
 for i,r in enumerate(groups[1]): out.append(pin(r,-19.05+i*2.03,-30.48,90))
 for i,r in enumerate(groups[2]): out.append(pin(r,25.4,-24.13+i*2.54,180))
 for i,r in enumerate(groups[3]): out.append(pin(r,19.05-i*2.03,30.48,270))
 out+=['    )','  )',')','']
 Path(dst).write_text("\n".join(out),encoding="utf-8")
if __name__=="__main__":
 if len(sys.argv)!=3: raise SystemExit(f"usage: {sys.argv[0]} input.csv output.kicad_sym")
 main(sys.argv[1],sys.argv[2])
