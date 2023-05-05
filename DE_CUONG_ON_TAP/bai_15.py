
# 15 Hiển thị các độ xám của của cửa sổ lân cận 5x5 của pixel có tọa độ dòng y=109, cột x=130 của ảnh Ig.

import cv2
import numpy as np

I = cv2.imread("C:\\Users\\DELL\\Pictures\\XuLyAnh\\anh1.jpg", 1)
# I=cv2.resize(I, (400, 200))
cv2.imshow("anh goc", I)
Ig = cv2.cvtColor(I, cv2.COLOR_BGR2GRAY)
cv2.imshow("anh xam", Ig)

y = 109
x = 130

print(Ig[y-2:y+3,x-2:x+3])

cv2.waitKey(0)
cv2.destroyAllWindows()