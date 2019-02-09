import cv2
import time
import numpy as np
from ImagePredict import Magic
from ImagePreProcess import (ImagePreProcess, WhatsCrackin)
size = 60
'''
    Image retrieval tools
'''
class Operation():
    def __init__(self,cap):
        self.ret = False
        self.cap = cv2.VideoCapture(cap)
    def retrieval(self):
        self.ret, self.frame = self.cap.read()
        #assert self.ret is not None
        return self.frame
    def status(self):
        # use ret to determine if you're getting an image
        self.ret, self.frame = self.cap.read()
        return self.ret
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
        cv2.drawContours(img_copy,i, -1, (0,0,255),1)
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
            if max_p > .5:
                if prediction[0]>.5 and prediction[0] == max_p:
                    name = 'triangle'
                    n_triangle += 1
                    confidence = prediction[0]
                if prediction[1]>.5 and prediction[1] == max_p:
                    name = 'star'
                    n_star += 1
                    confidence = prediction[1]
                if prediction[2]>.5 and prediction[2] == max_p:
                    name = 'square'
                    n_square += 1
                    confidence = prediction[2]
                if prediction[3]>.5 and prediction[3] == max_p:
                    name = 'circle'
                    n_circle += 1
                    confidence = prediction[3]
                if prediction[4]>.5 and prediction[4] == max_p:
                    name = 'line'
                    n_line += 1
                    confidence = prediction[4]
            cv2.putText(img_copy, name, org, cv2.FONT_HERSHEY_SIMPLEX, int(2.2*area/15000), (0,0,255), int(6*confidence), cv2.LINE_AA)
    def integrate(img):
        img = self.proc.process(img)
        img_copy = img.copy()
        cnt = self.wc.findCracks(img)
        for i in cnt:
            peri = cv2.arcLength(i, True)
            approx = cv2.approxPolyDP(i, 0.02 * peri, True)
            area = cv2.contourArea(i)
            if area < 100:
                continue
            getPredictions(img, img_copy, cnt, approx)
if __name__ == "__main__":
    op = Operation(1)
    proc = ImagePreProcess()
    wc = WhatsCrackin()
    magic = Magic()
    '''
    Running number of each shape
    '''
    n_triangle = 0
    n_circle = 0
    n_star = 0
    n_square = 0
    n_line = 0
    while True:
        raw = op.retrieval()
        img = proc.process(raw)
        img_copy = raw.copy()
        cnt = wc.findCracks(img)
        #print(cnt)
        for i in cnt:
            peri = cv2.arcLength(i, True)
            approx = cv2.approxPolyDP(i, 0.02 * peri, True)
            area = cv2.contourArea(i)
            if area < 100:
                continue
            x, y, w, h = cv2.boundingRect(approx)
            cv2.rectangle(img_copy, (x, y), (x+w, y+h), (0, 255, 0), 1)
            cropped = img_copy[y-60:y+h+60, x-60:w+x+60]
            coords = (x,y)
            cv2.drawContours(img,i, -1, (0,0,255),1)
            org = (coords[0], coords[1]+int(area/400))
            if np.prod(cropped.shape[:2])>10:
                #cv2.rectangle(img_copy,(x,y),(x+w,y+h),(0,255,0),3)
                cropped = cv2.resize(img, (60,60))
                mask = magic.abra(cropped)
                prediction = magic.alakazam(mask)
                print("Prediction {}".format(prediction))
                name = ''
                max_p = max(prediction)
                confidence = .5
                if max_p > .5:
                    if prediction[0]>.5 and prediction[0] == max_p:
                        name = 'triangle'
                        n_triangle += 1
                        confidence = prediction[0]
                    if prediction[1]>.5 and prediction[1] == max_p:
                        name = 'star'
                        n_star += 1
                        confidence = prediction[1]
                    if prediction[2]>.5 and prediction[2] == max_p:
                        name = 'square'
                        n_square += 1
                        confidence = prediction[2]
                    if prediction[3]>.5 and prediction[3] == max_p:
                        name = 'circle'
                        n_circle += 1
                        confidence = prediction[3]
                    if prediction[4]>.5 and prediction[4] == max_p:
                        name = 'line'
                        n_line += 1
                        confidence = prediction[4]
                cv2.putText(img_copy, name, org, cv2.FONT_HERSHEY_SIMPLEX, int(2.2*area/15000), (0,0,255), int(6*confidence), cv2.LINE_AA)
                #if text != '':
                    #img_copy[img_copy.shape[0]-200:img_copy.shape[0], img.shape[1]-200:img.shape[1]] = cv2.cvtColor(cv2.resize(cropped,(200,200)), cv2.COLOR_GRAY2BGR)
        #p, l = wc.findLength(cracks)
        cv2.imshow("Frame",img_copy)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    op.close()
    cv2.destroyAllWindows()

