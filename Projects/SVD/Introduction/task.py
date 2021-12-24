import numpy as np

# An example of SVD matrix decomposition,
# the procedure you will be using in this lesson.
a = np.random.randn(9, 6) + 1j*np.random.randn(9, 6)
u, s, vh = np.linalg.svd(a, full_matrices=True)

if __name__ == "__main__":
    print(u.shape, s.shape, vh.shape)
