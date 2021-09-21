import unittest
import numpy as np

from task import arr1, arr2, arr3, arr4, arr5, arr6


class TestCase(unittest.TestCase):
    def test_split_one(self):
        x = np.arange(24).reshape(6, 4)
        np.testing.assert_array_equal(arr1, np.split(x, 3)[0], err_msg='First split appears wrong!')
        np.testing.assert_array_equal(arr2, np.split(x, 3)[1], err_msg='First split appears wrong!')
        np.testing.assert_array_equal(arr3, np.split(x, 3)[2], err_msg='First split appears wrong!')

    def test_split_two(self):
        y = np.arange(12).reshape(3, 4)
        np.testing.assert_array_equal(arr4, np.array_split(y, 3, axis=1)[0], err_msg='Second split appears wrong!')
        np.testing.assert_array_equal(arr5, np.array_split(y, 3, axis=1)[1], err_msg='Second split appears wrong!')
        np.testing.assert_array_equal(arr6, np.array_split(y, 3, axis=1)[2], err_msg='Second split appears wrong!')


