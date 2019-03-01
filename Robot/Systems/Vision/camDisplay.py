import cv2

cap = cv2.VideoCapture(1)
cv2.namedWindow("val", cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty("val",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)

while True:
    ret, val = cap.read()
    image = cv2.cvtColor(val, cv2.COLOR_BGR2GRAY)
    ___,cnts,__ = cv2.findContours(image.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if len(cnts) >= 2:
        for i in cnts:
            peri = cv2.arcLength(i, True)
            approx = cv2.approxPolyDP(i, 0.1 * peri, True)
            x, y, w, h = cv2.boundingRect(i)
            cv2.rectangle(val, (x,y), (x+w, y+h), (0,255,0),2)
            cv2.drawContours(val,i,-1, (0,0,255),1)
    cv2.imshow('val', val)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

