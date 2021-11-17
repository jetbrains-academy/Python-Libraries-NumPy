import unittest
import numpy as np

from task import arr


# todo: replace this with an actual test
class TestCase(unittest.TestCase):
    def test_add(self):
        self.assertEqual((100, 4), arr.shape, msg="Wrong array shape.")
