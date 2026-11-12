#!/usr/bin/env python3
"""Offline HEAL teaching-log CSV validator. Performs no ROS/hardware operations."""
from __future__ import annotations

import argparse
import csv
import math
import sys
from pathlib import Path

REQUIRED = ("timestamp_sec", "joint1", "joint2", "joint3", "joint4", "joint5", "joint6")


def validate(path: Path) -> tuple[int, float]:
    """Return (sample_count, duration_seconds); raise ValueError on invalid input."""
    with path.open("r", encoding="utf-8-sig", newline="") as stream:
        reader = csv.DictReader(stream)
        headers = reader.fieldnames or []
        absent = [name for name in REQUIRED if name not in headers]
        if absent:
            raise ValueError("missing required columns: " + ", ".join(absent))

        previous = first = None
        count = 0
        for row_index, row in enumerate(reader, start=2):
            try:
                values = [float(row[name]) for name in REQUIRED]
            except (KeyError, TypeError, ValueError) as exc:
                raise ValueError(f"row {row_index}: invalid numeric field") from exc
            if not all(math.isfinite(value) for value in values):
                raise ValueError(f"row {row_index}: non-finite timestamp/joint value")
            timestamp = values[0]
            if previous is not None and timestamp <= previous:
                raise ValueError(f"row {row_index}: timestamp must be strictly increasing")
            if first is None:
                first = timestamp
            previous = timestamp
            count += 1

        if count < 2:
            raise ValueError("at least two joint-state samples are required")
        assert first is not None and previous is not None
        return count, previous - first


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv_file", type=Path)
    args = parser.parse_args()
    try:
        samples, duration = validate(args.csv_file)
    except (OSError, ValueError) as exc:
        print(f"INVALID: {exc}", file=sys.stderr)
        return 1
    print(f"VALID: {samples} samples; duration {duration:.6f} seconds")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
