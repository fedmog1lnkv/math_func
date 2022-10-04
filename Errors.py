# ---------Error for vector---------

def ensure_shape_vectors(arr1, arr2):
    if len(arr1) != len(arr2):
        raise ValueError("Error of different lengths vectors")


def ensure_types_vector(arr):
    for point in arr:
        if type(point) != int and type(point) != float:
            raise TypeError("An incorrect type in vector")


def ensure_types_vectors(arr1, arr2):
    ensure_types_vector(arr1)
    ensure_types_vector(arr2)


def ensure_full_vector(arr1, arr2):
    ensure_shape_vectors(arr1, arr2)
    ensure_types_vector(arr1)
    ensure_types_vector(arr2)


# ---------Error for matrix---------

def ensure_shape_matrix(arr1, arr2):
    if len(arr1) != len(arr2):
        raise ValueError("Error of different lengths matrix")
    for IX_row in range(len(arr1) - 1):
        if len(arr1[IX_row]) != len(arr1[IX_row + 1]):
            raise ValueError("Error of different lengths in rows matrix")
    for IX_row in range(len(arr2) - 1):
        if len(arr2[IX_row]) != len(arr2[IX_row + 1]):
            raise ValueError("Error of different lengths in rows matrix")


def ensure_types_matrix(arr):
    for row in arr:
        for j in range(len(row)):
            if type(row[j]) != int and type(row[j]) != float:
                raise TypeError("An incorrect type is found in one of the row")

def ensure_types_matrices(arr1, arr2):
    ensure_types_matrix(arr1)
    ensure_types_matrix(arr2)


def ensure_shape_matrix_mul(arr1, arr2):
    if len(arr1[0]) != len(arr2):
        raise ValueError("Cannot multiply the two matrices, incorrect dimensions")


def ensure_full_matrix(arr1, arr2):
    ensure_types_matrices(arr1, arr2)
    ensure_shape_matrix_mul(arr1, arr2)
