import math
from errors import *

EPS = 1e-10


def is_almost_equal(a, b, eps=EPS):
    return abs(a - b) <= eps


def lenght(vector_arr):
    """ Returns the length of the vector """
    ensure_types_vector(vector_arr)
    trunk = 0
    for coord in vector_arr:
        trunk += (coord ** 2)
    return trunk ** (1 / 2)


def scalar(vector_arr1, vector_arr2):
    """ Returns the scalar product of vectors """
    ensure_full_vector(vector_arr1, vector_arr2)
    trunk = 0
    for i in range(len(vector_arr1)):
        trunk += vector_arr1[i] * vector_arr2[i]
    return trunk


def normalize(vector_arr):
    """ Returns a normalized vector """
    ensure_types_vector(vector_arr)
    return [i / lenght(vector_arr) for i in vector_arr]


def cos_vectors(vector_arr1, vector_arr2):
    """ Return the cos value between two vectors with the specified accuracy (default is 5) """
    ensure_full_vector(vector_arr1, vector_arr2)
    return scalar(vector_arr1, vector_arr2) / (lenght(vector_arr1) * lenght(vector_arr2))


def angular(vector_arr1, vector_arr2):
    """ Returns the angle between vectors with the specified accuracy (default is 5) """
    cos = cos_vectors(vector_arr1, vector_arr2)
    rad = math.acos(cos)
    return rad / math.pi * 180


def sum_vectors(vector_arr1, vector_arr2):
    """ Return sum of vectors """
    ensure_full_vector(vector_arr1, vector_arr2)
    return [vector_arr1[i] + vector_arr2[i] for i in range(len(vector_arr1))]


def dif_vectors(vector_arr1, vector_arr2):
    """ Return difference of vectors """
    ensure_full_vector(vector_arr1, vector_arr2)
    return [vector_arr1[i] - vector_arr2[i] for i in range(len(vector_arr1))]


def is_scalar(vector_arr):
    return type(vector_arr) == int or type(vector_arr) == float


def sort_arguments(vector_arr1, vector_arr2):
    if is_scalar(vector_arr1):
        ensure_types_vector(vector_arr2)
        return vector_arr2, vector_arr1
    ensure_types_vector(vector_arr1)
    return vector_arr1, vector_arr2


def mul_vectors(vector_arr1, vector_arr2):
    """ Return multiplication of vectors or multiplying a vector by a scalar """
    if is_scalar(vector_arr1) or is_scalar(vector_arr2):
        vector_arr1, scal = sort_arguments(vector_arr1, vector_arr2)
        return [vector_arr1[i] * scal for i in range(len(vector_arr1))]
    ensure_full_vector(vector_arr1, vector_arr2)
    return [vector_arr1[i] * vector_arr2[i] for i in range(len(vector_arr1))]


def div_vectors(vector_arr1, vector_arr2):
    """ Return division of vectors or dividing a vector by a scalar """
    if is_scalar(vector_arr1) or is_scalar(vector_arr2):
        vector_arr1, scal = sort_arguments(vector_arr1, vector_arr2)
        return [vector_arr1[i] / scal for i in range(len(vector_arr1))]
    ensure_full_vector(vector_arr1, vector_arr2)
    return [vector_arr1[i] / vector_arr2[i] for i in range(len(vector_arr1))]


def is_collinear(vector_arr1, vector_arr2, eps=EPS):
    """ Checks vectors for collinearity with the specified accuracy (default is 5) """
    ensure_types_vectors(vector_arr1, vector_arr2)
    return is_almost_equal(abs(cos_vectors(vector_arr1, vector_arr2)), 1, eps)


def is_directional(vector_arr1, vector_arr2, eps=EPS):
    """ Checks vectors for co-directionality with a given accuracy (default is 5) """
    ensure_types_vectors(vector_arr1, vector_arr2)
    return is_almost_equal(cos_vectors(vector_arr1, vector_arr2), 1, eps)


def is_not_directional(vector_arr1, vector_arr2, eps=EPS):
    """ Returns the orthogonality value of vectors with a given accuracy (default is 5) """
    ensure_types_vectors(vector_arr1, vector_arr2)
    return is_almost_equal(cos_vectors(vector_arr1, vector_arr2), -1, eps)


def change_direction(vector_arr):
    """ Changes the direction of the vector """
    ensure_types_vector(vector_arr)
    return [vector_arr[i] * -1 for i in range(len(vector_arr))]


def projection(vector_arr1, vector_arr2):
    """ Returns the projection of a vector onto a vector """
    ensure_types_vectors(vector_arr1, vector_arr2)
    return scalar(vector_arr1, vector_arr2) / lenght(vector_arr2)


def is_orthogonal(vector_arr1, vector_arr2, eps=EPS):
    """ Returns the orthogonality value of vectors with a given accuracy (default is 5) """
    ensure_types_vectors(vector_arr1, vector_arr2)
    return is_almost_equal(cos_vectors(vector_arr1, vector_arr2), 0, eps)


def is_equal(vector_arr1, vector_arr2):
    """Check two vectors for equality"""
    ensure_full_vector(vector_arr1, vector_arr2)
    if lenght(vector_arr1) == lenght(vector_arr2) and is_collinear(vector_arr1, vector_arr2) and is_directional(
            vector_arr1, vector_arr2):
        return True
    return False
