
# 22 Kiểm tra pixel có tọa độ dòng y=100, cột x=300 có là điểm biên của ảnh Ig theo phép dò biên Canny không?

import cv2
import numpy as np

img = cv2.imread("C:\\Users\\DELL\\Pictures\\XuLyAnh\\anh1.jpg")
cv2.imshow("anh goc", img)

# Cài đặt giá trị cho bộ lọc canny
t_lower = 100  # Mức ngưỡng dưới
t_upper = 200  # Mức ngưỡng trên


# Cho qua bộ lọc Canny để lấy biên theo ngưỡng
Icanny = cv2.Canny(img, t_lower, t_upper, L2gradient=True)
cv2.imshow("Canny", Icanny)

y = 100
x = 300

if Icanny[y,x] == 1:
    print("co la diem bien")
else:
    print("ko la diem bien")


# print(Icanny[y-2:y+3,x-2:x+3])

cv2.waitKey(0)
cv2.destroyAllWindows()
