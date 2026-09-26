# SWD / recovery capture gate

Status: M3.7 source-gated interface definition.

This gate defines what must be known before J_SWD is materialized in the native
KiCad schematic. It deliberately does not invent a Tag-Connect pin numbering or
footprint.

## Required management signals

The recovery interface must expose:

- `MGMT_SWCLK` from U_MGMT SWCLK, QFN-80 pad 33.
- `MGMT_SWDIO` from U_MGMT SWDIO, QFN-80 pad 34.
- `MGMT_RUN` from U_MGMT RUN, QFN-80 pad 35.
- `MGMT_3V3` as the debugger target-voltage reference.
- `GND`.

RUN and SWD must remain usable without the Linux host.

## Connector decision gate

`management-bom.csv` currently locks only the connector *class*:
Tag-Connect/test-pad pattern, with a documented 2.54 mm adapter. Before a
numbered J_SWD symbol/footprint is captured, record and verify:

1. the exact Tag-Connect footprint or test-pad pattern;
2. its authoritative pin numbering;
3. which pin is VTREF, SWDIO, SWCLK, RUN/reset and GND;
4. whether any extra pins are NC or intentionally used;
5. mechanical keep-out / retention requirements;
6. the 2.54 mm adapter mapping.

Do not assign connector pin numbers from convention or memory.

## Native KiCad acceptance

J_SWD may move from `CLASS_LOCK` to a captured status only when:

- the selected footprint and pin map are recorded in the BOM or a source-lock
  file;
- U_MGMT pads 33, 34 and 35 are wired to the corresponding service nets;
- VTREF is `MGMT_3V3`;
- at least one GND connection is present;
- RUN has the source-qualified reset/default network required by the RP2354B
  reference design;
- KiCad netlist export confirms the service nets;
- ERC is run and any remaining findings are real/documented, not suppressed to
  make CI green.

Until then, the MCU pins are only `PIN_IDENTIFIED`.
