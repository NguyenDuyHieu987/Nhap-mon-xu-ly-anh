import matplotlib.pyplot as plt
import cv2
import numpy as np

img = cv2.imread("Images\\628548.jpg")
ims = cv2.resize(img, [640, 480])

Ihsv = cv2.cvtColor(ims, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(Ihsv)

v_new = np.zeros(v.shape, v.dtype)
# Giãn tuyến tính các giá trị mức xám kênh V
# Công thức: pixel = pixel*alpha + beta
alpha = 1.3  # tuong phan (contrast)
beta = 50  # do sang (brightness)

# for y in range(v.shape[0]):
#     for x in range(v.shape[1]):
#         v_new[y, x] = np.clip(alpha*v[y, x] + beta, 0, 255)

for y in range(v.shape[0]):
    for x in range(v.shape[1]):
        if (alpha * v[y, x] + beta) > 255:
            v_new[y, x] = 255
        elif (alpha * v[y, x] + beta) < 0:
            v_new[y, x] = 0
        else:
            v_new[y, x] = alpha * v[y, x] + beta

cv2.imshow("anh V tuyen tinh cac gia tri muc xam", v_new)

Ihsv_new = cv2.merge([h, s, v_new])
cv2.imshow("anh hsv tuyen tinh cac gia tri muc xam kenh V", Ihsv_new)

I_new = cv2.cvtColor(Ihsv_new, cv2.COLOR_HSV2BGR)
cv2.imshow("anh final", I_new)


cv2.waitKey(0)
cv2.destroyAllWindows()
