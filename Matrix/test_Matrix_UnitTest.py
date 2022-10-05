import unittest

import numpy as np

from random import randint

import Matrix as mat

import Errors


class Tests_Vector(unittest.TestCase):
    def test_positiv_test_int(self):
        rang = randint(2, 10)
        m1 = [[randint(-100, 100) for i in range(rang)] for j in range(rang)]
        m2 = [[randint(-100, 100) for i in range(rang)] for j in range(rang)]
        mnp1 = np.array(m1)
        mnp2 = np.array(m2)
        scalar = randint(-100, 100)

        self.assertEqual((mat.sum_matrix(m1, m2)), np.array(mnp1 + mnp2).tolist())
        self.assertEqual((mat.dif_matrix(m1, m2)), np.array(mnp1 - mnp2).tolist())
        self.assertEqual((mat.transportation_matrix(m1)), np.array(np.transpose(mnp1)).tolist())
        self.assertEqual((mat.mul_matrix(m1, m2)), np.array(mnp1.dot(mnp2)).tolist())
        self.assertEqual((mat.mul_matrix(m1, scalar)), np.array(mnp1.dot(scalar)).tolist())

    def test_type_matrix(self):
        rang = randint(2, 10)
        m1 = [[randint(-100, 100) for i in range(rang)] for j in range(rang)]
        m2 = [[randint(-100, 100) for i in range(rang)] for j in range(rang)]
        m2[rang - 1][rang - 1] = "a"

        with self.assertRaises(TypeError):
            mat.sum_matrix(m1, m2)
        with self.assertRaises(TypeError):
            mat.dif_matrix(m1, m2)
        with self.assertRaises(TypeError):
            mat.transportation_matrix(m2)
        with self.assertRaises(TypeError):
            mat.mul_matrix(m1, m2)
        with self.assertRaises(TypeError):
            mat.mul_matrix_row(m2, rang - 2, randint(-100, 100))
        with self.assertRaises(TypeError):
            mat.sum_matrix_rows(m2, rang - 1, rang - 2, randint(-100, 100))
        with self.assertRaises(TypeError):
            mat.dif_matrix_rows(m1, m2)

    def test_shape_matrix(self):
        rang = randint(2, 10)
        m1 = [[randint(-100, 100) for i in range(rang)] for j in range(rang)]
        m2 = [[randint(-100, 100) for i in range(rang)] for j in range(rang + 1)]

        with self.assertRaises(ValueError):
            mat.sum_matrix(m1, m2)
        with self.assertRaises(ValueError):
            mat.dif_matrix(m1, m2)
        with self.assertRaises(ValueError):
            mat.mul_matrix(m1, m2)
