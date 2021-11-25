import cv2 as cv
import numpy as np

def call_back(x):
    print(x)

img = np.zeros((400,500,3),np.uint8)
cv.namedWindow("image")
cv.createTrackbar("B","image",0,255,call_back)
cv.createTrackbar("G","image",0,255,call_back)
cv.createTrackbar("R","image",0,255,call_back)

switch = "0:OFF \n 1:ON"
cv.createTrackbar(switch,'image',0,1,call_back)
while(True):
    cv.imshow("image",img)

    if cv.waitKey(1) & 0xFF == 27:
        break
    b = cv.getTrackbarPos('B','image')
    g = cv.getTrackbarPos('G','image')
    r = cv.getTrackbarPos('R','image')
    s = cv.getTrackbarPos(switch,'image')
    print(b,g,r)
    if s==0:
        pass
    else:
        img[:] = [b,g,r]
