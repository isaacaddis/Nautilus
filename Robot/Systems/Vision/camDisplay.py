import cv2
import os
from . import ImagePreProcess
from . import geo
from . import Async
from . import Undistort
import time
import numpy as np
import time

class Display():
    def __init__(self, num):
        self.num = num
        self.cap = cv2.VideoCapture(num)
        self.und = Undistort.Undistort()
        self.proc = ImagePreProcess.ImagePreProcess()
        self.sd = geo.ShapeDetect()
        self.past_text, self.n_text = [0, 0, 0, 0, 0],[0, 0, 0, 0, 0] # follows the general data schema for shapes
    def __num__(self):
        return self.num
    def get(self, num=1):
        a = ""
        b = ""
        c = ""
        d = ""
        e = ""
        if num == 1:
            ret, val = self.cap.read()
            img_c = val.copy()
            val = val[0:int(val.shape[0]/1.33)]
            image = self.proc.process(val)
            ret, image = cv2.threshold(image,127,255,cv2.THRESH_BINARY)
            thresholded = image.copy() #to save thresholded image
            ___,cnts,__ = cv2.findContours(thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            current_len = 0
            max_n = 0
            for i in cnts:
                area = cv2.contourArea(i)
                if area > 165 and area < 4000:
                    if area > max_n:
                        max_n = area
                    current_len += 1
                    x, y, w, h = cv2.boundingRect(i)
                    cv2.rectangle(img_c, (x, y), (x+w, y+h), (0, 255, 0), 1)
                    s = self.sd.detect(i,img_c)
                    if s == "triangle":
                        self.n_text[0] += 1
                    elif s == "square":
                        self.n_text[1] += 1
                        cv2.imwrite('Images/'+str(area)+'-square.jpg',img[y:y+h, x:x+w])
                    elif s == "line":
                        self.n_text[2] += 1
                        cv2.imwrite('Images/'+str(area)+'line.jpg',img[y:y+h, x:x+w])
                    elif s == "circle":
                        self.n_text[3] += 1 
                    a = "# of shapes {}".format(current_len)
                    b = "# of triangles {}".format(self.n_text[0])
                    c = "# of squares {}".format(self.n_text[1])
                    d = "# of lines {}".format(self.n_text[2])
                    e = "# of circles {}".format(self.n_text[3])
            self.past_text = self.n_text
            self.n_text = [0, 0, 0, 0, 0]
            return (a,b,c,d,e, img_c)
