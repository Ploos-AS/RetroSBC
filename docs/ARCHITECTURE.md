# RetroSBC Architecture

## Purpose

RetroSBC is a purpose-built RISC-V + FPGA development computer for retro computing, hardware experimentation, education and automated qualification.

The Linux host handles storage, networking, compilers, containers, orchestration and user-facing tools. The FPGA handles deterministic, timing-sensitive and electrically specialized functions.

## Major domains

### Linux host

Responsibilities include:

- development toolchains;
- Git/CI integration;
- emulators and runtime qualification;
- storage and networking;
- FPGA image management;
- capture, tracing and test orchestration;
- BBS and terminal services.

### FPGA

The FPGA is not an optional accelerator. It is a first-class architectural component intended for:

- classic CPU cores;
- bus and peripheral logic;
- video/timing generation;
- deterministic I/O;
- protocol adaptation;
- hardware-in-the-loop instrumentation;
- educational HDL experiments.

### RetroCore

RetroCore is the working name for the FPGA framework, not the SBC itself. It should provide common clock/reset, control, discovery, interrupt and data-transfer facilities so individual cores do not invent incompatible host interfaces.

### RetroBus

RetroBus is the working name for a documented expansion interface intended to expose useful FPGA/host signals and power rails to external retro hardware and experiments.

## Compute baseline

M0 uses the SpacemiT K1/B1 family as the leading compute candidate because a compute module can remove LPDDR routing and much of the SoC integration complexity from the carrier.

This remains subject to M1 qualification, especially documentation quality, small-volume sourcing, lifecycle, electrical data and long-term software support.

## FPGA baseline

M0 uses a Lattice ECP5UM 45K-class device as the leading FPGA candidate. The design should preserve an open synthesis/place-and-route/bitstream workflow where practical.

Exact device, speed grade and package remain M1 decisions.

## Host/FPGA transport

PCIe Gen2 is a desired high-performance transport, but the software architecture must not assume PCIe from day one.

Rev-A bring-up may use a simpler control path first. A transport-independent register/control API is therefore a requirement.

## Hardware-in-the-loop

RetroSBC should eventually permit workflows such as:

```text
source -> build -> deploy -> reset target -> execute -> capture -> compare -> report
```

The same orchestration model should support FPGA cores, emulators and attached physical retro hardware where possible.

## Assets and licensing

RetroSBC must not distribute copyrighted Kickstart ROMs, commercial operating-system images, firmware or other assets for which redistribution rights are unavailable.

Qualification tooling should accept user-supplied assets and document hashes/requirements without committing those assets.
