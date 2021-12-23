import unittest
import numpy as np
from task import img_array_transposed, U, s, Vt, Sigma, reconstructed


class TestCase(unittest.TestCase):
    def test_sigma_shape(self):
        self.assertEqual((3, 408, 612), Sigma.shape, msg="Wrong shape of Sigma array.")

    def test_sigma(self):
        Sigma_test = np.zeros((3, 408, 612))
        for j in range(3):
            np.fill_diagonal(Sigma_test[j, :, :], s[j, :])
        np.testing.assert_array_equal(Sigma, Sigma_test, err_msg="Sigma array is filled with values incorrectly.")

    def test_reconstructed(self):
        Sigma_test = np.zeros((3, 408, 612))
        for j in range(3):
            np.fill_diagonal(Sigma_test[j, :, :], s[j, :])
        reconstructed_test = U @ Sigma @ Vt
        np.testing.assert_array_equal(reconstructed, reconstructed_test, 'The reconstructed array appears incorrect.')

    def test_reconstructed_shape(self):
        Sigma_test = np.zeros((3, 408, 612))
        for j in range(3):
            np.fill_diagonal(Sigma_test[j, :, :], s[j, :])
        reconstructed_test = U @ Sigma @ Vt
        self.assertEqual(reconstructed_test.shape, reconstructed.shape, msg='Wrong shape of the reconstructed array.')

