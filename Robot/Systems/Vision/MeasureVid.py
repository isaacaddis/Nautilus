import cv2 as cv
import numpy as np
import imutils
from methods import *

font = cv.FONT_HERSHEY_SIMPLEX
cap = cv.VideoCapture("VID.mp4")
image = ImagePreProcess()
length = " "
while(cap.isOpened()):
	ret, frame = cap.read()
	img = cv.GaussianBlur(frame,(5,5), 0)
	median = cv.medianBlur(img,5)
	blur = cv.bilateralFilter(median, 9, 75, 75)
	#img = image.process(frame)
	#cnts = cv.findContours(img, cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
	#cnts = imutils.grab_contours(cnts)
	hsv = cv.cvtColor(blur, cv.COLOR_BGR2HSV) 
	lower_red = np.array([110,102,102]) 
	upper_red = np.array([130,255,255]) 
	mask = cv.inRange(hsv, lower_red, upper_red) 
	res = cv.bitwise_and(blur,blur, mask= mask) 
	img = image.process(res)
	cnts = cv.findContours(img, cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
	cnts = imutils.grab_contours(cnts)
    
  
	for c in cnts :
		#perimeter = cv.arcLength(c,True)
		#approx = cv.approxPolyDP(c, 0.05*perimeter, True)
		#if len(approx) == 4 :
		if cv.contourArea(c) >= 500  :
			rect = cv.minAreaRect(c)
			box = cv.boxPoints(rect)
			box = np.int0(box)
			cv.drawContours(frame,[box],0,(0,0,255),2)
			if cv.waitKey(1) & 0xFF == ord('s'):
				(x, y), (width, height), rect_angle = rect
				if height < width :
					convert = 1.905/height
					length =  convert * width

				if height>width:
					convert = 1.905/width
					length =  convert * height
					
				print(length)
					
	cv.putText(frame,str(length),(100,100), font, 1,(50,50,255),1,cv.LINE_AA)


		#cv.drawContours(frame, [c], -1, (0, 255, 0), 2)
	cv.imshow('frame',frame)
	cv.imshow("Canny Edge", img)
	cv.imshow('mask',mask) 
	cv.imshow('res',res) 



			#cv.imwrite("image.jpg",frame)

	if cv.waitKey(1) & 0xFF == ord('q'):
			break


cap.release()
cv.destroyAllWindows()