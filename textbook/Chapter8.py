import math
from manage import nullcheck

def UnitVector (column_vec:tuple = ()) -> tuple:
    column_vec = nullcheck.ColumnVecInput(column_vec)
    mag = VectorMagnitude(column_vec)
    return (column_vec[0] / mag, column_vec[1] / mag)


def VectorMagnitude (column_vec:tuple = ()) -> float:
    column_vec = nullcheck.ColumnVecInput(column_vec)
    return math.sqrt((column_vec[0]**2 + column_vec[1]**2))


def TriangleLaw ():
    pass