import unittest

from task import x, w


class TestCase(unittest.TestCase):
    def test_shape_x(self):
        self.assertEqual((10, 1), x.shape, msg="Wrong shape of x.")

    def test_shape_w(self):
        self.assertEqual((3, 4), w.shape, msg="Wrong shape of w.")


