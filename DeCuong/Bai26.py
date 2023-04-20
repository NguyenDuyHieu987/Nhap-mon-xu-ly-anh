import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("Images/628548.jpg")
ims = cv2.resize(img, [640, 480])

img_hsv = cv2.cvtColor(ims, cv2.COLOR_RGB2HSV)
h, s, v = cv2.split(img_hsv)

img_median = cv2.medianBlur(s, 5)
cv2.imshow("loc median", img_median)


cv2.waitKey(0)
cv2.destroyAllWindows()
