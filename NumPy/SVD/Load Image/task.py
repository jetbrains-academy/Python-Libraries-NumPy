import matplotlib.pyplot as plt
img = plt.imread('horses.jpg')
print(type(img))
print(img.shape)
print(img.ndim)


plt.imshow(img)
plt.show()