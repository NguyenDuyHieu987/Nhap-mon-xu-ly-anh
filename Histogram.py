import matplotlib.pyplot as plt
import cv2 
import numpy as np

img = cv2.imread("Images\\628548.jpg")
ims = cv2.resize(img, [640, 480])

hist = cv2.calcHist([ims], [0], None, [256], [0, 256])

plt.plot(hist, color = 'r')
plt.hist(ims.ravel(), 256, [0, 256])
plt.title('Image Histogram For Blue Channel')
plt.show()