import cv2
import numpy as np
import threading
import imutils


class Contours():
    def __init__(self):
        #self.lower = np.array([107,55,55]) # blue
        #self.upper = np.array([140,255,255])
        self.lower = np.array([0,0,0]) #white
        self.upper = np.array([0,0,255])
        self.length = " "

    def applyMask(self,image):
        self.hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        self.mask = cv2.inRange(self.hsv, self.lower, self.upper)
        self.res = cv2.bitwise_and(image, image, mask = self.mask)
        self.mask = cv2.inRange(self.res, self.lower, self.upper)
        return self.mask

    def find(self,image):
        self.cnts = cv2.findContours(image, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE) #canny_edge
        #self.cnts = cv2.findContours(image, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) #mask image
        self.cnts = imutils.grab_contours(self.cnts)
        return self.cnts

    def measure(self, contour, image):
        if cv2.contourArea(contour) >= 500  :
            self.rect = cv2.minAreaRect(contour)
            self.box = cv2.boxPoints(self.rect)
            self.box = np.int0(self.box)
            cv2.drawContours(image,[self.box],0,(0,0,255),2)

            if cv2.waitKey(1) & 0xFF == ord('s'):
                (self.x,self. y), (self.width, self.height), self.rect_angle = self.rect

                if self.height < self.width :
                    self.convert = 1.905/self.height
                    self.length =  (6.5/5.9)*self.convert * self.width

                if self.height > self.width:
                    self.convert = 1.905/self.width
                    self.length =  (6.5/5.9)*self.convert * self.height

                return(str(self.length))
        return "" #empty string