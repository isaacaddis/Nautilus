import cv2
import numpy as np
from matplotlib import pyplot as plt

class ImagePreProcess():
    def __init__(self):
        pass
    def process(self, image):
        self.img = image
        kernel = np.ones((5,5), np.uint8)
        self.erosion = cv2.erode(self.img, kernel, iterations=1)
        self.dilation = cv2.dilate(self.erosion, kernel, iterations=1)
        #self.gray = cv2.cvtColor(self.dilation, cv2.COLOR_BGR2GRAY)
        self.blurred = cv2.GaussianBlur(self.dilation,(5,5), 0)
        #self.blurred = cv2.bilateralFilter(self.blurred, 11, 17)
        self.canny = cv2.Canny(self.blurred, 100,200)
        return self.canny
    def analysis(self):
        plt.subplot(121),plt.imshow(self.canny,cmap = 'gray')
        plt.title('Image'), plt.xticks([]), plt.yticks([])
class WhatsCrackin():
    def __init__(self):
        pass
    def findCracks(self, image):
        self.___, self.cnt, self.hierachy = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        self.c = max(cnt, key = cv2.contourArea)
        x,y,w,h = cv2.boundingRect(c)
        cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),3)
    def findLength(self, c):
        self.perimeter = cv2.arcLength(c, True)
        self.side_length = self.perimeter/4
    def approxCnt(self, c):
        cv2.approxPolyDP(cnt,getPerimeter(), True)
    def getPerimeter(self):
        return self.perimeter
    def getSideLength(self):
        return self.side_length





