
# 44 Tăng độ sáng của kênh V của ảnh Ihsv bằng phương pháp giãn tuyến tính giá trị mức xám. 
# Biến đổi ngược ảnh Ihsv về biểu diễn mầu RGB được ảnh I. Hiển thị lại ảnh I.


import cv2
import numpy as np

I = cv2.imread("C:\\Users\\DELL\\Pictures\\XuLyAnh\\anh3.jpg", 1)

# I = cv2.resize(I, (640, 480))
cv2.imshow("anh goc", I)

Ihsv = cv2.cvtColor(I, cv2.COLOR_BGR2HSV)
cv2.imshow("anh hsv", Ihsv)

h,s,v = cv2.split(Ihsv)
cv2.imshow("anh V", v)


v_new = np.zeros(v.shape, v.dtype)
# Giãn tuyến tính các giá trị mức xám kênh V
# Công thức: pixel = pixel*alpha + beta
alpha = 1.3     # tuong phan (contrast)
beta = 50       # do sang (brightness)

# for y in range(v.shape[0]):
#     for x in range(v.shape[1]):
#         v_new[y, x] = np.clip(alpha*v[y, x] + beta, 0, 255)

for y in range(v.shape[0]):
    for x in range(v.shape[1]):
        if (alpha*v[y, x] + beta) > 255:
            v_new[y, x] = 255
        elif (alpha*v[y, x] + beta) < 0:
            v_new[y, x] = 0
        else:
            v_new[y, x] = (alpha*v[y, x] + beta)

cv2.imshow("anh V tuyen tinh cac gia tri muc xam", v_new)

Ihsv_new = cv2.merge([h, s, v_new])
cv2.imshow("anh hsv tuyen tinh cac gia tri muc xam kenh V", Ihsv_new)

I_new = cv2.cvtColor(Ihsv_new, cv2.COLOR_HSV2BGR)
cv2.imshow("anh final", I_new)


cv2.waitKey(0)
cv2.destroyAllWindows()