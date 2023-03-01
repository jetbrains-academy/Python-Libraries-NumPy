import numpy as np
rng = np.random.default_rng()

a = rng.integers(100, size=(5, 20))


b = np.sort(a, axis=0)
ind = np.argsort(b, axis=1)
c = np.take_along_axis(b, ind, axis=1)


if __name__ == '__main__':
    print('\nUnsorted array:\n', a)
    print('\nSorted columns:\n', b)
    print('\nIndices to sort rows:\n', ind)
    print('\nSorted:\n', c)
