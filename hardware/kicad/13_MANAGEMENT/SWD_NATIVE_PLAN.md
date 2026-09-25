# Native J_SWD implementation plan

The selected Rev A development target is the **legged TC2030 6-pin Cortex SWD
footprint**. Tag-Connect documents the legged version for development and notes
that the no-legs cable can also be used with the legged footprint.

## Locked pin map

| J_SWD pin | RetroSBC net |
|---|---|
| 1 | MGMT_3V3 (VTREF) |
| 2 | MGMT_SWDIO |
| 3 | MGMT_RUN |
| 4 | MGMT_SWCLK |
| 5 | GND |
| 6 | SWO_RESERVED |

Pin 6 is not repurposed. It remains SWO/reserved until the RP2354B-side SWO
policy is explicitly defined.

## Capture rule

The native KiCad symbol may now use the numbered 1..6 interface above. The PCB
footprint itself must be transcribed or imported from the authoritative
Tag-Connect footprint dimensions rather than drawn from memory.

The next electrical capture shall wire U_MGMT pads 33/34/35 to J_SWD pins
4/2/3 respectively, pin 1 to MGMT_3V3 and pin 5 to GND. Do not mark J_SWD
CAPTURED_NATIVE until the exported netlist proves these mappings.
