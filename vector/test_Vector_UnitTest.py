import unittest
import vector as vec


class Tests_Vector(unittest.TestCase):

    def test_positiv_lenght(self):
        v = [4, 80, 18, -19, 57]
        self.assertEqual(vec.lenght(v), 101.73494974687902)

    def test_negative_TypeError_lenght(self):
        v = [4, 80, 18, "-19", 57]
        with self.assertRaises(TypeError):
            vec.lenght(v)

    def test_positiv_scalar(self):
        v1 = [31, -34, -77, 71, 53]
        v2 = [-77, 39, -64, 87, 51]
        self.assertEqual(vec.scalar(v1, v2), 10095)

    def test_negative_TypeError_scalar(self):
        v1 = [31, -34, -77, 71, 53]
        v2 = [-77, "39", -64, 87, 51]
        with self.assertRaises(TypeError):
            vec.scalar(v1, v2)

    def test_negative_ValueError_scalar(self):
        v1 = [31, -34, -77, 71, 53]
        v2 = [-77, -64, 87, 51]
        with self.assertRaises(ValueError):
            vec.scalar(v1, v2)

    def test_positiv_normalize(self):
        v = [-7, -75, 16]
        self.assertEqual(vec.normalize(v), [-0.0909014254011799, -0.9739438435840703, 0.20777468663126833])

    def test_negative_TypeError_normalize(self):
        v = [-7, "-75", 16]
        with self.assertRaises(TypeError):
            vec.normalize(v)

    def test_positive_cos_vectors(self):
        v1 = [-21, -64, 51, 54]
        v2 = [-93, -42, -14, 38]
        self.assertEqual(vec.cos_vectors(v1, v2), 0.5431396832694423)

    def test_negative_TypeError_cos_vectors(self):
        v1 = [-21, -64, 51, "54"]
        v2 = ["-93", -42, -14, 38]
        with self.assertRaises(TypeError):
            vec.cos_vectors(v1, v2)

    def test_negative_ValueError_cos_vectors(self):
        v1 = [-21, -64, 51, 54]
        v2 = [-93, -42, -14]
        with self.assertRaises(ValueError):
            vec.cos_vectors(v1, v2)

    def test_positive_angular(self):
        v1 = [51, 32, -41]
        v2 = [-48, 38, -63]
        self.assertEqual(vec.angular(v1, v2), 77.81148908681656)

    def test_positive_sum_vectors(self):
        v1 = [-77, 41, -46, -74]
        v2 = [-53, -77, 58, 45]
        self.assertEqual(vec.sum_vectors(v1, v2), [-130, -36, 12, -29])

    def test_negative_TypeError_sum_vectors(self):
        v1 = [-77, 41, -46, -74]
        v2 = [-53, -77, "58", 45]
        with self.assertRaises(TypeError):
            vec.sum_vectors(v1, v2)

    def test_negative_ValueError_sum_vectors(self):
        v1 = [-77, 41, -46]
        v2 = [-53, -77, 58, 45]
        with self.assertRaises(ValueError):
            vec.sum_vectors(v1, v2)

    def test_positive_dif_vectors(self):
        v1 = [5, 58, 78, 64, 99]
        v2 = [59, -72, 25, 5, 0]
        self.assertEqual(vec.dif_vectors(v1, v2), [-54, 130, 53, 59, 99])

    def test_negative_TypeError_dif_vectors(self):
        v1 = [5, "58", 78, 64, 99]
        v2 = [59, -72, 25, 5, "0"]
        with self.assertRaises(TypeError):
            vec.dif_vectors(v1, v2)

    def test_negative_ValueError_dif_vectors(self):
        v1 = [5, 58, 78, 64, 99]
        v2 = [59, 25, 5, 0]
        with self.assertRaises(ValueError):
            vec.dif_vectors(v1, v2)

    def test_positive_mul_vectors(self):
        v1 = [-99, 65, -35, -28, 60]
        v2 = [79, -10, -20, -33, -42]
        self.assertEqual(vec.mul_vectors(v1, v2), [-7821, -650, 700, 924, -2520])

    def test_negative_TypeError_mul_vectors(self):
        v1 = [-99, 65, -35, "-28", 60]
        v2 = [79, "-10", -20, -33, -42]
        with self.assertRaises(TypeError):
            vec.mul_vectors(v1, v2)

    def test_negative_ValueError_mul_vectors(self):
        v1 = [-99, 65, -35, 60]
        v2 = [79, -10, -20, -33, -42]
        with self.assertRaises(ValueError):
            vec.mul_vectors(v1, v2)

    def test_positive_mul_vectors_scalar(self):
        v = [2, -60]
        scalar = -76
        self.assertEqual(vec.mul_vectors(v, scalar), [-152, 4560])

    def test_negative_TypeError_mul_vectors_scalar(self):
        v = [2, "-60"]
        scalar = -76
        with self.assertRaises(TypeError):
            vec.mul_vectors(v, scalar)

    def test_positive_div_vectors(self):
        v1 = [-13, -68]
        v2 = [26, 82]
        self.assertEqual(vec.div_vectors(v1, v2), [-0.5, -0.8292682926829268])

    def test_negative_TypeError_div_vectors(self):
        v1 = [-44, -37, 88, -95]
        v2 = ["-12", -68, -71, -3]
        with self.assertRaises(TypeError):
            vec.div_vectors(v1, v2)

    def test_negative_ValueError_div_vectors(self):
        v1 = [-44, -37, 88, -95]
        v2 = [-68, -71, -3]
        with self.assertRaises(ValueError):
            vec.div_vectors(v1, v2)

    def test_positive_div_vectors_scalar(self):
        v = [-73, -15, 79, -34, -11]
        scalar = 4
        self.assertEqual(vec.div_vectors(v, scalar), [-18.25, -3.75, 19.75, -8.5, -2.75])

    def test_negative_TypeError_div_vectors_scalar(self):
        v = [-73, -15, 79, "-34", -11]
        scalar = 4
        with self.assertRaises(TypeError):
            vec.div_vectors(v, scalar)

    def test_positive_is_collinear(self):
        v1 = [2, 5]
        v2 = [4, 10]
        v3 = [3, 9]
        self.assertEqual(vec.is_collinear(v1, v2), True)
        self.assertEqual(vec.is_collinear(v2, v3), False)
        self.assertEqual(vec.is_collinear(v1, v3), False)

    def test_negative_TypeError_is_collinear(self):
        v1 = [2, 5]
        v2 = [4, "10"]
        with self.assertRaises(TypeError):
            vec.is_collinear(v1, v2)

    def test_positive_is_directional(self):
        v1 = [4, 0]
        v2 = [0, 8]
        self.assertEqual(vec.is_directional(v1, v2), False)

    def test_negative_TypeError_is_directional(self):
        v1 = [4, 0]
        v2 = [0, "8"]
        with self.assertRaises(TypeError):
            vec.is_directional(v1, v2)

    def test_positive_is_not_directional(self):
        v1 = [4, 0]
        v2 = [0, 8]
        self.assertEqual(vec.is_not_directional(v1, v2), False)

    def test_negative_TypeError_is_not_directional(self):
        v1 = ["4", 0]
        v2 = [0, 8]
        with self.assertRaises(TypeError):
            vec.is_not_directional(v1, v2)

    def test_positive_change_direction(self):
        v = [58, 89, 43]
        self.assertEqual(vec.change_direction(v), [-58, -89, -43])

    def test_negative_TypeError_change_direction(self):
        v = [58, "89", 43]
        with self.assertRaises(TypeError):
            vec.change_direction(v)

    def test_positive_is_orthogonal(self):
        v1 = [1, 2, 0]
        v2 = [2, -1, 0]
        self.assertEqual(vec.is_orthogonal(v1, v2), True)

    def test_negative_TypeError_is_orthogonal(self):
        v1 = [1, 2, 0]
        v2 = [2, "-1", 0]
        with self.assertRaises(TypeError):
            vec.is_orthogonal(v1, v2)

    def test_positive_is_equal(self):
        v1 = [1, 2]
        v2 = [1, 2]
        v3 = [3, 2]
        self.assertEqual(vec.is_equal(v1, v2), True)
        self.assertEqual(vec.is_equal(v1, v3), False)

    def test_negative_TypeError_is_equal(self):
        v1 = [1, "2"]
        v2 = [3, 2]
        with self.assertRaises(TypeError):
            vec.is_equal(v1, v2)

    def test_negative_ValueError_is_equal(self):
        v1 = [1]
        v2 = [3, 2]
        with self.assertRaises(ValueError):
            vec.is_equal(v1, v2)
