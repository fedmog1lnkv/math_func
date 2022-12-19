from math import pi
from errors import ensure_types_x_n


def factorial(a):
    ''' Returns the factorial of a '''
    product = 1
    for i in range(2, a + 1):
        product *= i
    return product


def maclaurin_exp(x, n):
    ''' Returns the exponent value of the decomposed Maclaurin series '''
    ensure_types_x_n(x, n)
    summ = 0
    for i in range(0, n + 1):
        summ += x ** i / factorial(i)
    return summ


def maclaurin_cos(x, n):
    ''' Returns the cosine value of the decomposed Maclaurin series '''
    ensure_types_x_n(x, n)
    summ = 0
    for i in range(0, n + 1):
        summ += ((-1) ** i / factorial(2 * i)) * (x ** (2 * i))
    return summ


def maclaurin_sin(x, n):
    ''' Returns the value of the sine of the decomposed Maclaurin series '''
    ensure_types_x_n(x, n)
    summ = 0
    for i in range(0, n + 1):
        summ += ((-1) ** i / factorial(2 * i + 1)) * (x ** (2 * i + 1))
    return summ


def maclaurin_arcsin(x, n):
    ''' Returns the value of the arcsin of the decomposed Maclaurin series '''
    ensure_types_x_n(x, n)
    summ = 0
    for i in range(0, n + 1):
        summ += (factorial(2 * i) * x ** (2 * i + 1)) / ((4 ** i) * (factorial(i) ** 2) * (2 * i + 1))
    return summ


def maclaurin_arccos(x, n):
    ''' Returns the value of the arccosine of the decomposed Maclaurin series '''
    ensure_types_x_n(x, n)
    return (pi / 2) - maclaurin_arcsin(x, n)
