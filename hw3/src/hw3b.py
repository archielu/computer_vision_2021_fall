from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

im = Image.open("lena.bmp")
r, c = im.size
img = np.asarray(im)

x = np.arange(256)
y = np.zeros(256, dtype = np.int32)

for i in range(r):
	for j in range(c):
		img[i][j] = img[i][j] // 3
		y[img[i][j]] += 1


im = Image.fromarray(img)
im.save('lena_div3.bmp',format='BMP')

plt.bar(x,y)
plt.savefig("histogram_div3.png",format="png")
