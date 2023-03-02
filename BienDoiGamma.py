import cv2
import numpy as np

img = cv2.imread("Images\\628548.jpg")
ims = cv2.resize(img, [640, 480])

img_gray = cv2.cvtColor(ims, cv2.COLOR_RGB2GRAY)

c, e, gamma = 4, 0, 5
img_exp = c * (255 * (img_gray / 255 + e) ** gamma)
img_exp = np.array(img_exp, dtype = np.uint8)

gamma = 0.05
img_exp1 = c * (255 * (img_gray / 255 + e) ** gamma)
img_exp1 = np.array(img_exp1, dtype = np.uint8)

cv2.imwrite("Images\\628548_luythua.jpg", img_exp)
cv2.imshow("img", ims)
cv2.imshow("Ham mu lon hon 1", img_exp)
cv2.imshow("Ham mu nho hon 1", img_exp1)

cv2.waitKey(0)
cv2.destroyAllWindows()