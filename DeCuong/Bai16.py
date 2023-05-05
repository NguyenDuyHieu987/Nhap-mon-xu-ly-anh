import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("Images/628548.jpg")
ims = cv2.resize(img, [640, 480])


b, g, r = cv2.split(ims)
cv2.imshow("b chanel", b)

cv2.waitKey(0)
cv2.destroyAllWindows()
