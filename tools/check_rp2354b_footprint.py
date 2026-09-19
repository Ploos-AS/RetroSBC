#!/usr/bin/env python3
from pathlib import Path
import re,sys
s=Path(sys.argv[1]).read_text(encoding="utf-8")
nums=[int(x) for x in re.findall(r'\(pad "([0-9]+)"',s)]
assert nums==list(range(1,81)), f"perimeter pads wrong: {nums}"
assert '(pad "EP"' in s, "missing EP"
assert s.count('(pad "')==81, "expected 81 pads total"
print("PASS: 80 perimeter pads + EP")
