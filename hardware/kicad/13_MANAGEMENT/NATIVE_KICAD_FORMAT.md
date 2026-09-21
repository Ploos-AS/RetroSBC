# Native KiCad schematic serialization reference

The first electrical Slice A edit is based on KiCad's documented schematic
s-expression structure rather than guessed syntax.

For every native schematic symbol the file must contain:

- an embedded symbol definition under `lib_symbols`;
- a schematic `symbol` instance with library identifier, position, unit,
  BOM/board flags, UUID and properties;
- a UUID mapping for every used pin;
- project/path instance data with reference and unit;
- native `wire` and `label` objects for electrical connectivity.

The root schematic UUID participates in instance paths. KiCad's own parser,
netlist exporter and ERC remain the authority: text presence alone is not
electrical qualification.

Reference: KiCad Developer Documentation, **Schematic File Format**, and KiCad
9 demo schematics serialized by Eeschema.

## RetroSBC transition rule

The current empty `lib_symbols` scaffold is deliberate. The Slice A change
must replace it with the embedded RP2354B symbol plus the passive symbols
actually instantiated. It must simultaneously replace the empty-netlist CI
assertion with `check_management_native_netlist.py`.

Do not claim CAPTURE PASS until the pinned KiCad 9.0.6 job exports a non-empty
netlist, ERC has been reviewed, and the rendered PDF has been visually checked.
