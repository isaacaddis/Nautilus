import cv2
import time
from ImagePreProcess import (ImagePreProcess, WhatsCrackin)
'''
    Image retrieval tools
'''
class Operation():
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
    def retrieval(self):
        print("Retrieving")
        self.ret, self.frame = self.cap.read()
        assert self.ret is not None
        return self.frame
    def close(self):
        self.cap.release()

if __name__ == "__main__":
    op = Operation()
    proc = ImagePreProcess()
    wc = WhatsCrackin()
    while True:
        raw = op.retrieval()
        img = proc.process(raw)
        cnt = wc.findCracks(img)
        print(cnt)
        for i in cnt:
            x, y, w, h = cv2.boundingRect(i)
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
        #p, l = wc.findLength(cracks)
        cv2.imshow("Frame",img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    op.close()
    cv2.destroyAllWindows()

