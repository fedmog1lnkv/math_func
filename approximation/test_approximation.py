import unittest
import approximation as apprx
from approximation.approximation import split_matrix


class Tests_Approximation(unittest.TestCase):

    def test_split_matrix(self):
        self.assertEqual(split_matrix([[1, 2], [3, 4], [3.5, 3], [6, 7]]), ([[1], [3], [3.5], [6]], [2, 4, 3, 7]))

    def test_least_squares_method(self):
        self.assertEqual(apprx.least_squares_method([[2, 3, 7], [3, 3, 7], [4, 7, 3]]),
                         [4.680851063829789, -2.063829787234044])

    def test_linear_approximation(self):
        self.assertEqual(apprx.linear_approximation([[1, 2], [3, 4], [3.5, 3], [6, 7]], [1, 3, 5]),
                         [[1, 1.660098522167488], [3, 3.630541871921183], [5, 5.600985221674876]])

    def test_polinom_approximation(self):
        self.assertEqual(apprx.polinom_approximation([0.48, -4.8, 13.96, -7.64], [1, 3, 5]),
                         [[1, 2.000000000000001], [3, 4.000000000000008], [5, 2.1600000000000117]])
