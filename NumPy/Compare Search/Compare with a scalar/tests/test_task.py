import unittest
import numpy as np

from task import filtered_arr, arr


# todo: replace this with an actual test
class TestCase(unittest.TestCase):
    def test_filter_shape(self):
        filter_ = arr % 4 == 0
        np.testing.assert_array_equal(filtered_arr.shape, arr[filter_].shape, err_msg='filtered_array shape does not match the expected shape.')

    def test_filter(self):
        filter_ = arr % 4 == 0
        np.testing.assert_array_equal(filtered_arr, arr[filter_], err_msg='filtered_array does not match the expected result.')
