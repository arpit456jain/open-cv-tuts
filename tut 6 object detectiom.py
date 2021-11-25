import cv2
import numpy as np

cap = cv2.VideoCapture(0)

def call_back(x):
    print(x)

# L_H = Lower Hue
# L_s = lower saturation
# L_v = lower value

cv2.namedWindow("Tracking")
cv2.createTrackbar('l_h','Tracking',0,255,call_back)
cv2.createTrackbar('l_s','Tracking',0,255,call_back)
cv2.createTrackbar('l_v','Tracking',0,255,call_back)

cv2.createTrackbar('u_h','Tracking',255,255,call_back)
cv2.createTrackbar('u_s','Tracking',255,255,call_back)
cv2.createTrackbar('u_v','Tracking',255,255,call_back)
while True:
    # frame = cv2.imread("images/smarties.png")
    success,frame = cap.read()
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    l_h = cv2.getTrackbarPos("l_h","Tracking")
    l_s = cv2.getTrackbarPos("l_s","Tracking")
    l_v = cv2.getTrackbarPos("l_v","Tracking")

    u_h = cv2.getTrackbarPos("u_h","Tracking")
    u_s = cv2.getTrackbarPos("u_s","Tracking")
    u_v = cv2.getTrackbarPos("u_v","Tracking")

    lb = np.array([l_h,l_s,l_v])
    up = np.array([u_h,u_s,u_v])

    mask = cv2.inRange(hsv,lb,up)

    result = cv2.bitwise_and(frame,frame,mask=mask)
    cv2.imshow("frame1",frame)
    cv2.imshow("frame2",mask)
    cv2.imshow("frame3",result)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()