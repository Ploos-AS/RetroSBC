# M3.3 — FPGA core compatibility contract

RetroSBC is intentionally a **multi-core FPGA platform**, not a board tied to one Ploos-AS core.

## Core classes

1. **Native RetroCore cores** — cores developed specifically for RetroSBC.
2. **Third-party adapted cores** — upstream FPGA cores retained under their original licenses and connected through a RetroSBC platform wrapper.
3. **Compatibility layers** — adapters for common MiST/MiSTer-style machine-core interfaces where technically and legally practical.

The goal is to make systems such as Amiga/Minimig, Atari ST, Commodore 64, 8-bit Atari, ZX Spectrum, MSX and other suitable cores practical on RetroSBC. Compatibility is per-core and must be qualified; no claim is made that an arbitrary MiSTer bitstream can run unchanged on ECP5.

## Platform services exposed to cores

A RetroSBC wrapper may provide:
- dedicated x16 SDR SDRAM;
- clocks and reset;
- Linux-host control/asset loading;
- video path;
- audio;
- USB keyboard/mouse/gamepad via host;
- physical DB9 ports;
- independent Linux-host and FPGA serial ports;
- MIDI;
- storage/image services;
- RetroBus and selected GPIO;
- optional FPGA/host high-speed transport.

## DB9 / joystick contract

Rev-A requires **two physical DE-9 (DB9) retro controller ports**.

They are first-class FPGA-facing ports intended for:
- Atari-standard digital joysticks;
- Amiga joysticks;
- compatible C64-style digital joysticks;
- mouse/paddle extensions where a core-specific adapter and electrical policy explicitly support them.

The ports are not raw FPGA pins. They require 5 V tolerant level translation/protection, current limiting where power is exported, ESD protection, and per-core direction/control policy.

Baseline digital signals per port:
- UP
- DOWN
- LEFT
- RIGHT
- FIRE1
- optional FIRE2/FIRE3 where the selected connector/electrical mapping permits
- GND
- protected peripheral supply where required

Mouse/paddle/analog behavior is **not assumed** merely because the connector is DE-9; each mode must be implemented and qualified.

## Third-party licensing

Third-party RTL remains under its upstream license. GPL cores such as Minimig are not relicensed as CERN-OHL-P-2.0 RetroCore RTL. Platform wrappers should be kept separable so license boundaries remain explicit.

## Initial qualification targets

- Minimig/Amiga OCS/ECS/AGA
- Atari ST/STe
- Commodore 64
- one simple 8-bit core as the portability/reference test

Each target receives a manifest describing upstream revision, license, resource use, clocks, memory, video/audio, input mapping and unsupported features.


## Serial-port contract

Rev-A requires **independent physical serial connectivity for both the Linux host and the FPGA**. Serial is a first-class RetroSBC function, not merely a debug header.

### Linux serial
The K1/B1 Linux side shall expose at least one dedicated UART through a real external serial interface. The preferred user-facing implementation is a standards-compliant RS-232 port using a MAX3232-class transceiver, while a separate 3.3 V TTL debug UART/header may be retained for bring-up and recovery.

### FPGA serial
The ECP5 shall expose an independent UART/serial path that FPGA cores can own directly without Linux bit-banging or forwarding being required. It shall support a real external RS-232 interface through appropriate level translation. This enables FPGA machines and BBS/terminal cores to behave like physical retro computers with their own serial hardware.

### Routing and bridging
Linux and FPGA serial interfaces remain independently usable. A controlled internal bridge/cross-connect may additionally allow Linux to communicate with, monitor, or service the FPGA UART, but this is supplementary and must not remove direct FPGA ownership.

Required design goals:
- Linux external RS-232;
- FPGA external RS-232;
- 3.3 V TTL debug UART for Linux bring-up;
- FPGA debug/auxiliary UART where practical;
- hardware flow-control signals where connector/pin budget permits;
- protection and proper RS-232 transceivers on external RS-232 connectors;
- no RS-232 voltage presented directly to B1 or ECP5 I/O.
