# M3.2 — SDR SDRAM production part lock

Status: **EXACT REV-A PART LOCK — electrical/PCB qualification pending**

## Primary Rev-A SDRAM

RetroSBC selects **ISSI IS42S16320B-6TLI** as the primary Rev-A dedicated FPGA SDR SDRAM.

Required characteristics:

- 512 Mbit / 64 MiB total density;
- 32M x16 organization (8M x16 x 4 banks);
- 3.3 V VDD/VDDQ;
- x16 data bus;
- four banks;
- 8K refresh cycles / 64 ms for industrial/commercial grades;
- CAS latency 2 or 3;
- JEDEC SDR SDRAM command interface;
- 54-pin TSOP-II preferred for maker-friendly Rev-A assembly and inspection.

Exact ordering code: **IS42S16320B-6TLI**.

- speed grade: -6 (166 MHz CL3; 100 MHz CL2 supported);
- temperature: Industrial, -40 °C to +85 °C;
- package: 54-pin TSOP-II;
- supply: 3.3 V;
- organization: 32M x16 / four banks.

The controller qualification point remains 100 MHz / CL2, intentionally below the device's CL3 maximum. Do not substitute the 2.5 V IS42R family.

## Controller geometry contract

For x16 IS42S16320F:

- BA[1:0]: four banks;
- row: A[12:0] (8192 rows);
- column: A[9:0] (1024 x16 columns);
- A10 is auto-precharge during READ/WRITE and PRECHARGE-ALL select during PRECHARGE;
- DQM[1:0] maps to the two byte lanes.

The controller address contract shall be explicitly **word addressed** at the physical SDRAM-controller boundary. A 25-bit word address spans 32M x16 words = 64 MiB. Byte-addressed masters must translate before this boundary.

## Initial timing target

Use a conservative **100 MHz maximum controller qualification point with CL=2** until PCB timing and the exact speed suffix are frozen. Timing parameters must be derived from the selected suffix datasheet and rounded up in clock cycles.

## Qualification still required

1. confirm distributor stock/procurement and define an approved alternate if required;
2. correct controller READ/WRITE A10 policy (explicit precharge vs auto-precharge, never both);
3. derive tRP/tRCD/tRFC/tMRD/tWR and refresh interval from the exact datasheet;
4. add a behavioral SDRAM model or stronger protocol assertions;
5. bind ECP5 bank voltage/pins and PCB constraints;
6. post-route timing;
7. physical board memory test.

This document is a component/geometry lock, not physical qualification.
