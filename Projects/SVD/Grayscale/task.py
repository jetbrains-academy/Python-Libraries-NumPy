from numpy import linalg
import matplotlib.pyplot as plt

img = plt.imread('horse.jpg')

img_rescaled = img / 255

img_gray = img_rescaled @ [0.2126, 0.7152, 0.0722]

if __name__ == '__main__':
    print(img_gray.shape)
    plt.imshow(img_gray, cmap="gray")
    plt.show()
