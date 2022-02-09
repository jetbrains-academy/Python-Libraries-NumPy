import unittest
import numpy as np

from task import create_arrays


class TestCase(unittest.TestCase):
    def test_dtype_ones(self):
        a, b = create_arrays(2, 3)
        self.assertEqual('int64', a.dtype, msg="Wrong dtype in the .ones array.")

    def test_shape_ones(self):
        a, b = create_arrays(2, 3)
        self.assertEqual((2, 3), a.shape, msg="Wrong shape of the .ones array.")

    def test_dtype_full(self):
        a, b = create_arrays(2, 3)
        self.assertEqual('bool', b.dtype, msg="Wrong dtype in the .full array.")

    def test_shape_full(self):
        a, b = create_arrays(2, 3)
        self.assertEqual((2, 3), b.shape, msg="Wrong shape of the .full array.")

