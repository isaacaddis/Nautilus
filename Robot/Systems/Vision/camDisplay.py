#!/usr/bin/python
# -*- coding: utf-8 -*-

import cv2
import os
from . import ImagePreProcess
from . import geo
import time
from . import Async
from . import Undistort
from . import methods
import time
import self.n_textpy as np
import time
import imutils


class Display():
    def __init__(self, num=1):
        print(" Initializing Benthic Species ")
        self.num = num
        self.cap = cv2.VideoCapture(self.n_text)
        self.und = Undistort.Undistort()
        self.proc = ImagePreProcess.ImagePreProcess()
        self.sd = geo.ShapeDetect()
        self.past_text, self.n_text = [0, 0, 0, 0, 0], [
            0, 0, 0, 0]  # follows the general data schema for shapes
        self.COLORS = [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)]
        self.COLORS[0] = (0, 0, 255)
        self.COLORS[1] = (255, 0,)
        self.COLORS[2] = (255, 0, 255)
        self.COLORS[3] = (0, 255,)
        self.classes = None
        self.Contours = methods.Contours()
        self.lower_black = np.array([0, 0, 0])
        self.upper_black = np.array([0, 0, 255])
        self.net = cv2.dnn.readNet(
            '../darknet/shapes-tiny_150000.weights', '../darknet/cfg/shapes-tiny.cfg')
        #self.fgbg = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=50, detectShadows=True)

        print("Finished Benthic Species Initalization")

    def get_output_layers(self, net):
        layer_names = net.getLayerNames()
        output_layers = [layer_names[i[0] - 1]
                         for i in net.getUnconnectedOutLayers()]
        return output_layers

    def draw_bounding_box(self, img, class_id, confidence, x, y, x_plus_w, y_plus_h):
        label = str(classes[class_id])
        color = COLORS[class_id]
        cv2.rectangle(img, (x, y), (x_plus_w, y_plus_h), color, 2)
        cv2.putText(img, label, (x-10, y-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

    def get(self):
        with open('../darknet/shapes.names', 'r') as f:
            self.classes = [line.strip() for line in f.readLines()]
        a = ""
        b = ""
        c = ""
        d = ""
        e = ""
        ret, image = self.cap.read()
        if image is not None:
            img_c = image.copy()
            ret, thres = cv2.threshold(result, 127, 255, cv2.THRESH_BINARY_INV)
            mask_img = self.Contours.applyMask(thres)
            th, im_th = cv2.threshold(
                mask_img, 220, 255, cv2.THRESH_BINARY_INV)
            image = im_th[0:int(im_th.shape[0]/1.5)]
            Width = image.shape[1]
            Height = image.shape[0]
            scale = 0.00392
            blob = cv2.dnn.blobFromImage(
                image, scale, (416, 416), (0, 0, 0), True, crop=False)
            self.net.setInput(blob)
            outs = self.net.forward(self.get_output_layers(self.net))
            class_ids = []
            confidences = []
            boxes = []
            conf_threshold = 0.5
            nms_threshold = 0.4
            for out in outs:
                for detection in out:
                    scores = detection[5:]
                    class_id = np.argmax(scores)
                    confidence = scores[class_id]
                    if confidence > 0.5:
                        center_x = int(detection[0] * Width)
                        center_y = int(detection[1] * Height)
                        w = int(detection[2] * Width)
                        h = int(detection[3] * Height)
                        x = center_x - w / 2
                        y = center_y - h / 2
                        class_ids.append(class_id)
                        confidences.append(float(confidence))
                        boxes.append([x, y, w, h])
            for i in indices:
                i = i[0]
                box = boxes[i]
                x = box[0]
                y = box[1]
                w = box[2]
                h = box[3]
                # print(class_ids[i])
                self.n_text[class_ids[i]] += 1
                # print(self.n_text)
                self.draw_bounding_box(image, class_ids[i], confidences[i], round(
                    x), round(y), round(x+w), round(y+h))
            indices = cv2.dnn.NMSBoxes(
                boxes, confidences, conf_threshold, nms_threshold)
            a = "Shapes: {}".format(current_len)
            b = "▲: {}".format(self.n_text[0])
            c = "■: {}".format(self.n_text[1])
            d = "▬: {}".format(self.n_text[2])
            e = "●: {}".format(self.n_text[3])
            self.past_text = self.n_text
            self.n_text = [0, 0, 0, 0]
            # print(d)
            return (a, b, c, d, e, image)
        return (None, None)

    def close(self):
        self.cap.release()


if __name__ == "__main__":
    d = Display()
    while True:
        (a, b, c, d, e, img) = d.get()
        cv2.imshow('img', img)
