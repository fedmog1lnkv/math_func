from slau import gauss_jordan_algorithm
from interpolation.interpolation import split_matrix_with_replace
from matrix import transportation_matrix, mul_matrix
from copy import deepcopy


def split_matrix(matrix):
    ''' Split the system into a matrix and a b - vector '''
    matrix = deepcopy(matrix)
    b = []
    for i in range(len(matrix)):
        b += [matrix[i][-1]]
        del matrix[i][-1]
    return matrix, b


def least_squares_method(matrix):
    ''' Returns the value of solving a system of equations by the least squares method '''
    matrix, b = split_matrix(matrix)
    matrix_transp = transportation_matrix(matrix)
    matrix = mul_matrix(matrix_transp, matrix)
    b = mul_matrix(matrix_transp, b)
    return gauss_jordan_algorithm(matrix, b)


def linear_approximation(matrix, vector_x):
    ''' Returns an approximation of a linear function '''
    matrix, b = split_matrix_with_replace(matrix)
    matrix_transp = transportation_matrix(matrix)
    matrix_delta = mul_matrix(matrix_transp, matrix)
    b = mul_matrix(matrix_transp, b)
    trunk = gauss_jordan_algorithm(matrix_delta, b)
    return [[item, trunk[0] * item + trunk[1]] for item in vector_x]


def polinom_approximation(data, vector_x):
    ''' Returns an approximation by a polynomial of any degree '''
    matrix = []
    for i in range(len(vector_x)):
        matrix_line = []
        for j in range(len(data)):
            matrix_line = [vector_x[i] ** j] + matrix_line
        matrix += [matrix_line]
    y_arr = mul_matrix(matrix, data)
    return [[vector_x[i], y_arr[i]] for i in range(len(y_arr))]
