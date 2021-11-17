import unittest
import numpy as np

from task import a, b


class TestCase(unittest.TestCase):
    def test_a(self):
        np.testing.assert_array_equal(a, np.arange(12, 30, 3), err_msg='Array a is not what we expected.')

    def test_b(self):
        np.testing.assert_array_equal(b, a.reshape(2, 3), err_msg='Array b is not what we expected.')
