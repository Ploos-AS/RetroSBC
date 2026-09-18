# FPGA qualification

This directory defines reproducible FPGA capacity qualification for RetroSBC.

## AGA reference gate

The AGA gate intentionally starts as an **upstream audit + synthesis harness**, not as copied HDL. MiSTer Minimig-AGA is GPL-licensed and its top-level platform integration targets Cyclone V/MiSTer, so importing it directly into RetroSBC would mix license obligations and vendor-specific primitives into the board repository.

M3.0 therefore has two steps:

1. CI proves that the open ECP5UM-85F toolchain target works.
2. AGA RTL is qualified in an isolated external-source job/adapter, preserving its upstream license and provenance.

Target command class for the board FPGA is:

```sh
yosys -p 'synth_ecp5 -top <top> -json build.json' ...
nextpnr-ecp5 --um5g-85k --package CABGA381 --json build.json ...
```

No Kickstart ROM is required or permitted for synthesis qualification.
