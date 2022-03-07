from PIL import Image
import  numpy as np 

im = Image.open('./lena.bmp')
r, c = im.size
img = np.asarray(im)

erosion = np.zeros((r,c), dtype = np.int32)
opening = np.zeros((r,c), dtype = np.int32)

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


""" Erosion"""
for i in range(r - kernel_sz + 1):
	for j in range(c - kernel_sz + 1):
		match = 0
		for x in range(5):
			for  y  in range(5):
				match = match + kernel[x][y] *  img[i+x][j+y]

		if match == one_kernel:
			erosion[i+2][j+2] = 1

""" Dilation """
for i in range(r):
	for j in range(c):
		if erosion[i][j] == 1:
			for x in range(-2,3,):
				if x+i < 0 or x+i >= r:
					break
				for y in range(-2,3):
					if j+y < 0 or j+y >= c:
						break
					if kernel[x+2][y+2] == 1:
						opening[i+x][j+y] = 255


im=Image.fromarray(opening)
im=im.convert("L")
im.save('lena_opening.bmp',format='BMP')