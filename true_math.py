from math import inf

def divide(first, second):
    res = 1.0
    if (isinstance(first, (int, float)) and isinstance(second, (int, float))):
        if second == 0:
            res = inf
        else:
            res = first / second
    return res
