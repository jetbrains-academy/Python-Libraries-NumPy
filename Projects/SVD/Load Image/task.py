import matplotlib.pyplot as plt

img = plt.imread('horse.jpg')  # Read image and transform it into a NumPy array.

print(type(img))
print(img.ndim)
print(img.shape)

if __name__ == '__main__':
    plt.imshow(img)  # Display data as an image.
    plt.show()  # Display all open figures.
