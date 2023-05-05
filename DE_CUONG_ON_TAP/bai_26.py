
# 26 Làm trơn ảnh kênh S của Ihsv theo bộ lọc median, kích thước cửa sổ lân cận là 5x5 được ảnh Is. Hiển thị ảnh Is.

import cv2
import numpy as np

Ig = cv2.imread("C:\\Users\\DELL\\Pictures\\XuLyAnh\\anhnhieu3.jpg", 1)
Ig = cv2.resize(Ig, (300, 250))
cv2.imshow("anh goc", Ig)

Ihsv = cv2.cvtColor(Ig, cv2.COLOR_BGR2HSV)
cv2.imshow("anh hsv", Ihsv)

h, s, v = cv2.split(Ihsv)
cv2.imshow("anh s", s)


kerner = 5  # cửa sổ 5x5
s_new = cv2.medianBlur(s, kerner)
cv2.imshow("anh s loc median 5x5", s_new)

Ihsv_new = cv2.merge([h, s_new, v])
cv2.imshow("anh hsv moi", Ihsv_new)

Is = cv2.cvtColor(Ihsv_new, cv2.COLOR_HSV2BGR)
cv2.imshow("anh final", Is)

cv2.waitKey(0)
cv2.destroyAllWindows()
