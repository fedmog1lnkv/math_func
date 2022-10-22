import unittest
import slau


class Tests_Vector(unittest.TestCase):

    def test_slau_1(self):
        matrix = [[2, 1, 1], [1, 1, -2], [1, 2, 1]]
        b = [8, -2, 2]
        self.assertEqual(slau.Gauss_Jordan_algorithm(matrix, b), [4.0, -2.0, 2.0])

    def test_slau_2(self):
        matrix = [[4, 2], [6, 1]]
        b = [22, 45]
        self.assertEqual(slau.Gauss_Jordan_algorithm(matrix, b), [17/2,-6])

    def test_slau_3(self):
        matrix = [[2, 3], [4, 3]]
        b = [2, 7]
        self.assertEqual(slau.Gauss_Jordan_algorithm(matrix, b), [2.5, -1])

    def test_slau_4(self):
        matrix = [[-1, 2, 6], [3, -6, 0], [1, 0, 6]]
        b = [15, -9, 5]
        self.assertEqual(slau.Gauss_Jordan_algorithm(matrix, b), [-7.0, -2.0, 2.0])

    def test_negative_slau(self):
        matrix = [[-1, 2, 6], [3, -6, 0], [1, 0]]
        b = [15, -9, 5]
        with self.assertRaises(ValueError):
            slau.Gauss_Jordan_algorithm(matrix, b)
