from matrix import *
from vector import *
from errors import *
from copy import deepcopy
import logging as log
import os


def Gauss_Jordan_algorithm(matrix, b, log_matrix=False):
    """
    Returns the result of solving a system of linear algebraic equations by the Gauss-Jordan method
    matrix - matrix of coefficients
    b - vector of constant terms
    """
    ensure_full_slau(matrix)
    log_management(log_matrix)

    matrix = deepcopy(matrix)
    b = deepcopy(b)

    n = len(matrix)

    for i in range(len(matrix)):
        matrix[i] += [b[i]] + [0] * n

    log.info("Initial matrix")
    matrix_for_log(matrix)

    for k in range(n):
        matrix = partial_rotation(matrix, k)
    log.info("Partial rotation")
    matrix_for_log(matrix)

    matrix = straight_move(matrix)
    matrix = reverse_move(matrix)
    matrix = dividing_by_leading_element(matrix)

    b = get_column(matrix, n)

    log.info("Answer")
    matrix_for_log(matrix)
    return b

def slau_by_inverse_matrix(matrix, b, log_matrix = False):
    ensure_full_slau(matrix)

    matrix = deepcopy(matrix)
    b = deepcopy(b)

    return mul_matrix(inverse_matrix(matrix, log_matrix), b)

def partial_rotation(matrix, IX_column):
    """ Partial rotation (removes zeros on the diagonal) """
    if abs(matrix[IX_column][IX_column]) < 1.0e-10:
        n = len(matrix)
        for i in range(IX_column + 1, n):
            if abs(matrix[i][IX_column]) > abs(matrix[IX_column][IX_column]):
                for j in range(IX_column, n):
                    matrix = row_switch(matrix, IX_column, j)
    return matrix


def dividing_by_leading_element(matrix):
    """ Dividing a row of a matrix by a leading element """
    n = len(matrix)
    for IX_row in range(n):
        leading_element = matrix[IX_row][IX_row]
        mul_matrix_row(matrix, IX_row, leading_element ** (-1))
        log.info(f"Dividing a row of a matrix by a leading element: {leading_element}")
        matrix_for_log(matrix)
    return matrix


def inverse_matrix(matrix, log_matrix=False):
    """ Finding the inverse matrix by the Gauss-Jordan method """
    ensure_full_slau(matrix)
    log_management(log_matrix)

    matrix = deepcopy(matrix)
    n = len(matrix)

    matrix = adding_unit_matrix(matrix)
    matrix = straight_move(matrix)
    matrix = reverse_move(matrix)
    matrix = dividing_by_leading_element(matrix)

    log.info("Inverse matrix")
    matrix_for_log(matrix)

    # Оставить только правую часть матрицы
    for i in range(n):
        matrix[i] = matrix[i][n:]

    return matrix


def adding_unit_matrix(matrix):
    """ Adds a unit matrix to the end of the matrix """
    for i in range(len(matrix)):
        matrix[i] += [int(i == j) for j in range(len(matrix))]
    return matrix


def straight_move(matrix):
    """ Bringing the extended matrix to a stepwise form """
    n = len(matrix)
    for x in range(n):
        matrix = partial_rotation(matrix, IX_column=x)
        for i in range(x + 1, n):
            factor = matrix[i][x] / matrix[x][x]
            for j in range(x, n * 2):
                matrix[i][j] -= factor * matrix[x][j]
    return matrix


def reverse_move(matrix):
    """ Reducing an extended matrix to a single one """
    n = len(matrix)
    for x in reversed(range(n)):
        for i in reversed(range(x)):
            factor = matrix[i][x] / matrix[x][x]
            for j in reversed(range(n * 2)):
                matrix[i][j] -= factor * matrix[x][j]
    return matrix


def log_management(condition):
    if condition:
        log.basicConfig(filename="matrix_log.log", filemode="w", level=log.INFO)
    else:
        log.basicConfig(level=log.disable())
        if os.path.isfile('matrix_log.log'):
            os.remove('matrix_log.log')


def matrix_for_log(matrix):
    """ Beautiful matrix output for logs """
    n = len(matrix)
    logg_msg = "\n"
    for i in range(len(matrix)):
        for j in range(n):
            logg_msg += "{:10.2f}".format(matrix[i][j])
        logg_msg += "{:5}".format("     |")
        for j in range(n, n * 2):
            logg_msg += "{:10.2f}".format(matrix[i][j])
        logg_msg += "\n"
    log.info(logg_msg)
