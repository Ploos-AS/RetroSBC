# M3.7 — Management MCU flash architecture lock

Status: **Rev-A architecture lock**

## Decision

Use **RP2354B** as the preferred fitted Rev-A management controller, subject to sourcing qualification.

RP2354B keeps the B-package I/O capacity while integrating **2 MiB flash** in the package. This is preferred over RP2350B plus an external boot flash for the standard board.

## Why integrated flash

For the management controller, simplicity and recovery are more valuable than large application storage.

Integrated flash:
- removes a separate external boot-flash IC from the normal BOM;
- removes associated QSPI routing and passives;
- reduces assembly and sourcing points;
- frees board area;
- reduces opportunities for boot-flash routing/assembly faults;
- keeps management firmware storage local to the MCU package.

The management firmware target is small enough that 2 MiB is ample for the expected service/debug/reset/telemetry functions.

## RP2350B fallback

Keep **RP2350B + external QSPI flash** as an approved fallback/alternate design path if:
- RP2354B availability is poor;
- RP2354B pricing is materially worse;
- qualification finds an integrated-flash limitation;
- an application later requires substantially more management firmware storage.

The schematic should preserve migration practicality where possible, but Rev-A does not need to fit both flash architectures simultaneously.

## Firmware storage policy

The management firmware should keep persistent configuration small and versioned.

Large logs, captures, FPGA assets or Linux data do not belong in management flash. They belong on Linux storage or the appropriate FPGA storage path.

## Recovery

Even with integrated flash, Rev-A shall provide:
- SWD programming/debug pads;
- documented boot/recovery entry;
- reset access;
- factory programming/test points;
- reproducible firmware build and flash procedure.

## Security posture

Do not enable irreversible security/OTP settings during ordinary development or manufacturing bring-up.

Any future secure-boot/signing policy must have a documented owner-recovery procedure before irreversible configuration is permitted.

## Remaining qualification

Before BOM lock:
1. verify RP2354B A4-or-later production availability;
2. verify exact package/ordering code;
3. confirm open SDK/toolchain support for the selected part;
4. prototype USB composite service interface;
5. qualify integrated-flash update/recovery;
6. lock management pin map and power/reset topology.
