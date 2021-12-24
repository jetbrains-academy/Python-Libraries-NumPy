import matplotlib.pyplot as plt

img = plt.imread('horse.jpg')  # Read image and transform it into a NumPy array.

img_rescaled = img / 255

red_channel = img_rescaled[:, :, 0]
green_channel = img_rescaled[:, :, 1]
blue_channel = img_rescaled[:, :, 2]

if __name__ == '__main__':
    print('Green channel: ')
    print(red_channel)
    print('\nRed channel: ')
    print(green_channel)
    print('\nBlue channel: ')
    print(blue_channel)


