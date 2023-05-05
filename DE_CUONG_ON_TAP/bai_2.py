
# 2 Chuyển ảnh Igray sang ảnh nhị phân Ib với ngưỡng Otsu

import cv2
import numpy as np

img = cv2.imread("C:\\Users\\DELL\\Pictures\\XuLyAnh\\anh1.jpg", 1)
# img = cv2.resize(img, (640, 480))
cv2.imshow("anh goc", img)

Igray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("anh xam", Igray)

ret, Ib = cv2.threshold(Igray, 0, 255, cv2.THRESH_OTSU)
cv2.imshow("anh nhi phan theo otsu", Ib)

cv2.waitKey(0)
cv2.destroyAllWindows()