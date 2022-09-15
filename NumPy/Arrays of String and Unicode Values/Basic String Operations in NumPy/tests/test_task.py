import unittest
import numpy as np

from task import read_data, get_line_lengths


def test_read_data(file):
    text = np.loadtxt(file, delimiter='.', dtype=np.bytes_)[:, 0]
    decoded_text = np.char.decode(text)
    upper_text = np.char.upper(decoded_text)
    return upper_text


def test_get_line_lengths(array):
    return np.char.str_len(array)


test_uppercase_text = test_read_data('text.txt')
test_line_lengths = test_get_line_lengths(test_uppercase_text)


class TestCase(unittest.TestCase):
    def test_upper(self):
        uppercase_text = read_data('text.txt')
        np.testing.assert_array_equal(uppercase_text, test_uppercase_text, err_msg='The first function does not work '
                                                                                   'as expected.')

    def test_upper_shape(self):
        uppercase_text = read_data('text.txt')
        self.assertEqual(test_uppercase_text.shape, uppercase_text.shape, msg="Expected array shape is (8,).")

    def test_lengths(self):
        uppercase_text = read_data('text.txt')
        line_lengths = get_line_lengths(uppercase_text)
        np.testing.assert_array_equal(line_lengths, test_line_lengths, err_msg='The second function does not work '
                                                                               'as expected.')

    def test_lengths_shape(self):
        uppercase_text = read_data('text.txt')
        line_lengths = get_line_lengths(uppercase_text)
        self.assertEqual(test_line_lengths.shape, line_lengths.shape, msg="Expected array shape is (8,).")
