# M3.2 — SDR SDRAM production part lock

Status: **CANDIDATE LOCK — electrical/PCB qualification pending**

## Primary Rev-A SDRAM

RetroSBC selects the **ISSI IS42S16320F family** as the Rev-A dedicated FPGA SDR SDRAM baseline.

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

The exact purchasable ordering suffix (speed/temperature/package) remains a procurement gate. Do not substitute the 2.5 V IS42R family.

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

1. freeze exact orderable suffix and second-source/procurement evidence;
2. correct controller READ/WRITE A10 policy (explicit precharge vs auto-precharge, never both);
3. derive tRP/tRCD/tRFC/tMRD/tWR and refresh interval from the exact datasheet;
4. add a behavioral SDRAM model or stronger protocol assertions;
5. bind ECP5 bank voltage/pins and PCB constraints;
6. post-route timing;
7. physical board memory test.

This document is a component/geometry lock, not physical qualification.
