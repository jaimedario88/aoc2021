import unittest
from .solution import (
    quantity_larger_measurements,
    quantity_sliding_window_larger_measurements,
)


class Day01Test(unittest.TestCase):
    def test_quantity_larger_measurements(self):
        self.assertEqual(
            quantity_larger_measurements(
                [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
            ),
            7,
        )

    def test_quantity_sliding_window_larger_measurements(self):
        self.assertEqual(
            quantity_sliding_window_larger_measurements(
                [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
            ),
            5,
        )
