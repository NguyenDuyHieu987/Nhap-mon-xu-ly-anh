import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("Images/628548.jpg", 0)
ims = cv2.resize(img, [640, 480])

y, x = 9, 11
neighborhood = ims[y - 2 : y + 3, x - 2 : x + 3]

cv2.imshow("Img", neighborhood)


cv2.waitKey(0)
cv2.destroyAllWindows()
