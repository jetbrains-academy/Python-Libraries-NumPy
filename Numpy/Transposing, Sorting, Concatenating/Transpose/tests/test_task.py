import unittest
import numpy as np

from task import a, b, c


class TestCase(unittest.TestCase):
    def test_arrays(self):
        b_test = np.array([[0, 3, 6], [1, 4, 7], [2, 5, 8]]).transpose()
        c_test = np.arange(12).reshape(3, 2, 2).transpose()
        a_test = np.array([['clear', 'conscience', 'is'],
                           ['usually', 'the', 'sign'],
                           ['of', 'bad', 'memory']])
        np.testing.assert_array_equal(a, a_test, err_msg='Array `a` is off!')
        np.testing.assert_array_equal(b, b_test, err_msg='Array `b` is off!')
        np.testing.assert_array_equal(c, c_test, err_msg='Array `c` is off!')

