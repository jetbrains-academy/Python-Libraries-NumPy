import unittest
import numpy as np

from task import img, img_rescaled, img_max, img_min, rescaled_max, rescaled_min


class TestCase(unittest.TestCase):
    def test_img_array(self):
        np.testing.assert_array_equal(img_rescaled, img / 255, err_msg='The data was not rescaled correctly.')

    def test_max_min_initial(self):
        self.assertEqual(255, img_max, msg='Incorrect max value for initial array.')
        self.assertEqual(0, img_min, msg='Incorrect min value for initial array.')

    def test_max_min_result(self):
        self.assertEqual(1.0, rescaled_max, msg='Incorrect max value for rescaled array.')
        self.assertEqual(0.0, rescaled_min, msg='Incorrect min value for rescaled array.')