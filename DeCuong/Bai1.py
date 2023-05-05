import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("Images/628548.jpg")
ims = cv2.resize(img, [640, 480])

img_hsv = cv2.cvtColor(ims, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(img_hsv)

histrgb = cv2.calcHist([s], [0], None, [256], [0, 256])
plt.plot(histrgb, color="b")
img_equalization = cv2.equalizeHist(s)

histrgb1 = cv2.calcHist([img_equalization], [0], None, [256], [0, 256])
plt.plot(histrgb1, color="g")
plt.title("hist kenh s")

cv2.imshow("s chanel equalizeHist", s)
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
