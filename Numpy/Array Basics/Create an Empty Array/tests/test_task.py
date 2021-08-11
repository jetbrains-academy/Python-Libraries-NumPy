import unittest
import numpy as np

from task import create_arrays


class TestCase(unittest.TestCase):
    def test_create_arrays(self):
        a, b = create_arrays(2, 3)
        self.assertEqual(a.dtype, 'int64', msg="Wrong dtype in the .ones array!")
        self.assertEqual(a.shape, (3, 2), msg="Wrong shape of the .ones array!")
        self.assertEqual(b.dtype, 'bool', msg="Wrong dtype in the .full array!")
        self.assertEqual(b.shape, (3, 2), msg="Wrong shape of the .full array!")

