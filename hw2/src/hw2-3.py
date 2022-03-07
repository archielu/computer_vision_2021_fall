from PIL import Image,ImageDraw
import numpy as np  

source_image = Image.open('./lena.bmp')
row, col = source_image.size

img_table = np.zeros((row + 2, col + 2), dtype = np.int32)
img_binary = np.zeros((row,col), dtype = np.int32)

# convert image to binary -0/1 image
for i in range(row):
	for j in range(col):
		pixel_value = source_image.getpixel((i,j))
		# threshold = 128
		if pixel_value >= 128:
			img_table[i+1][j+1] = 1
			img_binary[i][j] =  255

img_binary = img_binary.transpose()
img2 = Image.fromarray(img_binary)


# Initialize each 1-pixel to unique label
unique_label = 1
for i in range(1,row+1):
	for j in range(1,col+1):
		if img_table[i][j] == 1:
			img_table[i][j] = unique_label
			unique_label += 1

#np.savetxt("initlabel.csv",img_table)

# iterative algorithm 4-connected
change =  True
while change == True:
	change = False
	""" First Top Down """
	for i in range(1,row+1,1):
		for j in range(1,col+1,1):
			if img_table[i][j] != 0:
				obj_list = [img_table[i][j]]
				if img_table[i-1][j] != 0:
					obj_list.append(img_table[i-1][j])
				if img_table[i][j-1] != 0:
					obj_list.append(img_table[i][j-1])
				if img_table[i+1][j] != 0:
					obj_list.append(img_table[i+1][j])
				if img_table[i][j+1] != 0:
					obj_list.append(img_table[i][j+1])

				new_label  = min(obj_list)
				if img_table[i][j] != new_label:
					img_table[i][j] = new_label
					change = True


	""" Bottom Up"""
	for i in range(row+1,1,-1):
		for j in range(col+1,1,-1):
			if img_table[i][j] != 0:
				obj_list = [img_table[i][j]]
				if img_table[i-1][j] != 0:
					obj_list.append(img_table[i-1][j])
				if img_table[i][j-1] != 0:
					obj_list.append(img_table[i][j-1])
				if img_table[i+1][j] != 0:
					obj_list.append(img_table[i+1][j])
				if img_table[i][j+1] != 0:
					obj_list.append(img_table[i][j+1])

				new_label  = min(obj_list)
				if img_table[i][j] != new_label:
					img_table[i][j] = new_label
					change = True

"""
for i in range(1,row+1,1):
	for j in range(1,col+1,1):
		if img_table[i][j] != 0:
			if img_table[i-1][j] != 0 and img_table[i-1][j] != img_table[i][j]:
				print("Error")
			if img_table[i+1][j] != 0 and img_table[i+1][j] != img_table[i][j]:
				print("Error")
			if img_table[i][j-1] != 0 and img_table[i][j-1] != img_table[i][j]:
				print("Error")
			if img_table[i][j+1] != 0 and img_table[i][j+1] != img_table[i][j]:
				print("Error")

"""
#np.savetxt("label.csv",img_table, fmt="%d", delimiter=",")


"""Find out legal region ( Count  >= 500) """
"""labelList: [ label_number, top, left, down, right, count ] """
labelList = []

for i in range(1,row+1,1):
	for j in range(1,col+1,1):
		if img_table[i][j] != 0:
			if len(labelList) == 0:
				labelList.append([img_table[i][j],i-1,j-1,i-1,j-1,1])
			else:
				isExist  = False
				for k in range(len(labelList)):
					if img_table[i][j] == labelList[k][0]:
						isExist = True
						if labelList[k][1] > i-1:
							labelList[k][1] = i-1
						if labelList[k][2] > j-1:
							labelList[k][2] = j-1
						if labelList[k][3] < i-1:
							labelList[k][3] = i-1
						if labelList[k][4] < j-1:
							labelList[k][4] = j-1
						labelList[k][5] += 1

						break
				if isExist == False:
					labelList.append([img_table[i][j],i-1,j-1,i-1,j-1,1])


valid_label = []
for i in range(len(labelList)):
	if labelList[i][5] >= 500:
		valid_label.append([labelList[i][0],labelList[i][1],labelList[i][2],labelList[i][3],labelList[i][4],labelList[i][5]])

#print(len(valid_label))


"""position_sum: [label_id, row_sum, col_sum]"""
position_sum =  []
for k in range(len(valid_label)):
	target_label = valid_label[k][0]
	tmp = [target_label,0,0]
	for i in range(1,row+1):
		for j in range(1,col+1):
			if img_table[i][j] == target_label:
				tmp[1] += i-1
				tmp[2] += j-1
	position_sum.append(tmp)

#print(position_sum)


img2 = img2.convert("RGBA")

draw = ImageDraw.Draw(img2)

for i in range(len(valid_label)):
	top = valid_label[i][1]
	left = valid_label[i][2]
	down = valid_label[i][3]
	right = valid_label[i][4]

	centroid_row = int(position_sum[i][1] // valid_label[i][5])
	centroid_col = int(position_sum[i][2] // valid_label[i][5])


	draw.rectangle(((top,left),(down,right)),outline="blue")
	draw.line(((centroid_row-5,centroid_col), (centroid_row+5,centroid_col)), fill = "red", width = 1)
	draw.line(((centroid_row,centroid_col-5), (centroid_row,centroid_col+5)), fill = "red", width = 1)


img2.save('lena_binary_detect.bmp',format='BMP')






















