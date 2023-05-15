import unittest
import contextlib
import io

f = io.StringIO()
img_error = None
with contextlib.redirect_stdout(f):
    try:
        from task import img
    except FileNotFoundError as e:
        img_error = e
        pass
output = f.getvalue().split('\n')


class TestCase(unittest.TestCase):
    def test_img(self):
        self.assertIsNone(img_error, msg="Please check if you are opening horse.jpg")
