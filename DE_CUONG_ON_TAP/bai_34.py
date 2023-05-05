
# 34 Nhị phân ảnh Ig theo ngưỡng Otsu được ảnh nhị phân nền đen Ib.
# Xác định các đường contour của ảnh Ib gần tương tự với đường tròn. Vẽ các đường contour trên lên ảnh gốc I.

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

area_cnt = [cv2.contourArea(c) for c in contours]
max = area_cnt[0]
for i in range(len(area_cnt)):
    if max < area_cnt[i]:
        max = area_cnt[i]

for contour in contours:
    if cv2.contourArea(contour) > (max /(5)):
        cv2.drawContours(I_copy, [contour], -1, (0, 255, 255), 3)


# # Vẽ contour tìm đc lên hình gốc
# cv2.drawContours(I_copy, contours, -1, (0, 255, 255), 3)

cv2.imshow("anh contours", I_copy)


cv2.waitKey(0)
cv2.destroyAllWindows()
