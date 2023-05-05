import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("Images/628548.jpg")
ims = cv2.resize(img, [640, 480])

img_gray = cv2.cvtColor(ims, cv2.COLOR_BGR2GRAY)

sobelx = cv2.Sobel(img_gray, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=5)
sobely = cv2.Sobel(img_gray, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=5)

cv2.imshow("Sobel x", sobelx)
cv2.imshow("Sobel y", sobely)


cv2.waitKey(0)
cv2.destroyAllWindows()
