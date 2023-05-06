import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("Images/628548.jpg")

ims = cv2.resize(img, (640, 480))
ims_copy = ims.copy()

b, g, r = cv2.split(ims)
h, w, k = ims.shape
Igray = np.zeros((h, w), dtype="uint8")

Igray[:, :] = r * 0.39 + g * 0.5 + b * 0.11
print(Igray)
cv2.imshow("Igray", Igray)

ret, Ib = cv2.threshold(Igray, 0, 255, cv2.THRESH_OTSU)
print(ret)
cv2.imshow("THRESH_OTSU", Ib)

img_blur = cv2.blur(Igray, (5, 5))
cv2.imshow("img_blur", img_blur)

countours, hierarchy = cv2.findContours(Ib, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
cv2.drawContours(ims_copy, countours, -1, (0, 255, 255), 3)
cv2.imshow("img_blur", ims_copy)


cv2.waitKey(0)
cv2.destroyAllWindows()
