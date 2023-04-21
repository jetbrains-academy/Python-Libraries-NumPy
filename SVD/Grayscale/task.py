from numpy import linalg
import matplotlib.pyplot as plt

img = plt.imread('horse.jpg')

img_rescaled = img / 255

# TODO You need to multiply the img_rescaled by a vector representing grayscale
# img_rescaled @ [R, G, B]
img_gray = img_rescaled @ [0.2126, 0.7152, 0.0722]

if __name__ == '__main__':
    print(img_gray.shape)
    # Try to run without the cmap parameter or change it
    plt.imshow(img_gray, cmap="gray")
    plt.show()
