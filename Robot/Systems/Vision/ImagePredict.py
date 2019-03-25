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

    def only_color(img, h, s, v, h1, s1, v1):
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        (lower, upper) = (np.array([h, s, v]), np.array([h1, s1, v1]))
        mask = cv2.inRange(hsv, lower, upper)
        res = cv2.bitwise_and(img, img, mask=mask)
        kernel = np.ones((3, 3), np.uint)
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        return mask

    def abra(self, img):
        mask = cv2.resize(img, (60, 60))
        mask = only_color(mask, 
            48,
            92,
            0,
            64,
            255,
            255,
            )
        mask = 255 - mask
        mask = cv2.resize(img, (60, 60))
        cv2.imwrite('{}.jpg'.format(time.time()),mask)
        mask = mask.reshape(self.dot_product)
        mask = mask.astype('float32')
        mask /= 255
        return mask

    def kadabra(self):
        '''
            LOL .. hey .. it would be incomplete without this
        '''

        pass

    def alakazam(self, img):
        return self.model.predict(img.reshape(1,
                                  self.dot_product))[0].tolist()



            