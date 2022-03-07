from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

im = Image.open("lena_div3.bmp")
r, c = im.size
total_pixel = r * c

img = np.asarray(im)
x = np.arange(256)
histogram  = np.zeros(256, dtype = np.int32)

for i in range(r):
	for j in range(c):
		value = im.getpixel((i,j))
		histogram[value] += 1

s = np.zeros(256, dtype = np.int32)
s[0] = histogram[0]

for i in range(1,256):
	s[i] = s[i-1] + histogram[i]

for i in range(256):
	s[i] = round((s[i]*255) / total_pixel)
	histogram[i] = 0

for i in  range(r):
	for j in range(c):
		img[i][j] = s[img[i][j]]
		histogram[img[i][j]] += 1


im = Image.fromarray(img)
im.save('lena_equalization.bmp',format='BMP')
plt.bar(x,histogram)
plt.savefig("histogram_equalization.png",format="png")