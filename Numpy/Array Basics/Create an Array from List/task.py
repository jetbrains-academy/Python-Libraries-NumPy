import numpy as np


def create_array(x, y):
    list_ = [[i for i in range(y)] for i in range(x)]
    arr = np.array(list_)
    return arr


if __name__ == "__main__":
    array_ = create_array(3, 5)
    print(array_)
    print(array_.shape)
