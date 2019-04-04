import cv2
import os
import time
from geo import ShapeDetect
from ImagePredict import Magic
from ImagePreProcess import ImagePreProcess
import numpy as np

os.system("fuser -k /dev/video1")
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2' # removes pesky warning 
path = "~/Desktop/45C_Images"
cap = cv2.VideoCapture(1)
magic = Magic()
proc = ImagePreProcess()
dirname = "Images/"
shapes = []
n_text = [0, 0, 0, 0, 0] # follows the general data schema for shapes
last_len = 0

while cap.isOpened():
    ret, val = cap.read()
    img_c = val.copy()
    image = proc.process(val)
    ret, image = cv2.threshold(image,127,255,cv2.THRESH_BINARY)
    thresholded = image.copy()
    ___,cnts,__ = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    current_len = len(cnts)
    if current_len != last_len:
        #i = max(cnts, key=cv2.contourArea)
        for i in cnts:
            M = cv2.moments(c)
            cX = int(M["m10"]/M["m00"]*ratio)
            cY = int((M["m01"]/M["m00"]*ratio))
            shapes.push(ShapeDetect.detect(i))
            for s in shapes:
                if s == "triangle":
                    n_text[0] += 1
                elif s == "square":
                    n_text[1] += 1
                elif s == "line":
                    n_text[2] += 1
                elif s == "circle":
                    n_text[4] += 1 
            # area = cv2.contourArea(i)
            # if area > 1000 and area < 11800:
            #     x, y, w, h = cv2.boundingRect(i)
            #     coords = (x,y)
            #     cropped = img_c.copy()[y-45:y+h+45, x-45:w+x+45]
            #     org = (coords[0], coords[1]+int(area/400))
            #     cv2.rectangle(val, (x, y), (x+w, y+h), (0, 255, 0), 1)
            #     if np.prod(cropped.shape[:2])>10:
            #         mask = magic.abra(cropped)
            #         final = mask.copy()
            #         prediction = magic.alakazam(mask)
            #         text = '' 
            #         p_val, th = .25, .5
            #         if max(prediction)> p_val: 
            #             if prediction[0]>p_val and prediction[0]==max(prediction): 
            #                 text, th = 'triangle', prediction[0]
            #                 n_text[0] += 1
            #             if prediction[1]>p_val and prediction[1]==max(prediction): 
            #                 text, th = 'star', prediction[1]
            #                 n_text[1] += 1 
            #             if prediction[2]>p_val and prediction[2]==max(prediction): 
            #                 text, th = 'square', prediction[2]
            #                 n_text[2] += 1 
            #             if prediction[3]>p_val and prediction[3]==max(prediction): 
            #                 text, th = 'circle', prediction[3]
            #                 n_text[3] += 1
            #             # cv2.imwrite(os.path.join(dirname, '{}.jpg'.format(text)),cropped)E
            #         print(prediction)
                    last_len = current_len
                    # cv2.imshow('Final', final)  
                    cv2.putText(val,'Triangle: {}'.format(n_text[0]),(val.shape[1]-200,val.shape[0]-200), cv2.FONT_HERSHEY_SIMPLEX, 1,(255,0,0),4,cv2.LINE_AA)
                    cv2.putText(val,'Star: {}'.format(n_text[1]),(val.shape[1]-200,val.shape[0]-150), cv2.FONT_HERSHEY_SIMPLEX, 1,(255,0,0),4,cv2.LINE_AA)
                    cv2.putText(val,'Square: {}'.format(n_text[2]),(val.shape[1]-200,val.shape[0]-100), cv2.FONT_HERSHEY_SIMPLEX, 1,(255,0,0),4,cv2.LINE_AA)
                    cv2.putText(val,'Circle: {}'.format(n_text[3]),(val.shape[1]-200,val.shape[0]-20), cv2.FONT_HERSHEY_SIMPLEX, 1,(255,0,0),4,cv2.LINE_AA)
                else: 
                    print("A line")
    else:
        n_text = [0,0,0,0]
    cv2.imshow('Scratch',image)
    cv2.imshow('Unfiltered',val)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

