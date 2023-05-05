
# 27 Hiển thị các giá trị mức xám trong lân cận 5x5 của điểm ảnh có tọa độ dòng y=9, cột x=11.

import cv2
import numpy as np

Ig = cv2.imread("C:\\Users\\DELL\\Pictures\\XuLyAnh\\anh1.jpg",0)
# I=cv2.resize(I, (400, 200))
cv2.imshow("anh goc", Ig)

y = 9
x = 11

print(Ig[y-2:y+3,x-2:x+3])


cv2.waitKey(0)
cv2.destroyAllWindows()
