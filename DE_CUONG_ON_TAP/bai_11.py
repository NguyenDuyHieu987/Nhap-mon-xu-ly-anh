
# 11 Chuyển ảnh sang biểu diễn HSV được ma trận Ihsv. Hiển thị kênh V của Ihsv. 
# Xác định giá trị mức sáng lớn nhất và nhỏ nhất của kênh S của ảnh Ihsv

import cv2
import numpy as np

I = cv2.imread("C:\\Users\\DELL\\Pictures\\XuLyAnh\\anh1.jpg", 1)
# I=cv2.resize(I, (400, 200))
cv2.imshow("anh goc", I)

Ihsv = cv2.cvtColor(I, cv2.COLOR_BGR2HSV)
cv2.imshow("anh hsv", Ihsv)

h,s,v = cv2.split(Ihsv)
cv2.imshow("anh kenh V", v)

max = np.max(s)
min = np.min(s)
print("Gia tri muc sang lon nhat cua kenh S la:", max)
print("Gia tri muc sang nho nhat cua kenh S la:", min)

cv2.waitKey(0)
cv2.destroyAllWindows()