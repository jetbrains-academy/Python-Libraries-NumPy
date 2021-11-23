from numpy import linalg
import numpy as np
import matplotlib.pyplot as plt

img = plt.imread('horse.jpg')

img_rescaled = img / 255

img_gray = img_rescaled @ [0.2126, 0.7152, 0.0722]

U, s, Vt = linalg.svd(img_gray)

Sigma = np.zeros((U.shape[1], Vt.shape[0]))
np.fill_diagonal(Sigma, s)

if __name__ == '__main__':
    print(Sigma.shape)
    print(Sigma)

