import unittest
from numpy import pi
from task import sine_array


class TestCase(unittest.TestCase):
    def test_sine(self):
        a, b = sine_array(0, 2 * pi, 100)
        self.assertEqual(round(a[-1], 8), 6.28318531, msg="Ooops")
        self.assertEqual(b[-1], -2.4492935982947064e-16, msg="Ooops")
        self.assertEqual(a.shape, (100,), msg="Wrong num in array a")
        self.assertEqual(b.shape, (100,), msg="Wrong num in array b")
