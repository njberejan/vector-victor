#NO FOR OR WHILE LOOPS
#NO IMPORTING LIBRARIES
    #(built-in math operators like +, -, *, / ok)
    #math module ok

# Implement these linear algebra functions:
# vector shape in shape() !
# vector addition in vector_add() !
# vector subtraction in vector_sub() !
# vector sum in vector_sum()
# dot product in dot() !
# vector multiplication by a scalar in vector_multiply()
# mean of multiple vectors in vector_mean()
# magnitude in magnitude()
#RUN nosetests to run the test
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


def shape(vector):
    return len(vector),

def vector_add(vector1, vector2):
    if shape(vector1) != shape(vector2):
        raise ShapeError
    else:
        return [(x + y) for x, y in zip(vector1, vector2)]

def vector_sub(vector1, vector2):
    if shape(vector1) != shape(vector2):
        raise ShapeError
    else:
        return [(x - y) for x, y in zip(vector1, vector2)]

def vector_sum(*args):
    #go over why this works tomorrow
    if len(set(shape(i) for i in zip(*args)))>1:
        raise ShapeError
    else:
        return [sum(i) for i in zip(*args)]


def dot(vector1, vector2):
    if shape(vector1) != shape(vector2):
        raise ShapeError
    else:
        return sum(x * y for x, y in zip(vector1, vector2))

def vector_multiply(vector, scalar):
    return [x * scalar for x in vector]

def vector_mean(*args):
    return [float(sum(arg))/len(arg) for arg in zip(*args)]

def magnitude(vector):
    return [math.sqrt(x * x) for x in vector]
