import numpy as np

rng = np.random.default_rng()

x = np.arange(10)
x = x.reshape(10, 1)
y = np.ones(7)

w = rng.integers(2, size=(4, 3))
w = w.reshape(3, 4)
z = np.ones((3, 4))

if __name__ == '__main__':
    print(x)
    print(y)
    print(x + y)
    print(z)
    print(w)
    print(z * w)
