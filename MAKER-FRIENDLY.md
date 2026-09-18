# Maker-Friendly Hardware Standard

RetroSBC follows the Ploos-AS maker-friendly hardware standard.

The default design priority is **maker friendly first, cost second**. Technical requirements may justify exceptions, but significant exceptions must be documented explicitly.

## PCB defaults

Prefer standard, broadly available fabrication capabilities and conservative design rules. Use two layers, 1.6 mm FR-4 and 1 oz copper where technically practical. RetroSBC is expected to require a multilayer PCB because of its compute module, FPGA, memory/high-speed interfaces and routing requirements; that is a documented project-specific exception, not a change to the general Ploos-AS standard.

Avoid manufacturer-specific processes when broadly supported alternatives are practical. Specialized stack-ups, controlled impedance, fine-pitch routing or other advanced requirements must be documented with reproducible fabrication parameters.

## Components

Component and BOM selection also follows [COMPONENT-POLICY.md](COMPONENT-POLICY.md).

Prefer parts that are actively available, have documented substitutes where practical, and are easy for makers to identify and source. Prefer hand-solderable packages and through-hole parts where they materially improve accessibility, learning, socketing or repair.

Avoid BGA, very fine-pitch packages, blind/buried vias, via-in-pad and similar specialized processes unless required by the design. RetroSBC's compute module and high-speed architecture may necessarily introduce maker-unfriendly technologies; keep those complexities contained where practical so maker-accessible I/O, expansion, debug and repair remain first-class goals.

## Assembly, expansion and repair

Where practical:

- provide accessible test points for power rails, clocks, reset, buses and diagnostic signals;
- expose useful UART/JTAG/debug interfaces;
- clearly label connectors, polarity, pin 1, jumpers, switches and test points;
- use standard connectors and fasteners;
- keep replaceable or serviceable parts accessible;
- design RetroBus and retro I/O for experimentation and safe probing;
- document power requirements and protection;
- provide useful bring-up and fault-finding procedures.

## Documentation

Released hardware should include the schematic, KiCad PCB source, qualified manufacturing package, BOM, assembly notes, connector/pinout documentation, programming instructions, test-point information, expected measurements, bring-up procedure, troubleshooting information and known substitutions where applicable.

## Manufacturer neutrality

The qualified manufacturing package must remain usable independently of PCBWay, JLCPCB, OSH Park or any other ordering service. Manufacturer-specific profiles and links are conveniences only.

## Exceptions

RetroSBC is more technically demanding than many maker boards. FPGA, compute-module, high-speed and multilayer requirements may override the default two-layer/simple-assembly preference.

Every significant exception should be justified in the hardware/manufacturing documentation, and the design should isolate unavoidable complexity rather than spreading it unnecessarily across the board.

## Qualification

Automated CI should enforce maker-friendly requirements that can be checked reliably from KiCad design data. Human-review requirements remain release checklist items. Passing manufacturing CI does not waive documented maker-friendly review or project-specific exception handling.
