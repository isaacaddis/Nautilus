import cv2
import numpy as np
from matplotlib import pyplot as plt

class ImagePreProcess():
    def __init__(self):
        self.x = 0
    def process(self, image):
        self.img = image
        kernel = np.ones((5,5), np.uint8)
        self.erosion = cv2.erode(self.img, kernel, iterations=1)
        self.dilation = cv2.dilate(self.erosion, kernel, iterations=1)
        #self.gray = cv2.cvtColor(self.dilation, cv2.COLOR_BGR2GRAY)
        self.blurred = cv2.GaussianBlur(self.dilation,(5,5), 0)
        #self.blurred = cv2.bilateralFilter(self.blurred, 11, 17)
        self.canny = cv2.Canny(self.blurred, 100,200)
        return self.canny
    def analysis(self):
        plt.subplot(121),plt.imshow(self.canny,cmap = 'gray')
        plt.title('Image'), plt.xticks([]), plt.yticks([])


