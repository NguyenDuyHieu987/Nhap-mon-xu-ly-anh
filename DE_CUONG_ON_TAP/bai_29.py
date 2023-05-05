
# 29 Làm trơn kênh S của ảnh Ihsv với bộ lọc median kích thước cửa sổ 3x3
# Biến đổi ngược ảnh Ihsv về biểu diễn mầu RGB được ảnh I. Hiển thị ảnh I3.

import cv2
import numpy as np

Ig = cv2.imread("C:\\Users\\DELL\\Pictures\\XuLyAnh\\anhnhieu3.jpg", 1)
Ig = cv2.resize(Ig, (300, 250))
cv2.imshow("anh goc", Ig)

Ihsv = cv2.cvtColor(Ig, cv2.COLOR_BGR2HSV)
cv2.imshow("anh hsv", Ihsv)

h, s, v = cv2.split(Ihsv)
cv2.imshow("anh s", s)

kerner = 3  # cửa sổ 3x3
s_new = cv2.medianBlur(s, kerner)
cv2.imshow("anh s loc median 3x3", s_new)

Ihsv_new = cv2.merge([h, s_new, v])
cv2.imshow("anh hsv moi", Ihsv_new)

I = cv2.cvtColor(Ihsv_new, cv2.COLOR_HSV2BGR)
cv2.imshow("anh final", I)

cv2.waitKey(0)
cv2.destroyAllWindows()