#!/usr/bin/env python3
"""Validate an authoritative RP2354B/RP2350B QFN-80 pin transcription."""
import csv
import sys
from pathlib import Path

REQUIRED_COLUMNS = {"pad", "pin_name", "pin_type", "source"}
EXPECTED_PADS = set(range(1, 81))

def main(path: str) -> int:
    p = Path(path)
    with p.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    if not rows:
        print("FAIL: no rows")
        return 1
    missing_cols = REQUIRED_COLUMNS - set(rows[0])
    if missing_cols:
        print("FAIL: missing columns:", ", ".join(sorted(missing_cols)))
        return 1
    pads = []
    errors = []
    for n, row in enumerate(rows, start=2):
        try:
            pad = int(row["pad"])
        except ValueError:
            errors.append(f"line {n}: invalid pad {row['pad']!r}")
            continue
        pads.append(pad)
        if not row["pin_name"].strip():
            errors.append(f"line {n}: empty pin_name")
        if not row["pin_type"].strip():
            errors.append(f"line {n}: empty pin_type")
        if not row["source"].strip():
            errors.append(f"line {n}: empty source")
    seen = set()
    dup = sorted({x for x in pads if x in seen or seen.add(x)})
    actual = set(pads)
    missing = sorted(EXPECTED_PADS - actual)
    extra = sorted(actual - EXPECTED_PADS)
    if len(rows) != 80:
        errors.append(f"expected 80 rows, got {len(rows)}")
    if dup:
        errors.append(f"duplicate pads: {dup}")
    if missing:
        errors.append(f"missing pads: {missing}")
    if extra:
        errors.append(f"out-of-range pads: {extra}")
    if errors:
        for e in errors:
            print("FAIL:", e)
        return 1
    print("PASS: QFN-80 transcription contains exactly pads 1..80 with required metadata")
    return 0

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"usage: {sys.argv[0]} <qfn80.csv>")
        raise SystemExit(2)
    raise SystemExit(main(sys.argv[1]))
