

class ShapeError(Exception):
    pass

def are_equal (x , y, tolerance=0.001):
    return abs(x - y) <= tolerance

def shape(vector):
    """
    shape takes a vector and
    return a tuple with the number of rows
    """

    return (len(vector),)

def shape_diff_error(vector1, vector2):
    if shape(vector1) != shape(vector2):
        raise ShapeError("Vectors must be the same size")
    else:
        return True


def vector_add(vector1, vector2):
    """
    [a b] + [c d] = [a+c b+d]
    """

    shape_diff_error(vector1, vector2)
    return [x + y for x, y in zip(vector1, vector2)]

def vector_sub(vector1, vector2):
    """
    [a b] - [c d] = [a-c b-d]
    """

    shape_diff_error(vector1, vector2)
    return [x - y for x, y in zip(vector1, vector2)]


def vector_sum(*args):
    """vector_sum can take any number of vectors and add them together."""

    length = [len(i) for i in args]
    if max(length) != min(length):
        raise ShapeError("Vectors must be the same size")
    return [sum(x) for x in zip(*args)]


def dot(vector1, vector2):
    """
    dot([a b], [c d])   = a * c + b * d
    dot(Vector, Vector) = Scalar
    """
    shape_diff_error(vector1, vector2)
    # return sum([vector1[i] * vector2[i] for i in range(len(vector1))])
    return sum([a * b for a, b in zip(vector1, vector2)])


def vector_multiply(vector1, scalar):
    """
    [a b] * Z = [a*Z b*Z]
    Vector * Scalar = Vector
    """

    return [scalar * x for x in vector1]

def vector_mean(*args):
    """
    mean([a b], [c d]) = [mean(a, c) mean(b, d)]
    mean(Vector)       = Vector
    """

    return[x/len(args) for x in vector_sum(*args)]

def magnitude(vector1):
    """
    magnitude([a b])  = sqrt(a^2 + b^2)
    magnitude(Vector) = Scalar
    """

    return sum(x ** 2 for x in vector1) ** 0.5


def shape_matrices(matrix):
    """
    shape takes a matrix and return a tuple with
    the number of rows and columns
    """

    return (len(matrix), len(matrix[0]))

def matrix_row(matrix, row):
    """
           0 1  <- columns
       0 [[a b]]
       1 [[c d]]
       ^
     rows
    """
    return matrix[row]

def matrix_col(matrix, column):
    """
           0 1  <- columns
       0 [[a b]]
       1 [[c d]]
       ^
     rows
    """

    return [group[column] for group in matrix]

def matrix_add(matrix1, matrix2):
    return []
