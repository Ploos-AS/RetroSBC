# M3 — AGA Synthesis Qualification Plan

Status: **M3.0 STARTED**

## Reference

The current MiSTer Minimig-AGA repository is the reference for AGA feature/capacity investigation. It is Verilog and is published as GPL-licensed upstream material.

## Important consequence

RetroSBC's own FPGA/hardware licensing remains CERN-OHL-P-2.0. GPL Minimig RTL is therefore **not copied into the RetroSBC source tree as if it were native RetroCore RTL**. Qualification must preserve upstream provenance/license, preferably by fetching a pinned upstream revision in CI or by using a separately maintained adapter/core repository.

## Porting risks

MiSTer targets Intel Cyclone V and includes platform-specific integration. ECP5 qualification may require replacement/adaptation of:
- PLL/clock primitives;
- memory interface;
- MiSTer HPS framework;
- video/DDR plumbing;
- vendor RAM/DSP primitives where inferred incompatibly;
- top-level constraints.

Therefore a failed direct Yosys build would not mean the 85F lacks capacity; vendor/platform dependencies must first be separated from portable machine RTL.

## Gates

### M3.0 — toolchain target
- [x] define ECP5UM-85F/CABGA381 Yosys/nextpnr target;
- [x] add small native RTL smoke design;
- [ ] run CI and retain utilization/timing logs.

### M3.1 — upstream audit
- [ ] pin an exact Minimig-AGA upstream revision;
- [ ] record upstream license/provenance;
- [ ] classify portable RTL vs MiSTer/Cyclone-V integration;
- [ ] enumerate required ECP5 adapters.

### M3.2 — AGA synthesis
- [ ] synthesize portable/adapted AGA design with Yosys;
- [ ] place-and-route on ECP5UM-85F;
- [ ] archive LUT/FF/BRAM/DSP utilization;
- [ ] archive max-frequency/timing result;
- [ ] compare against <=70% LUT planning target.

### M3.3 — 45F comparison
Only after 85F succeeds, repeat against 45F to determine whether a cost-reduced SKU is technically useful.

## Interpretation

Capacity is proven only by a representative adapted build. Upstream Cyclone-V utilization numbers are evidence for planning, not proof of ECP5 fit.
