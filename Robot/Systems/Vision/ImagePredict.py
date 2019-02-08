import cv2
import numpy as np
from keras.models import load_model

class Magic():
    def __init__(self):
        self.model = load_model("../Util/shapes_model.h5")
        self.dot_product = np.prod([60,60])
    def abra(self, img):
        mask = cv2.resize(img, (60,60))
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
        return self.model.predict(img.reshape(1, self.dot_product))[0].tolist()

