
# 19 Hiển thị tỷ lệ giữa giá trị độ cao và độ rộng của ảnh I.

import cv2
import numpy as np

I = cv2.imread("C:\\Users\\DELL\\Pictures\\XuLyAnh\\anh1.jpg")
# I=cv2.resize(I, (400, 200))
cv2.imshow("anh goc", I)

ti_le = I.shape[0]/I.shape[1]
print(ti_le)

cv2.waitKey(0)
cv2.destroyAllWindows()