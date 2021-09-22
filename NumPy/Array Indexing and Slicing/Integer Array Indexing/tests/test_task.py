import unittest
import numpy as np

from task import x, y, a, b, c, d, e

class TestCase(unittest.TestCase):
    def test_shape(self):
        self.assertEqual(a.shape, (4,), msg='Wrong shape of array a.')
        self.assertEqual(b.shape, (3, 3), msg='Wrong shape of array b.')
        self.assertEqual(c.shape, (3, 7), msg='Wrong shape of array c.')
        self.assertEqual(d.shape, (3,), msg='Wrong shape of array d.')
        self.assertEqual(e.shape, (3,), msg='Wrong shape of array e.')

    def test_arrays(self):
        np.testing.assert_array_equal(a, x[np.array([7, 13, 28, 33])], err_msg='Array a is not what we expected.')
        np.testing.assert_array_equal(b, x[np.array([[0, 1, 2], [10, 11, 12], [28, 29, 30]])], err_msg='Array b is not what we expected.')
        np.testing.assert_array_equal(c, y[np.array([0, 2, 4])], err_msg='Array c is not what we expected.')
        np.testing.assert_array_equal(d, y[np.array([0, 2, 4]), np.array([0, 1, 2])], err_msg='Array d is not what we expected.')
        np.testing.assert_array_equal(e, y[np.array([1, 2, 4]), 6], err_msg='Array e is not what we expected.')
