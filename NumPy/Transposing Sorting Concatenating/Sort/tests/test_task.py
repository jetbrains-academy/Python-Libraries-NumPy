import unittest

from task import a, b, ind, c


class TestCase(unittest.TestCase):
    def test_array_b_shape(self):
        self.assertEqual(a.shape, b.shape, msg="Array b needs to be of the same shape as a.")

    def test_array_b_sorted(self):
        self.assertTrue(all([b[0, n] <= b[1, n] <= b[2, n] <= b[3, n] <= b[4, n] for n in range(b.shape[1])]),
                        msg='Columns in b do not appear to be sorted.')

    def test_array_ind(self):
        self.assertEqual(a.shape, ind.shape, msg="Array ind needs to be of the same shape as a.")

    def test_array_c(self):
        self.assertEqual(a.shape, c.shape, msg="Array c needs to be of the same shape as a.")

    def test_array_c_sorted(self):
        self.assertTrue(all([c[0, n] <= c[1, n] <= c[2, n] <= c[3, n] <= c[4, n] for n in range(c.shape[1])]),
                        msg='Columns in c do not appear to be sorted.')

    def test_array_c_sorted_rows(self):
        for i in c:
            self.assertTrue(i[0] == min(i) and i[-1] == max(i), msg="Rows in array c should be sorted.")
