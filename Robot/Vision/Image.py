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
        return self.frame
    def close(self):
        self.cap.release()
if __name__ == "__main__":
    op = Operation()
    i = 0
    while True:
        i+=1
        print("Iteration: "+str(i))
        frame = op.retrieval()
        #proc = ImagePreProcess(frame)
        #img = proc.process()
        cv2.imshow("Image", frame)
        if cv2.waitKey(0) == 27:
            op.close()
            cv2.destroyAllWindows()

