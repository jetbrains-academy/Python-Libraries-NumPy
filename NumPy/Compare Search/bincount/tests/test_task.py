import unittest

from task import find_most_frequent_class


class TestCase(unittest.TestCase):
    def test_most_frequent_class1(self):
        self.assertEqual(1, find_most_frequent_class('data.csv'), msg="Incorrect class found for task data.")

    def test_most_frequent_class2(self):
        self.assertEqual(4, find_most_frequent_class('test_data1.csv'), msg="Incorrect class found for test data.")

    def test_most_frequent_class3(self):
        self.assertEqual(37, find_most_frequent_class('test_data2.csv'), msg="Incorrect class found for test data.")