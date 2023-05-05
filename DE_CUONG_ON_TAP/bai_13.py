
# 13 Chuyển kênh S của ảnh sang ảnh nhị phân Ib với ngưỡng Otsu. Hiển thị ảnh nhị phân Ib. Hiển thị ảnh I

import cv2
import numpy as np

I = cv2.imread("C:\\Users\\DELL\\Pictures\\XuLyAnh\\anh1.jpg", 1)
# I=cv2.resize(I, (400, 200))
cv2.imshow("anh goc", I)

Ihsv = cv2.cvtColor(I, cv2.COLOR_BGR2HSV)
cv2.imshow("anh hsv", Ihsv)

h,s,v = cv2.split(Ihsv)
cv2.imshow("anh kenh S", s)
# cv2.imshow("anh kenh S khong dung split", Ihsv[:,:,1])

ret, Ib = cv2.threshold(s, 0, 255, cv2.THRESH_OTSU)
cv2.imshow("anh s nhi phan theo otsu", Ib)

Ihsv_new = cv2.merge([h, Ib, v])
cv2.imshow("anh hsv moi", Ihsv_new)

I_new = cv2.cvtColor(Ihsv_new, cv2.COLOR_HSV2BGR)
cv2.imshow("anh final", I_new)

cv2.waitKey(0)
cv2.destroyAllWindows()