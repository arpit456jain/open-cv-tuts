import cv2
import numpy as np

img = cv2.imread("images/gradient.png")

ret,frame = cv2.threshold(img,128,255,cv2.THRESH_BINARY)
print(ret,type(ret))
print(frame,type(frame))
cv2.imshow("image",img)
cv2.imshow("threshold",frame)
cv2.waitKey(0)
cv2.destroyAllWindows()