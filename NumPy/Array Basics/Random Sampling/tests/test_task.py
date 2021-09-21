import unittest
import numpy as np

from task import *


class TestCase(unittest.TestCase):
    def test_normal(self):
        self.assertEqual(s.shape, (1000,), msg="Draw 1000 samples")
        self.assertEqual(round(abs(mu - np.mean(s)), 1), 0.0,  msg="Mean should be close to 0.0")
        self.assertEqual(round(abs(sigma - np.std(s, ddof=1)), 1), 0.0,  msg="Variance should be close to 0.0")

