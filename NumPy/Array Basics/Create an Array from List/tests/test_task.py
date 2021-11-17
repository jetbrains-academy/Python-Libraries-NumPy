import unittest

from task import *


class TestCase(unittest.TestCase):
    def test_one(self):
        self.assertEqual((1, 2), create_array(1, 2).shape, msg="Something is wrong.")

    def test_two(self):
        self.assertEqual((3, 5), create_array(3, 5).shape, msg="Something is wrong.")
