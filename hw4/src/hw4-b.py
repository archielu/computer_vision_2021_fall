from PIL import Image
import numpy as np 


im = Image.open('./lena.bmp')
r, c = im.size

img = np.asarray(im)
erosion = np.zeros((r,c), np.int32)

kernel=np.array([[0,1,1,1,0],
                 [1,1,1,1,1],
                 [1,1,1,1,1],
                 [1,1,1,1,1],
                 [0,1,1,1,0]])

one_kernel = np.sum(kernel)
kernel_sz = kernel.shape[0]

"""Binarize the image"""
for i in range(r):
	for j in range(c):
		if img[i,j] >= 128:
			img[i,j] = 1
		else:
			img[i,j] = 0


for i in range(r - kernel_sz + 1):
	for j in range(c - kernel_sz + 1):
		match = 0
		for x in range(5):
			for  y  in range(5):
				match = match + kernel[x][y] *  img[i+x][j+y]

		if match == one_kernel:
			erosion[i+2][j+2] = 255


im = Image.fromarray(erosion)
im=im.convert("L")
im.save('lena_erosion.bmp',format='BMP')
