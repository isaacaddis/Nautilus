import cv2
import os
from . import ImagePreProcess
from . import geo
from . import Async
import time
import numpy as np
import time

class Display():
    def __init__(self, num):
        self.num = num
        self.cap = cv2.VideoCapture(num)
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
        if True:
            ret, val = self.cap.read()
            if num == 0:
                return val
            if num == 1:
                img_c = val.copy()
                val = val[0:int(val.shape[0]/1.33)]
                image = self.proc.process(val)
                ret, image = cv2.threshold(image,127,255,cv2.THRESH_BINARY)
                thresholded = image.copy() #to save thresholded image
                ___,cnts,__ = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
                current_len = 0
                #cv2.imwrite('paper.jpg', focus)
                #___,cnts,__ = cv2.findContours(focus, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
                max_n = 0
                for i in cnts:
                    area = cv2.contourArea(i)
                    #print("Area: {}".format(area))
                    if area > 165 and area < 4000:
                        if area > max_n:
                            max_n = area
                        #print("Area" + str(max_n))
                        #print(self.sm.averageColor(img_c,i)) 
                        current_len += 1
                        x, y, w, h = cv2.boundingRect(i)
                        cv2.rectangle(img_c, (x, y), (x+w, y+h), (0, 255, 0), 1)
                        s = self.sd.detect(i,img_c)
                        #print("Shape: {}".format(s))
                        if s == "triangle":
                            self.n_text[0] += 1
                        elif s == "square":
                            self.n_text[1] += 1
                        elif s == "line":
                            self.n_text[2] += 1
                        elif s == "circle":
                            self.n_text[3] += 1 
                        a = "# of shapes {}".format(current_len)
                        b = "# of triangles {}".format(self.n_text[0])
                        c = "# of squares {}".format(self.n_text[1])
                        d = "# of lines {}".format(self.n_text[2])
                        e = "# of circles {}".format(self.n_text[3])
                        #final_str = a+b+c+d+e
                        #print(final_str)
                self.past_text = self.n_text
                self.n_text = [0, 0, 0, 0, 0]
                return (a,b,c,d,e, img_c)
            #cv2.imshow('Focused Image',focus)
            #if cv2.waitKey(1) & 0xFF == ord('q'):
                #break

