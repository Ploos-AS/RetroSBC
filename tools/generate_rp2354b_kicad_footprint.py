#!/usr/bin/env python3
"""Generate the RP2354B QFN-80 recommended PCB footprint from Raspberry Pi Figure 146."""
from pathlib import Path
PITCH=0.4
N=20
PAD_W=0.22
PAD_L=0.78
EP=3.40
OUTER=10.573
INNER=9.013
def pad(n,x,y,rot):
    return f'  (pad "{n}" smd roundrect (at {x:.3f} {y:.3f} {rot}) (size {PAD_L:.3f} {PAD_W:.3f}) (layers "F.Cu" "F.Paste" "F.Mask") (roundrect_rratio 0.2))'
def main(dst):
    out=['(footprint "RetroSBC:RP2354B_QFN80" (version 20240108) (generator pcbnew)',
         '  (layer "F.Cu")',
         '  (attr smd)',
         '  (fp_rect (start -5 -5) (end 5 5) (stroke (width 0.05) (type default)) (fill none) (layer "F.Fab"))']
    # Pin 1 at upper-left, then counter-clockwise around the package.
    # 20 pads per side; centres are on the 9.013 mm inner-span line.
    c=(N-1)*PITCH/2
    num=1
    for i in range(N):
        out.append(pad(num,-(INNER/2+PAD_L/2),c-i*PITCH,0)); num+=1
    for i in range(N):
        out.append(pad(num,-c+i*PITCH,-(INNER/2+PAD_L/2),90)); num+=1
    for i in range(N):
        out.append(pad(num,(INNER/2+PAD_L/2),-c+i*PITCH,180)); num+=1
    for i in range(N):
        out.append(pad(num,c-i*PITCH,(INNER/2+PAD_L/2),270)); num+=1
    out.append(f'  (pad "EP" smd rect (at 0 0) (size {EP:.3f} {EP:.3f}) (layers "F.Cu" "F.Paste" "F.Mask"))')
    out += ['  (fp_circle (center -4.5 -4.5) (end -4.3 -4.5) (stroke (width 0.15) (type default)) (fill none) (layer "F.SilkS"))',')','']
    Path(dst).write_text("\n".join(out),encoding="utf-8")
if __name__=="__main__":
    import sys
    if len(sys.argv)!=2: raise SystemExit(f"usage: {sys.argv[0]} <output.kicad_mod>")
    main(sys.argv[1])
