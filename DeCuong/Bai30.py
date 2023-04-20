import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("Images/628548.jpg")
ims = cv2.resize(img, [640, 480])

# img_gray = cv2.cvtColor(ims, cv2.COLOR_BGR2GRAY)


img_canny = cv2.Canny(ims, threshold1=100, threshold2=200, L2gradient=True)
print(img_canny[109, 130] > 0)

cv2.imshow("Image", img_canny)

cv2.waitKey(0)
cv2.destroyAllWindows()
