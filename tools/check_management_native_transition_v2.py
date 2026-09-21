#!/usr/bin/env python3
"""Guard the native Slice A transition without treating prose as connectivity."""
from pathlib import Path

root = Path("hardware/kicad/13_MANAGEMENT")
sch = (root / "13_MANAGEMENT.kicad_sch").read_text()
contract = (root / "KICAD_REAL_POWER_CAPTURE.md").read_text()

assert "(kicad_sch " in sch
assert "(lib_symbols)" in sch, "native capture has started; retire scaffold transition gate"
assert "(symbol (lib_id" not in sch, "native symbols present; retire scaffold transition gate"

for token in ("U_MGMT", "L_MGMT_CORE", "C_MGMT_VREG_IN", "C_MGMT_VREG_OUT",
              "R_MGMT_VREG_AVDD", "C_MGMT_VREG_AVDD",
              "MGMT_3V3", "MGMT_1V1", "VREG_AVDD", "GND"):
    assert token in contract, f"capture contract missing {token}"

assert "MGMT_1V1_FB" not in sch, "obsolete feedback net remains in scaffold"
assert "FB_MGMT_CORE" not in sch, "obsolete feedback component remains in scaffold"
assert "VREG_FB" in contract and "direct" in contract.lower(), "direct feedback rule missing"

print("PASS: scaffold is clean and native Slice A contract is ready")
