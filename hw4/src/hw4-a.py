from PIL import Image
import numpy as np 


im = Image.open('./lena.bmp')
r, c = im.size
img = np.asarray(im)

dilation = np.zeros((r, c) , dtype = np.int32)

kernel=np.array([[0,1,1,1,0],
                 [1,1,1,1,1],
                 [1,1,1,1,1],
                 [1,1,1,1,1],
                 [0,1,1,1,0]])

for i in range(r):
	for j in range(c):
		if img[i][j] >= 128:
			img[i][j] = 1
		else:
			img[i][j] = 0



for i in range(r):
	for j in range(c):
		if img[i][j] == 1:
			for x in range(-2,3):
				if i+x < 0 or i+x >= 512:
					break
				for y in range(-2,3):
					if j+y < 0 or j+y >= 512:
						break
					if kernel[x+2][y+2] == 1:
						dilation[i+x][j+y] = 255


im = Image.fromarray(dilation)
im = im.convert("L")
im.save('lena_dilation.bmp',format='BMP')