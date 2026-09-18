# Contributing to RetroSBC

RetroSBC welcomes hardware, HDL, software, documentation and qualification contributions.

## Principles

- Keep changes reviewable and documented.
- Prefer reproducible tools and open file formats.
- Do not commit proprietary ROMs, commercial OS images, keys, credentials or unredistributable firmware.
- Record component sources and datasheet revisions for hardware decisions.
- Do not silently change connector pinouts or electrical contracts.
- Treat hardware ABI, RetroBus and RetroCore ABI changes as compatibility-sensitive.
- Add tests/checks for machine-readable artifacts where practical.

## Hardware

KiCad is the intended source format. Generated fabrication files must never replace editable source files as the canonical design.

## HDL

Prefer an open build flow where technically practical. Imported cores require explicit license and provenance review.

## Software

Keep host-facing interfaces transport-independent where possible so FPGA communication can evolve from initial bring-up to PCIe without rewriting user tooling.
