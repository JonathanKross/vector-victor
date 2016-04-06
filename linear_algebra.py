import math


class ShapeError(Exception):
    pass

m = [3, 4]
n = [5, 0]

v = [1, 3, 0]
w = [0, 2, 4]
u = [1, 1, 1]
y = [10, 20, 30]
z = [0, 0, 0]

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
    return sum([vector1[i] * vector2[i] for i in range(len(vector1))])
    # return sum([a * b for a , b in zip (vector1, vector2)])


def vector_multiply():
    """
    [a b]  *  Z     = [a*Z b*Z]
    Vector * Scalar = Vector
    """
    assert vector_multiply(v, 0.5) == [0.5, 1.5, 0]
    assert vector_multiply(m, 2) == [6, 8]




if __name__ == '__main__':
    main()
