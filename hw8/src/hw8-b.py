from PIL import Image
import numpy as np 
import SNR


im = Image.open('./lena.bmp')
img = np.asarray(im)
r, c = img.shape

img_005 = np.zeros((r,c),dtype=np.int32)
img_005[0:r,0:c] = img[0:r,0:c]

noise = np.random.uniform(0.0,1.0,(r,c))

for i in range(r):
	for j in range(c):
		if noise[i][j] > 0.95:
			img_005[i][j] = 255
		if noise[i][j] < 0.05:
			img_005[i][j] = 0

Snr = SNR.snr(img, img_005)
print(f'snr_sp_005: {Snr}')

im=Image.fromarray(img_005)
im.show()
im=im.convert("L")
im.save('lena_salt_and_pepper005.bmp',format='BMP')




img_010 = np.zeros((r,c),dtype=np.int32)
img_010[0:r,0:c] = img[0:r,0:c]

noise = np.random.uniform(0.0,1.0,(r,c))

for i in range(r):
	for j in range(c):
		if noise[i][j] > 0.9:
			img_010[i][j] = 255
		if noise[i][j] < 0.1:
			img_010[i][j] = 0

Snr = SNR.snr(img, img_010)
print(f'snr_sp_010: {Snr}')

im=Image.fromarray(img_010)
im.show()
im=im.convert("L")
im.save('lena_salt_and_pepper010.bmp',format='BMP')







