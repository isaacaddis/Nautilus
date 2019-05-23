import cv2 as cv
import numpy as np
import imutils
from methods import *

font = cv.FONT_HERSHEY_SIMPLEX
cap = cv.VideoCapture(0)
image = ImagePreProcess()
length = " "
while(cap.isOpened()):
	ret, frame = cap.read()
	#img = image.process(frame)
	#cnts = cv.findContours(img, cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
	#cnts = imutils.grab_contours(cnts)
	hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV) 
	lower_red = np.array([107,47,47]) 
	upper_red = np.array([130,255,255]) 
	mask = cv.inRange(hsv, lower_red, upper_red) 
	res = cv.bitwise_and(frame,frame, mask= mask) 
	img = image.process(res)
	cnts = cv.findContours(img, cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
	cnts = imutils.grab_contours(cnts)
    
  
	for c in cnts :

		if cv.contourArea(c) >160:
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