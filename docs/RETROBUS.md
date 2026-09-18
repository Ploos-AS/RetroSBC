# RetroBus

RetroBus is the proposed expansion interface for RetroSBC.

## Goals

- useful for breadboards, adapters and custom retro hardware;
- FPGA-friendly;
- clearly labelled and documented;
- electrically safe for normal development mistakes;
- expose power and ground generously;
- support digital buses, interrupts and clocks;
- permit selected 5 V retro interfaces through appropriate translation;
- avoid copying another SBC header merely for compatibility.

## Candidate signal classes

The final pinout is intentionally deferred to M1.

- 5 V
- 3.3 V
- optional 1.8 V reference
- ground
- FPGA GPIO
- clock
- interrupt
- chip-select
- read/write or direction/control
- data bus
- address/control signals
- I2C/SPI/UART as muxable functions where useful

## Safety

FPGA pins must not be directly exposed to arbitrary 5 V signals unless the selected FPGA/device bank explicitly permits it. Level shifting, buffering and protection are part of the interface design, not optional accessories.
