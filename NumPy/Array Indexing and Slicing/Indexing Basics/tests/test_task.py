import unittest
import numpy as np

from task import a, b, x


class TestCase(unittest.TestCase):
    def test_arrays_shape(self):
        self.assertEqual(b.shape, (5, 2), msg="Wrong shape of array b")
        self.assertEqual(type(a), np.int64, msg="a has to be a numpy.int64")

    def test_array_content(self):
        self.assertEqual(a, 19, msg="a has to be equal to 19")
        np.testing.assert_array_equal(b, x[::2, ::2], err_msg='Something wrong in array b!')

