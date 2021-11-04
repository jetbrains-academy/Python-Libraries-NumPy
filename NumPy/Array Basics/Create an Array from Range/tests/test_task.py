import unittest
import numpy as np
from task import array_from_range

try:
    down = array_from_range(100, 0, -10)


    class TestCase1(unittest.TestCase):
        def test_step(self):
            np.testing.assert_array_equal(np.arange(100, 0, -10), down, err_msg='Your function does not produce the '
                                                                                'expected result when step argument is provided.')

        def test_no_step(self):
            up = array_from_range(100, 110)

            np.testing.assert_array_equal(np.arange(100, 110), up, err_msg='Your function does not produce the '
                                                                           'expected result when step argument is not provided.')
except TypeError:
    class TestCase2(unittest.TestCase):
        def test_bad(self):
            self.assertTrue(False, msg='Your function definition possibly has an invalid number of arguments.')
