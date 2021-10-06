import unittest
import numpy as np

from task import *

test_values, test_labels = np.array(csv[:, :2], dtype=float), np.array(csv[:, 2], dtype=np.int64)


class TestCase(unittest.TestCase):
    def test_input(self):
        np.testing.assert_array_equal(test_values, values, err_msg='Input values were not extracted properly from the '
                                                                   'csv.')
        np.testing.assert_array_equal(test_labels, labels, err_msg='Labels were not extracted properly from the '
                                                                   'csv.')

    def test_predict(self):
        result = predict(values)
        test_result = predict(test_values)
        np.testing.assert_array_equal(result, test_result, err_msg='Something wrong with the prediction.')

