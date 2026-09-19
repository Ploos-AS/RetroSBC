# FPGA pin binding

This directory contains the machine-readable Rev-A FPGA binding source.

The CSV starts with representative logical nets marked `UNBOUND`. Exact package balls and banks must be populated only from Lattice's official ECP5UM-85 pinout data. The table is intended to drive LPF constraints, schematic review and CI.

Do not replace `UNBOUND` with guessed values.

The complete logical net inventory will be expanded before exact placement so every mandatory Rev-A interface is accounted for.
