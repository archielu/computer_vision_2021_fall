from PIL import Image
import numpy as np



im = Image.open('./lena.bmp')
img =  np.array(im)
r, c = img.shape

for i in range(r):
	for j in range(c):
		if(img[i][j] >= 128):
			img[i][j] = 255
		else:
			img[i][j] = 0

im = Image.fromarray(img)
im.save('lena_binary.bmp', format='BMP')

