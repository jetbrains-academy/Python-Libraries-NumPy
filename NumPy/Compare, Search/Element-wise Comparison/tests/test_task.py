import unittest
import numpy as np

from task import *


class TestCase(unittest.TestCase):
    def test_array_b(self):
        test_b = np.arange(0, 25, 6)
        self.assertEqual(b.shape, test_b.shape, msg='Shape of array b has to be (5,).')

    def test_array_c(self):
        test_b = np.arange(0, 25, 6)
        test_c = np.equal(a, test_b)
        np.testing.assert_array_equal(compare_a_b, test_c, err_msg='Boolean arrays do not match.')
