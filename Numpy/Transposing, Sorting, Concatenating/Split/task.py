import numpy as np

x = np.arange(24).reshape(6, 4)
# [[ 0  1  2  3]
# [ 4  5  6  7]
# [ 8  9 10 11]
# [12 13 14 15]
# [16 17 18 19]
# [20 21 22 23]]

arr1, arr2, arr3 = np.split(x, 3)

y = np.arange(12).reshape(3, 4)
# [[ 0  1  2  3]
# [ 4  5  6  7]
# [ 8  9 10 11]]

arr4, arr5, arr6 = np.array_split(y, 3, axis=1)

if __name__ == '__main__':
    print(arr1, '\n', arr2, '\n', arr3, '\n')
    print(arr4, '\n', arr5, '\n',  arr6)