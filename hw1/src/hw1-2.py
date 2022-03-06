import os

import cv2
import numpy as np 
import imutils


def rotate(img, angle):
	"""Rotate image with angle counterclockwise"""
	result = imutils.rotate(img, angle = angle)

	return result



def shrink_half(img):
	img_size = img.shape
	new_size = int(img_size[0] / 2)
	result = cv2.resize(img, (new_size, new_size), interpolation=cv2.INTER_AREA)

	return result



def binarize(img, threshold):
	val, result = cv2.threshold(img, threshold, 255, 0)

	return  result



def main():
	"""Load image"""
	img_path = "./lena.bmp"

	img_origin = cv2.imread(img_path)

	img_rotate = rotate(img_origin, -45)
	cv2.imwrite('./lena_rotate.bmp', img_rotate)

	img_shrink_half = shrink_half(img_origin)
	cv2.imwrite('./lena_shrink_half.bmp', img_shrink_half)

	img_binarize = binarize(img_origin, 128)
	cv2.imwrite('./lena_binarize.bmp', img_binarize)






if __name__ == "__main__":
	main()
