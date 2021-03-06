import unittest
import numpy as np
from task import calculate_entropy

rng = np.random.default_rng()


a = rng.integers(1, 20, size=10)  # Generate some dataset.
b = a / sum(a)
task_data = [0.16666667, 0.01754386, 0.05263158, 0.13157895, 0.16666667,
             0.13157895, 0.14035088, 0.01754386, 0.12280702, 0.05263158]


print(-np.sum(b * np.log2(b)))


class TestCase(unittest.TestCase):
    def test_entropy_task_data(self):
        self.assertEqual(-np.sum(task_data * np.log2(task_data)), calculate_entropy(task_data),
                         msg='Wrong answer for task dataset.')

    def test_entropy_test(self):
        self.assertEqual(-np.sum(b * np.log2(b)), calculate_entropy(b),
                         msg='Wrong answer for test dataset.')

