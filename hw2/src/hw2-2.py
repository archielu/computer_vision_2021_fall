from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


im = Image.open('lena.bmp')
r, c = im.size

y = np.zeros(256, dtype = np.int)

for i in range(r):
	for j in range(c):
		y[im.getpixel((i,j))] += 1


x= np.arange(256)
plt.bar(x,y)
plt.savefig("histogram", format = "png")





