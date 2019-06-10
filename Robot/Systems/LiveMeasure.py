import cv2 as cv
import numpy as np
import imutils
from ImagePreProcess import *
from Undistort import *
class LiveMeasure():
	def __init__(self):
		print("Optimization is enabled [T/F]: {}".format(cv2.useOptimized()))
	def get(self):
		DIM=(640, 480)
		K=np.array([[553.350692313905, 0.0, 342.9451779392026], [0.0, 545.573637355145, 211.4054580385251], [0.0, 0.0, 1.0]])
		D=np.array([[-0.2807810032443438], [2.1812482493268424], [-8.101784482269283], [10.048341560961232]])

		font = cv.FONT_HERSHEY_SIMPLEX
		cap = cv.VideoCapture("1")
		image = ImagePreProcess()
		length = " "
		setting = 1
		und = Undistort()
		ret, frame = cap.read()
		h,w = frame.shape[:2]
		#map1, map2 = cv.fisheye.initUndistortRectifyMap(K, D, np.eye(3), K, DIM, cv.CV_16SC2)
		undistorted_img = und.rectify(frame)

		#img = cv.GaussianBlur(undistorted_img,(5,5), 0)
		#median = cv.medianBlur(img,5)
		#blur = cv.bilateralFilter(median, 9, 75, 75)
		#img = image.process(frame)
		#thresh = cv2.threshold(undistorted_img,127,255,cv2.THRESH_BINARY)
		#cnts = cv.findContours(thresh, cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
		#cnts = imutils.grab_contours(cnts)
		hsv = cv.cvtColor(undistorted_img, cv.COLOR_BGR2HSV)
		#lower_red = np.array([110,65,65])
		#upper_red = np.array([130,255,255])
		map1, map2 = cv.fisheye.initUndistortRectifyMap(K, D, np.eye(3), K, DIM, cv.CV_16SC2)
		undistorted_img = cv.remap(frame, map1, map2, interpolation=cv.INTER_LINEAR, borderMode=cv.BORDER_CONSTANT)
		#img = cv.GaussianBlur(undistorted_img,(5,5), 0)
		#median = cv.medianBlur(img,5)
		#blur = cv.bilateralFilter(median, 9, 75, 75)
		hsv = cv.cvtColor(undistorted_img, cv.COLOR_BGR2HSV)
	 
		if cv.waitKey(1) & 0xFF == ord('a'):
			setting +=1
		if setting%2 == 1:
			lower_red = np.array([110,55,55])
			upper_red = np.array([140,255,255])
		if setting%2 == 0:
			lower_red = np.array([110,45,45])
			upper_red = np.array([140,255,255])
		mask = cv.inRange(hsv, lower_red, upper_red)
		res = cv.bitwise_and(undistorted_img,undistorted_img, mask= mask)
		mask = cv.inRange(hsv, lower_red, upper_red)
		res = cv.bitwise_and(undistorted_img,undistorted_img, mask= mask)
	 
		img = image.process(res)
		cnts = cv.findContours(img, cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
		cnts = imutils.grab_contours(cnts)


		for c in cnts :
	 
			if cv.contourArea(c) >= 500:
			if cv.contourArea(c) >= 500  :
	 
				rect = cv.minAreaRect(c)
				box = cv.boxPoints(rect)
				box = np.int0(box)
				cv.drawContours(undistorted_img,[box],0,(0,0,255),2)

				if cv.waitKey(1) & 0xFF == ord('s'):
					(x, y), (width, height), rect_angle = rect

					if height < width :
						convert = 1.905/height
						length =  (6.5/5.9)*convert * width

					if height>width:
						convert = 1.905/width
						length =  (6.5/5.9)*convert * height

					print(length)

		#cv.putText(undistorted_img,str(length),(100,100), font, 1,(50,50,255),1,cv.LINE_AA)


			#cv.drawContours(frame, [c], -1, (0, 255, 0), 2)

		#cv.imshow('frame',frame)
		#cv.imshow("undistorted", undistorted_img)
		#cv.imshow("Canny Edge", img)
		#cv.imshow('mask',mask)
		#cv.imshow('res',res)
		#print(lower_red)
		return (length, frame)


				#cv.imwrite("image.jpg",frame)

		# if cv.waitKey(1) & 0xFF == ord('q'):
		# 		break