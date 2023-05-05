import matplotlib.pyplot as plt
import cv2
import numpy as np

img = cv2.imread("Images\\628548.jpg")
ims = cv2.resize(img, [640, 480])

img_hsv = cv2.cvtColor(ims, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(img_hsv)

histrgb = cv2.calcHist(v, [0], None, [256], [0, 256])
plt.plot(histrgb, color="g")
plt.title("hist kenh v ")

plt.show()
