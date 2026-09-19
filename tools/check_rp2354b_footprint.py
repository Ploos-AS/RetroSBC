#!/usr/bin/env python3
from pathlib import Path
import re,sys
s=Path(sys.argv[1]).read_text(encoding="utf-8")
nums=[int(x) for x in re.findall(r'\(pad "([0-9]+)"',s)]
assert nums==list(range(1,81)), f"perimeter pads wrong: {nums}"
assert '(pad "EP"' in s, "missing EP"
assert s.count('(pad "')==81, "expected 81 pads total"
assert '(size 3.400 3.400)' in s, "EP size must be 3.400 x 3.400 mm"
assert '(size 0.780 0.220)' in s, "perimeter land size must be 0.780 x 0.220 mm"
assert s.count('(at -4.896 ') == 20, "left-side pad centres drifted"
assert s.count('(at 4.896 ') == 20, "right-side pad centres drifted"
assert s.count('(at 0 -4.896 90)') == 1, "bottom-side pad geometry drifted"
assert s.count('(at 0 4.896 270)') == 1, "top-side pad geometry drifted"
print("PASS: 80 perimeter pads + EP")
