
# 16 Hiển thị kênh B của ảnh I. 

import cv2
import numpy as np

I = cv2.imread("C:\\Users\\DELL\\Pictures\\XuLyAnh\\anh1.jpg", 1)
# I=cv2.resize(I, (400, 200))
cv2.imshow("anh goc", I)

b,g,r = cv2.split(I)
cv2.imshow("anh kenh B", b)

cv2.waitKey(0)
cv2.destroyAllWindows()
