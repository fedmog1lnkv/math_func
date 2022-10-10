import unittest

import numpy as np

from random import randint

import Vector as vec

import Errors


class Tests_Vector(unittest.TestCase):

    def test_positiv_test_int(self):
        rang = randint(2, 100)
        v1 = [randint(-100, 100) for i in range(rang)]
        v2 = [randint(-100, 100) for i in range(rang)]
        rounding = randint(0, 15)

        self.assertEqual(vec.lenght(v1), np.linalg.norm(np.array(v1)))

        self.assertEqual(vec.scalar(v1, v2), np.dot(np.array(v1), np.array(v2)))
# также проверка нормализации norm(v1)
        self.assertEqual(vec.cos_vectors(v1, v2, rounding),
                         (round((np.dot(v1, v2)) / (np.linalg.norm(v1) * np.linalg.norm(v2)), rounding)))

        self.assertEqual(vec.angular(v1, v2, 0), (round((np.arccos(np.dot(np.array(v1), np.array(v2)) / (np.linalg.norm(np.array(v1)) * np.linalg.norm(np.array(v2)))) * 360/2/np.pi), 0)))

        self.assertEqual(vec.sum_vectors(v1, v2), list((np.array(v1) + np.array(v2))))

        self.assertEqual(vec.dif_vectors(v1, v2), list((np.array(v1) - np.array(v2))))

        self.assertEqual(vec.mul_vectors(v1, v2), list((np.array(v1) * np.array(v2))))

        scal = randint(-100, 100)
        self.assertEqual(vec.mul_vectors(v1, scal), list((np.array(v1) * scal)))
        self.assertEqual(vec.mul_vectors(scal, v2), list((np.array(v2) * scal)))

        if not (0 in v1 or 0 in v2 and scal != 0):
            self.assertEqual(vec.div_vectors(v1, v2), list((np.array(v1) / np.array(v2))))
            self.assertEqual(vec.div_vectors(v1, scal), list((np.array(v1) / scal)))
            self.assertEqual(vec.div_vectors(scal, v2), list((np.array(v2) / scal)))

    def test_different_lengths_vectors(self):

        rang1, rang2 = randint(2, 100), randint(2, 100)
        while rang1 == rang2:
            rang1, rang2 = randint(2, 100), randint(2, 100)
        v1 = [randint(-100, 100) for i in range(rang1)]
        v2 = [randint(-100, 100) for i in range(rang2)]

        with self.assertRaises(ValueError):
            vec.scalar(v1, v2)
        with self.assertRaises(ValueError):
            vec.cos_vectors(v1, v2)
        with self.assertRaises(ValueError):
            vec.angular(v1, v2)
        with self.assertRaises(ValueError):
            vec.sum_vectors(v1, v2)
        with self.assertRaises(ValueError):
            vec.dif_vectors(v1, v2)
        with self.assertRaises(ValueError):
            vec.mul_vectors(v1, v2)
        with self.assertRaises(ValueError):
            vec.div_vectors(v1, v2)
        with self.assertRaises(ValueError):
            vec.is_equal(v1, v2)

    def test_type_vectors(self):
        v1 = [randint(-100, 100) for i in range(4)] + ["a"]
        v2 = [randint(-100, 100) for i in range(5)]

        with self.assertRaises(TypeError):
            vec.normalize(v1)
        with self.assertRaises(TypeError):
            vec.cos_vectors(v1, v2)
        with self.assertRaises(TypeError):
            vec.angular(v1, v2)
        with self.assertRaises(TypeError):
            vec.sum_vectors(v1, v2)
        with self.assertRaises(TypeError):
            vec.dif_vectors(v1, v2)
        with self.assertRaises(TypeError):
            vec.sort_arguments(v1, 1)
        with self.assertRaises(TypeError):
            vec.mul_vectors(v1, v2)
        with self.assertRaises(TypeError):
            vec.div_vectors(v1, v2)
        with self.assertRaises(TypeError):
            vec.is_collinear(v1, v2)
        with self.assertRaises(TypeError):
            vec.is_directional(v1, v2)
        with self.assertRaises(TypeError):
            vec.is_not_directional(v1, v2)
        with self.assertRaises(TypeError):
            vec.change_direction(v1)
        with self.assertRaises(TypeError):
            vec.projection(v1, v2)
        with self.assertRaises(TypeError):
            vec.is_orthogonal(v1, v2)


if __name__ == '__main__':
    unittest.main()
