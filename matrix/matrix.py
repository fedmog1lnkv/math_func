import vector.vector as vec
from errors import *
from copy import deepcopy


def sum_matrix(matrix1, matrix2):
    """ Return sum of matrices """
    ensure_full_matrix(matrix1, matrix2)
    return [vec.sum_vectors(matrix1[IX_cell], matrix2[IX_cell]) for IX_cell in range(len(matrix1))]


def dif_matrix(matrix1, matrix2):
    """ Return difference of matrices """
    ensure_full_matrix(matrix1, matrix2)
    return [vec.dif_vectors(matrix1[IX_cell], matrix2[IX_cell]) for IX_cell in range(len(matrix1))]


def transportation_matrix(matrix):
    """ Transposes the matrix """
    ensure_types_matrix(matrix)
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]


def sort_arguments(matrix1, matrix2):
    if vec.is_scalar(matrix1) or vec.is_vector(matrix1):
        ensure_types_matrix(matrix2)
        return matrix2, matrix1
    ensure_types_matrix(matrix1)
    return matrix1, matrix2


def mul_matrix(matrix1, matrix2):
    """ Return multiplication of matrices or multiplying a matrix by a scalar """
    if vec.is_scalar(matrix1) or vec.is_scalar(matrix2):
        matrix1, scal = sort_arguments(matrix1, matrix2)
        return [vec.mul_vectors(matrix1[IX_row], scal) for IX_row in range(len(matrix1))]

    elif vec.is_vector(matrix1) or vec.is_vector(matrix2):
        matrix1, vector = sort_arguments(matrix1, matrix2)
        matrix_out = []
        for i in range(len(matrix1)):
            for c in range(len(matrix1)):
                trunk = 0
                for j in range(len(matrix1[c])):
                    trunk += matrix1[i][j] * vector[j]
            matrix_out += [trunk]
        return matrix_out

    ensure_full_matrix(matrix1, matrix2)
    matrix_out = []
    for i in range(len(matrix1)):
        trunk = []
        for j in range(len(matrix2[i])):
            cell = 0
            for k in range(len(matrix1[i])):
                cell += matrix1[i][k] * matrix2[k][j]
            trunk += [cell]
        matrix_out += [trunk]
    return matrix_out


def get_row(matrix, row, do_copy=True):
    """ Returns a row from the matrix by index """
    if do_copy == True:
        return deepcopy(matrix[row])
    return matrix[row]


def get_column(matrix, column, do_copy=True):
    """ Returns a column from the matrix by index """
    return get_row(transportation_matrix(matrix), column, do_copy)


def row_switch(matrix, row1, row2, do_copy=True):
    """ Returns a matrix with permuted rows by indexes """
    if do_copy == True:
        matrix_copy = deepcopy(matrix)
        matrix_copy[row1], matrix_copy[row2] = matrix_copy[row2], matrix_copy[row1]
        return matrix_copy
    matrix[row1], matrix[row2] = matrix[row2], matrix[row1]
    return matrix


def mul_matrix_row(matrix, row, scalar):
    """ Multiplies a row from the matrix by a given index by a scalar """
    ensure_types_matrix(matrix)
    matrix[row] = vec.mul_vectors(matrix[row], scalar)
    return matrix


def sum_matrix_rows(matrix, row1, row2, scalar):
    """ Returns the matrix in which the rows are stacked, which are multiplied by a scalar """
    ensure_types_matrix(matrix)
    matrix = [row for row in matrix]
    matrix[row1] = vec.sum_vectors(matrix[row1], vec.mul_vectors(get_row(matrix, row2), scalar))
    return matrix


def dif_matrix_rows(matrix, row1, row2, scalar):
    """ Returns a matrix in which the rows are subtracted, which are multiplied by a scalar """
    ensure_types_matrix(matrix)
    matrix = [row for row in matrix]
    matrix[row1] = vec.dif_vectors(matrix[row1], vec.mul_vectors(get_row(matrix, row2), scalar))
    return matrix
