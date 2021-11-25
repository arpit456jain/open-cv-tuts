import cv2
import numpy as np
# black image

img = np.zeros([512,512,3],np.uint8)
# img = cv2.imread("images/lena.jpg")

print(img.shape)
img1 = cv2.line(img,(0,0),(256,256),(255,0,0),10)
img2 = cv2.line(img,(0,0),(256,0),(0,255,0),10)
img3 = cv2.line(img,(0,0),(0,256),(0,0,255),10)
cv2.arrowedLine(img,(256,256),(512,512),(0,0,255),5)
cv2.rectangle(img,(22,22),(222,222),(0,100,100),-1)
cv2.rectangle(img,(10,10),(300,300),(0,100,100),5)
cv2.circle(img,(222,222),100,(200,200,200),5)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,"opencv",(10,400),font,4,(255,255,255),10,cv2.LINE_AA)

cv2.imshow("img 1",img)
k = cv2.waitKey(0) # for indefinitly
if k == 27:
    cv2.destroyAllWindows()
elif k == ord('q'):
    cv2.destroyAllWindows()
