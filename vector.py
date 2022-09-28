import math

# Error handling according to the EAFP rule
class Error(Exception):
    pass

def after_comma(number, digit=0):
    '''  '''
    return float(f"{number:.{digit}f}")


def lenght(vector_arr):
    ''' Returns the length of the vector '''
    trunk = 0
    for coord in vector_arr:
        trunk += (coord ** 2)
    return trunk ** (1 / 2)


def scalar(vector_arr1, vector_arr2):
    ''' Returns the scalar product of vectors '''
    try:
        trunk = 0
        for i in range(len(vector_arr1)):
            trunk += vector_arr1[i] * vector_arr2[i]
        return trunk
    except:
        raise Error("Type mismatch")


def normalize(vector_arr):
    ''' Returns a normalized vector '''
    return [i / lenght(vector_arr) for i in vector_arr]


def cos_vectors(vector_arr1, vector_arr2, digit=5):
    ''' Return the cos value between two vectors with the specified accuracy (default is 5) '''
    return after_comma(scalar(vector_arr1, vector_arr2) / (lenght(vector_arr1) * lenght(vector_arr2)), digit)


def angular(vector_arr1, vector_arr2, digit=5):
    ''' Returns the angle between vectors with the specified accuracy (default is 5) '''
    cos = cos_vectors(vector_arr1, vector_arr2, digit)
    rad = math.acos(cos)
    return round(rad / math.pi * 180, digit)


def sum_vectors(vector_arr1, vector_arr2):
    ''' Return sum of vectors '''
    return [vector_arr1[i] + vector_arr2[i] for i in range(len(vector_arr1))]


def dif_vectors(vector_arr1, vector_arr2):
    ''' Return difference of vectors '''
    return [vector_arr1[i] - vector_arr2[i] for i in range(len(vector_arr1))]


def mul_vectors(vector_arr1, vector_arr2):
    ''' Return multiplication of vectors or multiplying a vector by a scalar '''
    try:
        if type(vector_arr1) == int or type(vector_arr1) == float:
            return [vector_arr2[i] * vector_arr1 for i in range(len(vector_arr2))]
        elif type(vector_arr2) == int or type(vector_arr2) == float:
            return [vector_arr1[i] * vector_arr2 for i in range(len(vector_arr1))]
        return [vector_arr1[i] * vector_arr2[i] for i in range(len(vector_arr1))]
    except:
        raise Error("Type mismatch")


def div_vectors(vector_arr1, vector_arr2):
    ''' Return division of vectors or dividing a vector by a scalar '''
    try:
        if type(vector_arr1) == int or type(vector_arr1) == float:
            return [vector_arr2[i] / vector_arr1 for i in range(len(vector_arr2))]
        elif type(vector_arr2) == int or type(vector_arr2) == float:
            return [vector_arr1[i] / vector_arr2 for i in range(len(vector_arr1))]
        return [vector_arr1[i] / vector_arr2[i] for i in range(len(vector_arr1))]
    except:
        raise Error("Type mismatch")


def is_collinear(vector_arr1, vector_arr2, digit=5):
    ''' Checks vectors for collinearity with the specified accuracy (default is 5) '''
    return abs(cos_vectors(vector_arr1, vector_arr2, digit)) == 1.0


def is_directional(vector_arr1, vector_arr2, digit=5):
    ''' Checks vectors for co-directionality with a given accuracy (default is 5) '''
    return cos_vectors(vector_arr1, vector_arr2, digit) == 1.0


def is_not_directional(vector_arr1, vector_arr2, digit=3):
    ''' Returns the orthogonality value of vectors with a given accuracy (default is 5) '''
    return cos_vectors(vector_arr1, vector_arr2, digit) == -1.0


def change_direction(vector_arr):
    ''' Changes the direction of the vector '''
    vector_arr = [vector_arr[i] * -1 for i in range(len(vector_arr))]


def projection(vector_arr1, vector_arr2):
    ''' Returns the projection of a vector onto a vector '''
    return scalar(vector_arr1, vector_arr2) / lenght(vector_arr2)


def is_orthogonal(vector_arr1, vector_arr2, digit=5):
    ''' Returns the orthogonality value of vectors with a given accuracy (default is 5) '''
    return cos_vectors(vector_arr1, vector_arr2, digit) == 0


def is_equal(vector_arr1, vector_arr2, digit=0):
    """Check two vectors for equality"""
    assert len(vector_arr1) == len(vector_arr2), "Vector dimension error"
    for i in range(len(vector_arr1)):
        if vector_arr1[i] - vector_arr2[i] > 0 + digit:
            return False
    return True
