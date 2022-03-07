from PIL import Image
import numpy as np 


im = Image.open('./lena.bmp')
r, c = im.size

img = np.asarray(im)
img_c = np.asarray(im)

A_J = np.zeros((r,c) , dtype = np.int32)
Ac_K = np.zeros((r,c), dtype = np.int32)
H_A_M = np.zeros((r,c), dtype = np.int32)

J=np.array([[0,0,0],
            [1,1,0],
            [0,1,0]])

K=np.array([[0,1,1],
            [0,0,1],
            [0,0,0]])

one_kernel = np.sum(J)

for i in range(r):
	for j in range(c):
		if img[i][j] >= 128:
			img[i][j] = 1
			img_c[i][j] = 0
		else:
			img[i][j] = 0
			img_c[i][j] = 1


""" A-J """
for i in range(r-2):
	for j in range(c-2):
		match = 0
		for x in range(3):
			for y in range(3):
				match += J[x][y] * img[i+x][j+y]

		if match == one_kernel:
			A_J[i+1][j+1] = 1

""" Ac-K"""
for i in range(r-2):
	for j in range(c-2):
		match = 0
		for x in range(3):
			for y in range(3):
				match += K[x][y] * img_c[i+x][j+y]

		if match == one_kernel:
			Ac_K[i+1][j+1] = 1

""" Intersection of A-J and Ac-K """
for i in range(r):
	for j in range(c):
		if A_J[i][j] == 1 and  Ac_K[i][j] == 1:
			H_A_M[i][j] = 255

im = Image.fromarray(H_A_M)
im = im.convert("L")
im.save('lena_HitAndMiss.bmp',format='BMP')
