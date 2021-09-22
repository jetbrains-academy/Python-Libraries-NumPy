import unittest

from task import *


class TestCase(unittest.TestCase):
    def test_add(self):
        self.assertEqual(create_array(1, 2).shape, (1, 2), msg="Something is wrong.")
        self.assertEqual(create_array(3, 5).shape, (3, 5), msg="Something is wrong.")
