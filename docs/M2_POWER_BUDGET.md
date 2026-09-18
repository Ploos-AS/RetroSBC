# M2 — Preliminary Power Budget

Status: **ENGINEERING BUDGET — not regulator sizing approval**

The carrier power design must be sized from measured/proven worst-case loads before schematic freeze. The following rails are now explicit because the selected ECP5UM requires them.

## FPGA rails

| Rail | Purpose | Rev-A rule |
|---|---|---|
| 1.1 V | ECP5 VCC core | dedicated low-voltage regulator |
| 1.1 V filtered | ECP5UM SERDES VCCA/VCCHRX/VCCHTX | quiet filtering per Lattice checklist |
| 2.5 V | VCCAUX and SERDES VCCAUXA | dedicated/qualified rail |
| 3.3 V | selected FPGA I/O banks, config flash, low-speed logic | general logic rail |
| SDRAM rail | FPGA external SDRAM | 3.3 V for SDR SDRAM baseline |
| 5 V peripheral | protected external/peripheral power | switched/current-limited |

Lattice's current hardware checklist calls for ECP5 1.1 V core, 2.5 V auxiliary, selectable 1.2–3.3 V VCCIO, and filtered SERDES supplies. SERDES analog rails must be treated as noise-sensitive.

## Decoupling contract

Use the current Lattice ECP5 hardware checklist at schematic/layout time. The present checklist recommends local bulk plus 100 nF-per-pin style decoupling and ferrite filtering on auxiliary/SERDES rails. Exact capacitor count/value placement follows the final device pinout and rail grouping.

## Budget method

M2 schematic freeze requires a spreadsheet/table containing:
- B1 maximum/peak module input load;
- FPGA static, configuration/inrush and implementation-dependent dynamic load;
- SDRAM peak load;
- USB VBUS allocation;
- NVMe allowance;
- Ethernet PHY load;
- HDMI/level-shifter/peripheral load;
- DB9/RetroBus externally available 5 V budget;
- regulator efficiency and thermal margin.

Use the Lattice power calculator once the representative RetroCore utilization and clocks exist.

## Margin

Regulators shall not be selected from typical load alone. Target engineering margin is >=25% after realistic worst-case load and conversion losses, unless a component-specific transient analysis requires more.
