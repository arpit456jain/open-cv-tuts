import numpy as  np
import cv2
from matplotlib import pyplot as plt


img = cv2.imread("images/messi5.jpg",cv2.IMREAD_GRAYSCALE)

#laplacian
lap = cv2.Laplacian(img,cv2.CV_64F,ksize=3)
lap = np.uint8(np.absolute(lap))

sobelX = cv2.Sobel(img,cv2.CV_64F,1,0)
sobelX = np.uint8(np.absolute(sobelX))

sobelY = cv2.Sobel(img,cv2.CV_64F,0,1)
sobelY = np.uint8(np.absolute(sobelY))

sobel_combined = cv2.bitwise_or(sobelX,sobelY)

canny = cv2.Canny(img,100,200)

titles = ['normal image','laplacian','sobelX','sobelY','sobel_combined','canny']
images = [img,lap,sobelX,sobelY,sobel_combined,canny]

for i in range(6):
    plt.subplot(2,3,i+1)
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
    plt.imshow(images[i],cmap = 'gray')

plt.show()

