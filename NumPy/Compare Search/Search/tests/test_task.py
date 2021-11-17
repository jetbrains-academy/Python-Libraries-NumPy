import unittest
import numpy as np

from task import temperatures, days, high, low, result, warm_days


class TestCase(unittest.TestCase):
    def test_week(self):
        high_test = ['High']
        low_test = ['Low']
        np.testing.assert_array_equal(result, np.where(temperatures > 15, high_test, low_test),
                                      err_msg='Your `result` array '
                                              'does not contain the values we expected.')

    def test_shape(self):
        self.assertEqual(days.shape, result.shape, msg='Shape of the array `result` should match the shape of `days`.')

    def test_names(self):
        np.testing.assert_array_equal(warm_days, days[temperatures > 15],
                                      err_msg='`warm_days` array is off. It should contain '
                                              'the names of days when temperature was higher than 15')
