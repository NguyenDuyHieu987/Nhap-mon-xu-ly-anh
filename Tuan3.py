import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("Images/628548.jpg")
img = cv2.resize(img, [640, 480])

b, r, g = cv2.split(img)

img2 = np.zeros((480, 640), dtype="uint8")
img2[:, :] = b * 0.11 + r * 0.39 + g * 0.5


cv2.imshow("img2", img2)

cv2.waitKey(0)
cv2.destroyAllWindows()
