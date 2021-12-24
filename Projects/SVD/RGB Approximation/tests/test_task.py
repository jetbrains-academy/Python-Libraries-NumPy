import unittest
import numpy as np


class TestCase(unittest.TestCase):
    def test_approx(self):
        try:
            from task import U, Sigma, Vt, k, approx_img
            approx_img_test = U @ Sigma[..., :k] @ Vt[..., :k, :]
            self.assertEqual(approx_img_test.shape, approx_img.shape, 'Wrong shape of approx_img array.')
            np.testing.assert_array_equal(approx_img, approx_img_test, 'Something is wrong :/')

        except ValueError:
            self.fail('Check your slicing carefully.')
