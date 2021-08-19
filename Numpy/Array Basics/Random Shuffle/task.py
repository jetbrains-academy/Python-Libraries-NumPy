import numpy as np

rng = np.random.default_rng()

arr = np.arange(100).reshape(5, 20)
rng.shuffle(arr)
permuted_2d = rng.permutation(arr, axis=1)
fully_random = rng.permutation(arr.flatten()).reshape(5, 20)


if __name__ == '__main__':
    print(arr)
    for i in arr:
        print(i[0], min(i))
        print(i[-1], max(i))
    print(permuted_2d)
    print(fully_random)
