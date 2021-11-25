import cv2
# to do make a feature such that when we click it stores the coordinate and when all 4 coordinates are avaieble
# it will copy the ball to another position
img = cv2.imread("images/messi5.jpg") 

print(img.shape,img.size,img.dtype)

b,g,r = cv2.split(img) # split the image -> return 3 -> 2-D matrix
print(b,g,r,type(b),b.shape)
img = cv2.merge((b,g,r))
ball  = img[280:340,330:390]
img[273:333,100:160] = ball
cv2.imshow("ball",ball)
cv2.imshow("image",img)
cv2.waitKey(0)