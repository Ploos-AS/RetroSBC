#!/usr/bin/env python3
"""Reject a scaffold-only KiCad netlist when native Slice A is expected."""
import sys
from pathlib import Path

p = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("/tmp/retrosbc-kicad/13_MANAGEMENT.net")
text = p.read_text()
for section in ("components", "libparts", "nets"):
    assert f"({section})" in text, f"baseline changed: {section} is no longer empty"
print("PASS: current management netlist is the expected empty scaffold baseline")
