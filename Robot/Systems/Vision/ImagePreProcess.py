import cv2
import numpy as np

class ImagePreProcess():
    def __init__(self):
        pass
    def process(self, image):
        self.img = image
        kernel = np.ones((5,5), np.uint8)
        self.erosion = cv2.erode(self.img, kernel, iterations=1)
        self.dilation = cv2.dilate(self.erosion, kernel, iterations=1)
        self.blurred = cv2.GaussianBlur(self.dilation,(5,5), 0)
        #self.canny = cv2.Canny(self.blurred, 100,200)
        return self.blurred
class WhatsCrackin():
    def __init__(self):
        pass
    def findCracks(self, image):
        __, self.cnt, __ = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        return self.cnt
    '''
        if len(self.cnt) > 0:
            self.c = max(self.cnt, key = cv2.contourArea)
            #x,y,w,h = cv2.boundingRect(self.c)
            cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),3)
            return self.c
    '''
    def findLength(self, c):
        self.perimeter = cv2.arcLength(c, True)
        self.side_length = self.perimeter/4
        return (self.perimeter, self.side_length)
    '''
        Params:

        c - Contour
        p - Perimeter
    '''
    def approxCnt(self, c, p):
        cv2.approxPolyDP(cnt,p, True)





