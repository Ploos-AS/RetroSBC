# M2 — FPGA Memory, Configuration Flash and Clock Baseline

## External FPGA memory

Rev-A requirement remains **>=32 MiB dedicated SDR SDRAM**.

Preferred organization: 256 Mbit x16 SDR SDRAM (16M x16), 3.3 V, with an actively supported industrial-temperature option preferred.

The exact MPN is deliberately not frozen from a generic web listing. M2 must select from currently orderable parts and validate:
- x16 organization;
- capacity >=256 Mbit;
- supported clock/timing at the intended RetroCore rate;
- package routability from BG381;
- lifecycle and second-source risk;
- open HDL controller support.

This memory is for deterministic FPGA-side machine state/frame/audio/bus use and is independent of B1 LPDDR4X.

## FPGA configuration flash

Capacity target: **128 Mbit SPI/QSPI NOR**.

A Winbond W25Q128-class device is electrically suitable as a reference class (2.7–3.6 V, SPI/Dual/Quad), but the exact production OPN must pass the component/longevity policy before lock. Avoid marking an NRND variant as the production baseline.

The design must support recovery/programming through FPGA JTAG and external SPI flash programming flow.

## Clock plan

Provide separate clock footprints/domains for:
- FPGA fabric/reference clock;
- SERDES/PCIe reference as required by the chosen implementation;
- SDRAM clock generated/managed by FPGA;
- optional retro/video clock requirements.

Clock oscillator power must be locally filtered/decoupled. Do not source a critical SERDES reference from a casual GPIO.

Exact oscillator frequencies/MPNs are locked only after the PCIe and representative RetroCore timing plan is compiled.
