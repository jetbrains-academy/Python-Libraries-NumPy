import unittest
import numpy as np

from task import a, b, c


class TestCase(unittest.TestCase):
    def test_a(self):
        a_test = np.array([['clear', 'conscience', 'is'],
                           ['usually', 'the', 'sign'],
                           ['of', 'bad', 'memory']])
        np.testing.assert_array_equal(a, a_test, err_msg='Array `a` is off.')

    def test_b(self):
        b_test = np.array([[0, 3, 6], [1, 4, 7], [2, 5, 8]]).transpose()
        np.testing.assert_array_equal(b, b_test, err_msg='Array `b` is off.')

    def test_c(self):
        c_test = np.arange(12).reshape(3, 2, 2).transpose()
        np.testing.assert_array_equal(c, c_test, err_msg='Array `c` is off.')

