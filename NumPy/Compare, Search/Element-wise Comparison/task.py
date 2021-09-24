import numpy as np

a = np.arange(20).reshape(4, 5)
b = np.arange(0, 25, 6)
compare_a_b = np.equal(a, b)


if __name__ == '__main__':
    print(a)
    print(b)
    print(np.array_equal(compare_a_b, np.array([[True, False, False, False, False],
                                                [False, True, False, False, False],
                                                [False, False, True, False, False],
                                                [False, False, False, True, False]])))

