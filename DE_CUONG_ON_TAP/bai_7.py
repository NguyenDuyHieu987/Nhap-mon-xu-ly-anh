
# 7 Chuyển ảnh mầu I sang ảnh HSV. Hiển thị kênh S.
# Hiển thị các giá trị điểm ảnh trong cửa sổ lân cận 5x5 của điểm ảnh với tọa độ dòng y=10, cột x=20.

import cv2
import numpy as np

I = cv2.imread("C:\\Users\\DELL\\Pictures\\XuLyAnh\\anh1.jpg", 1)
# I=cv2.resize(I, (400, 200))
cv2.imshow("anh goc", I)

Ihsv = cv2.cvtColor(I, cv2.COLOR_BGR2HSV)
cv2.imshow("anh hsv", Ihsv)

h,s,v = cv2.split(Ihsv)
cv2.imshow("anh kenh S", s)

y = 10
x = 20

print(s[y-2:y+3,x-2:x+3])


cv2.waitKey(0)
cv2.destroyAllWindows()