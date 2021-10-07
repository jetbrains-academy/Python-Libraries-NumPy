import unittest
import numpy as np

from task import read_data

X = read_data('text.txt')


class TestCase(unittest.TestCase):
    def test_add(self):
        self.assertTrue('numpy.str_' in str(type(X[0])), msg='Wrong dtype.')
