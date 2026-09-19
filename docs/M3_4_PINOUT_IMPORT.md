# M3.4 — ECP5 vendor pinout import

The project now has a deterministic import step for the official Lattice ECP5UM-85 pinout CSV.

Run:

```sh
python3 tools/normalize_ecp5_pinout.py <official-lattice-pinout.csv> hardware/fpga/lfe5um85-bg381-vendor-normalized.csv
```

The importer does not fetch or invent data. It normalizes the vendor file into:
- package_ball
- bank
- vendor_function
- source_row

The normalized file is then reviewed and used to populate the canonical Rev-A binding table.

## Safety gate

Physical `UNBOUND` values may only be replaced after:
1. the input file is confirmed to be the official Lattice ECP5UM-85 pinout;
2. the detected columns are reviewed;
3. the normalized row count and package functions are sanity-checked;
4. configuration/JTAG/power/ground/NC/reserved resources are classified;
5. duplicate-ball validation passes.

This keeps exact pin binding reproducible without committing guessed ball names.
