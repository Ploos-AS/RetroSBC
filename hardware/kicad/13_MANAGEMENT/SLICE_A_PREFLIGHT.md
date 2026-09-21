# Slice A native-capture preflight

This gate protects the first native KiCad electrical edit.

It verifies that the regulator source rows are reference-locked, the validated
RP2354B symbol and footprint contain pads 61–65, and the current schematic is
still the expected empty electrical scaffold.

Run:

`python tools/check_management_slice_a_preflight.py`

A PASS means the repository inputs are internally ready for native KiCad
materialization. It does **not** mean the schematic has been captured or passed
ERC.

The native edit must be performed with KiCad-compatible serialization and then
qualified by parse/ERC/netlist checks; do not fabricate symbol-instance syntax
without a KiCad round-trip.
