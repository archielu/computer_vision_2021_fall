import os

import cv2
import numpy as np 


def upside_down(img):
	""" Vertically mirror the image."""
	img_size = img.shape
	img_H = img_size[0]

	result = np.zeros(img_size, np.int)
	for i in range(img_H):
		result[i, :, : ] =  img[img_H - 1- i, :, : ]

	return result


def right_side_left(img):
	""" Horizontally mirror the image."""
	img_size = img.shape
	img_W = img_size[1]

	result = np.zeros(img_size, np.int)
	for i in range(img_W):
		result[:, i, : ] =  img[:, img_W- 1- i, : ]

	return result

def  diagonal_mirror(img):
	"""Diagonal mirror the image."""
	img_size = img.shape
	img_H = img_size[0]

	result = np.zeros(img_size, np.int)
	for row in range(img_H):
		result[:, row, : ] = img[row, :, : ]

	return result


def diagonal_flip(img):
	"""Diagonal flip the image"""
	ud_img = upside_down(img)
	result = right_side_left(ud_img)

	return result





def main():
	"""Load image"""
	img_path = "./lena.bmp"

	img_origin = cv2.imread(img_path)

	img_upside_down = upside_down(img_origin)
	cv2.imwrite('./lena_upside_down.bmp', img_upside_down)

	img_right_side_left = right_side_left(img_origin)
	cv2.imwrite('./lena_right_side_left.bmp', img_right_side_left)

	img_diagonal_flip = diagonal_flip(img_origin)
	cv2.imwrite('./lena_diagonal_flip.bmp', img_diagonal_flip)





if __name__ == "__main__":
	main()








