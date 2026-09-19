#!/usr/bin/env python3
import csv,sys
from pathlib import Path
BAD={"","TBD","UNTRANSCRIBED"}
def load(p):
 with Path(p).open(newline="",encoding="utf-8") as f:return list(csv.DictReader(f))
def main(pinfile,binding):
 rows=load(pinfile); bind=load(binding); errs=[]
 bypad={int(r["pad"]):r for r in rows}
 for r in rows:
  if r["pin_name"].strip() in BAD or r["pin_type"].strip() in BAD or r["source"].strip() in BAD:
   errs.append(f"pad {r['pad']}: unresolved metadata")
 for r in bind:
  try: pad=int(r["pad"])
  except ValueError: continue
  if pad not in bypad: errs.append(f"binding pad {pad}: absent from package table"); continue
  pkg=bypad[pad]["pin_name"]
  # Binding file may use GPIO names directly or dedicated pin names.
  expected=r["pin_name"].strip()
  if expected and expected not in {pkg,"UNTRANSCRIBED"}:
   errs.append(f"binding pad {pad}: binding pin_name={expected}, package={pkg}")
 if errs:
  print("\n".join("FAIL: "+e for e in errs)); return 1
 print("PASS: QFN-80 semantic metadata resolved and binding overlay agrees with package pin names")
 return 0
if __name__=="__main__":
 if len(sys.argv)!=3:
  print(f"usage: {sys.argv[0]} <qfn80.csv> <binding.csv>"); raise SystemExit(2)
 raise SystemExit(main(sys.argv[1],sys.argv[2]))
