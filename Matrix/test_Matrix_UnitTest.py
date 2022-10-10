import unittest
import matrix as mat


class Tests_Vector(unittest.TestCase):

    def test_positiv_sum_matrix(self):
        m1 = [[-6, -73, 96, 12], [59, 70, -100, -96], [-63, -33, 64, -56], [-83, -29, -22, 3]]
        m2 = [[-48, -10, -53, -56], [54, -34, 18, -15], [77, -50, -90, 29], [-50, 88, 1, -49]]
        self.assertEqual((mat.sum_matrix(m1, m2)),
                         [[-54, -83, 43, -44], [113, 36, -82, -111], [14, -83, -26, -27], [-133, 59, -21, -46]])

    def test_negative_TypeError_sum_matrix(self):
        m1 = [[-6, -73, 96, 12], [59, 70, -100, "a"], [-63, -33, 64, -56], [-83, -29, -22, 3]]
        m2 = [[-48, -10, -53, -56], [54, -34, 18, -15], [77, -50, -90, 29], [-50, 88, 1, -49]]
        with self.assertRaises(TypeError):
            mat.sum_matrix(m1, m2)

    def test_negative_ValueError_sum_matrix(self):
        m1 = [[-6, -73, 96, 12], [59, 70, -100, -96], [-63, -33, 64, -56], [-83, -29, -22, 3]]
        m2 = [[-48, -10, -53, -56], [54, -34, 18, -15], [-50, 88, 1, -49]]
        with self.assertRaises(ValueError):
            mat.sum_matrix(m1, m2)

    def test_positiv_dif_matrix(self):
        m1 = [[87, 14, 76], [-2, -40, 97], [91, -24, -21]]
        m2 = [[-14, 54, 90], [65, 42, -87], [27, 16, -52]]
        self.assertEqual((mat.dif_matrix(m1, m2)), [[101, -40, -14], [-67, -82, 184], [64, -40, 31]])

    def test_negative_TypeError_dif_matrix(self):
        m1 = [[87, 14, 76], [-2, "a", 97], [91, -24, -21]]
        m2 = [[-14, 54, 90], [65, 42, -87], [27, 16, -52]]
        with self.assertRaises(TypeError):
            mat.sum_matrix(m1, m2)

    def test_negative_ValueError_dif_matrix(self):
        m1 = [[87, 14, 76], [91, -24, -21]]
        m2 = [[-14, 54, 90], [65, 42, -87], [27, 16, -52]]
        with self.assertRaises(ValueError):
            mat.sum_matrix(m1, m2)

    def test_positiv_transportation_matrix(self):
        m1 = [[-61, -51], [78, -3]]
        self.assertEqual((mat.transportation_matrix(m1)), [[-61, 78], [-51, -3]])

    def test_negative_TypeError_transportation_matrix(self):
        m = [["-61", -51], [78, -3]]
        with self.assertRaises(TypeError):
            mat.transportation_matrix(m)

    def test_positiv_mul_matrix(self):
        m1 = [[-40, 14, -81], [-1, 54, 85], [-91, -15, -68]]
        m2 = [[8, 96, -56], [93, 7, -10], [-50, -38, 72]]
        self.assertEqual((mat.mul_matrix(m1, m2)), [[5032, -664, -3732], [764, -2948, 5636], [1277, -6257, 350]])

    def test_negative_TypeError_mul_matrix(self):
        m1 = [[-40, 14, -81], ["-1", 54, 85], [-91, -15, -68]]
        m2 = [[8, 96, -56], [93, 7, -10], [-50, -38, 72]]
        with self.assertRaises(TypeError):
            mat.mul_matrix(m1, m2)

    def test_negative_ValueError_mul_matrix(self):
        m1 = [[-40, 14, -81], [-91, -15, -68]]
        m2 = [[8, 96, -56], [93, 7, -10], [-50, -38, 72]]
        with self.assertRaises(ValueError):
            mat.mul_matrix(m1, m2)

    def test_positiv_mul_matrix_scalar(self):
        m = [[-35, 25], [-68, -11]]
        scalar = -39
        self.assertEqual((mat.mul_matrix(m, scalar)), [[1365, -975], [2652, 429]])

    def test_negative_TypeError_mul_matrix_scalar(self):
        m = [[-35, "25"], [-68, -11]]
        scalar = -39
        with self.assertRaises(TypeError):
            mat.mul_matrix(m, scalar)

    def test_positiv_get_row_matrix(self):
        m = [[100, 94, 48], [60, -82, 80], [31, -5, -5]]
        row = 2
        self.assertEqual((mat.get_row(m, row)), [31, -5, -5])

    def test_positiv_get_column_matrix(self):
        m = [[-26, 89, 72, 18], [-38, -13, 44, 35], [31, -39, 3, -96], [-7, 5, -98, -82]]
        col = 2
        self.assertEqual((mat.get_column(m, col)), [72, 44, 3, -98])

    def test_positiv_row_switch_matrix(self):
        m = [[-85, -23, 11], [73, -10, 25], [58, -83, 25]]
        row1 = 1
        row2 = 2
        self.assertEqual((mat.row_switch(m, row1, row2)), [[73, -10, 25], [-85, -23, 11], [58, -83, 25]])

    def test_positiv_mul_matrix_row_matrix(self):
        m = [[-91, 18, -35], [-16, 18, -48], [-45, 60, -22]]
        row = 1
        scalar = 63
        self.assertEqual((mat.mul_matrix_row(m, row, scalar)), [[-5733, 1134, -2205], [-16, 18, -48], [-45, 60, -22]])

    def test_negative_TypeError_mul_matrix_row_matrix(self):
        m = [[-91, 18, -35], [-16, 18, -48], [-45, "60", -22]]
        row = 1
        scalar = 63
        with self.assertRaises(TypeError):
            mat.mul_matrix_row(m, row, scalar)

    def test_positiv_sum_matrix_rows_matrix(self):
        m = [[87, 75], [-26, 29]]
        row1 = 0
        row2 = 1
        scalar = -2
        self.assertEqual((mat.sum_matrix_rows(m, row1, row2, scalar)), [[87, 75], [26, -29]])

    def test_negative_TypeError_sum_matrix_rows_matrix(self):
        m = [[87, "75"], [-26, 29]]
        row1 = 0
        row2 = 1
        scalar = -2
        with self.assertRaises(TypeError):
            mat.sum_matrix_rows(m, row1, row2, scalar)

    def test_positiv_dif_matrix_rows_matrix(self):
        m = [[97, -71, -42], [-59, 12, -60], [23, 1, -28]]
        row1 = 1
        row2 = 2
        scalar = 89
        self.assertEqual((mat.dif_matrix_rows(m, row1, row2, scalar)),
                         [[-1950, -160, 2450], [-59, 12, -60], [23, 1, -28]])

    def test_negative_TypeError_dif_matrix_rows_matrix(self):
        m = [[97, -71, -42], [-59, 12, -60], [23, 1, "-28"]]
        row1 = 1
        row2 = 2
        scalar = 89
        with self.assertRaises(TypeError):
            mat.dif_matrix_rows(m, row1, row2, scalar)
