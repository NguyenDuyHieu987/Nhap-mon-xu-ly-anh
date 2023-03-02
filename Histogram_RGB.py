import matplotlib.pyplot as plt
import cv2 
import numpy as np

img = cv2.imread("Images\\628548.jpg")
ims = cv2.resize(img, [640, 480])
cv2.imshow('gg', ims)

color = ('b', 'g', 'r')
for i, col in enumerate(color):
    histrgb = cv2.calcHist([ims], [i], None, [256], [0, 256])
    plt.plot(histrgb, color = col)
plt.show()