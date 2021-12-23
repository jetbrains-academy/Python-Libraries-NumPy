import unittest
import contextlib
import io

f = io.StringIO()
with contextlib.redirect_stdout(f):
    from task import img
output = f.getvalue().split('\n')


class TestCase(unittest.TestCase):
    def test_ndim(self):
        expected, actual = str(img.ndim), output[1]
        self.assertEqual(expected, actual, msg="The second print statement should print the ndim of the image array.")

    def test_shape(self):
        expected, actual = str(img.shape), output[2]
        self.assertEqual(expected, actual, msg="The third print statement should print the shape of the image array.")
