import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("Images/628548.jpg")
ims = cv2.resize(img, [640, 480])


img_hsv = cv2.cvtColor(ims, cv2.COLOR_BGR2HSV)

h, s, v = cv2.split(img_hsv)

cv2.imshow("s chanel", s)

cv2.waitKey(0)
cv2.destroyAllWindows()
