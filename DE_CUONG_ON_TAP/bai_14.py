
# 14 Hiển thị ảnh I và giá trị tỉ lệ giữa độ cao và độ rộng của ảnh.

import cv2
import numpy as np

I = cv2.imread("C:\\Users\\DELL\\Pictures\\XuLyAnh\\anh1.jpg")
# I=cv2.resize(I, (400, 200))
cv2.imshow("anh goc", I)

ti_le = I.shape[0]/I.shape[1]
print(ti_le)

cv2.waitKey(0)
cv2.destroyAllWindows()