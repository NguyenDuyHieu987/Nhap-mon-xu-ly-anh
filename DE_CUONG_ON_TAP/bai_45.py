
# 45 Xác định biên theo phương pháp Canny của kênh V của ảnh Ihsv được ảnh nhị phân Ivb.

import cv2
import numpy as np

I = cv2.imread("C:\\Users\\DELL\\Pictures\\XuLyAnh\\anh3.jpg", 1)

# I = cv2.resize(I, (640, 480))
cv2.imshow("anh goc", I)

Ihsv = cv2.cvtColor(I, cv2.COLOR_BGR2HSV)
cv2.imshow("anh hsv", Ihsv)

h,s,v = cv2.split(Ihsv)
cv2.imshow("anh V", v)

# Cài đặt giá trị cho bộ lọc canny
t_lower = 50  # Mức ngưỡng dưới
t_upper = 150  # Mức ngưỡng trên

# Cho qua bộ lọc Canny để lấy biên theo ngưỡng
Ivb = cv2.Canny(v, t_lower, t_upper, L2gradient=True)
cv2.imshow("Canny", Ivb)


if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()