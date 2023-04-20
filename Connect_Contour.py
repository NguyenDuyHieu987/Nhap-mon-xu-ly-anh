import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("Images/628548.jpg")
ims = cv2.resize(img, [640, 480])

img_gray = cv2.cvtColor(ims, cv2.COLOR_BGR2GRAY)

t_lower = 50
t_upper = 150

img_canny = cv2.Canny(img_gray, t_lower, t_upper, L2gradient=True)
cv2.imshow("Canny", img_canny)
cv2.imshow("anh goc", ims)

kernel = np.ones((5, 5), np.uint8)
kernel1 = np.ones((3, 3), dtype=np.uint8)
Iclosing = cv2.morphologyEx(img_canny, cv2.MORPH_CLOSE, kernel1)
cv2.imshow("img closing", Iclosing)

kernel2 = np.ones((2, 2), dtype=np.uint8)
Ierose = cv2.erode(img_canny, kernel2, iterations=1)
cv2.imshow("img erose", Ierose)

Idilate = cv2.dilate(img_canny, kernel, iterations=1)
cv2.imshow("img dilate", Idilate)

cv2.waitKey(0)
cv2.destroyAllWindows()
