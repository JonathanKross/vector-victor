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

def vector_add(vector1, vector2):
    """
    [a b]  + [c d]  = [a+c b+d]
    """
    if len(vector1) != len(vector2):
        raise ShapeError()
    else:
        return [x + y for x, y in zip(vector1, vector2)]

def test_vector_sub():
    """
    [a b]  - [c d]  = [a-c b-d]
    """
    assert vector_sub(v, w) == [1, 1, -4]
    assert vector_sub(w, v) == [-1, -1, 4]
    assert vector_sub(y, z) == y
    assert vector_sub(w, u) == vector_sub(z, vector_sub(u, w))





if __name__ == '__main__':
    main()
