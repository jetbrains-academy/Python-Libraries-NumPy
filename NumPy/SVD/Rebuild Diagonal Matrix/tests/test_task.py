import unittest
import numpy as np
from task import U, s, Vt, Sigma


class TestCase(unittest.TestCase):
    def test_shape(self):
        test_sigma = np.zeros((U.shape[1], Vt.shape[0]))
        np.fill_diagonal(test_sigma, s)
        self.assertEqual(test_sigma.shape, Sigma.shape, 'Wrong shape of Sigma array.')

    def test_sigma(self):
        test_sigma = np.zeros((U.shape[1], Vt.shape[0]))
        np.fill_diagonal(test_sigma, s)
        np.testing.assert_array_equal(Sigma, test_sigma,
                                      'The values in the resulting Sigma array do not match the expected.')
