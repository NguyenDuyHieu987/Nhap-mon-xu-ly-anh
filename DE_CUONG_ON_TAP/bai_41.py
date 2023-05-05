
# 41 Tăng độ sáng của kênh V của ảnh Ihsv bằng phương pháp cân bằng histogram. 
# Biến đổi ngược ảnh Ihsv về biểu diễn mầu RGB được ảnh I.


import cv2
import numpy as np

I = cv2.imread("C:\\Users\\DELL\\Pictures\\XuLyAnh\\anh3.jpg", 1)

# I = cv2.resize(I, (640, 480))
cv2.imshow("anh goc", I)

Ihsv = cv2.cvtColor(I, cv2.COLOR_BGR2HSV)
cv2.imshow("anh hsv", Ihsv)

h,s,v = cv2.split(Ihsv)
cv2.imshow("anh V", v)

v_new = cv2.equalizeHist(v)
cv2.imshow("anh V can bang histogram", v_new)

Ihsv_new = cv2.merge([h, s, v_new])
cv2.imshow("anh hsv can bang histogram kenh V", Ihsv_new)

I_new = cv2.cvtColor(Ihsv_new, cv2.COLOR_HSV2BGR)
cv2.imshow("anh final", I_new)


cv2.waitKey(0)
cv2.destroyAllWindows()