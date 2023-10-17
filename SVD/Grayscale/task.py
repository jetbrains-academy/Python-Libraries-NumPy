from numpy import linalg
import matplotlib.pyplot as plt

img = plt.imread('horse.jpg')

img_rescaled = img / 255

# TODO You need to multiply the img_rescaled by a vector representing grayscale
# img_rescaled @ grayscale_vector
grayscale_vector = [0.2126, 0.7152, 0.0722]
img_gray = img_rescaled @ grayscale_vector

if __name__ == '__main__':
    print(img_gray.shape)
    figure = plt.gcf()
    figure.set_size_inches(25, 25)
    # Try to run without the cmap parameter or change it
    plt.imshow(img_gray, cmap="gray")
    plt.show()
