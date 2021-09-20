import numpy as np

arr = np.arange(1000)
filter_ = arr % 4 == 0
filtered_arr = arr[filter_]


if __name__ == '__main__':
    print(filtered_arr)
