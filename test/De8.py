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
print(Igray.mean())

img_x = cv2.Sobel(Igray, cv2.CV_64F, 1, 0, ksize=5)
cv2.imshow("Igray sobel", img_x)
print(img_x)

img_canny = cv2.Canny(Igray, 100, 200, L2gradient=True)
cv2.imshow("Igray canny", img_canny)
print(img_canny[100, 120] == 1)

ret, Ib = cv2.threshold(Igray, 123, 255, cv2.THRESH_OTSU)
print(ret)
contours, hierarchy = cv2.findContours(Ib, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
areas = [cv2.contourArea(cnt) for cnt in contours]
max_area = np.argmax(areas)

cv2.drawContours(ims_copy, contours[max_area], -1, (0, 255, 255), 3)


cv2.putText(
    ims_copy, str(max_area), (270, 320), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0)
)
cv2.imshow("contour max area", ims_copy)


cv2.waitKey(0)
cv2.destroyAllWindows()
