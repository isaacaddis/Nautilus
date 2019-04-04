import cv2
class ShapeDetect:
	def __init__(self):
		pass
	def detect(self, c):
		peri = cv2.arcLength(c, True)
		approx = cv2.approxPolyDP(c, 0.04*peri, True)
		if len(approx) ==3:
			return 'triangle'
		elif len(approx) ==4:
			(x, y, w, h) = cv2.boundingRect(approx)
			ar = w / float(h)
			if ar >= .95 and ar <= 1.15:
				return 'square'
			else:
				return 'line'
		else:
			return 'circle'