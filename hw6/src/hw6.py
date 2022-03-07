from PIL import Image
import numpy as np 

im = Image.open('./lena.bmp')
img = np.asarray(im)
r,c = img.shape

for i in range(r):
	for j in range(c):
		if img[i][j] >= 128:
			img[i][j] = 1
		else:
			img[i][j] = 0


new_img = np.zeros((66,66), dtype = np.int32)

for i in range(1,65):
	for j in range(1,65):
		img[i-1][j-1] = img[8*i-8][8*j-8]
		new_img[i][j] = img[8*i-8][8*j-8]


def h(b,c,d,e):
	if b == c and (d != b or e != b):
		return 'q'
	if b == c and (d == b and e == b):
		return 'r'
	if b != c:
		return 's'


def f(a1,a2,a3,a4):
	if a1 == 'r' and a2 == 'r' and a3 == 'r' and a4 == 'r':
		return 5
	count = 0
	if a1 == 'q':
		count += 1
	if a2 == 'q':
		count += 1
	if a3 == 'q':
		count += 1
	if a4 == 'q':
		count += 1

	return count


for i in range(1,65):
	for j in range(1,65):
		if new_img[i][j] == 1:
			a1 = h(new_img[i][j],new_img[i][j+1],new_img[i-1][j+1],new_img[i-1][j])
			a2 = h(new_img[i][j],new_img[i-1][j],new_img[i-1][j-1],new_img[i][j-1])
			a3 = h(new_img[i][j],new_img[i][j-1],new_img[i+1][j-1],new_img[i+1][j])
			a4 = h(new_img[i][j],new_img[i+1][j],new_img[i+1][j+1],new_img[i][j+1])

			img[i-1][j-1] = f(a1,a2,a3,a4)


f = open('yokoi_number.txt','w')

for i in range(64):
    for j in range(64):
        if img[i][j]==0:
            print(" ",end='')
            f.write(" ")
        else:
            print(img[i][j],end="")
            f.write(str(img[i][j]))
    print()
    f.write("\n")

f.close()



