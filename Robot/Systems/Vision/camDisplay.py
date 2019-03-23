import cv2
import os
import time
from ImagePredict import Magic
from ImagePreProcess import ImagePreProcess
import numpy as np

os.system("fuser -k /dev/video0")
path = "~/Desktop/45C_Images"
cap = cv2.VideoCapture(0)
# cv2.namedWindow("val", cv2.WND_PROP_FULLSCREEN)
# cv2.setWindowProperty("val",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
n=0
magic = Magic()
proc = ImagePreProcess()

while cap.isOpened():
    n += 1
    ret, val = cap.read()
    img_c = val.copy()
    image = proc.process(val)
    # image = cv2.cvtColor(img_c, cv2.COLOR_BGR2GRAY)
    ret, image = cv2.threshold(image, 127, 255, 0)
    cnts,__ = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for i in cnts:
        area = cv2.contourArea(i)
        # print("Area: {}".format(area))
        if area > 100 and area < 3000:
            x, y, w, h = cv2.boundingRect(i)
            coords = (x,y)
            cropped = img_c.copy()[y-60:y+h+60, x-60:w+x+60]
            org = (coords[0], coords[1]+int(area/400))
            # jpeg = Image.fromarray(cropped,'RGB')
            cv2.rectangle(val, (x, y), (x+w, y+h), (0, 255, 0), 1)
            if np.prod(cropped.shape[:2])>10:
                # cropped = cv2.resize(cropped, (60,60))
                mask = magic.abra(cropped)
                prediction = magic.alakazam(mask)
                text = '' 
                p_val, th = .25, .5 
                if max(prediction)> p_val: 
                    if prediction[0]>p_val and prediction[0]==max(prediction): 
                        text, th = 'triangle', prediction[0] 
                    if prediction[1]>p_val and prediction[1]==max(prediction): 
                        text, th = 'star', prediction[1] 
                    if prediction[2]>p_val and prediction[2]==max(prediction): 
                        text, th = 'square', prediction[2] 
                    if prediction[3]>p_val and prediction[3]==max(prediction): 
                        text, th = 'circle', prediction[3]
                    cv2.imwrite('{}.jpg'.format(max(text)),cropped)
                # name = ''
                print(prediction)
            else:
                print("A line")
    cv2.imshow('val', val)
    cv2.imshow('image',image)
    # cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

