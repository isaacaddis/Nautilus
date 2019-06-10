import cv2 
import numpy as np
import time


class ShapeDetect:
	def __init__(self):
		self.params = cv2.SimpleBlobDetector_Params()
	def get_blobs(self, img):
		pass
		# self.params.minThreshold = 0
		# self.params.minRepeatability = 2
		# self.params.filterByColor = True
		# self.params.blobColor = 0
		# self.params.filterByArea = True
		# self.params.minArea = 85
		# self.params.maxArea = 20000
		# self.params.filterByCircularity = False
		# self.params.filterByInertia = False
		# self.params.filterByConvexity = True
		# self.params.minConvexity = 0.8

		"""self.detector = cv2.SimpleBlobDetector_create(self.params)
		detected = self.detector.detect(img)
		cleaned = []
		for d in detected:
			cleaned += [{
				'center': (np.int(d.pt[0]), np.int(d.pt[1])),
				'size': np.int(d.size / 1.05),
				'lower': None,
				'upper': None
				}] 
		lower = []
		upper = []
		for c in range(len(cleaned)):
			x, y = cleaned[c]['center']
			size = cleaned[c]['size']
			Y_low = max(y-size, 0)
			Y_high = min(y+size, img.shape[0])
			X_low = max(x - size, 0)
			X_high = min(y + size, img.shape[1])
			lower = (X_low, Y_low)
			upper = (X_high, Y_high)
			cleaned[c]['lower'] = lower
			cleaned[c]['upper'] = upper
		return (detected, cleaned)
		# for i in cleaned:
		# 	(lowerX, lowerY) = cleaned['lower']
		# 	(upperX, upperY) = cleaned['upper']
		# 	roi = img[lowerY:upperY, lowerX:upperX]"""

	def detect(self, c,img):
		peri = cv2.arcLength(c, True)
		approx = cv2.approxPolyDP(c, 0.04*peri, True)
		(x, y, w, h) = cv2.boundingRect(approx)
		# circles = cv2.HoughCircles(img, cv2.cv.CV_HOUGH_GRADIENT, 1.2, 100)
		# if circles is not None:
			
		if len(approx) ==3:
			#cv2.imwrite('triangle.jpg',img[y:y+h, x:x+w])
			return 'triangle'
		elif len(approx) == 4:
			#rect = cv2.minAreaRect(c)
			#w, h = rect[1]
			ar = w / h

			if ar <0.8:
				cv2.imwrite('Images/'+str(ar)+'-line.jpg',img[y:y+h, x:x+w])
				return 'line'
			elif ar > 2.5:
				return ''
			else:
				cv2.imwrite('Images/'+str(ar)+'-square.jpg',img[y:y+h, x:x+w])
				return 'square'
		else:
			#cv2.imwrite(str(time.time())+'-circle.jpg',img[y:y+h, x:x+w])
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
		avg_color = np.average(temp, axis = (0,1))
		#cv2.putText(temp,'Color: {}'.format(avg_color),(temp.shape[1]-400,temp.shape[0]-300), cv2.FONT_HERSHEY_SIMPLEX, 1,(255,0,0),1,cv2.LINE_AA)
		#cv2.imwrite(str(avg_color)+'.jpg',temp)
		return avg_color

