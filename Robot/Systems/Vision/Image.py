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
'''
if __name__ == "__main__":
    op = Operation(1)
    proc = ImagePreProcess()
    wc = WhatsCrackin()
    magic = Magic()
    #Running number of each shape
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
        gray = cv2.cvtColor(img_copy,cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(img_copy, 50, 150, aperatureSize=3)
        lines = cv2.HoughLines(edges, 1, np.pi/180,200)
        for rho, theta in lines[0]:
            a = np.cos(thetha)
            b = np.sin(thetha)
            x0 = a*rho
            y0 = b*rho
            x1 = int(x0 + 1000*-b)
            y1 = int(y0 + 1000*a)
            x2 = int(x0 - 1000*(-b))
            y2 = int(y0 - 1000*a)
            cv2.line(img_copy, (x1,y1),(x2,y2),(0,0,255),2)
        for i in cnt:
            peri = cv2.arcLength(i, True)
            approx = cv2.approxPolyDP(i, 0.02 * peri, True)
            area = cv2.contourArea(i)
            if area < 100:
                continue
            x, y, w, h = cv2.boundingRect(approx)
            #cv2.rectangle(img_copy, (x, y), (x+w, y+h), (0, 255, 0), 1)
            cropped = img_copy[y-60:y+h+60, x-60:w+x+60]
            coords = (x,y)
            #cv2.drawContours(img,i, -1, (0,0,255),1)
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
                img_copy = lsd.drawSegments(img,lines)
                cv2.putText(img_copy, name, org, cv2.FONT_HERSHEY_SIMPLEX, int(2.2*area/15000), (0,0,255), int(6*confidence), cv2.LINE_AA)
                #if text != '':
                    #img_copy[img_copy.shape[0]-200:img_copy.shape[0], img.shape[1]-200:img.shape[1]] = cv2.cvtColor(cv2.resize(cropped,(200,200)), cv2.COLOR_GRAY2BGR)
        #p, l = wc.findLength(cracks)
        cv2.imshow("Frame",img_copy)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    op.close()
    cv2.destroyAllWindows()
'''
