import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("Images/a9f2c3f3c1911dcf4480.jpg")
ims = cv2.resize(img, [640, 480])


# (h, w) = ims.shape[:2]
# (cX, cY) = (w // 2, h // 2)
# # rotate our image by 45 degrees around the center of the image
# M = cv2.getRotationMatrix2D((cX, cY), 45, 1.0)
# rotated = cv2.warpAffine(img, M, (w, h))

import imutils

rotated = imutils.rotate(img, 45)
cv2.imshow("Rotated by 45 Degrees", rotated)


cv2.waitKey(0)
cv2.destroyAllWindows()
