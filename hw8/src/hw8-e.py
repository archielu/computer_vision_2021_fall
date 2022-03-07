from PIL import Image
import numpy as np 
import SNR


def dilation(img):
	r,c = img.shape
	kernel=np.array([[0,1,1,1,0],
                 [1,1,1,1,1],
                 [1,1,1,1,1],
                 [1,1,1,1,1],
                 [0,1,1,1,0]])


	Dilation = np.zeros((r,c),dtype=np.int32)

	"""Gray Scale Dilation: Maximum"""
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

			Dilation[i][j] = tmp

	return Dilation


def erosion(img):
	r,c = img.shape
	kernel=np.array([[0,1,1,1,0],
                 [1,1,1,1,1],
                 [1,1,1,1,1],
                 [1,1,1,1,1],
                 [0,1,1,1,0]])

	Erosion = np.zeros((r,c), dtype = np.int32)
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

			Erosion[i][j] = tmp

	return Erosion


def opening(img):
    return dilation(erosion(img))

def closing(img):
    return erosion(dilation(img))




im=Image.open('./lena.bmp')
img = np.asarray(im)

im1=Image.open('lena_Gaussian10.bmp')
im2=Image.open('lena_Gaussian30.bmp')
im3=Image.open('lena_salt_and_pepper010.bmp')
im4=Image.open('lena_salt_and_pepper005.bmp')


img1oc=np.asarray(im1)
img1co=np.asarray(im1)

img2oc=np.asarray(im2)
img2co=np.asarray(im2)

img3oc=np.asarray(im3)
img3co=np.asarray(im3)

img4oc=np.asarray(im4)
img4co=np.asarray(im4)



tmpImg=opening(closing(img1oc))
Snr=SNR.snr(img,tmpImg)
print(f'snr Gaussian10 c-o: {Snr}')
im1=Image.fromarray(tmpImg)
im1.show()
im1=im1.convert("L")
im1.save('lena_gauss10_closing_opening.bmp',format='BMP')

tmpImg=closing(opening(img1co))
Snr=SNR.snr(img,tmpImg)
print(f'snr Gaussian10 o-c: {Snr}')
im1=Image.fromarray(tmpImg)
im1.show()
im1=im1.convert("L")
im1.save('lena_gauss10_opening_closing.bmp',format='BMP')

tmpImg=opening(closing(img2oc))
Snr=SNR.snr(img,tmpImg)
print(f'snr Gaussian30 c-o: {Snr}')
im2=Image.fromarray(tmpImg)
im2.show()
im2=im2.convert("L")
im2.save('lena_gauss30_closing_opening.bmp',format='BMP')

tmpImg=closing(opening(img2co))
Snr=SNR.snr(img,tmpImg)
print(f'snr Gaussian10 o-c: {Snr}')
im2=Image.fromarray(tmpImg)
im2.show()
im2=im2.convert("L")
im2.save('lena_gauss30_opening_closing.bmp',format='BMP')

tmpImg=opening(closing(img3oc))
Snr=SNR.snr(img,tmpImg)
print(f'snr SAP 0.1 c-o: {Snr}')
im3=Image.fromarray(tmpImg)
im3.show()
im3=im3.convert("L")
im3.save('lena_sap01_closing_opening.bmp',format='BMP')


tmpImg=closing(opening(img3co))
Snr=SNR.snr(img,tmpImg)
print(f'snr SAP 0.1 o-c: {Snr}')
im3=Image.fromarray(tmpImg)
im3.show()
im3=im3.convert("L")
im3.save('lena_sap01_opening_closing.bmp',format='BMP')


tmpImg=opening(closing(img4oc))
Snr=SNR.snr(img,tmpImg)
print(f'snr SAP 0.05 c-o: {Snr}')
im4=Image.fromarray(tmpImg)
im4.show()
im4=im4.convert("L")
im4.save('lena_sap005_closing_opening.bmp',format='BMP')


tmpImg=closing(opening(img4co))
Snr=SNR.snr(img,tmpImg)
print(f'snr SAP 0.05 o-c: {Snr}')
im4=Image.fromarray(tmpImg)
im4.show()
im4=im4.convert("L")
im4.save('lena_sap005_opening_closing.bmp',format='BMP')

