"""Unit tests for the offline (non-ROS) teaching-data checker."""
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from validate_teach_csv import validate  # noqa: E402

HEADER = "timestamp_sec,joint1,joint2,joint3,joint4,joint5,joint6\n"


class CsvValidationTest(unittest.TestCase):
    def run_validate(self, rows: str):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "samples.csv"
            path.write_text(HEADER + rows, encoding="utf-8")
            return validate(path)

    def test_valid(self):
        n, duration = self.run_validate("1,0,0,0,0,0,0\n1.01,0.1,0,0,0,0,0\n")
        self.assertEqual(n, 2)
        self.assertAlmostEqual(duration, 0.01)

    def test_repeated_timestamps(self):
        with self.assertRaisesRegex(ValueError, "strictly increasing"):
            self.run_validate("1,0,0,0,0,0,0\n1,0,0,0,0,0,0\n")

    def test_nan(self):
        with self.assertRaisesRegex(ValueError, "non-finite"):
            self.run_validate("1,0,0,0,0,0,0\n2,nan,0,0,0,0,0\n")

    def test_insufficient_samples(self):
        with self.assertRaisesRegex(ValueError, "at least two"):
            self.run_validate("1,0,0,0,0,0,0\n")


if __name__ == "__main__":
    unittest.main()
