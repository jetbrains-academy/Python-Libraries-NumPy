import numpy as np

x = np.arange(35)
y = x.reshape(5, 7)

a = x[np.array([7, 13, 28, 33])]
b = x[np.array([[0, 1, 2], [10, 11, 12], [28, 29, 30]])]


c = y[np.array([0, 2, 4])]
d = y[np.array([0, 2, 4]), np.array([0, 1, 2])]
e = y[np.array([1, 2, 4]), 6]


if __name__ == '__main__':
    print(y)
    print('\n', a.shape)
    print('\n', b.shape)
    print('\n', c.shape)
    print('\n', d.shape)
    print('\n', e.shape)
