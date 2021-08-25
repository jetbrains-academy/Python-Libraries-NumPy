import numpy as np
rng = np.random.default_rng()

k = 3
arr = rng.normal(1, 1, 10)
target = 0
distances = abs(arr - target)

indices = np.argpartition(distances, k)
partitioned_by_distance = arr[indices]
k_nearest = partitioned_by_distance[:k]

if __name__ == '__main__':
    print('Data:\n', arr)
    print('\nDistances from target value:\n', distances)
    print('\nIndices of partitioned data:\n', indices)
    print('\nPartitioned data:\n', partitioned_by_distance)
    print('\nK=3 nearest data points\n', k_nearest)
