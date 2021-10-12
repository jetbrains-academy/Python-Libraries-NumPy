import unittest
import numpy as np
import string

from task import remove_extra_stuff, text

test_text = np.array(['Method #1:', 'Using isdigit() method', '  Method #2:', 'Using regex'])

class TestCase(unittest.TestCase):
    def test_array(self):
        txt = remove_extra_stuff(text)
        np.testing.assert_array_equal(txt,
                                      np.char.translate(text, str.maketrans('AEIOUY', 'aeiouy', string.punctuation + string.digits + string.whitespace)),
                                      err_msg="Your function does something else. Please check out the expected result in the"
                                              "task description.")

    def test_chars(self):
        txt = remove_extra_stuff(test_text)
        check_digits = [char not in element for char in string.digits for element in txt]
        check_whitespace = [char not in element for char in string.whitespace for element in txt]
        check_punctuation = [char not in element for char in string.punctuation for element in txt]
        self.assertTrue(all(check_punctuation), msg='Your result still contains punctuation.')
        self.assertTrue(all(check_digits), msg='Your result still contains digits.')
        self.assertTrue(all(check_whitespace), msg='Your result still contains whitespaces.')
