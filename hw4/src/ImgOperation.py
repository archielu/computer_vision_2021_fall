from PIL import Image
import numpy as np



def Image_Read(file_name):
	im=Image.open(file_name)
	row,col=im.size
	return im, row, col

def Image_Binarize(img, threshold):
	sz = img.shape
	r, c =  sz[0], sz[1]
	for i in range(r):
		for j in range(c):
			if img[i][j] >= threshold:
				img[i][j] = 1
			else:
				img[i][j] = 0
	return img
	

