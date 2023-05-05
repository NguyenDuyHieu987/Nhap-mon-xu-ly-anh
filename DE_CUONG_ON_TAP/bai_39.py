
# 39 Nhị phân hóa ảnh Is theo ngưỡng Otsu được ảnh nhị phân Ib. 
# Xác định đường contour có chu vi lớn nhất của ảnh Ib. Vẽ đường contour trên ảnh I.


import cv2
import numpy as np

I = cv2.imread("C:\\Users\\DELL\\Pictures\\XuLyAnh\\anh3.jpg", 1)

# I = cv2.resize(I, (640, 480))
cv2.imshow("anh goc", I)
I_copy = I.copy()
I_copy_2 = I.copy()
I_copy_3 = I.copy()

Ig = cv2.cvtColor(I, cv2.COLOR_BGR2GRAY)
cv2.imshow("anh xam", Ig)

ret, Ib = cv2.threshold(Ig, 0, 255, cv2.THRESH_OTSU)

# # Nghịch đảo ảnh nhị phân
# Ib = cv2.bitwise_not(Ib)

cv2.imshow("anh nhi phan theo otsu", Ib)

contours, hierarchy = cv2.findContours(Ib, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Vẽ contour tìm đc lên hình gốc
cv2.drawContours(I_copy, contours, -1, (255, 0, 0), 3)

# # Tìm contour có diện tích lớn nhất
# areas_DT = [cv2.contourArea(c) for c in contours]
# max_DT = np.argmax(areas_DT)
# cnt_DT = contours[max_DT]
# cv2.drawContours(I_copy_2, cnt_DT, -1, (255, 0, 0), 3)

# Tìm contour có chu vi lớn nhất
areas_CV = [cv2.arcLength(c, True) for c in contours]
max_CV = np.argmax(areas_CV)
cnt_CV = contours[max_CV]
cv = cv2.arcLength(cnt_CV, True)
cv2.drawContours(I_copy_3, cnt_CV, -1, (255, 0, 0), 3)


# cv2.putText(I_copy_2, f"Dien tich: {max_DT}",
#                 (150, 100), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 1.2, (0, 0, 255))

# cv2.putText(I_copy_3, f"Chu vi: {cv}",
#                 (150, 200), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 1.2, (0, 0, 255))



cv2.imshow("anh contours", I_copy)
# cv2.imshow("anh contours dien tich lon nhat", I_copy_2)
cv2.imshow("anh contours chu vi lon nhat", I_copy_3)

cv2.waitKey(0)
cv2.destroyAllWindows()