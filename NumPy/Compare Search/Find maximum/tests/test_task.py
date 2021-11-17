import unittest
import numpy as np

from task import result


data = np.genfromtxt('data.csv', delimiter=',', dtype=np.int64)
maxima = np.argmax(data, axis=1)
maxima = np.expand_dims(maxima, axis=1)
test_result = np.take_along_axis(data, maxima, axis=1)


class TestCase(unittest.TestCase):
    def test_array(self):
        np.testing.assert_array_equal(result, test_result, err_msg='Your result does not match the expected.')

    def test_array_shape(self):
        self.assertEqual(test_result.shape, result.shape, msg='Shape of the array result should be (100, 1).')
