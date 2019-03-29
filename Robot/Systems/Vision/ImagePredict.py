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

    def only_color(self,img, h, s, v, h1, s1, v1):
        # hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        (lower, upper) = (np.array([h, s, v]), np.array([h1, s1, v1]))
        # mask = cv2.inRange(hsv, lower, upper)
        # res = cv2.bitwise_and(img, img, mask=mask)
        kernel = np.ones((3, 3), np.uint)
        mask = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
        return mask

    def abra(self, img):
        # mask = cv2.resize(img, (60, 60))
        cv2.imwrite('1.jpg', img)
        mask = self.only_color(img, 0,0,0,180,255,100)
        # mask = 255 - mask
        mask = cv2.resize(mask, (60, 60))
        # zeroes = np.zeros((60,60))
        # n_zeroes = zeroes[...,np.newaxis]
        mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
        # height, width, channels = zeroes.shape
        # print('Channels: {}'.format(channels))
        # mask = 255 - mask
        # mask = cv2.resize(img, (60, 60))
        # cv2.imshow('mask', mask)\
        cv2.imwrite('2.jpg', mask)
        # n_mask = mask.reshape(60, 60,1)
        print('Shape: {}'.format(mask.shape))
        n_mask = mask.astype('float32')
        n_mask /= 255
        cv2.imwrite('mask.jpg', n_mask)
        return n_mask

    def kadabra(self):
        pass

    def alakazam(self, img):
        return self.model.predict(img.reshape(1,
                                  self.dot_product))[0].tolist()



            