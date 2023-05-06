import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("Images/628548.jpg")

ims = cv2.resize(img, (640, 480))
ims_copy = ims.copy()

h, w, k = ims.shape
print("h/w:", h / w)
ims_256 = cv2.resize(ims, (256, 256))
cv2.imshow("ims_256", ims_256)

img_hsv = cv2.cvtColor(ims, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(img_hsv)
# cv2.imshow("kenh s1", img_hsv[:, :, 1])
cv2.imshow("kenh s", s)

img_canny = cv2.Canny(v, threshold1=100, threshold2=200, L2gradient=True)

cv2.imshow("img_canny v", img_canny)

hist1 = cv2.calcHist([s], [0], None, [256], [0, 256])
plt.plot(hist1, color="r")
plt.title("kenh s")
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
