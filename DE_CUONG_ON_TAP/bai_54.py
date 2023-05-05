
# 54 Xác định ma trận gradient theo hướng x của Ig sử dụng toán tử Sobel và hiển thị ma trận kết quả.

import cv2
import numpy as np

Ig = cv2.imread("C:\\Users\\DELL\\Pictures\\XuLyAnh\\anh1.jpg", 0)
cv2.imshow("anh goc", Ig)

# kernelx = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, -1]])
# kernely = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])

# img_sobelx = cv2.filter2D(Ig, -1, kernelx)
# img_sobely = cv2.filter2D(Ig, -1, kernely)
# img_sobelxy = img_sobelx + img_sobely

# cv2.imshow("sobel X", img_sobelx)
# cv2.imshow("sobel Y", img_sobely)
# cv2.imshow("sobel X + Y", img_sobelxy)


img_x = cv2.Sobel(Ig, cv2.CV_64F, 1, 0, ksize=5)  # theo X
# img_y = cv2.Sobel(Ig, cv2.CV_64F, 0, 1, ksize=5)  # theo Y
# img_xy = cv2.Sobel(Ig, cv2.CV_64F, 1, 1, ksize=5)  # theo XY

print(img_x)
# print(img_y)
# print(img_xy)

cv2.imshow("sobel X", img_x)
# cv2.imshow("sobel Y", img_y)
# cv2.imshow("sobel X + Y", img_xy)


cv2.waitKey(0)
cv2.destroyAllWindows()
