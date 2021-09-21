import unittest

from task import x, w


class TestCase(unittest.TestCase):
    def test_shape(self):
        self.assertEqual(x.shape, (10, 1), msg="wrong shape of x!")
        self.assertEqual(w.shape, (3, 4), msg="wrong shape of x!")


