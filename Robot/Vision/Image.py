import cv2
import time
from  ImagePreProcess import ImagePreProcess

class Operation():
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
    def retrieval(self):
        self.ret, self.frame = self.cap.read()
        #cv2.imshow("frame", self.frame)
        #assert self.ret is not None
        #print("Type: " + str(type(self.frame)))
        #cv2.imshow("Frame", self.frame)
        return self.frame
    def close(self):
        self.cap.release()
if __name__ == "__main__":
    op = Operation()
    proc = ImagePreProcess()
    while True:
        raw = op.retrieval()
        img = proc.process(raw)
        cv2.imshow("Frame",img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    op.close()
    cv2.destroyAllWindows()
