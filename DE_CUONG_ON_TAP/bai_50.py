
# 50 Xác định đường contour có chu vi lớn nhất của ảnh Ib. Vẽ đường contour trên ảnh gốc I.


import cv2
import numpy as np

I = cv2.imread("C:\\Users\\DELL\\Pictures\\XuLyAnh\\anh5.jpg", 1)
# I = cv2.resize(I, (640, 480))
cv2.imshow("anh goc", I)
I_copy = I.copy()
I_copy_2 = I.copy()
I_copy_3 = I.copy()

Ig = cv2.cvtColor(I, cv2.COLOR_BGR2GRAY)
cv2.imshow("anh xam", Ig)

ret, Ib = cv2.threshold(Ig, 90, 255, cv2.THRESH_OTSU)
cv2.imshow("anh nhi phan theo otsu", Ib)

contours, hierarchy = cv2.findContours(Ib, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Vẽ contour tìm đc lên hình gốc
cv2.drawContours(I_copy, contours, -1, (0, 255, 255), 3)


length_cnt = [cv2.arcLength(cnt,True) for cnt in contours]
# print(length_cnt)
# max = length_cnt[0]
max_index = np.argmax(length_cnt)
cv2.drawContours(I_copy_2, contours[max_index], -1, (0, 255, 255), 3)

# for i in range(len(length_cnt)):
#     if max < length_cnt[i]:
#         max = length_cnt[i]

# print(max)

# for contour in contours:
#     if cv2.arcLength(contour, True) > (max /(1.2)):
#         cv2.drawContours(I_copy_3, [contour], -1, (0, 255, 255), 3)



# # Tìm contour có chu vi lớn nhất
# areas = [cv2.arcLength(c, True) for c in contours]
# # print(areas)
# max_area = np.argmax(areas)
# # print(f"vi tri contour co chu vi lon nhat: {max_area}")
# cnt = contours[max_area]
# # print(f"gia tri contour co chu vi lon nhat: {areas[max_area]}")
# cv2.drawContours(I_copy_2, cnt, -1, (0, 0, 255), 3)

# # print(areas[max_area]/1.2)

# # for c in contours:
# #     area = cv2.arcLength(c, True)
# #     if area > areas[max_area]/3.0:
# #         # print(areas.index(area))
# #         cv2.drawContours(I_copy_3, contours[areas.index(area)], -1, (255, 0, 0), 3)


cv2.imshow("anh contours", I_copy)
cv2.imshow("anh contours lon nhat", I_copy_2)
# cv2.imshow("anh contours co CV > CVLN/3", I_copy_3)

cv2.waitKey(0)
cv2.destroyAllWindows()