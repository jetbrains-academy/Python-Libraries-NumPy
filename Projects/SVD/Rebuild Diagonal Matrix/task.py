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
    # Print shape of the diagonal matrix:
    print(Sigma.shape)
    # Print the norm of the difference between img_gray and the reconstructed SVD product:
    print(linalg.norm(img_gray - U @ Sigma @ Vt))
    # Check if the reconstructed product is close to the original matrix
    print(np.allclose(img_gray, U @ Sigma @ Vt))

