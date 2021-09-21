import unittest
import numpy as np

from task import a, b, c, stacked


class TestCase(unittest.TestCase):
    def test_arr(self):
        np.testing.assert_array_equal(b, np.arange(4).reshape(1, 4),
                                      err_msg='Array b should be of shape (1, 4) and have values from 0 to 3.')
        np.testing.assert_array_equal(c, np.concatenate((a, np.arange(4).reshape(1, 4)), axis=0),
                                      err_msg='Array c is not what we expected!')
        np.testing.assert_array_equal(stacked, np.vstack((np.arange(10), np.arange(20, 30), np.arange(40, 50))),
                                      err_msg='Array stacked is not what we expected!')
