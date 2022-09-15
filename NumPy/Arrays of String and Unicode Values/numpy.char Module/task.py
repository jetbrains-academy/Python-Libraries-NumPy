import numpy as np


def read_data(file):
    # This will result in two elements for each line of text, such as
    # [b'Some text', b'']. You will need only the first of them,
    # so use slicing in the TODO below.
    text = np.loadtxt(file, delimiter='.', dtype=np.bytes_)
    return np.char.decode(text[:, 0])

if __name__ == '__main__':
    X = read_data('text.txt')
    print(X)
    # This should NOT be a list:
    print(X[0])
    # This should NOT be a numpy.ndarray:
    print(type(X[0]))
