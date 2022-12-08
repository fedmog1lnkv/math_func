from slau import *
from copy import deepcopy


def split_matrix_with_replace(matrix):
    ''' Return y values as result and replace y values to 1 in coords_matrix '''
    matrix = deepcopy(matrix)
    b = []
    for i in range(len(matrix)):
        b += [matrix[i][-1]]
        matrix[i][-1] = 1
    return matrix, b


def get_line_equation(matrix):
    ''' Return line equation '''
    matrix, b = split_matrix_with_replace(matrix)
    return slau_by_inverse_matrix(matrix, b)


def linear_interpolation(matrix):
    ''' Return interpolate value '''
    line_equation = get_line_equation(matrix)
    x = min(matrix[1][0], matrix[0][0]) + (max(matrix[1][0], matrix[0][0]) - min(matrix[1][0], matrix[0][0])) / 2
    return [x, x * line_equation[0] + line_equation[-1]]


def linear_extrapolate(matrix, indent=3):
    ''' Return extrapolate value '''
    line_equation = get_line_equation(matrix)
    x = min(matrix[1][0], matrix[0][0]) - indent
    return [x, x * line_equation[0] + line_equation[-1]]


def interpolate_piece_line(data, indent=3):
    ''' Return interpolate value of piece function '''
    matrix_xy = []
    for IX_line in range(len(data) - 1):
        copy_data_xy = [elem[:] for elem in data]
        matrix = copy_data_xy[IX_line:IX_line + 2]
        if IX_line == 0:
            matrix_xy += [linear_extrapolate(matrix, indent=indent)]
        matrix_xy += [linear_interpolation(matrix)]
        if IX_line == len(data) - 2:
            matrix_xy += [linear_extrapolate(matrix, indent=-indent)]
    return matrix_xy


def lagrange_interpolation_polynomial(data, x):
    ''' Return lagranzh interpolation polinomial value '''
    s = 0
    for i in range(len(data)):
        s += data[i][1] * get_basic_polynomials(data, x, i)
    return s


def get_basic_polynomials(data, x, i):
    ''' Return a product of range '''
    l = 1
    for j in range(len(data)):
        if j != i:
            l *= (x - data[j][0]) / (data[i][0] - data[j][0])
    return l
