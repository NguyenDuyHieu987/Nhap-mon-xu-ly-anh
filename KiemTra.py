import cv2
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread("Images/628548.jpg")
ims = cv2.resize(img, (640, 480))

# Câu 1=======================

b, g, r = cv2.split(ims)
iGRAY = np.zeros((480, 640), dtype="uint8")
iGRAY[:, :] = r * 0.28 + g * 0.45 + b * 0.13

c, e, gamma = 4, 0, 7
img_exp = c * (255 * (iGRAY / 255 + e) ** gamma)
img_exp = np.array(img_exp, dtype=np.uint8)
# c = (
#     (np.max(img_exp.ravel()) - np.min(img_exp.ravel()))
#     / (np.max(img_exp.ravel()) + np.min(img_exp.ravel()))
#     * 255
# )
print(np.max(img_exp.ravel()))
cv2.imshow("anh bien doi mu", img_exp)


# cv2.imshow("img gray", iGRAY)

# Câu 2==================

# img_hsv = cv2.cvtColor(ims, cv2.COLOR_BGR2HSV)
# h, s, v = cv2.split(img_hsv)
# hist1 = cv2.calcHist([h], [0], None, [256], [0, 256])
# plt.plot(hist1, color="r")
# hist2 = cv2.calcHist([s], [0], None, [256], [0, 256])
# plt.plot(hist2, color="g")
# hist3 = cv2.calcHist([v], [0], None, [256], [0, 256])
# plt.plot(hist3, color="b")
# plt.show()

# iHSV_s_equalhist = cv2.equalizeHist(s)
# cv2.imshow("img equalizeHist s chanel", iHSV_s_equalhist)

# Câu 3====================

# ims2 = cv2.resize(img, (320, 240))
# img_hsv = cv2.cvtColor(ims2, cv2.COLOR_BGR2HSV)
# h, s, v = cv2.split(img_hsv)
# cv2.imshow("img s chanel", s)

# # a)
# ims2_gray = s[48:52, 68:72]
# print(ims2_gray)

# # b)
# ims2_gray = s[26:74, 46:94]
# print(ims2_gray)
# cv2.imshow("img 50x70", ims2_gray)
# ims2_gray_equalhist = cv2.equalizeHist(ims2_gray)
# cv2.imshow("img 50x70 equalizeHist", ims2_gray_equalhist)

# Câu 4====================

# img_s_loc = cv2.blur(ims, (5, 5))
# cv2.imshow("img loc trung binh", img_s_loc)


cv2.waitKey(0)
cv2.destroyAllWindows()
