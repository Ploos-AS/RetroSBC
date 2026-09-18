# M3.2 — SDRAM Adapter

Status: **IMPLEMENTATION STARTED**

The first memory adapter establishes a 16-bit, byte-enabled request/acknowledge contract between machine RTL and the future physical SDR SDRAM controller.

## Why two layers

The AGA/machine side must not depend on a particular SDRAM chip or controller implementation. The bridge therefore separates:
- machine request/address/write-data/byte-enables;
- physical memory-controller request/response.

A small synthesizable model exists only for CI. It is explicitly **not** a DRAM timing model and must never be used as evidence that SDR SDRAM timing works.

## Addressing

The bridge currently exposes 25 address bits and a 16-bit datapath, enough architectural address space for the >=32 MiB Rev-A memory target. Final byte/word address semantics are frozen when the selected SDRAM controller and AGA memory map are connected.

## Next gates

- synthesize bridge/model with Yosys on the ECP5 flow;
- add simulation for read/write handshake;
- select physical SDR SDRAM MPN;
- implement ECP5 SDRAM controller/PHY;
- constrain SDRAM clock and I/O timing;
- connect representative AGA memory master;
- measure utilization and timing.
