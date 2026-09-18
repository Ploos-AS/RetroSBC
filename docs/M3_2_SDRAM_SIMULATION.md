# M3.2 — SDRAM protocol simulation

Status: **CI QUALIFICATION ADDED**

The controller now has a self-checking RTL testbench. It checks the observable command protocol rather than claiming electrical SDRAM qualification.

Covered:
- CKE/power-up completion;
- PRECHARGE during initialization;
- at least two initialization AUTO REFRESH commands;
- LOAD MODE REGISTER;
- READ completion and returned data;
- WRITE command and byte-mask behavior;
- periodic refresh after initialization;
- request completion timeout.

This remains a controller-level simulation. Datasheet timing, board constraints, signal integrity and hardware operation remain gates after the production SDRAM MPN is selected.
