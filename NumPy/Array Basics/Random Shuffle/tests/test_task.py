import unittest
import numpy as np

from task import arr, permuted_2d, fully_random


class TestCase(unittest.TestCase):
    def test_shape(self):
        self.assertEqual(arr.shape, (5, 20), msg="Wrong shape of the array 'arr'.")
        self.assertEqual(permuted_2d.shape, (5, 20), msg="Wrong shape of the array 'permuted_2d'.")
        self.assertEqual(fully_random.shape, (5, 20), msg="Wrong shape of the array 'fully_random'.")

    def test_arr(self):
        for i in arr:
            # This test checks if in each row the minimum element goes first and maximum - last.
            self.assertTrue(i[0] == min(i) and i[-1] == max(i), msg="'arr' should be shuffled along the 0th axis.")

    def test_two_d(self):
        for i in permuted_2d:
            # This test checks that differences between all neighboring elements in rows of the array
            # are not equal to 1 (in non-shuffled rows they would be).
            self.assertFalse(all([(x - i[i.tolist().index(x) - 1]) == 1 for x in i if i.tolist().index(x) > 0]),
                             msg="'permuted_2d' should be shuffled along the 1st axis.")

    def test_random(self):
        # This test checks if elements were also randomized between the rows.
        for i in fully_random:
            self.assertTrue(max(i) - min(i) > 19, "'fully_random' needs to be fully shuffled.")
