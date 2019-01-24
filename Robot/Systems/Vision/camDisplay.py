import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, val = cap.read()
    cv2.imshow('val', val)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

