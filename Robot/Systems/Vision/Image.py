import cv2
import time
import numpy as np
size = 60
'''
    Image retrieval tools
'''
class Operation():
    def __init__(self,cap):
        self.ret = False
        self.cap = cv2.VideoCapture(cap)
    def get(self):
        self.ret, self.frame = self.cap.read()
        #assert self.ret is not None
        return self.ret, self.frame
    def close(self):
        self.cap.release()
class VisionIntegrate():
    def __init__(self):
        self.proc = ImagePreProcess()
        self.wc = WhatsCrackin()
        self.magic = Magic()
        #Init counters
        self.n_triangle = 0
        self.n_circle = 0
        self.n_star = 0
        self.n_square = 0
        self.n_line = 0
    def getPredictions(self, img, img_copy, cnt, approx):
        x, y, w, h = cv2.boundingRect(approx)
        cv2.rectangle(img_copy, (x, y), (x+w, y+h), (0, 255, 0), 1)
        cropped = img_copy[y-60:y+h+60, x-60:w+x+60]
        coords = (x,y)
        cv2.drawContours(img_copy, cnt, -1, (0,0,255),1)
        org = (coords[0], coords[1]+int(area/400))
        if np.prod(cropped.shape[:2])>10:
            #cv2.rectangle(img_copy,(x,y),(x+w,y+h),(0,255,0),3)
            cropped = cv2.resize(img, (60,60))
            mask = self.magic.abra(cropped)
            prediction = self.magic.alakazam(mask)
            print("Prediction {}".format(prediction))
            name = ''
            max_p = max(prediction)
            confidence = .5
    def integrate(self,img):
        img = self.proc.process(img)
        img_copy = img.copy()
        cnt = self.wc.findCracks(img)
        for i in cnt:
            peri = cv2.arcLength(i, True)
            approx = cv2.approxPolyDP(i, 0.02 * peri, True)
            area = cv2.contourArea(i)
            if area < 100:
                continue
        return img_copy