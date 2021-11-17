import unittest
import numpy as np

from task import a, b, x


class TestCase(unittest.TestCase):
    def test_arrays_shape(self):
        self.assertEqual((5, 2), b.shape, msg="Wrong shape of array b.")

    def test_array_content(self):
        self.assertEqual(19, a, msg="a has to be equal to 19.")

    def test_array_b(self):
        np.testing.assert_array_equal(b, x[::2, ::2], err_msg='Something wrong in array b.')

