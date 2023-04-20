import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("Images/628548.jpg")
ims = cv2.resize(img, [640, 480])

img_gray = cv2.cvtColor(ims, cv2.COLOR_BGR2GRAY)

kernel1 = np.array([[-1, 1, 1], [-1, -2, 1], [-1, 1, 1]])
kernel2 = np.array([[1, 1, 1], [-1, -2, 1], [-1, -1, 1]])
kernel3 = np.array([[1, 1, -1], [-1, -2, 1], [-1, -1, 1]])
kernel4 = np.array([[-1, -1, -1], [-1, -2, 1], [-1, -1, 1]])


img_Compass1 = cv2.filter2D(img_gray, -1, kernel1)
img_Compass2 = cv2.filter2D(img_gray, -1, kernel2)
img_Compass3 = cv2.filter2D(img_gray, -1, kernel3)
img_Compass4 = cv2.filter2D(img_gray, -1, kernel4)


img_Compass = img_Compass1 + img_Compass2 + img_Compass3 + img_Compass4

cv2.imshow("anh Compass1", img_Compass1)
cv2.imshow("anh Compass2", img_Compass2)
cv2.imshow("anh Compass3", img_Compass3)
cv2.imshow("anh Compass4", img_Compass4)
cv2.imshow("anh Compass", img_Compass)
cv2.imshow("anh goc", ims)

cv2.waitKey(0)
cv2.destroyAllWindows()
