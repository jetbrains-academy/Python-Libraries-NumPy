import numpy as np


def read_data(file):
    text = np.loadtxt(file, delimiter='\n', dtype=np.bytes_)
    return np.char.decode(text)


if __name__ == '__main__':
    X = read_data('text.txt')
    print(X)
    print(type(X[0]))
