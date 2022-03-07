from PIL import Image
import numpy as np 
import SNR


im = Image.open('./lena.bmp')
img = np.asarray(im)
r, c = img.shape


img_10 = np.zeros((r,c),dtype=np.int32)
img_10[0:r,0:c] = img[0:r,0:c]

img_10 = img_10+10*np.random.normal(0,1,(r,c))
im = Image.fromarray(img_10)
im.show()
im = im.convert("L")
im.save('lena_Gaussian10.bmp',format='BMP')
Snr = SNR.snr(img,img_10)
print(f'snr10: {Snr}')



img_30 = np.zeros((r,c),dtype=np.int32)
img_30[0:r,0:c] = img[0:r,0:c]

img_30 = img_30+30*np.random.normal(0,1,(r,c))
im = Image.fromarray(img_30)
im.show()
im = im.convert("L")
im.save('lena_Gaussian30.bmp',format='BMP')
Snr = SNR.snr(img,img_30)
print(f'snr30: {Snr}')








