# M3.4 — BG381 package capability map

Status: **authoritative package-level constraints recorded; exact balls still unbound**

Target: LFE5UM-85F-7BG381I.

## Vendor-confirmed package facts

The official Lattice ECP5/ECP5-5G family data sheet and ECP5 download set are the authority for package capabilities and pinout.

For LFE5UM-85 in 381 caBGA, the package provides:
- 205 user I/O;
- 4 SERDES channels;
- user I/O in banks 2, 3, 6 and 7;
- 65 high-speed differential input pairs / 33 differential output pairs across those banks;
- 8 DQS groups (>11 pins/group) across banks 2, 3, 6 and 7.

The Lattice download set also publishes the exact **ECP5UM-85 Pinout** CSV and **ECP5UM caBGA381 Migration** CSV. Exact package-ball assignment must come from those files, not from this summary.

## Bank-level planning

| Bank | Differential input/output pair capability | DQS groups | Rev-A planning role |
|---|---:|---:|---|
| 2 | 17 / 9 | 2 | SDRAM candidate / high-speed-capable GPIO |
| 3 | 16 / 8 | 2 | SDRAM candidate / video / GPIO |
| 6 | 16 / 8 | 2 | retro I/O / video / GPIO candidate |
| 7 | 16 / 8 | 2 | retro I/O / video / GPIO candidate |

This is a planning classification only. SDRAM placement is not locked to a bank until exact pinout, board escape/routing and clock/DQS capabilities are reviewed.

## Raw capacity versus current inventory

Current logical inventory: 145 generic-I/O rows, including 32 optional maker GPIO rows.

The package advertises 205 user I/O, so the raw arithmetic headroom is 60 I/O positions. That number is **not** equivalent to 60 freely assignable GPIO because bank voltage, clock-capable pins, differential pairing, configuration, routing locality and high-speed resource constraints reduce practical freedom.

The 32-pin maker-GPIO target therefore remains plausible and is retained for placement qualification.

## Placement order

1. reserve configuration/JTAG/dedicated resources;
2. reserve SERDES and reference-clock resources;
3. place SDRAM as a coherent timing group;
4. place FPGA video and required clock/differential resources;
5. place host-control and fixed retro I/O;
6. place RetroBus;
7. place up to 32 maker GPIO from the remaining compatible I/O.

## PASS gate

Package-level capability planning is PASS when CI is green. Exact pin-placement remains OPEN until the official pinout CSV is normalized into the binding table and checked for:
- duplicate balls;
- bank/VCCIO compatibility;
- clock capability;
- differential-pair requirements;
- reserved/configuration resources;
- physical routing practicality.
