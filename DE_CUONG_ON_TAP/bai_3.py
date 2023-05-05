
# 3 Chuyển ảnh mầu Img sang ảnh đa cấp xám (grayscale) theo công thức xác định mức độ xám
# từ tổ hợp các thành phần mầu (r, g, b) theo tỷ lệ (0.39, 0.5, 0.11), được ma trận ảnh Ig. Hiển thị ảnh Ig.

import cv2
import numpy as np

Img = cv2.imread("C:\\Users\\DELL\\Pictures\\XuLyAnh\\anh1.jpg", 1)
cv2.imshow("anh goc", Img)

h,w,k = Img.shape
Ig = np.zeros((h, w), dtype='uint8')
b,g,r = cv2.split(Img)
Ig[:, :] = 0.39 * r + 0.5 * g + 0.11 * b

cv2.imshow("anh xam", Ig)

cv2.waitKey(0)
cv2.destroyAllWindows()