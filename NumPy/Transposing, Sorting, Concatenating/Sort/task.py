import numpy as np
rng = np.random.default_rng()

a = rng.integers(100, size=(5, 20))


b = np.sort(a, axis=0)  # Sort columns
ind = np.argsort(b, axis=1)  # Indices to sort rows
c = np.take_along_axis(b, ind, axis=1)  # Sort rows using indices ind


if __name__ == '__main__':
    print('\nUnsorted array:\n', a)
    print('\nSorted columns:\n', b)
    print('\nIndices to sort rows:\n', ind)
    print('\nSorted:\n', c)
