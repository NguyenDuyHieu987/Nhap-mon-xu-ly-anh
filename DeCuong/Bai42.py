import matplotlib.pyplot as plt
import cv2
import numpy as np

img = cv2.imread("Images\\d391fa5e837959270068.jpg")
ims = cv2.resize(img, [640, 480])

img_hsv = cv2.cvtColor(ims, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(img_hsv)

c = 255 / np.log(1 + np.max(v))
img_log = c * (np.log(v + 1))
img_log = np.array(img_log, dtype=np.uint8)

img_hsv = cv2.merge([h, s, img_log])
img_rgb = cv2.cvtColor(img_hsv, cv2.COLOR_HSV2RGB)

cv2.imshow("anh bien doi log", img_log)
cv2.imshow("img hsv", img_hsv)
cv2.imshow("img rgb", img_rgb)


cv2.waitKey(0)
cv2.destroyAllWindows()
