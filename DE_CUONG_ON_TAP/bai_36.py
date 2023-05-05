
# 36 Nhị phân ảnh Ig theo ngưỡng Otsu được ảnh nhị phân nền đen Ib.
# Xác đường contour của ảnh Ib có diện tích lớn nhất. Vẽ đường contour tìm được trên lên ảnh gốc I.

import cv2
import numpy as np

I = cv2.imread("C:\\Users\\DELL\\Pictures\\XuLyAnh\\anh3.jpg", 1)
# I = cv2.resize(I, (640, 480))
cv2.imshow("anh goc", I)
I_copy = I.copy()
I_copy_2 = I.copy()

Ig = cv2.cvtColor(I, cv2.COLOR_BGR2GRAY)
cv2.imshow("anh xam", Ig)

ret, Ib = cv2.threshold(Ig, 90, 255, cv2.THRESH_OTSU)
cv2.imshow("anh nhi phan theo otsu", Ib)

contours, hierarchy = cv2.findContours(Ib, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Vẽ contour tìm đc lên hình gốc
cv2.drawContours(I_copy, contours, -1, (0, 255, 255), 3)


# Tìm contour có diện tích lớn nhất
areas_DT = [cv2.contourArea(c) for c in contours]
max_DT = np.argmax(areas_DT)
cnt_DT = contours[max_DT]
cv2.drawContours(I_copy_2, cnt_DT, -1, (0, 0, 255), 3)

# # Vẽ hình bao quanh contours lớn nhất
# x, y, w, h = cv2.boundingRect(cnt_DT)
# cv2.rectangle(I_copy_2, (x, y), (x+w, y+h), (0, 0, 255), 2)


cv2.imshow("anh contours", I_copy)
cv2.imshow("anh contours lon nhat", I_copy_2)

cv2.waitKey(0)
cv2.destroyAllWindows()