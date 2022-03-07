from PIL import Image
import numpy as np 


im = Image.open('./lena.bmp')
r, c = im.size

img = np.asarray(im)
closing = np.zeros((r,c), dtype = np.int32)
dilation = np.zeros((r,c), dtype = np.int32)

kernel=np.array([[0,1,1,1,0],
                 [1,1,1,1,1],
                 [1,1,1,1,1],
                 [1,1,1,1,1],
                 [0,1,1,1,0]])



"""Gray Scale Closing : Dilation -> Erosion"""
for i in range(r):
	for j in range(c):
		tmp = img[i][j]
		for x in range(-2,3):
			if i+x < 0 or i+x >= 512:
				break
			for y in range(-2,3):
				if j+y < 0 or j+y >= 512:
					break
				if kernel[x+2][y+2] == 1:
					tmp = max(tmp,img[i+x][y+j])

		dilation[i][j] = tmp


for i in range(r):
	for j in range(c):
		tmp = dilation[i][j]
		for x in range(-2,3):
			if i+x < 0 or i+x >= 512:
				break
			for y in range(-2,3):
				if j+y < 0 or j+y >= 512:
					break
				if kernel[x+2][y+2] == 1:
					tmp = min(tmp,dilation[i+x][j+y])

		closing[i][j] = tmp


im = Image.fromarray(closing)
im = im.convert("L")
im.save('lena_gray_scale_closing.bmp', format = 'BMP')


