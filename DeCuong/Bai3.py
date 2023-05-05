import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("Images/628548.jpg")
ims = cv2.resize(img, [640, 480])

b, g, r = cv2.split(ims)
h, w, k = ims.shape
cv2.imshow("anh truoc b", b)
cv2.imshow("anh truoc g", g)
cv2.imshow("anh truoc r", r)

Igray = np.zeros((h, w), dtype="uint8")

Igray[:, :] = 0.39 * r + 0.5 * g + 0.11 * b

cv2.imshow("Igray", Igray)

cv2.waitKey(0)
cv2.destroyAllWindows()
