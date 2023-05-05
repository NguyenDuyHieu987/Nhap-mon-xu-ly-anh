
# 42 Tăng độ sáng của kênh V của ảnh Ihsv bằng phương pháp giãn mức xám. 
# Biến đổi ngược ảnh Ihsv về biểu diễn mầu RGB được ảnh I mới.


import cv2
import numpy as np

I = cv2.imread("C:\\Users\\DELL\\Pictures\\XuLyAnh\\anh3.jpg", 1)

# I = cv2.resize(I, (640, 480))
cv2.imshow("anh goc", I)

Ihsv = cv2.cvtColor(I, cv2.COLOR_BGR2HSV)
cv2.imshow("anh hsv", Ihsv)

h,s,v = cv2.split(Ihsv)
cv2.imshow("anh V", v)

# Giãn mức xám kênh V (biến đổi log)
c = 255/np.log(1 + np.max(v))
v_new = c*(np.log(v + 1))
v_new = np.array(v_new, dtype=np.uint8)
cv2.imshow("anh V gian muc xam", v_new)

Ihsv_new = cv2.merge([h, s, v_new])
cv2.imshow("anh hsv gian muc xam kenh V", Ihsv_new)

I_new = cv2.cvtColor(Ihsv_new, cv2.COLOR_HSV2BGR)
cv2.imshow("anh final", I_new)


cv2.waitKey(0)
cv2.destroyAllWindows()