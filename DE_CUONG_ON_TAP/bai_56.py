
# 56 Xác định và vẽ histogram của kênh S của ảnh Ihsv.


import matplotlib.pyplot as plt
import cv2
import numpy as np

I = cv2.imread("C:\\Users\\DELL\\Pictures\\XuLyAnh\\anh1.jpg", 1)
cv2.imshow("anh goc", I)

Ihsv = cv2.cvtColor(I, cv2.COLOR_BGR2HSV)
cv2.imshow("anh hsv", Ihsv)

h,s,v = cv2.split(Ihsv)
cv2.imshow("anh S", s)

hist_S = cv2.calcHist(s, [0], None, [256], [0,256])
plt.plot(hist_S, color='r')
plt.title("Histogram kenh S ")
plt.show()


if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
