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
- serial/MIDI;
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
