import matplotlib.pyplot as plt
import cv2
import numpy as np

img = cv2.imread("Images\\628548.jpg")
ims = cv2.resize(img, [640, 480])

img_hsv = cv2.cvtColor(ims, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(img_hsv)

v_equalization = cv2.equalizeHist(v)

img_hsv = cv2.merge([h, s, v_equalization])
img_rgb = cv2.cvtColor(img_hsv, cv2.COLOR_HSV2RGB)

cv2.imshow("v chanel", v_equalization)
cv2.imshow("img hsv", img_hsv)
cv2.imshow("img rgb", img_rgb)

cv2.waitKey(0)
cv2.destroyAllWindows()
