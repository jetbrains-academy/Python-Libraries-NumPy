import numpy as np

a = np.arange(20).reshape(2, 2, 5)
b = np.array([[True, False], [False, True]])
c = a[b]

if __name__ == '__main__':
    print('Array a:\n', a, '\n')
    print('Indexed array c:\n', c)
    print(c.shape)
