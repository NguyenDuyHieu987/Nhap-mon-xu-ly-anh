import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("Images/628548.jpg")
ims = cv2.resize(img, [640, 480])

img_gray = cv2.cvtColor(ims, cv2.COLOR_BGR2GRAY)

kernel1 = np.array([[0, -1, 0], [-1, 4, -1], [0, -1, 0]])
kernel2 = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])
kernel3 = np.array([[1, -2, 1], [-2, 4, -2], [1, -2, 1]])

img_prewitt1 = cv2.filter2D(img_gray, -1, kernel1)
img_prewitt2 = cv2.filter2D(img_gray, -1, kernel2)
img_prewitt3 = cv2.filter2D(img_gray, -1, kernel3)


img_prewitt = img_prewitt1 + img_prewitt2 + img_prewitt3

cv2.imshow("anh prewitt1", img_prewitt1)
cv2.imshow("anh prewitt2", img_prewitt2)
cv2.imshow("anh prewitt3", img_prewitt3)
cv2.imshow("anh prewitt", img_prewitt)
cv2.imshow("anh goc", ims)

cv2.waitKey(0)
cv2.destroyAllWindows()
