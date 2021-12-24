import unittest
import numpy as np

from task import img_rescaled, red_channel, green_channel, blue_channel


class TestCase(unittest.TestCase):
    def test_red(self):
        np.testing.assert_array_equal(red_channel, img_rescaled[:, :, 0],
                                      'Red slice looks incorrect.')

    def test_green(self):
        np.testing.assert_array_equal(green_channel, img_rescaled[:, :, 1],
                                      'Green slice looks incorrect.')

    def test_blue(self):
        np.testing.assert_array_equal(blue_channel, img_rescaled[:, :, 2],
                                      'Blue channel slice looks incorrect.')
