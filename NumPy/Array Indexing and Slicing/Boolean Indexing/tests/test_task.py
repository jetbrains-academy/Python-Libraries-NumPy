import unittest
import numpy as np

from task import a, mask, c


class TestCase(unittest.TestCase):
    def test_add(self):
        test_a = np.arange(20).reshape(2, 2, 5)
        test_b = np.array([[True, False], [False, True]])
        np.testing.assert_array_equal(a, test_a, err_msg='Array `a` seems off!')
        np.testing.assert_array_equal(c, test_a[test_b], err_msg='Array `c` seems off!')
        np.testing.assert_array_equal(mask, test_b, err_msg='Something wrong with the mask array!')


