import unittest
import interpolation as inter
from interpolation.interpolation import split_matrix, get_line_equation, get_basic_polynomials


class Tests_Interpolation(unittest.TestCase):

    def test_split_matrix(self):
        self.assertEqual(split_matrix([[2, 5], [6, 9]]), ([[2, 1], [6, 1]], [5, 9]))

    def test_get_line_equation(self):
        self.assertEqual(get_line_equation([[2, 5], [6, 9]]), [1, 3])

    def test_linear_interpolation(self):
        self.assertEqual(inter.linear_interpolation([[2, 5], [6, 9]]), [4, 7])

    def test_linear_extrapolate(self):
        self.assertEqual(inter.linear_extrapolate([[2, 5], [6, 9]], 1), [1, 4])

    def test_interpolate_piece_line(self):
        self.assertEqual(inter.interpolate_piece_line([[1, 2], [3, 4], [3.5, 3], [6, 7]]),
                         [[-2, -1], [2, 3], [3.25, 3.499999999999999], [4.75, 5], [6.5, 7.800000000000001]])

    def test_get_basic_polynomials(self):
        data = [[1, 2], [3, 4], [3.5, 3], [6, 7]]
        self.assertEqual(get_basic_polynomials(data, data[0][0], 0), 1)

    def test_lagrange_interpolation_polynomial(self):
        data = [[1, 2], [3, 4], [3.5, 3], [6, 7]]
        for i in range(len(data)):
            self.assertEqual(inter.lagrange_interpolation_polynomial(data, data[i][0]), data[i][1])
