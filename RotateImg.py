import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("Images/a9f2c3f3c1911dcf4480.jpg", 0)
# ims = cv2.resize(img, [640, 480])

thresh, img_gray = cv2.threshold(img, 200, 255, cv2.THRESH_OTSU)

kernel1 = np.ones((5, 5), dtype=np.uint8)

Ierose = cv2.erode(img_gray, kernel1, iterations=1)
Ierose = cv2.erode(Ierose, kernel1, iterations=1)

cv2.imshow("img", img)
cv2.imshow("img closing", Ierose)

cv2.waitKey(0)
cv2.destroyAllWindows()
