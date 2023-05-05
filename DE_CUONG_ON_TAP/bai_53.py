
# 53 Xác định giá trị mức xám nhỏ nhất, lớn nhất và trung bình của ảnh Ig. Hiển thị các giá trị này.

import cv2
import numpy as np

Ig = cv2.imread("C:\\Users\\DELL\\Pictures\\XuLyAnh\\anh1.jpg", 0)
cv2.imshow("anh goc", Ig)

max = np.max(Ig)
min = np.min(Ig)
mean = np.mean(Ig)
print("Muc xam lon nhat cua anh Ig la:", max)
print("Muc xam nho nhat cua anh Ig la:", min)
print("Muc xam trung binh cua anh Ig la:", mean)

cv2.waitKey(0)
cv2.destroyAllWindows()
