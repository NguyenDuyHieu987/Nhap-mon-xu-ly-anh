
# 23 Làm trơn ảnh Ig theo bộ lọc trung bình cộng với lân cận cửa sổ kích thước 5x5 thu được ảnh Im.


import cv2
import numpy as np
import matplotlib.pyplot as plt

Ig = cv2.imread("C:\\Users\\DELL\\Pictures\\XuLyAnh\\anhnhieu.jpg", 0)
cv2.imshow("anh goc", Ig)

kerner = (5,5)
Im = cv2.blur(Ig, kerner)
cv2.imshow("anh loc trung binh 5x5", Im)


cv2.waitKey(0)
cv2.destroyAllWindows()
