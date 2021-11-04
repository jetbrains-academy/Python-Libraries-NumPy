import numpy as np


def reshape_transpose(start, stop, step=1):
    array = np.arange(start, stop, step)
    reshaped = array.reshape(1, array.shape[0])
    return reshaped.T


if __name__ == '__main__':
    print(reshape_transpose(1, 100, 10))
    print(reshape_transpose(0, 5))
