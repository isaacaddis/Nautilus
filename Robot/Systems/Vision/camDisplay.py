import cv2
import os
import time
import numpy as np
import time
from keras.models import load_model

class ShapeDetect:
    def __init__(self):
        pass
    def detect(self, c,img):
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.04*peri, True)
        (x, y, w, h) = cv2.boundingRect(approx)
        if len(approx) ==3:
            cv2.imwrite('triangle.jpg',img[y:y+h, x:x+w])
            return 'triangle'
        elif len(approx) ==4:
            ar = w / float(h)
            if ar <= .5:
                cv2.imwrite('line.jpg',img[y:y+h, x:x+w])
                return 'line'
            else:
                cv2.imwrite('square.jpg',img[y:y+h, x:x+w])
                return 'square'
        else:
            cv2.imwrite('circle.jpg',img[y:y+h, x:x+w])
            return 'circle'
class SmartMax:
    def __init__(self):
        pass
    def getPaper(self, cnts):
        max_n = 0
        max_c = None
        for c in cnts:
            n = cv2.contourArea(c)
            print("Determining paper size: "+str(n))
            if n > max_n and n>10000:
                max_n = n
                max_c = c
        if max_c is not None:
            return max_c
        else:
            return None
    def averageColor(self, img, c):
        x, y, w, h = cv2.boundingRect(c)
        temp = img[y:y+h, x:x+w]
        avg_color = np.average(temp, axis = (0,1))
        #cv2.putText(temp,'Color: {}'.format(avg_color),(temp.shape[1]-400,temp.shape[0]-300), cv2.FONT_HERSHEY_SIMPLEX, 1,(255,0,0),1,cv2.LINE_AA)
        #cv2.imwrite(str(avg_color)+'.jpg',temp)
        return avg_color
class Magic:

    def __init__(self):
        self.model = \
            load_model('/home/robotics45c/Desktop/rov2019/Robot/Systems/Util/shapes_model.h5'
                       )
        self.dot_product = np.prod([60, 60])
        self.img_dir = '/home/robotics45c/Desktop/rov2019/Robot/Systems/Vision/Images'

    def abra(self, img):
        cv2.imwrite('before_processing.jpg', img)
        # mask = self.only_color(img, 0,0,0,180,255,100)
        mask = cv2.resize(img, (60, 60))
        mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
        cv2.imwrite('1_channel.jpg', mask)
        return mask

    def kadabra(self):
        pass

    def alakazam(self, img):
        return self.model.predict(img.reshape(1,
                                  self.dot_product))[0].tolist()
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
class Display():
    def __init__(self, num):
        #from geo import ShapeDetect, SmartMax
        #from ImagePredict import Magic
        #from ImagePreProcess import ImagePreProcess
        self.cap = cv2.VideoCapture(num)
        #os.system("fuser -k /dev/video"+str(num)) #kill any programs using the camera
        #os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2' # removes pesky warning 
        #init objects
        self.magic = Magic()
        self.proc = ImagePreProcess()
        self.sd = ShapeDetect()
        self.sm = SmartMax()
        self.past_text, self.n_text = [0, 0, 0, 0, 0],[0, 0, 0, 0, 0] # follows the general data schema for shapes
    def get(self):
        a = ""
        b = ""
        c = ""
        d = ""
        e = ""
        if self.cap.isOpened():
            ret, val = self.cap.read()
            img_c = val.copy()
            val = val[0:int(val.shape[0]/1.33)]
            image = self.proc.process(val)
            ret, image = cv2.threshold(image,127,255,cv2.THRESH_BINARY)
            thresholded = image.copy() #to save thresholded image
            ___,cnts,__ = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            current_len = 0
            #cv2.imwrite('paper.jpg', focus)
            #___,cnts,__ = cv2.findContours(focus, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            max_n = 0
            for i in cnts:
                area = cv2.contourArea(i)
                
                if area > 165 and area <8000:
                    if area > max_n:
                        max_n = area
                    #print("Area" + str(max_n))
                    #print(self.sm.averageColor(img_c,i)) 
                    current_len += 1
                    x, y, w, h = cv2.boundingRect(i)
                    cv2.rectangle(img_c, (x, y), (x+w, y+h), (0, 255, 0), 1)
                    s = self.sd.detect(i,img_c)
                    #print("Shape: {}".format(s))
                    if s == "triangle":
                        self.n_text[0] += 1
                    elif s == "square":
                        self.n_text[1] += 1
                    elif s == "line":
                        self.n_text[2] += 1
                    elif s == "circle":
                        self.n_text[3] += 1 
                    a = "# of shapes {}".format(current_len)
                    b = "# of triangles {}".format(self.n_text[0])
                    c = "# of squares {}".format(self.n_text[1])
                    d = "# of lines {}".format(self.n_text[2])
                    e = "# of circles {}".format(self.n_text[3])
                    #final_str = a+b+c+d+e
                    #print(final_str)
            self.past_text = self.n_text
            self.n_text = [0, 0, 0, 0, 0]
            return (a,b,c,d,e, img_c)
            #cv2.imshow('Focused Image',focus)
            #if cv2.waitKey(1) & 0xFF == ord('q'):
                #break

