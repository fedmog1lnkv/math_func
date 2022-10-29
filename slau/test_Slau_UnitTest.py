import unittest
import slau


class Tests_Slau(unittest.TestCase):

    def test_GJA_1(self):
        matrix = [[2, 1, 1], [1, 1, -2], [1, 2, 1]]
        b = [8, -2, 2]
        self.assertEqual(slau.Gauss_Jordan_algorithm(matrix, b), [4.0, -2.0, 2.0])

    def test_GJA_2(self):
        matrix = [[4, 2], [6, 1]]
        b = [22, 45]
        self.assertEqual(slau.Gauss_Jordan_algorithm(matrix, b), [17 / 2, -6])

    def test_GJA_3(self):
        matrix = [[2, 3], [4, 3]]
        b = [2, 7]
        self.assertEqual(slau.Gauss_Jordan_algorithm(matrix, b), [2.5, -1])

    def test_GJA_4(self):
        matrix = [[-1, 2, 6], [3, -6, 0], [1, 0, 6]]
        b = [15, -9, 5]
        self.assertEqual(slau.Gauss_Jordan_algorithm(matrix, b), [-7.0, -2.0, 2.0])

    def test_negative_slau(self):
        matrix = [[-1, 2, 6], [3, -6, 0], [1, 0]]
        b = [15, -9, 5]
        with self.assertRaises(ValueError):
            slau.Gauss_Jordan_algorithm(matrix, b)

    def test_inv_matrix_1(self):
        matrix = [[1, 2], [3, 4]]
        self.assertEqual(slau.inverse_matrix(matrix, True), [[-2, 1], [1.5, -0.5]])

    def test_inv_matrix_2(self):
        matrix = [[2, 3], [-1, 1]]
        self.assertEqual(slau.inverse_matrix(matrix, True), [[1 / 5, -3 / 5], [1 / 5, 2 / 5]])

    def test_inv_matrix_3(self):
        matrix = [[1, -2, 0], [3, 4, 2], [-1, 3, 1]]
        self.assertEqual(slau.inverse_matrix(matrix, True),
                         [[-2 / 8, 2 / 8, -4 / 8], [-5 / 8, 1 / 8, -2 / 8], [13 / 8, -1 / 8, 10 / 8]])

    def test_slau_inverse_1(self):
        matrix = [[2, 1, 1], [1, 1, -2], [1, 2, 1]]
        b = [8, -2, 2]
        self.assertEqual(slau.slau_by_inverse_matrix(matrix, b), [4.0, -2.0, 2.0])

    def test_slau_inverse_2(self):
        matrix = [[4, 2], [6, 1]]
        b = [22, 45]
        self.assertEqual(slau.slau_by_inverse_matrix(matrix, b), [17 / 2, -6])

    def test_slau_inverse_3(self):
        matrix = [[-1, 2, 6], [3, -6, 0], [1, 0, 6]]
        b = [15, -9, 5]
        self.assertEqual(slau.slau_by_inverse_matrix(matrix, b), [-7.0, -2.0, 2.0])
