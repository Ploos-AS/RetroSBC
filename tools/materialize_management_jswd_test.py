#!/usr/bin/env python3
"""Build a disposable KiCad schematic containing the generated J_SWD symbol.

Never edits 13_MANAGEMENT.kicad_sch. CI parses the disposable file first.
"""
from pathlib import Path
import re

base=Path("hardware/kicad/13_MANAGEMENT/13_MANAGEMENT.kicad_sch").read_text()\n
frag=Path("hardware/kicad/13_MANAGEMENT/generated-jswd-capture.kicad_sexpr").read_text()
lib, inst = frag.split("\n\n",1)
inst=inst.split("\n# net contract:",1)[0].strip()

# Insert the generated library symbol immediately before lib_symbols closes.
m=re.search(r'\n  \)\n  \(text "RetroSBC 13_MANAGEMENT',base)
if not m:
    raise SystemExit("lib_symbols closing anchor not found")
base=base[:m.start()]+"\n    "+lib.replace("\n","\n    ")+"\n  )\n  (text \"RetroSBC 13_MANAGEMENT"+base[m.end():]

# Insert the instance before sheet_instances. Exact anchor; no broad component regex.
anchor='  (sheet_instances (path "/" (page "1")))'
if anchor not in base:
    raise SystemExit("sheet_instances anchor not found")
base=base.replace(anchor,inst+"\n  "+anchor,1)

out=Path("/tmp/retrosbc-kicad/J_SWD_PARSE_TEST.kicad_sch")
out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(base)
print(out)
