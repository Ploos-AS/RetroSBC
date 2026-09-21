# Native KiCad qualification gate

Before Slice A is materialized, CI proves that the pinned KiCad 9.0.6 toolchain
can perform all three operations required after the electrical edit:

1. parse/render the schematic;
2. export a native schematic netlist;
3. run schematic ERC.

The scaffold is not an electrical design and this gate does **not** grant
CAPTURE PASS. Its purpose is to qualify the exact CLI operations that will judge
the first native Slice A edit.

After native objects land, the netlist output must additionally be compared
against `rp2354b-power-netlist.csv`, and ERC findings must be fixed or narrowly
documented before Slice A can pass.
