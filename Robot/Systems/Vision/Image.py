import cv2
import time
import os
'''
    Image retrieval tools
'''
class Operation():
    def __init__(self,c):
        self.ret = False
        self.c = c
        self.cap = cv2.VideoCapture(c)
        print('c')
    def __c__(self):
        return self.c
    def get(self):
        self.ret, self.frame = self.cap.read()
        #assert self.ret is not None
        return self.ret, self.frame
    def close(self):
        self.cap.release()
