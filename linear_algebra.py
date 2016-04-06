#NO FOR OR WHILE LOOPS
#NO IMPORTING LIBRARIES
    #(built-in math operators like +, -, *, / ok)
    #math module ok

# Implement these linear algebra functions:
# vector shape in shape() !
# vector addition in vector_add() !
# vector subtraction in vector_sub() !
# vector sum in vector_sum() !
# dot product in dot()
# vector multiplication by a scalar in vector_multiply()
# mean of multiple vectors in vector_mean()
# magnitude in magnitude()
#RUN nosetests to run the test

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
    return [(x + y) for x, y in zip(vector1, vector2)]

def vector_sub(vector1, vector2):
    return [(x - y) for x, y in zip(vector1, vector2)]
#
# def vector_sum(**kwargs):
#     summed_list = zip(**kwargs)
#     [sum(item for item in summed_list)]
#
def dot(vector1, vector2):
    sum(x * y for x, y in zip(vector1, vector2))
