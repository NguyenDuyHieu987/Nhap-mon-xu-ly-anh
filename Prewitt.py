import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("Images/628548.jpg")
ims = cv2.resize(img, [640, 480])

img_gray = cv2.cvtColor(ims, cv2.COLOR_BGR2GRAY)

kernelX = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]])
kernelY = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
img_prewittX = cv2.filter2D(img_gray, -1, kernelX)
img_prewittY = cv2.filter2D(img_gray, -1, kernelY)

img_prewitt = img_prewittX + img_prewittY

cv2.imshow("anh prewittX", img_prewittX)
cv2.imshow("anh prewittY", img_prewittY)
cv2.imshow("anh prewitt", img_prewitt)
cv2.imshow("anh goc", ims)

cv2.waitKey(0)
cv2.destroyAllWindows()
