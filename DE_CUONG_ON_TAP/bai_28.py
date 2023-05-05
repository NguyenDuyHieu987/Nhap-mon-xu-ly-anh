
# 28 Làm trơn ảnh kênh V của Ihsv theo bộ lọc trung bình cộng, Kích thước cửa sổ lân cận là 3x3 được ảnh Iv. Hiển thị ảnh Iv

import cv2
import numpy as np

Ig = cv2.imread("C:\\Users\\DELL\\Pictures\\XuLyAnh\\anhnhieu3.jpg", 1)
Ig = cv2.resize(Ig, (300, 250))
cv2.imshow("anh goc", Ig)

Ihsv = cv2.cvtColor(Ig, cv2.COLOR_BGR2HSV)
cv2.imshow("anh hsv", Ihsv)

h, s, v = cv2.split(Ihsv)
cv2.imshow("anh V", v)

kerner = (3,3)  # cửa sổ 3x3
v_new = cv2.blur(v, kerner)
cv2.imshow("anh v loc median 3x3", v_new)

Ihsv_new = cv2.merge([h, v_new, v])
cv2.imshow("anh hsv moi", Ihsv_new)

Iv = cv2.cvtColor(Ihsv_new, cv2.COLOR_HSV2BGR)
cv2.imshow("anh final", Iv)

cv2.waitKey(0)
cv2.destroyAllWindows()