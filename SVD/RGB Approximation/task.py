from numpy import linalg
import numpy as np
import matplotlib.pyplot as plt

img = plt.imread('horse.jpg')

img_rescaled = img / 255

# To learn the missing steps see the full version of the course Python Libraries - Numpy
img_array_transposed = np.transpose(img_rescaled, (2, 0, 1))
U, s, Vt = linalg.svd(img_array_transposed)

Sigma = np.zeros((3, 408, 612))
for j in range(3):
    np.fill_diagonal(Sigma[j, :, :], s[j, :])

reconstructed = U @ Sigma @ Vt

reconstructed = np.clip(reconstructed, 0, 1)

# TODO Try and change this parameter to see how the quality of compression changes
k = 10
# Multiply the U matrix by Sigma[..., :k] and Vt[..., :k, :]
approx_img = U @ Sigma[..., :k] @ Vt[..., :k, :]

fig, axes = plt.subplots(1, 2)
axes[0].imshow(np.transpose(approx_img, (1, 2, 0)))
axes[1].imshow(np.transpose(reconstructed, (1, 2, 0)))

if __name__ == '__main__':
    print(approx_img.shape)
    plt.show()
