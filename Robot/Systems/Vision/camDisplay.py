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
            crop_frame = img_c[0:int(img_c.shape[0]/1.58)]
            rgb_planes = cv2.split(crop_frame)
            result_planes = []
            for plane in rgb_planes:
                dilated_img = cv2.dilate(plane, np.ones((7,7), np.uint8))
                #bg_img = cv2.medianBlur(dilated_img, 21)
                bg_img = dilated_img
                diff_img = 255 - cv2.absdiff(plane, bg_img)
                result_planes.append(diff_img)

            result = cv2.merge(result_planes)
            ret,th1 = cv2.threshold(result,127,255,cv2.THRESH_BINARY_INV)
            mask_img = self.Contours.applyMask(th1)
            th, im_th = cv2.threshold(mask_img, 220, 255, cv2.THRESH_BINARY_INV)

            # Copy the thresholded image.
            im_floodfill = im_th.copy()

            # Mask used to flood filling.
            # Notice the size needs to be 2 pixels than the image.
            h, w = im_th.shape[:2]
            mask = np.zeros((h+2, w+2), np.uint8)

            # Floodfill from point (0, 0)
            cv2.floodFill(im_floodfill, mask, (0,0), 255);

            # Invert floodfilled image
            im_floodfill_inv = cv2.bitwise_not(im_floodfill)

            # Combine the two images to get the foreground.
            im_out = im_th | im_floodfill_inv
            _,cnts,__ = cv2.findContours(im_out, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            """crop_frame = img_c
            ret,thres = cv2.threshold(crop_frame,127,255,cv2.THRESH_BINARY_INV)
            mask_img = self.Contours.applyMask(thres)
            __,cnts,_ = cv2.findContours(mask_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)"""
            current_len = 0
            max_n = 0
            for i in cnts:
                area = cv2.contourArea(i)
                if area > 25 and area < 3200:
                    if area > max_n:
                        max_n = area
                    #print("Max area: {}".format(max_n))
                    current_len += 1
                    cv2.drawContours(img_c, [i], 0, (0,0,255),cv2.FILLED)
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
<<<<<<< HEAD
            return (a,b,c,d,e, img_c)
        return (None, None)
||||||| merged common ancestors
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
                    within_bound = sd.check(box, 215, 440, 260)
                    if (within_bound):
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
=======
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
>>>>>>> a4d8d7238d77a98de53029ae8d997eeb11ca7300
    def close(self):
        self.cap.release()
if __name__ == "__main__":
    d = Display()
    while True:
        (a, b, c, d, e, img) = d.get()
        cv2.imshow('img', img)