import cv2
import os
import time
from geo import ShapeDetect
from ImagePredict import Magic
from ImagePreProcess import ImagePreProcess
import numpy as np
import time

os.system("fuser -k /dev/video1")
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2' # removes pesky warning 

cap = cv2.VideoCapture(1)
magic = Magic()
proc = ImagePreProcess()
sd = ShapeDetect()

last_len = 0
past_text, n_text = [0, 0, 0, 0, 0],[0, 0, 0, 0, 0] # follows the general data schema for shapes

while cap.isOpened():
    ret, val = cap.read()
    img_c = val.copy()
    image = proc.process(val)
    ret, image = cv2.threshold(image,127,255,cv2.THRESH_BINARY)
    thresholded = image.copy()
    ___,cnts,__ = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    current_len = 0
    for i in cnts:
        area = cv2.contourArea(i)
        if area > 600 and area < 11800:
            current_len += 1
            x, y, w, h = cv2.boundingRect(i)
            cv2.rectangle(val, (x, y), (x+w, y+h), (0, 255, 0), 1)
            s = sd.detect(i)
            print("Shape: {}".format(s))
            if s == "triangle":
                n_text[0] += 1
            elif s == "square":
                n_text[1] += 1
            elif s == "line":
                n_text[2] += 1
            elif s == "circle":
                n_text[3] += 1 
            print("# of shapes {}".format(current_len))
            if current_len > 0:
                cv2.putText(val,'Number of Shapes: {}'.format(current_len),(val.shape[1]-400,val.shape[0]-300), cv2.FONT_HERSHEY_SIMPLEX, 1,(255,0,0),1,cv2.LINE_AA)
            else:
                cv2.putText(val,'Number of Shapes: {}'.format(last_len),(val.shape[1]-400,val.shape[0]-300), cv2.FONT_HERSHEY_SIMPLEX, 1,(255,0,0),1,cv2.LINE_AA)
            if n_text[0] > 0:
                cv2.putText(val,'Triangle: {}'.format(n_text[0]),(val.shape[1]-350,val.shape[0]-200), cv2.FONT_HERSHEY_SIMPLEX, 1,(255,0,0),1,cv2.LINE_AA)
            else:
                cv2.putText(val,'Triangle: {}'.format(past_text[0]),(val.shape[1]-350,val.shape[0]-200), cv2.FONT_HERSHEY_SIMPLEX, 1,(255,0,0),1,cv2.LINE_AA)
            if n_text[1] > 0:
                cv2.putText(val,'Square: {}'.format(n_text[1]),(val.shape[1]-350,val.shape[0]-150), cv2.FONT_HERSHEY_SIMPLEX, 1,(255,0,0),1,cv2.LINE_AA)
            else:
                cv2.putText(val,'Square: {}'.format(past_text[1]),(val.shape[1]-350,val.shape[0]-150), cv2.FONT_HERSHEY_SIMPLEX, 1,(255,0,0),1,cv2.LINE_AA)
            if n_text[2] > 0:
                cv2.putText(val,'Line: {}'.format(n_text[2]),(val.shape[1]-350,val.shape[0]-100), cv2.FONT_HERSHEY_SIMPLEX, 1,(255,0,0),1,cv2.LINE_AA)
            else:
                cv2.putText(val,'Line: {}'.format(past_text[2]),(val.shape[1]-350,val.shape[0]-100), cv2.FONT_HERSHEY_SIMPLEX, 1,(255,0,0),1,cv2.LINE_AA)
            if n_text[3] > 0:
                cv2.putText(val,'Circle: {}'.format(n_text[3]),(val.shape[1]-350,val.shape[0]-20), cv2.FONT_HERSHEY_SIMPLEX, 1,(255,0,0),1,cv2.LINE_AA)
            else:
                cv2.putText(val,'Circle: {}'.format(past_text[3]),(val.shape[1]-350,val.shape[0]-20), cv2.FONT_HERSHEY_SIMPLEX, 1,(255,0,0),1,cv2.LINE_AA)

    past_text = n_text
    last_len = current_len
    n_text = [0, 0, 0, 0, 0]

    cv2.imshow('Scratch',image)
    cv2.imshow('Unfiltered',val)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

