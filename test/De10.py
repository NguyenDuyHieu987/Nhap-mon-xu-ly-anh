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

cv2.imshow("Igray", Igray)

img_x = cv2.Sobel(Igray, cv2.CV_64F, 1, 0, ksize=5)
cv2.imshow("Igray sobel", img_x)
print(img_x)


img_canny = cv2.Canny(Igray, 100, 200)
cv2.imshow("img_canny", img_canny)
print(img_canny[100, 120])
print(img_canny[100, 120] == 1)

cv2.waitKey(0)
cv2.destroyAllWindows()
