import cv2
import time

'''
    Image retrieval tools
'''
class Operation():
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
    def retrieval(self):
        print("Retrieving")
        self.ret, self.frame = self.cap.read()
        assert self.ret is not None
        return self.frame
    def close(self):
        self.cap.release()
'''
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
'''
