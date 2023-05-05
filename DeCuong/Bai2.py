import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("Images/628548.jpg")
ims = cv2.resize(img, [640, 480])

Igray = cv2.cvtColor(ims, cv2.COLOR_BGR2GRAY)
ret, Ib = cv2.threshold(Igray, 0, 255, cv2.THRESH_OTSU)

cv2.imshow("img thresh otsu", Ib)

cv2.waitKey(0)
cv2.destroyAllWindows()
