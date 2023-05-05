
# 30 Lấy biên của ảnh Ig theo phương pháp Canny được ảnh biên Ie là ảnh nhị phân nền đen. Hiển thị ảnh Ie.
# Kiểm tra các điểm ảnh của pixel có tọa độ dòng y=109, cột x=130 có phải là điểm biên của Ig theo phương pháp dò biên Canny

import cv2
import numpy as np

img = cv2.imread("C:\\Users\\DELL\\Pictures\\XuLyAnh\\anh1.jpg")
cv2.imshow("anh goc", img)

# Cài đặt giá trị cho bộ lọc canny
t_lower = 100  # Mức ngưỡng dưới
t_upper = 200  # Mức ngưỡng trên


# Cho qua bộ lọc Canny để lấy biên theo ngưỡng
Ie = cv2.Canny(img, t_lower, t_upper, L2gradient=True)
cv2.imshow("Canny", Ie)

y = 109
x = 130

if Ie[y,x] > 0:
    print("co la diem bien")
else:
    print("ko la diem bien")

# print(Ie[y-2:y+3,x-2:x+3])

cv2.waitKey(0)
cv2.destroyAllWindows()
