import cv2

cap = cv2.VideoCapture(1)
cv2.namedWindow("val", cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty("val",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)

while True:
    ret, val = cap.read()
    cv2.imshow('val', val)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

