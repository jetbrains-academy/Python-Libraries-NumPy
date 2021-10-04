import unittest

from task import find_most_frequent_class


class TestCase(unittest.TestCase):
    def test_most_frequent_class(self):
        self.assertEqual(find_most_frequent_class('data.csv'), 1, msg="Incorrect class found for task data.")
        self.assertEqual(find_most_frequent_class('test_data1.csv'), 4, msg="Incorrect class found for test data.")
        self.assertEqual(find_most_frequent_class('test_data2.csv'), 37, msg="Incorrect class found for test data.")