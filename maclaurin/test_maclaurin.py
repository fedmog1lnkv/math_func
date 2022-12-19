import unittest
import maclaurin as macl
from maclaurin.maclaurin import factorial


class Tests_maclaurin(unittest.TestCase):
    def test_maclaurin_exp(self):
        n = 5
        x = 2
        answer = 7.266666666666667
        self.assertEqual(macl.maclaurin_exp(x, n), answer)

    def test_negative_maclaurin_exp(self):
        with self.assertRaises(TypeError):
            macl.maclaurin_exp(1, "2")

    def test_maclaurin_sin(self):
        n = 5
        x = 1.5
        answer = 0.9974949556821353
        self.assertEqual(macl.maclaurin_sin(x, n), answer)

    def test_negative_maclaurin_sin(self):
        with self.assertRaises(TypeError):
            macl.maclaurin_sin(1, 0.5)

    def test_maclaurin_cos(self):
        n = 5
        x = 5
        answer = -0.16274663800705724
        self.assertEqual(macl.maclaurin_cos(x, n), answer)

    def test_negative_maclaurin_cos(self):
        with self.assertRaises(TypeError):
            macl.maclaurin_cos("1", 2)

    def test_maclaurin_arcsin(self):
        n = 3
        x = 1
        answer = 1.286309523809524
        self.assertEqual(macl.maclaurin_arcsin(x, n), answer)

    def test_negative_maclaurin_arcsin(self):
        with self.assertRaises(TypeError):
            macl.maclaurin_arcsin(1, 2.3)

    def test_maclaurin_arccos(self):
        n = 2
        x = 1
        answer = 0.32912966012822986
        self.assertEqual(macl.maclaurin_arccos(x, n), answer)

    def test_negative_maclaurin_arccos(self):
        with self.assertRaises(TypeError):
            macl.maclaurin_arccos(1, )
