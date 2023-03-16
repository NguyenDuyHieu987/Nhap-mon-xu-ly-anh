import matplotlib.pyplot as plt
import cv2
import numpy as np

img = cv2.imread(
    "Images\\628548.jpg",
)
ims = cv2.resize(img, [640, 480])

# bai 3
b, g, r = cv2.split(ims)
hist = cv2.calcHist([ims], [0], None, [256], [0, 256])
plt.plot(hist, color="r")
plt.title("Image Histogram")
# plt.show()

img_equalization_b = cv2.equalizeHist(b)
img_equalization_g = cv2.equalizeHist(g)
img_equalization_r = cv2.equalizeHist(r)

hist1 = cv2.calcHist([img_equalization_b], [0], None, [256], [0, 256])
hist2 = cv2.calcHist([img_equalization_g], [0], None, [256], [0, 256])
hist3 = cv2.calcHist([img_equalization_r], [0], None, [256], [0, 256])
plt.plot(hist1, color="r")
plt.plot(hist2, color="g")
plt.plot(hist3, color="b")
plt.title("Image Histogram Equalization")
plt.show()

# img_equalization_rgb = cv2.cvtColor(img_equalization, cv2.COLOR_GRAY2BGR)
img_merge_bgr = cv2.merge([img_equalization_b, img_equalization_g, img_equalization_r])
img_merge_gbr = cv2.merge([img_equalization_g, img_equalization_b, img_equalization_r])
img_merge_rgb = cv2.merge([img_equalization_r, img_equalization_g, img_equalization_b])
cv2.imshow("Anh img_merge_bgr", img_merge_bgr)
cv2.imshow("Anh img_merge_gbr", img_merge_gbr)
cv2.imshow("Anh img_merge_rgb", img_merge_rgb)

img_equalization_hsv = cv2.cvtColor(img_merge_rgb, cv2.COLOR_RGB2HSV)
h, s, v = cv2.split(img_equalization_hsv)
img_merge_hsv = cv2.merge([h, s, v])

cv2.imshow("Anh img_merge_hsv", img_merge_hsv)

# bai 1
# img_hsv = cv2.cvtColor(ims, cv2.COLOR_RGB2HSV)
# h, s, v = cv2.split(img_hsv)

# c = 255 / np.log(1 + np.max(v))
# v_log = c * (np.log(v + 1))
# v_log = np.array(v_log, dtype=np.uint8)

# img_merge_hsv = cv2.merge([h, s, v_log])

# img_merge_rgb = cv2.cvtColor(img_merge_hsv, cv2.COLOR_HSV2RGB)

# cv2.imshow("Anh img_merge_hsv", img_merge_rgb)


# bai 2


cv2.waitKey(0)
cv2.destroyAllWindows()
