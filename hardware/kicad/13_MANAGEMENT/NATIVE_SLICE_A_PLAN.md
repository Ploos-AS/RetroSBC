# Native Slice A implementation plan

KiCad 9.0.6 is now the CI parser baseline.

The next electrical change to `13_MANAGEMENT.kicad_sch` must be a real native
KiCad schematic edit, not a text-only capture description. The implementation
must contain these component instances:

- U_MGMT — RP2354B_QFN80, project-local validated symbol and footprint
- L_MGMT_CORE — 3.3uH
- C_MGMT_VREG_IN — 4.7uF
- C_MGMT_VREG_OUT — 4.7uF
- R_MGMT_VREG_AVDD — 33R
- C_MGMT_VREG_AVDD — 4.7uF

Required named connectivity is MGMT_3V3, MGMT_1V1, VREG_AVDD and GND. VREG_FB
pad 65 senses MGMT_1V1 directly. No feedback divider or MGMT_1V1_FB net is
permitted.

## Native-file rule

A schematic symbol instance must reference an embedded library symbol, carry a
UUID, properties, pin UUID mappings and project/path instance data. Wires and
labels are native schematic objects with their own UUIDs. Therefore the
materialization step must be round-tripped through KiCad 9.0.6 and accepted by
`kicad-cli`; hand-written approximate symbol-instance syntax is not accepted.

## Acceptance sequence

1. Materialize Slice A native objects.
2. Parse/export the resulting schematic with the pinned KiCad CLI gate.
3. Export a native netlist and compare the regulator connectivity with
   `rp2354b-power-netlist.csv`.
4. Run ERC and either fix findings or record narrowly justified exceptions.
5. Replace the scaffold-only preflight with a post-capture validator.
6. Perform visual review before declaring Slice A CAPTURE PASS.
