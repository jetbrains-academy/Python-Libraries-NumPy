import unittest
import numpy as np
from numpy import linalg

from task import img_gray, U, s, Vt


class TestCase(unittest.TestCase):
    def test_svd(self):
        test_U, test_s, test_Vt = linalg.svd(img_gray)
        np.testing.assert_array_equal(U, test_U,
                                      'Matrix U doesn\'t match the expected. Use linalg.svd to complete the task.')
        np.testing.assert_array_equal(s, test_s,
                                      'Matrix s doesn\'t match the expected. Use linalg.svd to complete the task.')
        np.testing.assert_array_equal(Vt, test_Vt,
                                      'Matrix Vt doesn\'t match the expected.Use linalg.svd to complete the task.')
