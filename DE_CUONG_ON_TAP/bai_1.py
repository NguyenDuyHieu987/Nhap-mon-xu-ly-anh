
# 1 Cân bằng histogram của kênh S của ảnh Ihsv

import matplotlib.pyplot as plt
import cv2
import numpy as np

img = cv2.imread("C:\\Users\\DELL\\Pictures\\XuLyAnh\\anh1.jpg", 1)
# img = cv2.resize(img, (640, 480))
cv2.imshow("anh goc", img)

Ihsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow("anh hsv", Ihsv)

h, s, v = cv2.split(Ihsv)
cv2.imshow("anh S", s)

img_equalization = cv2.equalizeHist(s)
cv2.imshow("anh can bang histogram kenh S", img_equalization)


cv2.waitKey(0)
cv2.destroyAllWindows()

