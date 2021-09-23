import numpy as np

data = np.genfromtxt('data.csv', delimiter=',', dtype=np.int64)
maxima = np.argmax(data, axis=1)
maxima = np.expand_dims(maxima, axis=1)
result = np.take_along_axis(data, maxima, axis=1)

if __name__ == '__main__':
    print(result)
