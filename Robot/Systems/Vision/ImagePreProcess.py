#!/usr/bin/env python
import cv2
import numpy as np

class ImagePreProcess():
    def __init__(self):
        pass
    def process(self, image):
        '''
            Return canny-edge image.
        '''
        #self.img = cv2.imread(image, cv2.COLOR_RGB2GRAY)
        self.img = cv2.GaussianBlur(image,(5,5), 0)
        self.kernel = np.ones((5,5), np.uint8)
        self.erosion = cv2.erode(self.img, self.kernel, iterations=1)
        self.dilation = cv2.dilate(self.erosion, self.kernel, iterations=1)
        self.canny = cv2.Canny(self.dilation, 100,200)
        return self.dilation
class WhatsCrackin():
    def __init__(self):
        pass
    def findCracks(self, image):
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        ret, image =  cv2.threshold(image,127,255,0)
        __,self.cnt,__ = cv2.findContours(image.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        return self.cnt
    def integrate(self, img, cnt):
        print(cnt)
        #peri = cv2.arcLength(i, True)
        #approx = cv2.approxPolyDP(i, 0.02 * peri, True)
        '''
        if area < 100:
            continue
        '''
        #x, y, w, h = cv2.boundingRect(approx)
        #cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0),1)
        #cropped = img[y-60:y+h+60,x-60:w+x+60] #only the region of img with contour in question
        cv2.drawContours(img,cnt,-1, (0,0,255),1)
        #return img

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





