import numpy as  np
import cv2
from matplotlib import pyplot as plt

# img = cv2.imread("images/smarties.png",cv2.IMREAD_GRAYSCALE)
img = cv2.imread("images/j.png",cv2.IMREAD_GRAYSCALE)

# _,mask = cv2.threshold(img,220,255,cv2.THRESH_BINARY_INV)
mask = img
kernel = np.ones([2,2],np.uint8)

dilation = cv2.dilate(mask,kernel,iterations=2)
erosion = cv2.erode(mask,kernel,iterations=1)

opening = cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel)
closing = cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernel)

morphological_gradient = cv2.morphologyEx(mask,cv2.MORPH_GRADIENT,kernel)
morphological_topHat = cv2.morphologyEx(mask,cv2.MORPH_TOPHAT,kernel)

titles = ['image','mask','dilated','erosion','opening','closing','gradient','tophat']
images = [img , mask , dilation , erosion , opening , closing , morphological_gradient , morphological_topHat]

for i in range(8):
    plt.subplot(2,4,i+1)
    plt.title(titles[i])
    plt.imshow(images[i],cmap = 'gray')

plt.show()

