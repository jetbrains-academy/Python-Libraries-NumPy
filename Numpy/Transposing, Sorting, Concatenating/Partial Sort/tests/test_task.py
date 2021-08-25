import unittest

from task import *


class TestCase(unittest.TestCase):
    def test_add(self):
        self.assertEqual(indices.shape, distances.shape, msg="`indices` has to have the same shape as `distances`")
        self.assertTrue(all([partitioned_by_distance[i] < partitioned_by_distance[k] for i in range(k)]) and
                        all([partitioned_by_distance[i] >= partitioned_by_distance[k] for i in range(k, arr.shape[0])]),
                        msg='`partitioned_by_distance` does not seem to be partitioned!')
        self.assertEqual(k_nearest.shape[0], 3, msg='k_nearest should contain 3 values closest to 0')
