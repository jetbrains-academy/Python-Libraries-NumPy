import unittest
import numpy as np

from task import x, y, a, b, c, d, e


class TestCase(unittest.TestCase):
    def test_shape_a(self):
        self.assertEqual((4,), a.shape, msg='Wrong shape of array a.')

    def test_shape_b(self):
        self.assertEqual((3, 3), b.shape, msg='Wrong shape of array b.')

    def test_shape_c(self):
        self.assertEqual((3, 7), c.shape, msg='Wrong shape of array c.')

    def test_shape_d(self):
        self.assertEqual((3,), d.shape, msg='Wrong shape of array d.')

    def test_shape_e(self):
        self.assertEqual((3,), e.shape, msg='Wrong shape of array e.')

    def test_array_a(self):
        np.testing.assert_array_equal(a, x[np.array([7, 13, 28, 33])], err_msg='Array a is not what we expected.')

    def test_array_b(self):
        np.testing.assert_array_equal(b, x[np.array([[0, 1, 2], [10, 11, 12], [28, 29, 30]])], err_msg='Array b is not what we expected.')

    def test_array_c(self):
        np.testing.assert_array_equal(c, y[np.array([0, 2, 4])], err_msg='Array c is not what we expected.')

    def test_array_d(self):
        np.testing.assert_array_equal(d, y[np.array([0, 2, 4]), np.array([0, 1, 2])], err_msg='Array d is not what we expected.')

    def test_array_e(self):
        np.testing.assert_array_equal(e, y[np.array([1, 2, 4]), 6], err_msg='Array e is not what we expected.')
