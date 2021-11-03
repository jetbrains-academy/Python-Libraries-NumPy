import unittest
import numpy as np
from task import reshape_transpose


def transpose_test(start, stop, step=1):
    array = np.arange(start, stop, step)
    reshaped = array.reshape(1, array.shape[0])
    return reshaped.T


class TestCase(unittest.TestCase):
    def test_transpose_shape(self):
        np.testing.assert_array_equal(transpose_test(0, 1000, 10).shape, reshape_transpose(0, 1000, 10).shape, err_msg='Expected and actual shapes do not match.')
        np.testing.assert_array_equal(transpose_test(100, 0, -10).shape, reshape_transpose(100, 0, -10).shape, err_msg='Expected and actual shapes do not match.')
        np.testing.assert_array_equal(transpose_test(0, 100).shape, reshape_transpose(0, 100).shape, err_msg='Expected and actual shapes do not match.')
