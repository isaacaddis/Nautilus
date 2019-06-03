import threading
import cv2

class Async:
	def __init__(self, src, width = 640, height = 480):
		self.src = src
		self.cap = cv2.VideoCapture(self.src)
		self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
		self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
		self.grabbed, self.frame = self.cap.read()
		self.started = False
		self.read_lock = threading.Lock()
	def set(self, var1, var2):
		self.cap.set(var1,var2)
	def start(self):
	    if self.started:
	        print('[!] Asynchroneous video capturing has already been started.')
	        return None
	    self.started = True
	    self.thread = threading.Thread(target=self.update, args=())
	    self.thread.start()
	    return self

	def update(self):
	    while self.started:
	        grabbed, frame = self.cap.read()
	        if frame is not None:
		        with self.read_lock:
		            self.grabbed = grabbed
		            self.frame = frame

	def read(self):
	    with self.read_lock:
	        frame = self.frame.copy()
	        grabbed = self.grabbed
	    return grabbed, frame

	def stop(self):
	    self.started = False
	    self.thread.join()

	def __exit__(self, exec_type, exc_value, traceback):
	    self.cap.release()