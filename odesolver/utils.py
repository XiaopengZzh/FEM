import os
import numpy as np

resolution = np.array([900, 900])
offset = resolution / 2
scale = 200


def writeToFile(filename, frameNum, x):
    if not os.path.exists('output'):
        os.makedirs('output')

    with open(f"output/{filename}", 'a') as f:
        f.write(f"{frameNum}\t{x[0]}\t{x[1]}\n")


def generateUnitCircle(n):
    res = np.zeros([n, 2], dtype=np.float32)
    for i in range(n):
        res[i, 0] = np.cos(2 * np.pi * i / n)
        res[i, 1] = np.sin(2 * np.pi * i / n)
    return res


def screen_projection(x):
    return [offset[0] + scale * x[0], resolution[1] - (offset[1] + scale * x[1])]
