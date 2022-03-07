from PIL import Image
import numpy as np 

im = Image.open('./lena.bmp')
r, c = im.size

erosion = np.zeros((r,c), dtype = np.int32)
img  = np.asarray(im)


kernel=np.array([[0,1,1,1,0],
                 [1,1,1,1,1],
                 [1,1,1,1,1],
                 [1,1,1,1,1],
                 [0,1,1,1,0]])


"""Gray Scale Erosion: Minimum"""
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
					tmp = min(tmp,img[i+x][y+j])

		erosion[i][j] = tmp

im = Image.fromarray(erosion)
im = im.convert("L")
im.save('lena_gray_scale_erosion.bmp', format = 'BMP')




