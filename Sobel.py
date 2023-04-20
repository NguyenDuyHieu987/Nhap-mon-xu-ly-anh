import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("Images/628548.jpg")
ims = cv2.resize(img, [640, 480])

img_gray = cv2.cvtColor(ims, cv2.COLOR_BGR2GRAY)

kernelX = np.array([[-1, 1, 1], [-2, 0, 2], [-1, 0, -1]])
kernelY = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
img_SobelX = cv2.filter2D(img_gray, -1, kernelX)
img_SobelY = cv2.filter2D(img_gray, -1, kernelY)
img_Sobel = img_SobelX + img_SobelY

img_x = cv2.Sobel(img_gray, cv2.CV_64F, 1, 0, ksize=5)
img_y = cv2.Sobel(img_gray, cv2.CV_64F, 0, 1, ksize=5)
img_xy = cv2.Sobel(img_gray, cv2.CV_64F, 1, 1, ksize=5)

# cv2.imshow("anh goc", ims)
# cv2.imshow("anh SobelX", img_SobelX)
# cv2.imshow("anh SobelY", img_SobelY)
# cv2.imshow("anh Sobel", img_Sobel)

cv2.imshow("anh SobelX", img_x)
cv2.imshow("anh SobelY", img_y)
cv2.imshow("anh Sobel", img_xy)


cv2.waitKey(0)
cv2.destroyAllWindows()
