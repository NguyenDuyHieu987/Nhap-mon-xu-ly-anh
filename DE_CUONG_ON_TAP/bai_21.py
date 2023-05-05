
# 21 Hiệu chỉnh lại ảnh I với size mới là độ cao 256, độ rộng 256 được ảnh mới

import cv2
import numpy as np

I = cv2.imread("C:\\Users\\DELL\\Pictures\\XuLyAnh\\anh1.jpg")
cv2.imshow("anh goc", I)

h_new = 256
w_new = 256

I_new = cv2.resize(I, (w_new, h_new))
cv2.imshow("anh moi", I_new)


cv2.waitKey(0)
cv2.destroyAllWindows()
