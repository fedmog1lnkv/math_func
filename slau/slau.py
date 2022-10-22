from matrix.matrix import *
from errors import *
import logging as log
import os


def Gauss_Jordan_algorithm(matrix, b, log_matrix=False):
    """
    Returns the result of solving a system of linear algebraic equations by the Gauss-Jordan method
    matrix - matrix of coefficients
    b - vector of constant terms
    """
    ensure_full_slau(matrix)

    matrix = deepcopy(matrix)
    b = deepcopy(b)

    log_management(log_matrix)

    log.info("Initial matrix")
    matrix_for_log(matrix, b)

    n = len(b)
    for k in range(n):
        matrix, b = partial_rotation(matrix, b, k)
        matrix, b = dividing_by_leading_element(matrix, b, k)
        matrix, b = variables_to_zeros(matrix, b, k)

    log.info("Answer")
    matrix_for_log(matrix, b)
    return b


def partial_rotation(matrix, b, IX_column):
    """ Partial rotation (removes zeros on the diagonal) """
    n = len(b)
    if abs(matrix[IX_column][IX_column]) < 1.0e-10:
        for i in range(IX_column + 1, n):
            if abs(matrix[i][IX_column]) > abs(matrix[IX_column][IX_column]):
                for j in range(IX_column, n):
                    matrix = row_switch(matrix, IX_column, j)
                b = row_switch(b, IX_column, i)
                break

    log.info("Partial rotation")
    matrix_for_log(matrix, b)
    return matrix, b


def dividing_by_leading_element(matrix, b, IX_column):
    """ Dividing a row of a matrix by a leading element """
    n = len(b)
    leading_element = matrix[IX_column][IX_column]
    matrix = mul_matrix_row(matrix, IX_column, leading_element ** (-1))
    b[IX_column] /= leading_element

    log.info(f"Dividing a row of a matrix by a leading element: {leading_element}")
    matrix_for_log(matrix, b)
    return matrix, b


def variables_to_zeros(matrix, b, IX_column):
    """ Replacing variables in the column with zeros (except for the position of the leading element) """
    n = len(b)
    for i in range(n):
        if i == IX_column or matrix[i][IX_column] == 0:
            continue
        factor = matrix[i][IX_column]
        for j in range(IX_column, n):
            matrix[i][j] -= factor * matrix[IX_column][j]
        b[i] -= factor * b[IX_column]
    log.info(f"Replacing values with zeros in column: {IX_column}")
    matrix_for_log(matrix, b)
    return matrix, b


def log_management(condition):
    if condition:
        log.basicConfig(filename="matrix_log.log", filemode="w", level=log.INFO)
    else:
        log.basicConfig(level=log.disable())
        if os.path.isfile('matrix_log.log'):
            os.remove('matrix_log.log')


def matrix_for_log(matrix, b):
    """ Beautiful matrix output for logs """
    logg_msg = "\n"
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            logg_msg += "{:10.2f}".format(matrix[i][j])
        logg_msg += "{:5}".format("     |") + "{:10.2f}".format(b[i]) + "\n"
    log.info(logg_msg)
