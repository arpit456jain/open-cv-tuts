import cv2

img1 = cv2.imread("images/lena.jpg",1)
img2 = cv2.imread("images/lena.jpg",0)
img3 = cv2.imread("images/lena.jpg",-1)


cv2.imshow("img 1",img1)
cv2.imshow("img 2",img2)
cv2.imshow("img 3",img3)

k = cv2.waitKey(0) # for indefinitly
# cv2.waitKey(1)  # for 1 milli second
if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite("lena_grayScale.png",img2)
    cv2.destroyAllWindows()
