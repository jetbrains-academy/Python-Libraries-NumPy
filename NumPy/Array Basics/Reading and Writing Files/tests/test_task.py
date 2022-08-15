import unittest
import numpy as np


from task import arr


class TestCase(unittest.TestCase):
    def test_arr_shape(self):
        self.assertEqual((100, 4), arr.shape, msg="Wrong array shape.")

    def test_arr(self):
        data = 'somedata.csv'
        test_arr = np.genfromtxt(data, delimiter=',', skip_header=3)
        np.testing.assert_array_equal(arr, test_arr, err_msg="Wrong array contents.")

