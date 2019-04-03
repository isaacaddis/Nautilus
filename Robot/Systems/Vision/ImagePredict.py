#!/usr/bin/python
# -*- coding: utf-8 -*-
import cv2
import numpy as np
from keras.models import load_model
import os
import time

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



            