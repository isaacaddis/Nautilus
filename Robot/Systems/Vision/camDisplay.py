import cv2
import os
import time
from PIL import Image

os.system("fuser -k /dev/video0")
path = "~/Desktop/45C_Images"
cap = cv2.VideoCapture(0)
cv2.namedWindow("val", cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty("val",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
n=0

while True:
    n += 1
    ret, val = cap.read()
    image = cv2.cvtColor(val, cv2.COLOR_BGR2GRAY)
    cnts,__ = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for i in cnts:
        area = cv2.contourArea(i)
        print("Area: {}".format(area))
        if area > 100 and area < 3000:
            x, y, w, h = cv2.boundingRect(i)
            cropped = val.copy()[y-60:y+h+60, x-60:w+x+60]
            cv2.rectangle(val, (x, y), (x+w, y+h), (0, 255, 0), 1)
            # jpeg = Image.fromarray(cropped,'RGB')
            if n % 5 == 0:
                cv2.imwrite('{}.jpg'.format(time.ctime()),cropped)  
    cv2.imshow('val', val)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

