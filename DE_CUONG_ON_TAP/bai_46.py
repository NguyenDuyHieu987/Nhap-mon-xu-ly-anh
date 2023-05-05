
# 46 Xác định các contour của ảnh Im và vẽ vị trí các contour lên ảnh gốc I ban đầu.


import cv2
import numpy as np

I = cv2.imread("C:\\Users\\DELL\\Pictures\\XuLyAnh\\anh5.jpg", 1)
# I = cv2.resize(I, (640, 480))
cv2.imshow("anh goc", I)
I_copy = I.copy()

Ig = cv2.cvtColor(I, cv2.COLOR_BGR2GRAY)
cv2.imshow("anh xam", Ig)

ret, Ib = cv2.threshold(Ig, 90, 255, cv2.THRESH_OTSU)
cv2.imshow("anh nhi phan theo otsu", Ib)

contours, hierarchy = cv2.findContours(Ib, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Vẽ contour tìm đc lên hình gốc
cv2.drawContours(I_copy, contours, -1, (0, 255, 255), 3)

cv2.imshow("anh contours", I_copy)

cv2.waitKey(0)
cv2.destroyAllWindows()