# M3.7 — QFN-80 footprint source evidence

This is the evidence ledger for the physical footprint. It intentionally records graphical dimensions as **IMAGE_REVIEW_REQUIRED** instead of inventing values from text extraction.

The current RP2350 datasheet identifies the QFN-80 as 10×10 mm with reduced ePad size and the package has 0.4 mm pitch. The datasheet's QFN-80 pinout also identifies the centre GND pad and all 80 numbered perimeter pads. citeturn0search0turn4view0

## Important source limitation

The package drawing is graphical. Text extraction exposes the package identity and pinout, but does not reliably expose every mechanical dimension callout. Therefore lead dimensions, exposed-pad dimensions and land-pattern values are not promoted to numeric source-of-truth values until the drawing itself is visually inspected.

This is deliberate: **no guessed land pattern**.

## Land pattern source

Raspberry Pi's hardware-design guide states that the RP2350B Minimal design is the reference design for the QFN-80 family and recommends closely following the layout/component selections, especially around the switching regulator. citeturn0search1

The eventual footprint must therefore be checked against both:
1. the dimensioned package drawing;
2. the official Minimal-B PCB/footprint implementation.

## Next gate

Complete the IMAGE_REVIEW_REQUIRED rows, attach the exact drawing callout/figure for each value, then generate the KiCad footprint and validate pad numbering/orientation and EP/GND.
