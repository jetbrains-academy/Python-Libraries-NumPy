import unittest
import numpy as np
from numpy import linalg

from task import img_rescaled, img_gray


class TestCase(unittest.TestCase):
    def test_shape(self):
        correct = img_rescaled @ [0.2126, 0.7152, 0.0722]
        self.assertEqual(correct.shape, img_gray.shape,
                         'Matrix multiplication was performed incorrectly. Check out the hint.')

    def test_gray(self):
        correct = img_rescaled @ [0.2126, 0.7152, 0.0722]
        np.testing.assert_array_equal(img_gray, correct,
                                      'The gray matrix looks wrong. Please check the coefficients.')
