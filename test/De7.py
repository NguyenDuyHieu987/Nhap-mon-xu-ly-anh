import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("Images/628548.jpg")

ims = cv2.resize(img, (640, 480))
ims_copy = ims.copy()

img_hsv = cv2.cvtColor(ims, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(img_hsv)
cv2.imshow("kenh s", s)
print("v mean:", v.mean())

img_blur = cv2.blur(s, (5, 5))
cv2.imshow("img_blur s", img_blur)

ret, Ib = cv2.threshold(img_blur, 0, 256, cv2.THRESH_OTSU)
cv2.imshow("img_blur threshold", Ib)

contours, hierarchy = cv2.findContours(Ib, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

perimeter = [cv2.arcLength(cnt, True) for cnt in contours]
max_perimeter = np.argmax(perimeter)
cv2.drawContours(ims_copy, contours[max_perimeter], -1, (0, 255, 255), 3)
cv2.imshow("max_perimeter", ims_copy)

v_new = np.zeros(v.shape, v.dtype)
# Giãn tuyến tính các giá trị mức xám kênh V
# Công thức: pixel = pixel*alpha + beta
alpha = 1  # tuong phan (contrast)
beta = 10  # do sang (brightness)

for y in range(v.shape[0]):
    for x in range(v.shape[1]):
        v_new[y, x] = np.clip(alpha * v[y, x] + beta, 0, 255)


new_img_gray = cv2.normalize(v, None, 0, 255, cv2.NORM_MINMAX)


img_hsv1 = cv2.merge([h, s, v_new])
img_rgb = cv2.cvtColor(img_hsv1, cv2.COLOR_HSV2RGB)

cv2.imshow("img_rgb", img_rgb)

cv2.waitKey(0)
cv2.destroyAllWindows()
