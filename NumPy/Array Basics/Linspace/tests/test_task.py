import unittest
from numpy import pi
from task import sine_array


class TestCase(unittest.TestCase):
    def test_linspace(self):
        a, b = sine_array(0, 2 * pi, 100)
        self.assertEqual(6.28318531, round(a[-1], 8), msg="Ooops!")

    def test_sine(self):
        a, b = sine_array(0, 2 * pi, 100)
        self.assertAlmostEqual(0, b[-1], msg="Ooops!")

    def test_linspace_shape(self):
        a, b = sine_array(0, 2 * pi, 100)
        self.assertEqual((100,), a.shape, msg="Wrong shape of array a.")

    def test_sine_shape(self):
        a, b = sine_array(0, 2 * pi, 100)
        self.assertEqual((100,), b.shape, msg="Wrong shape of array b.")
