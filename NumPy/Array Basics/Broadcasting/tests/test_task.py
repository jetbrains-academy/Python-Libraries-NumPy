import unittest

from task import x, w


class TestCase(unittest.TestCase):
    def test_shape(self):
        self.assertEqual(x.shape, (10, 1), msg="Wrong shape of x.")
        self.assertEqual(w.shape, (3, 4), msg="Wrong shape of w.")


