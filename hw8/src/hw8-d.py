from PIL import Image
import numpy as np
import SNR



def med33(img):
    r, c = img.shape
    img=np.pad(img,(1,1),'edge')
    result = np.zeros((r,c),dtype=np.int32)
    for i in range(1,r+1):
        for j in range(1,c+1):
            tmp=img[i-1:i+2,j-1:j+2]
            result[i-1][j-1] = np.median(tmp)            
    return result


def med55(img):
    r, c=img.shape
    img = np.pad(img,(2,2),'edge')
    result = np.zeros((r,c),dtype=np.int32)
    for i in range(2,r+2):
        for j in range(2,c+2):
            tmp = img[i-2:i+3,j-2:j+3]
            result[i-2][j-2] = np.median(tmp)
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

tmpImg=med33(img133)
Snr=SNR.snr(img,tmpImg)
print(f'snr Gaussian10 med33: {Snr}')
im1=Image.fromarray(tmpImg)
im1.show()
im1=im1.convert("L")
im1.save('lena_gauss10_med33.bmp',format='BMP')

tmpImg=med55(img155)
Snr=SNR.snr(img,tmpImg)
print(f'snr Gaussian10 med55: {Snr}')
im1=Image.fromarray(tmpImg)
im1.show()
im1=im1.convert("L")
im1.save('lena_gauss10_med55.bmp',format='BMP')

tmpImg=med33(img233)
Snr=SNR.snr(img,tmpImg)
print(f'snr Gaussian30 med33: {Snr}')
im2=Image.fromarray(tmpImg)
im2.show()
im2=im2.convert("L")
im2.save('lena_gauss30_med33.bmp',format='BMP')

tmpImg=med55(img255)
Snr=SNR.snr(img,tmpImg)
print(f'snr Gaussian30 med55: {Snr}')
im2=Image.fromarray(tmpImg)
im2.show()
im2=im2.convert("L")
im2.save('lena_gauss30_med55.bmp',format='BMP')

tmpImg=med33(img333)
Snr=SNR.snr(img,tmpImg)
print(f'snr SAP 0.1 med33: {Snr}')
im3=Image.fromarray(tmpImg)
im3.show()
im3=im3.convert("L")
im3.save('lena_sap01_med33.bmp',format='BMP')


tmpImg=med55(img355)
Snr=SNR.snr(img,tmpImg)
print(f'snr SAP 0.1 med55: {Snr}')
im3=Image.fromarray(tmpImg)
im3.show()
im3=im3.convert("L")
im3.save('lena_sap01_med55.bmp',format='BMP')


tmpImg=med33(img433)
Snr=SNR.snr(img,tmpImg)
print(f'snr SAP 0.05 med33: {Snr}')
im4=Image.fromarray(tmpImg)
im4.show()
im4=im4.convert("L")
im4.save('lena_sap005_med33.bmp',format='BMP')


tmpImg=med55(img455)
Snr=SNR.snr(img,tmpImg)
print(f'snr SAP 0.05 med55: {Snr}')
im4=Image.fromarray(tmpImg)
im4.show()
im4=im4.convert("L")
im4.save('lena_sap005_med55.bmp',format='BMP')