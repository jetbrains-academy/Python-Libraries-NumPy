import unittest
import numpy as np


class TestCase(unittest.TestCase):

    def test_approx_k(self):
        try:
            from task import k, U, Sigma, Vt, approx
            approx_test = U @ Sigma[:, :k] @ Vt[:k, :]
            np.testing.assert_array_equal(approx, approx_test,
                                          'The approximation does not look right.')
        except ValueError:
            self.fail('You have to use only the first k columns of Sigma and the first k rows of Vt')