import Vector as vec
from Vector.Errors import *


def sum_matrix(matrix1, matrix2):
    '''  '''
    ensure_shape_matrix(matrix1, matrix2)
    ensure_types_matrix(matrix1)
    ensure_types_matrix(matrix2)
    return [vec.sum_vectors(matrix1[IX_cell], matrix2[IX_cell]) for IX_cell in range(len(matrix1))]


def dif_matrix(matrix1, matrix2):
    '''  '''
    ensure_shape_matrix(matrix1, matrix2)
    ensure_types_matrix(matrix1)
    ensure_types_matrix(matrix2)
    return [vec.dif_vectors(matrix1[IX_cell], matrix2[IX_cell]) for IX_cell in range(len(matrix1))]


def transportation_matrix(matrix):
    '''  '''
    ensure_types_matrix(matrix)
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]


def mul_matrix(matrix1, matrix2):
    '''  '''
    if type(matrix1) == int or type(matrix1) == float:
        ensure_types_matrix(matrix2)
        return [vec.mul_vectors(matrix2[IX_row], matrix1) for IX_row in range(len(matrix2))]
    elif type(matrix2) == int or type(matrix2) == float:
        ensure_types_matrix(matrix1)
        return [vec.mul_vectors(matrix1[IX_row], matrix2) for IX_row in range(len(matrix1))]
    ensure_types_matrix(matrix1)
    ensure_types_matrix(matrix2)
    ensure_shape_matrix_mul(matrix1, matrix2)

    matrix_out = []
    for i in range(len(matrix1)):
        trunk = []
        for j in range(len(matrix2)):
            cell = 0
            for k in range(len(matrix1[j])):
                cell += matrix1[i][k] * matrix2[k][j]
            trunk += [cell]
        matrix_out += [trunk]
    return matrix_out


def row_index(matrix, row):
    '''  '''
    return matrix[row - 1]


def column_index(matrix, column):
    '''  '''
    return row_index(transportation_matrix(matrix), column)


def row_switch(matrix, row1, row2):
    '''  '''
    matrix[row1 - 1], matrix[row2 - 1] = matrix[row2 - 1], matrix[row1 - 1]
    return matrix


def mul_matrix_row(matrix, row, scalar):
    '''  '''
    matrix[row - 1] = vec.mul_vectors(matrix[row - 1], scalar)
    return matrix
