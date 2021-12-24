import unittest
import numpy as np

from task import img, red_pixel_data


class TestCase(unittest.TestCase):
    def test_red(self):
        expected, actual = img[:, :, 0], red_pixel_data
        np.testing.assert_array_equal(expected, actual, err_msg="Got a wrong red array.")

