# M3.5 — Linux/K1 persistent storage lock

Status: **Rev-A architecture lock; exact B1 routing and component MPNs remain qualification gates**

## eMMC

Onboard eMMC is the mandatory default Linux system disk.

Rev-A targets:
- eMMC 5.1;
- 8-bit data bus where exposed by B1;
- HS200/HS400 capability where the B1 routing and selected device permit;
- **64 GiB standard capacity**;
- 32 GiB acceptable as a cost-reduced assembly option;
- 128 GiB optional compatible assembly variant.

The schematic/PCB should use a JEDEC-standard eMMC BGA footprint selected from devices with multiple-source or migration potential where practical. The exact footprint and MPN must be locked before schematic capture; capacity alone is not sufficient qualification.

Linux rootfs, package database, logs and normal system state belong on eMMC by default. This avoids depending on a removable microSD card for normal operation.

## Linux microSD

A separate user-accessible K1/B1 microSD slot remains mandatory for:
- recovery/install media;
- diagnostics;
- removable transfer;
- alternate boot/service images.

It must not be electrically shared with the FPGA microSD slot.

## M.2 NVMe

Rev-A shall provide an M-key NVMe socket if B1 PCIe routing qualification passes.

Mechanical target:
- **M.2 2280 primary**;
- mounting positions for **2242 and 2230** should be included if board mechanics permit;
- PCIe x2 routed when B1 supports the reserved x2 path;
- x1 operation acceptable as an initial compatibility mode;
- 3.3 V power budget sized for realistic NVMe peak load;
- PERST#/CLKREQ#/reference-clock requirements implemented according to the final K1/B1 PCIe contract.

The socket is for NVMe/PCIe storage, not SATA M.2.

NVMe is optional for boot and operation. RetroSBC must remain fully usable from onboard eMMC without an SSD installed.

## Storage roles

| Medium | Domain | Rev-A | Default role |
|---|---|---|---|
| eMMC 64 GiB | Linux/K1 | mandatory | OS/rootfs and robust persistent state |
| K1 microSD | Linux/K1 | mandatory | recovery/removable media |
| FPGA microSD | FPGA | mandatory | direct core assets/images |
| M.2 NVMe | Linux/K1 | preferred, routing-gated | large/high-write storage |
| FPGA SDRAM | FPGA | mandatory | volatile working memory |

## Qualification gates

Before schematic lock:
1. obtain authoritative B1 module pin/mux documentation;
2. prove eMMC interface is exposed with the required bus width;
3. prove a dedicated K1 SD path is exposed;
4. prove the reserved PCIe x2/x1 path can reach the M.2 socket;
5. lock exact eMMC package/MPN and compatible alternates;
6. calculate eMMC + microSD + NVMe power budget;
7. define Linux boot/recovery order;
8. review M.2 placement, retention screw positions and thermal clearance.
