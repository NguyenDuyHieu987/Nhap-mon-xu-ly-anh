import cv2
import numpy as np

img = cv2.imread("Images\\628548.jpg")
ims = cv2.resize(img, [640, 480])

img_hsv = cv2.cvtColor(ims, cv2.COLOR_RGB2HSV)

h, s, v = cv2.split(ims)
h_amban = 255 - h

img_merge = cv2.merge([h_amban, s, v])
img_rgb = cv2.cvtColor(ims, cv2.COLOR_HSV2RGB)

cv2.imshow("img", ims)
cv2.imshow("anh bien doi log", img_rgb)

cv2.waitKey(0)
cv2.destroyAllWindows()