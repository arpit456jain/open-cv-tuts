import numpy as  np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread("images/watter.jpeg")

img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

kernel = np.ones((5,5),np.float32)/25

dst1 = cv2.filter2D(img,-1,kernel)
blur = cv2.blur(img,(5,5))
g_blur = cv2.GaussianBlur(img,(5,5),0)
median_blur = cv2.medianBlur(img,5)

titles = ['image','smooth 1','blur','gaussian blur','median blur']
images = [img,dst1,blur,g_blur,median_blur]

for i in range(5):
    plt.subplot(2,3,i+1)
    plt.title(titles[i])
    plt.imshow(images[i],cmap = 'gray')

plt.show()

