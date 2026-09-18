# RetroCore

RetroCore is the proposed open FPGA framework used by RetroSBC.

It is not one emulated computer and should not become a collection of unrelated HDL projects. Its purpose is to provide reusable infrastructure around cores.

## Planned common services

- clock and reset management;
- host-visible identification and capability registers;
- standardized control/status registers;
- interrupt delivery;
- memory/data-transfer abstraction;
- trace/capture hooks;
- external I/O routing;
- core reset/run/stop control;
- versioned ABI.

## Design rule

Host applications should target a documented RetroCore ABI rather than knowing FPGA implementation details.

A core should be able to declare capabilities such as video, serial, controller ports, storage interfaces and debug features.

## M0 non-goals

M0 does not select or import third-party machine cores. Core licensing and provenance must be reviewed before integration.
