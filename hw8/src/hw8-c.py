from PIL import Image
import numpy as np
import SNR


def box33(img):
	r, c = img.shape
	img = np.pad(img,(1,1),'edge')
	box=np.array([[1,1,1],
                  [1,1,1],
                  [1,1,1]])
	coef = 1.0 / box.sum()
	result = np.zeros((r,c), dtype = np.int32)
	for i in range(1,r+1):
		for j in range(1,c+1):
			s = 0.0
			for a in range(3):
				for b in range(3):
					s += img[i-1+a][j-1+b] * box[a][b]

			result[i-1][j-1] = s * coef

	return result



def box55(img):
    r, c=img.shape
    img = np.pad(img,(2,2),'edge')
    box = np.array([[1,1,1,1,1],
                  [1,1,1,1,1],
                  [1,1,1,1,1],
                  [1,1,1,1,1],
                  [1,1,1,1,1]])
    coef = 1.0 / box.sum()
    result = np.zeros((r,c), dtype = np.int32)
    for i in range(2,r+2):
        for j in range(2,c+2):
            s=0.0
            for a in range(5):
                for b in range(5):
                    s += img[i-2+a][j-2+b] * box[a][b]
            result[i-2][j-2] = s*coef

    return result


im=Image.open('./lena.bmp')
img = np.asarray(im)

im1=Image.open('lena_Gaussian10.bmp')
im2=Image.open('lena_Gaussian30.bmp')
im3=Image.open('lena_salt_and_pepper010.bmp')
im4=Image.open('lena_salt_and_pepper005.bmp')

img133=np.asarray(im1)
img155=np.asarray(im1)

img233=np.asarray(im2)
img255=np.asarray(im2)

img333=np.asarray(im3)
img355=np.asarray(im3)

img433=np.asarray(im4)
img455=np.asarray(im4)

tmpImg=box33(img133)
Snr=SNR.snr(img,tmpImg)
print(f'snr Gaussian10 box33: {Snr}')
im1=Image.fromarray(tmpImg)
im1.show()
im1=im1.convert("L")
im1.save('lena_gauss10_box33.bmp',format='BMP')

tmpImg=box55(img155)
Snr=SNR.snr(img,tmpImg)
print(f'snr Gaussian10 box55: {Snr}')
im1=Image.fromarray(tmpImg)
im1.show()
im1=im1.convert("L")
im1.save('lena_gauss10_box55.bmp',format='BMP')

tmpImg=box33(img233)
Snr=SNR.snr(img,tmpImg)
print(f'snr Gaussian30 box33: {Snr}')
im2.show()
im2=im2.convert("L")
im2.save('lena_gauss30_box33.bmp',format='BMP')

tmpImg=box55(img255)
Snr=SNR.snr(img,tmpImg)
print(f'snr Gaussian30 box55: {Snr}')
im2=Image.fromarray(tmpImg)
im2.show()
im2=im2.convert("L")
im2.save('lena_gauss30_box55.bmp',format='BMP')

tmpImg=box33(img333)
Snr=SNR.snr(img,tmpImg)
print(f'snr salt and pepper 0.1 box33: {Snr}')
im3=Image.fromarray(tmpImg)
im3.show()
im3=im3.convert("L")
im3.save('lena_sap01_box33.bmp',format='BMP')


tmpImg=box55(img355)
Snr=SNR.snr(img,tmpImg)
print(f'snr salt and pepper 0.1 box55: {Snr}')
im3=Image.fromarray(tmpImg)
im3.show()
im3=im3.convert("L")
im3.save('lena_sap01_box55.bmp',format='BMP')


tmpImg=box33(img433)
Snr=SNR.snr(img,tmpImg)
print(f'snr salt and pepper 0.05 box33: {Snr}')
im4=Image.fromarray(tmpImg)
im4.show()
im4=im4.convert("L")
im4.save('lena_sap005_box33.bmp',format='BMP')


tmpImg=box55(img455)
Snr=SNR.snr(img,tmpImg)
print(f'snr salt and pepper 0.05 box55: {Snr}')
im4=Image.fromarray(tmpImg)
im4.show()
im4=im4.convert("L")
im4.save('lena_sap005_box55.bmp',format='BMP')