import numpy as np

a = np.arange(12, 30, 3)
b = a.reshape(2, 3)

if __name__ == "__main__":
    print(a)
    print('shape : ', a.shape)
    print('\nAfter reshaping : ')
    print(b)
    print('shape : ', b.shape)
