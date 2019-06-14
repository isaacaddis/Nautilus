import cv2 
import numpy as np
import time


class ShapeDetect:
	def __init__(self):
		self.params = cv2.SimpleBlobDetector_Params()
	def clean_contours(self, cnts):
		return [i[0] for i in cnts]
	def calc_vector_difference(self,v1,v2):
		return np.linalg.norm(v1-v2)
	def calc_angle_dist_from_vectors(self,v1, v2):
		return np.degrees(np.arccos(np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))))
	def calc_edges(self,vertices):
	    lengths = []
	    for offset in range(len(vertices)):
	        p1, p2 = np.roll(vertices, offset, axis=0)[:2]
	        lengths += [np.linalg.norm(p1 - p2)]
	    return np.array(lengths)
	def calc_angles(self,vertices):
		angles = []
		for offset in range(len(vertices)):
			p1,p2 = np.roll(vertices, offset, axis = 0)[:3]
			angles += [np.linalg.norm(p1-p2)]
		return np.array(angles)
	def draft_circle(self,x,y,r,n_points):
		circle = []
		for i in range(0, n_points):
			circle += [[[r * np.sin(i) + y, r * np.cos(i) +x]]]
		return np.array(circle, np.int32)
	def check(self, box, firstX, secondX, lower_bound):
		self.x1 , self.y1 = box[0]
		self.x2 , self.y2 = box[1]
		self.x3 , self.y3 = box[2]
		self.x4,  self.y4 = box[3]
		self.boolean1  = False
		self.boolean2  = False
		self.boolean3  = False
		self.boolean4  = False
		self.Finalboolean  = False
		self.b = 0
		if((self.x1 > firstX or self.y1 < lower_bound) and (self.x1 < secondX or self.y1> lower_bound ) ):
			self.boolean1  = True
	def check(self, box, firstX, secondX, lower_bound):
		self.x1 , self.y1 = box[0]
		self.x2 , self.y2 = box[1]
		self.x3 , self.y3 = box[2]
		self.x4,  self.y4 = box[3]
		self.boolean1  = False
		self.boolean2  = False
		self.boolean3  = False
		self.boolean4  = False
		self.Finalboolean  = False
		self.b = 0
		if((self.x1 > firstX or self.y1 < lower_bound) and (self.x1 < secondX or self.y1> lower_bound ) ):
			self.boolean1  = True

		if((self.x2 >firstX or self.y2 < lower_bound) and (self.x2 < secondX or self.y2> lower_bound) ):
			self.boolean2  = True

		if((self.x3 >firstX or self.y3 < lower_bound) and (self.x3 < secondX or self.y3> lower_bound) ):
			self.boolean3  = True

		if((self.x4 >firstX  or self.y4 < lower_bound) and (self.x4 < secondX or self.y4> lower_bound) ):
			self.boolean4  = True

		self.array = [self.boolean1, self.boolean2, self.boolean3, self.boolean4]
		for i in self.array:
			if i == True:
				self.b += 1

		if(self.b >= 3):
			self.Finalboolean = True
										
		return self.Finalboolean
		
		
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
			rect = cv2.minAreaRect(c)
			w, h = rect[1]
			ar = w / h

			if ar <0.75 or ar >2.205:
				#cv2.imwrite('Images/'+str(ar)+'-line.jpg',img[y:y+h, x:x+w])
				return 'line'
			#elif ar > 2.5:
				#return ''
			#else:
			#cv2.imwrite('Images/'+str(ar)+'-square.jpg',img[y:y+h, x:x+w])
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
