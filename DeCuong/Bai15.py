import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("Images/628548.jpg")
ims = cv2.resize(img, [640, 480])


img_gray = cv2.cvtColor(ims, cv2.COLOR_BGR2GRAY)
cv2.imshow("img gray", img_gray)

x = 130
y = 109
img_hsv_5x5 = img_gray[y - 2 : y + 2, x - 2 : x + 2]
print(img_hsv_5x5)
cv2.imshow("img gray 5x5", img_hsv_5x5)

cv2.waitKey(0)
cv2.destroyAllWindows()
