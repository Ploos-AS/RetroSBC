# FPGA Variants

## Primary Rev-A

`LFE5UM-85F-7BG381I`

84K LUT class, SERDES-capable, BG381.

This is the schematic and PCB baseline.

## Cost-reduced candidate

`LFE5UM-45F-7BG381I`

44K LUT class, SERDES-capable, BG381.

Do not market or populate this variant until synthesis demonstrates that the required RetroCore profile and platform services fit with acceptable reserve and timing.

## Compatibility rule

Sharing BG381 does **not** by itself prove drop-in pin compatibility. The PCB may support both only after the official Lattice migration/pinout data is checked and the common pin/rail constraints are encoded in the schematic and constraints files.
