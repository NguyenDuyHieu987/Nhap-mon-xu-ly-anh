
# 20 Hiệu chỉnh lại ảnh I với size mới là độ cao 256, ảnh giữ nguyên tỷ lệ so với ảnh gốc, được ảnh mới . 

import cv2
import numpy as np

I = cv2.imread("C:\\Users\\DELL\\Pictures\\XuLyAnh\\anh1.jpg")
# I=cv2.resize(I, (400, 200))
cv2.imshow("anh goc", I)

h_new = 124

print(I.shape[0])
ti_le = h_new/I.shape[0]
print(ti_le)
w = int(I.shape[1] * ti_le)
print(w)

I_new = cv2.resize(I, (w, h_new))
cv2.imshow("anh moi", I_new)


cv2.waitKey(0)
cv2.destroyAllWindows()
