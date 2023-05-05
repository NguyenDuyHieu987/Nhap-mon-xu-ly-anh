import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("Images/628548.jpg")
ims = cv2.resize(img, [640, 480])


img_hsv = cv2.cvtColor(ims, cv2.COLOR_BGR2HSV)

x = 5
y = 10
img_hsv_5x5 = img_hsv[y - 2 : y + 2, x - 2 : x + 2]
print(img_hsv_5x5)
cv2.imshow("img 5x5", img_hsv)

cv2.waitKey(0)
cv2.destroyAllWindows()
