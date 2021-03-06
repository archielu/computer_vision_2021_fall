from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

im = Image.open("lena.bmp")

r, c = im.size

x = np.arange(256)
y = np.zeros(256, dtype = np.int32)

for i in range(r):
	for j in range(c):
		value = im.getpixel((i,j))
		y[value] += 1

plt.bar(x,y)
plt.savefig("histogram.png", format = "png")

