import matplotlib.pyplot as plt
import cv2
import numpy as np

img = cv2.imread("Images\\628548.jpg")
ims = cv2.resize(img, [640, 480])

img_hsv = cv2.cvtColor(ims, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(img_hsv)

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

cv2.imshow("v chanel", v_new)

img_hsv = cv2.merge([h, s, v_new])
cv2.imshow("img hsv", img_hsv)

img_rgb = cv2.cvtColor(img_hsv, cv2.COLOR_HSV2BGR)
cv2.imshow("img rgb", img_rgb)


cv2.waitKey(0)
cv2.destroyAllWindows()
