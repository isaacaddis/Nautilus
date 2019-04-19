import cv2
import numpy as np
import time

class ShapeDetect:
	def __init__(self):
		pass
	def detect(self, c):
		peri = cv2.arcLength(c, True)
		approx = cv2.approxPolyDP(c, 0.04*peri, True)
		if len(approx) ==3:
			return 'triangle'
		elif len(approx) ==4:
			(x, y, w, h) = cv2.boundingRect(approx)
			ar = w / float(h)
			if ar >= .85 and ar <= 1.25:
				return 'square'
			else:
				return 'line'
		else:
			return 'circle'
class SmartMax:
	def __init__(self):
		pass
	def getPaper(self, cnts):
		max_n = 0
		max_c = None
		for c in cnts:
			n = cv2.contourArea(c)
			print("Determining paper size: "+str(n))
			if n > max_n and n>10000:
				max_n = n
				max_c = c
		if max_c is not None:
			return max_c
		else:
			return None
	def averageColor(self, img, c):
		x, y, w, h = cv2.boundingRect(c)
		temp = img[y:y+h, x:x+w]
		avg_color_per_row = np.average(temp, axis =0)
		avg_color = np.average(avg_color_per_row, axis = 0)
		cv2.putText(temp,'Color: {}'.format(avg_color),(temp.shape[1]-400,temp.shape[0]-300), cv2.FONT_HERSHEY_SIMPLEX, 1,(255,0,0),1,cv2.LINE_AA)
		cv2.imwrite(str(time.ctime())+'.jpg',temp)
		return avg_color

