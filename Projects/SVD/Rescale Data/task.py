import matplotlib.pyplot as plt

img = plt.imread('horse.jpg')  # Read image and transform it into a NumPy array.

img_rescaled = img / 255

img_max, img_min = img.max(), img.min()
rescaled_max, rescaled_min = img_rescaled.max(), img_rescaled.min()

if __name__ == '__main__':
    print(img_max, img_min)
    print(rescaled_max, rescaled_min)

