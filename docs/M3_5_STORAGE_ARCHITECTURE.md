# M3.5 — Rev-A storage architecture

Status: **architecture lock candidate**

RetroSBC needs storage for two distinct domains: the Linux/K1 host and FPGA machine cores. They must not depend on a single removable medium.

## Linux/K1 storage

### Mandatory onboard eMMC
Rev-A shall provide onboard eMMC as the robust default Linux system storage.

K1 provides an 8-bit eMMC 5.1 interface with HS200/HS400 capability. The board shall route this to soldered eMMC, subject to final B1 module interface availability.

Target capacity:
- 32 GiB minimum production target;
- 64 GiB preferred standard configuration;
- larger compatible devices permitted.

Linux root filesystem should normally live on eMMC rather than removable microSD.

### Mandatory removable microSD
A dedicated K1 SD interface shall provide a user-accessible microSD slot for:
- installation/recovery;
- removable datasets;
- disk images/ROM assets where legally supplied by the user;
- diagnostics and field service.

K1 supports SD 3.0 UHS-I. Exact B1 exposure and voltage switching must be confirmed from the module documentation.

### NVMe
M.2 NVMe remains a preferred/high-value Rev-A option using the reserved K1 PCIe path. It is intended for large image libraries, build trees, RAB/archive use and high-write workloads.

NVMe does not replace onboard eMMC: the machine should remain bootable and useful without an M.2 device installed.

## FPGA storage

### Dedicated FPGA microSD
Rev-A shall provide a **separate physical microSD slot directly accessible by the FPGA**.

Purpose:
- standalone core assets;
- floppy/HDD/tape/cartridge images;
- FPGA-only boot/diagnostic content;
- core qualification without Linux in the real-time data path.

Baseline electrical interface:
- 3.3 V;
- SPI-mode support is mandatory for first bring-up;
- native 4-bit SD mode is preferred if FPGA pin budget and implementation permit;
- card detect preferred;
- ESD protection and local decoupling;
- no electrical sharing with the Linux microSD slot.

The FPGA slot must remain usable even if Linux is unavailable.

## Host/FPGA sharing

Linux may transfer assets to FPGA SDRAM or expose files through the host-control/high-speed bridge, but this is an additional service rather than the only FPGA storage path.

Direct physical dual-master access to the same SD/eMMC bus is not a Rev-A requirement; avoiding it simplifies arbitration and failure modes.

## Recommended Rev-A hierarchy

1. **eMMC (Linux, onboard, mandatory)** — robust OS/root storage.
2. **microSD (Linux/K1, mandatory)** — recovery/removable media.
3. **microSD (FPGA, mandatory)** — direct core storage.
4. **M.2 NVMe (Linux/K1, preferred)** — high-capacity/high-performance storage.
5. FPGA SDRAM — volatile working memory, not persistent storage.

## Qualification gates

Before schematic lock:
- verify B1 exposes K1 eMMC and SD interfaces required by this plan;
- lock eMMC voltage, package and capacity family;
- decide FPGA SD SPI-only vs SPI + native 4-bit routing;
- account for FPGA SD signals in M3.4 pin placement;
- define card-detect/write-protect behavior;
- define ESD/power/current-limit circuitry;
- verify M.2 lane allocation against the K1/B1 PCIe plan.
