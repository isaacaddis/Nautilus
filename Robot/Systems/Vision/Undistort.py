import cv2
import numpy as np
class Undistort():
	def __init__(self):
		self.dim=(640, 480)
		self.k=np.array([[553.350692313905, 0.0, 342.9451779392026], [0.0, 545.573637355145, 211.4054580385251], [0.0, 0.0, 1.0]])
		self.d=np.array([[-0.2807810032443438], [2.1812482493268424], [-8.101784482269283], [10.048341560961232]]) 
	def rectify(self, frame):
		map1, map2 = cv2.fisheye.initUndistortRectifyMap(self.k, self.d, np.eye(3), self.k, self.dim, cv2.CV_16SC2)
		undistorted_img = cv2.remap(frame, map1, map2, interpolation=cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT)
		return undistorted_img