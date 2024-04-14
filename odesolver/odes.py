import numpy as np
import math


def fUnitCircle(x):
    res = np.array([0.0, 0.0])
    r = x[0] ** 2 + x[1] ** 2
    res[0] = -r * x[1]
    res[1] = r * x[0]
    return res


def initUnitCircle():
    return np.array([1.0, 0.0])


def exactSolutionUnitCircle(t):
    return np.array([math.cos(t), math.sin(t)])
