import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("Images/Lena.jpg")

img_hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
h, s, v = cv2.split(img_hsv)


smooth_image_f2D_5_5 = cv2.blur(img, (3, 3))

cv2.imshow("Image", smooth_image_f2D_5_5)

cv2.waitKey(0)
cv2.destroyAllWindows()
