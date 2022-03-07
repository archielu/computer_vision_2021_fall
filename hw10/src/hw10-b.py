
from  PIL import Image
import numpy as np 
import math

threshold=15

im=Image.open('../lena.bmp')
img=np.asarray(im)
r, c = img.shape

mask=np.array([[1,1,1],
               [1,-8,1],
               [1,1,1]])/3

img=np.pad(img,(1,1),'edge')
mat=np.zeros((r,c),dtype=np.int32)

for i in range(1,r+1):
    for j in range(1,c+1):
        tmp=img[i-1:i+2,j-1:j+2]
        t=0
        for a in range(3):
            for b in range(3):
                t+=tmp[a][b]*mask[a][b]

        if t>=threshold:
            mat[i-1][j-1]=1
        elif t<=-threshold:
            mat[i-1][j-1]=-1
        else:
            mat[i-1][j-1]=0

final=np.zeros((r,c),dtype=np.int32)

mat=np.pad(mat,(1,1),'edge')
for i in range(1,r+1):
    for j in range(1,c+1):
        if mat[i][j] == 1 and (mat[i-1][j] == -1 or mat[i-1][j+1] == -1 or mat[i-1][j-1] == -1 or mat[i][j+1] == -1 or mat[i][j-1] == -1 or mat[i+1][j] == -1 or mat[i+1][j-1] == -1 or mat[i+1][j+1] == -1 ):
            final[i-1][j-1] = 0
        else:
            final[i-1][j-1] =  255

im=Image.fromarray(final)
im.show()
im=im.convert('L')
im.save('lena_laplace2.bmp',format='BMP')