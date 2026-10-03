# Native Slice A implementation

This branch starts the CI transition from the electrically empty management
scaffold to native KiCad Slice A.

The workflow now uses the corrected transition checker before KiCad parsing and
expects the exported netlist to satisfy `check_management_native_netlist.py`.
That means this branch is intentionally red until the native schematic edit
adds U_MGMT and the locked regulator block.

## Required electrical objects

- U_MGMT — RP2354B_QFN80
- L_MGMT_CORE — 3.3uH
- C_MGMT_VREG_IN — 4.7uF
- C_MGMT_VREG_OUT — 4.7uF
- R_MGMT_VREG_AVDD — 33R
- C_MGMT_VREG_AVDD — 4.7uF

Required named nets: MGMT_3V3, MGMT_1V1, VREG_AVDD and GND.

This deliberately prevents the old empty-netlist baseline from remaining green
once native capture work begins.
