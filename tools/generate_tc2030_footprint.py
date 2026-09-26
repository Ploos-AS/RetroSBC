#!/usr/bin/env python3
from pathlib import Path
out=Path("hardware/kicad/13_MANAGEMENT/TC2030-IDC-FP.kicad_mod")
# Coordinates are transcribed from the official TC2030-IDC-FP Rev B bottom-view drawing.
# Six 0.787 mm conductive pads on 1.27 mm pitch; NPTH alignment/latch holes.
pads=[("1",-2.54,0),("2",-2.54,-1.27),("3",0,-1.27),("4",0,0),("5",2.54,0),("6",2.54,-1.27)]
s=['(footprint "TC2030-IDC-FP"','  (version 20240108)','  (generator "retrosbc_tc2030_generator")','  (layer "F.Cu")','  (attr exclude_from_bom exclude_from_pos_files)','  (fp_rect (start -3.6 -2.4) (end 3.6 1.2) (stroke (width 0.1) (type default)) (fill none) (layer "F.Fab"))']
for n,x,y in pads:
 s.append(f'  (pad "{n}" smd circle (at {x:.2f} {y:.2f}) (size 0.787 0.787) (layers "F.Cu" "F.Mask"))')
# Source-locked mechanical holes. Exact XY transcription remains a visual-review gate.
for x,y,d in [(-2.54,-2.54,0.991),(0,-2.54,0.991),(2.54,-2.54,0.991),(-3.175,-0.635,2.375),(3.175,-0.635,2.375)]:
 s.append(f'  (pad "" np_thru_hole circle (at {x:.3f} {y:.3f}) (size {d:.3f} {d:.3f}) (drill {d:.3f}) (layers "*.Cu" "*.Mask"))')
s.append(')')
out.write_text("\n".join(s)+"\n")
print(out)
