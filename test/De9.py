import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("Images/628548.jpg")

ims = cv2.resize(img, (640, 480))
ims_copy = ims.copy()

img_hsv = cv2.cvtColor(ims, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(img_hsv)
cv2.imshow("s chanel", s)
print(v.max())


img_blur = cv2.blur(v, (3, 3))
cv2.imshow("img_blur", img_blur)

img_equalizeHist = cv2.equalizeHist(v)
img_hsv1 = cv2.merge([h, s, img_equalizeHist])
img_rgb = cv2.cvtColor(img_hsv1, cv2.COLOR_HSV2RGB)
cv2.imshow("img_rgb", img_rgb)

hist = cv2.calcHist(img_rgb, [0], None, [256], [0, 256])

plt.plot(hist, color="r")
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
