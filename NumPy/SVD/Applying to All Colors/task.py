from numpy import linalg
import numpy as np
import matplotlib.pyplot as plt

img = plt.imread('horse.jpg')

img_rescaled = img / 255

img_array_transposed = np.transpose(img_rescaled, (2, 0, 1))
U, s, Vt = linalg.svd(img_array_transposed)

if __name__ == '__main__':
    print(img_array_transposed.shape)
    print(U.shape, s.shape, Vt.shape)

