import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("Images/628548.jpg")
ims = cv2.resize(img, [640, 480])

img_gray = cv2.cvtColor(ims, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(img_gray, 90, 255, cv2.THRESH_OTSU)
cv2.imshow("anh nhi phan theo otsu", thresh)


cv2.waitKey(0)
cv2.destroyAllWindows()
