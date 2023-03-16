import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("Images/Lena.jpg", 0)


img_loc = cv2.medianBlur(img, 9)

img_hist = cv2.equalizeHist(img_loc)

cv2.imshow("img", img)
cv2.imshow("img loc", img_loc)
cv2.imshow("img loc equalhist", img_hist)

hist = cv2.calcHist([img_hist], [0], None, [256], [0, 256])
plt.plot(hist, color="b")
plt.show()

gamma = 1.8
img_constr = np.power(img_loc, gamma)
max_val = np.max(img_constr.ravel())
img_constr = img_constr / max_val * 255
img_constr = img_constr.astype(np.uint8)
cv2.imshow("anh loc constr", img_constr)

img2 = cv2.imread("Images/628548.jpg")
ims = cv2.resize(img2, (640, 480))


img_hsv = cv2.cvtColor(ims, cv2.COLOR_RGB2HSV)
cv2.imshow("anh hsv", img_hsv)

h, s, v = cv2.split(ims)
img_merge = cv2.merge([h * 0.3, s * 0.5, v * 0.2])

cv2.imshow("anh g", img_merge)

img_gray = cv2.cvtColor(ims, cv2.COLOR_RGB2GRAY)
ret, bw = cv2.threshold(img_gray, 100, 255, cv2.THRESH_OTSU)
iHSV = np.zeros((480, 640), dtype="uint8")
iHSV[:, :] = 0.3 * h + 0.5 * s + 0.2 * s
cv2.imshow("img iHSV", iHSV)

c, e, gamma = 4, 0, 5
img_exp = c * (255 * (img_gray / 255 + e) ** gamma)
img_exp = np.array(img_exp, dtype=np.uint8)
cv2.imshow("Ham mu lon hon 1", img_exp)


cv2.waitKey(0)
cv2.destroyAllWindows()
