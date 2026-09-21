# KiCad CI environment

The management schematic is validated with the official KiCad container and
`kicad-cli`.

Pinned CI baseline: **KiCad 9.0.6**.

The first gate deliberately performs a real schematic parse by exporting the
management sheet to PDF. This catches native file-format/parser failures before
Slice A starts adding electrical objects.

Once Slice A is materialized, this workflow is the home for ERC and native
netlist checks as well.

The container is CLI-only; no GUI behavior is claimed by this gate.
