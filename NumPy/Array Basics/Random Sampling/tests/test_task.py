import unittest
import numpy as np

from task import *


class TestCase(unittest.TestCase):
    def test_draw(self):
        self.assertEqual((1000,), s.shape, msg="Draw 1000 samples.")

    def test_mean(self):
        self.assertEqual(0.0,  round(abs(mu - np.mean(s)), 1), msg="Mean should be close to 0.0.")

    def test_variance(self):
        self.assertEqual(0.0,  round(abs(sigma - np.std(s, ddof=1)), 1), msg="Variance should be close to 0.0.")

