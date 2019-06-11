#!/usr/bin/python
# -*- coding: utf-8 -*-

import cv2
import os
from . import ImagePreProcess
from . import geo
import time
from . import Async
from . import Undistort
from . import methods
import time
import numpy as np
import time
import imutils

class Display():
    def __init__(self, num=1):
        print(" Initializing Benthic Species ")
        self.num = num
        self.cap = cv2.VideoCapture(num)
        self.und = Undistort.Undistort()
        self.proc = ImagePreProcess.ImagePreProcess()
        self.sd = geo.ShapeDetect()
        self.past_text, self.n_text = [0, 0, 0, 0, 0],[0, 0, 0, 0, 0] # follows the general data schema for shapes
        self.Contours = methods.Contours()
        self.lower_black = np.array([0,0,0])
        self.upper_black = np.array([0,0,255])
        self.fgbg = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=50, detectShadows=True)

        print("Finished Benthic Species Initalization")
    def get(self):
        a = ""
        b = ""
        c = ""
        d = ""
        e = ""
        ret, val = self.cap.read()
        if val is not None:
            img_c  = val.copy()
            #crop_frame = val[0:int(val.shape[0]/1.52)]
            crop_frame = img_c
            #crop_frame = cv2.cvtColor(val, cv2.COLOR_BGR2GRAY)
            #crop_frame = self.proc.process(crop_frame)
            #cv2.imwrite('cropped.jpg',crop_frame)
           #detected, keypoints = self.sd.get_blobs(crop_frame) 
            #wk = cv2.drawKeypoints(img_c, detected, np.array([]), (0,255,0), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
            #print(keypoints)
            """current_len = 0
            print(len(keypoints))
            for k in keypoints:
                #print(k)
                (lowerX, lowerY) = k['lower']
                (upperX, upperY) = k['upper']
                #print(lowerX)
                roi = crop_frame[lowerY:upperY, lowerX:upperX]
                #cv2.imwrite(str(time.time())+'.jpg',roi)
                #cv2.imwrite('roi.jpg',roi)
                #print(roi)
                threshed_img = cv2.threshold(roi, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
                #threshed_img = self.proc.process(threshed_img)
                #print(threshed_img)
                ___,cnts,___ = cv2.findContours(threshed_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
                cnts = sorted(cnts, key=cv2.contourArea, reverse=True)
                if len(cnts) > 0:
                    shape = cnts[0]
                    convex_hull = cv2.convexHull(shape)
                    current_len += 1
                    s = self.sd.detect(convex_hull,img_c)
                    if s == "triangle":
                        self.n_text[0] += 1
                    elif s == "square":
                        self.n_text[1] += 1
                    elif s == "line":
                        self.n_text[2] += 1
                    elif s == "circle":
                        self.n_text[3] += 1 
                    a = "Shapes: {}".format(current_len)
                    b = "▲: {}".format(self.n_text[0])
                    c = "■: {}".format(self.n_text[1])
                    d = "▬ {}".format(self.n_text[2])
                    e = "●: {}".format(self.n_text[3])
                    cv2.drawContours(img_c, [shape + k['center']-k['size']], -1, (0,255,0),2)
            self.n_text = [0, 0, 0, 0, 0]
            return (a,b,c,d,e, img_c)"""
            ret,thres = cv2.threshold(crop_frame,127,255,cv2.THRESH_BINARY_INV)
            mask_img = self.Contours.applyMask(thres)
            fgmask = self.fgbg.apply(mask_img)
            __,cnts,_ = cv2.findContours(fgmask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            current_len = 0
            max_n = 0
            for i in cnts:
                area = cv2.contourArea(i)
                if area > 125 and area < 3000:
                    if area > max_n:
                        max_n = area
                    #print("Max area: {}".format(max_n))
                    rect = cv2.minAreaRect(c)
                    box = cv2.boxPoints(rect)
                    box = np.int0(box)
                    current_len += 1
                    cv2.drawContours(img_c, [i], 0, (0,0,255))
                    s = self.sd.detect(i,img_c)
                    if s == "triangle":
                        self.n_text[0] += 1
                    elif s == "square":
                        self.n_text[1] += 1
                    elif s == "line":
                        self.n_text[2] += 1
                    elif s == "circle":
                        self.n_text[3] += 1 
                    a = "Shapes: {}".format(current_len)
                    b = "▲: {}".format(self.n_text[0])
                    c = "■: {}".format(self.n_text[1])
                    d = "▬ {}".format(self.n_text[2])
                    e = "●: {}".format(self.n_text[3])
            self.past_text = self.n_text
            self.n_text = [0, 0, 0, 0, 0]
            return (a,b,c,d,e, img_c)
        return (None, None)
    def close(self):
        self.cap.release()
if __name__ == "__main__":
    d = Display()
    while True:
        (a, b, c, d, e, img) = d.get()
        cv2.imshow('img', img)