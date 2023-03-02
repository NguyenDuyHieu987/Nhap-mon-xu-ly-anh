import matplotlib.pyplot as plt
import cv2
import numpy as np

img = cv2.imread("Images\\628548.jpg", 0)
ims = cv2.resize(img, [640, 480])

img_equalization = cv2.equalizeHist(ims)

cv2.imshow("Anh goc", ims)
cv2.imshow("Anh can bang histogram", img_equalization)

hist1 = cv2.calcHist([ims], [0], None, [256], [0, 256])
plt.plot(hist1, color="b")

hist2 = cv2.calcHist([img_equalization], [0], None, [256], [0, 256])
plt.plot(hist2, color="r")

plt.title("Image Histogram")
plt.show()
