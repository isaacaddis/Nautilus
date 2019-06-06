import cv2
import numpy as np

class ImagePreProcess():
    def __init__(self):
        pass
    def process(self, image):

        '''
            Returns blurred, morphed, and canny-edged image.
        '''
        #image = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
        self.img = cv2.GaussianBlur(image,(5,5), 0)
        self.median = cv2.medianBlur(self.img,5)
        self.blur = cv2.bilateralFilter(self.median, 9, 75, 75)
        self.kernel = np.ones((5,5), np.uint8)
        self.erosion = cv2.erode(self.blur, self.kernel, iterations=1)
        self.dilation = cv2.dilate(self.erosion, self.kernel, iterations=1)
        self.canny = cv2.Canny(self.dilation, 100,200)
        return self.canny
        