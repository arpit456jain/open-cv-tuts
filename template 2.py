import numpy as  np
import cv2
from matplotlib import pyplot as plt


img = cv2.imread("images/j.png",cv2.IMREAD_GRAYSCALE)

titles = []
images = []

for i in range(4):
    plt.subplot(2,2,i+1)
    plt.title(titles[i])
    plt.imshow(images[i],cmap = 'gray')

plt.show()

