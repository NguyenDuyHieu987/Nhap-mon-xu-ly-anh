
# 52 Xác định đường contour có tỉ lệ giữa chu vi và diện tích là lớn nhất của ảnh Ib. 
# Vẽ đường contour trên ảnh gốc I . Hiển thị ảnh


import cv2
import numpy as np

I = cv2.imread("C:\\Users\\DELL\\Pictures\\XuLyAnh\\anh3.jpg", 1)
# I = cv2.resize(I, (640, 480))
# cv2.imshow("anh goc", I)
I_copy = I.copy()
I_copy_2 = I.copy()
I_copy_3 = I.copy()

Ig = cv2.cvtColor(I, cv2.COLOR_BGR2GRAY)
# cv2.imshow("anh xam", Ig)

ret, Ib = cv2.threshold(Ig, 90, 255, cv2.THRESH_OTSU)
# cv2.imshow("anh nhi phan theo otsu", Ib)

contours, hierarchy = cv2.findContours(Ib, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Vẽ contour tìm đc lên hình gốc
cv2.drawContours(I_copy, contours, -1, (0, 255, 255), 3)


area_cnt = [cv2.contourArea(cnt) for cnt in contours]
length_cnt = [cv2.arcLength(cnt,True) for cnt in contours]
# ti_le_cnt = [length_cnt[i]/area_cnt[i] for i in range(len(area_cnt))]
ti_le_cnt = []
for i in range(len(area_cnt)):
    if area_cnt[i] > 0:
        ti_le_cnt.append(length_cnt[i] * length_cnt[i] / area_cnt[i])
    else:
        ti_le_cnt.append(0)

# print(area_cnt)
# print(length_cnt)
# print(ti_le_cnt)

max_DT_index = np.argmax(area_cnt)
max_CV_index = np.argmax(length_cnt)
max_ti_le_index = np.argmax(ti_le_cnt)

# print(max_DT_index)
# print(max_CV_index)
# print(max_ti_le_index)


cv2.drawContours(I_copy_2, contours[max_ti_le_index], -1, (0, 255, 255), 3)

max_DT = area_cnt[0]
max_CV = length_cnt[0]
max_ti_le = ti_le_cnt[0]

# for i in range(len(area_cnt)):
#     if max_DT < area_cnt[i]:
#         max_DT = area_cnt[i]

# for i in range(len(length_cnt)):
#     if max_CV < length_cnt[i]:
#         max_CV = length_cnt[i]

# for i in range(len(ti_le_cnt)):
#     if max_ti_le < ti_le_cnt[i]:
#         max_ti_le = ti_le_cnt[i]


# for contour in contours:
#     if cv2.contourArea(contour) > (max_ti_le /(1.1)):
#         cv2.drawContours(I_copy_3, [contour], -1, (0, 255, 255), 3)


cv2.imshow("anh contours", I_copy)
cv2.imshow("anh contours lon nhat", I_copy_2)
# cv2.imshow("anh contours co ti_le > ti_le/3", I_copy_3)

cv2.waitKey(0)
cv2.destroyAllWindows()