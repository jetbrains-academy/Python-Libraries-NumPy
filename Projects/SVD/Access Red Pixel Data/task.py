import matplotlib.pyplot as plt

img = plt.imread('horse.jpg')  # Read image and transform it into a NumPy array.

red_pixel_data = img[:, :, 0]

if __name__ == '__main__':
    print(red_pixel_data)
    print(red_pixel_data.shape)

