
# 25 Làm trơn ảnh kênh S của ảnh theo bộ lọc trung bình cộng với lân cận cửa sổ kích thước 5x5 thu được ảnh Im. Hiển thị ảnh kết quả Im.

import cv2
import numpy as np

Ig = cv2.imread("C:\\Users\\DELL\\Pictures\\XuLyAnh\\anhnhieu3.jpg", 1)
Ig = cv2.resize(Ig, (300, 250))
cv2.imshow("anh goc", Ig)

Ig_hsv = cv2.cvtColor(Ig, cv2.COLOR_BGR2HSV)
cv2.imshow("anh hsv", Ig_hsv)

h, s, v = cv2.split(Ig_hsv)
cv2.imshow("anh s", s)


kerner = (5,5)
s_new = cv2.blur(s, kerner)
cv2.imshow("anh s loc trung binh 5x5", s_new)

Ig_hsv_new = cv2.merge([h, s_new, v])
cv2.imshow("anh hsv moi", Ig_hsv_new)

Im = cv2.cvtColor(Ig_hsv_new, cv2.COLOR_HSV2BGR)
cv2.imshow("anh final", Im)

cv2.waitKey(0)
cv2.destroyAllWindows()
