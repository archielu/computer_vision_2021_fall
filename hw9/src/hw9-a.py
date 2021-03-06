from PIL import Image
import numpy as np 
import math


threshold = 12
im = Image.open('./lena.bmp')
img = np.asarray(im)
r, c = img.shape

op1=np.array([[-1,0],
              [0,1]])
op2=np.array([[0,-1],
              [1,0]])

img = np.pad(img,(0,1),'edge')
mat=np.zeros((r,c),dtype=np.int32)


for i in range(r):
	for j in range(c):
		tmp = img[i:i+2,j:j+2]

		r1 = 0
		r2 = 0
		for a in range(2):
			for b in range(2):
				r1 += tmp[a][b] * op1[a][b]
				r2 += tmp[a][b] * op2[a][b]

		mat[i][j]=round(math.sqrt(r1*r1+r2*r2))
		if mat[i][j] >= threshold:
			mat[i][j] = 0
		else:
			mat[i][j] = 255


im=Image.fromarray(mat)
im.show()
im=im.convert('L')
im.save('lena_Roberts.bmp',format='BMP')
