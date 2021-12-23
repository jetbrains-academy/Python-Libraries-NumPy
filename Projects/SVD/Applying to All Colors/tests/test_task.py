import unittest
import numpy as np
from numpy import linalg
from task import img_rescaled, img_array_transposed, U, s, Vt


class TestCase(unittest.TestCase):
    def test_transpose(self):
        np.testing.assert_array_equal(img_array_transposed, np.transpose(img_rescaled, (2, 0, 1)),
                                      'The transposed array does not look right.')

    def test_svd(self):
        transposed_test = np.transpose(img_rescaled, (2, 0, 1))
        U_test, s_test, Vt_test = linalg.svd(transposed_test)
        np.testing.assert_array_equal(U, U_test,
                                      'Your decomposition does not look right. Go back to "SVD on One Matrix" to refresh the topic.')
        np.testing.assert_array_equal(s, s_test,
                                      'Your decomposition does not look right. Go back to "SVD on One Matrix" to refresh the topic.')
        np.testing.assert_array_equal(Vt, Vt_test,
                                      'Your decomposition does not look right. Go back to "SVD on One Matrix" to refresh the topic.')
