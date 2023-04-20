import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("Images/628548.jpg")
img = cv2.resize(img, [640, 480])

img_gray = cv2.cvtColor(img, cv2.COLOR_RGBA2GRAY)
thread, ims = cv2.threshold(img_gray, 0, 255, cv2.THRESH_OTSU)

cv2.imshow("ims", ims)

cv2.waitKey(0)
cv2.destroyAllWindows()
