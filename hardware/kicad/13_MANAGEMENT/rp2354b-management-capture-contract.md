# M3.7 — RP2354B management schematic capture contract

Status: **capture contract; KiCad wiring pending**

## U_MGMT package binding

The management MCU shall use:
- symbol: `RP2354B_QFN80`;
- footprint: `RetroSBC:RP2354B_QFN80`;
- numbered pads 1..80 mapped one-to-one;
- exposed pad `EP` mapped to `GND`.

The symbol/footprint pair must remain generated/validated by the existing CI gates.

## Power capture

Capture the following named nets:
- `MGMT_3V3`
- `MGMT_1V1`
- `GND`

The power topology must implement the previously locked RP2354B regulator/reference topology:
- VREG input from the qualified management supply;
- VREG_LX through the reference inductor;
- filtered 1.1 V rail returned to VREG_FB and DVDD as specified;
- VREG_PGND and EP/GND tied into the ground system;
- local decoupling at each applicable supply pin;
- required bulk capacitance on the 3.3 V management rail.

## Service/debug

Reserve explicit nets/connectors for:
- `MGMT_RUN`
- SWDIO
- SWCLK
- 3V3
- GND
- USB D+
- USB D-

RUN and SWD must remain accessible without depending on the Linux processor.

## USB

Use the validated RP2354B pad assignment:
- USB D- → package pad 66
- USB D+ → package pad 67

D+ and D- each receive the locked 27 ohm series termination close to U_MGMT.

USB-C CC resistors and VBUS protection/current handling remain separate capture blocks.

## Capture order

1. Place U_MGMT with the validated symbol/footprint.
2. Place power symbols and named rails.
3. Capture VREG network and decoupling.
4. Capture RUN/SWD.
5. Capture USB D+/D- and 27 ohm series resistors.
6. Add USB-C service/protection circuitry.
7. Run KiCad ERC.
8. Run netlist/package-binding checks.
9. Compare captured power topology against the current official RP2350B Minimal reference.

No electrical PASS is claimed by this contract alone.
