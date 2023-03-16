import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("Images/Lena.jpg", 0)
# ims = cv2.resize(img, (800, 540))
cv2.imshow("anh goc", img)

img_mean = cv2.blur(img, (9, 9))
cv2.imshow("anh loc", img_mean)

s = [(3, 3), (5, 5), (7, 7)]
for i, k in enumerate(s):
    img_mean1 = cv2.blur(img, k)
    cv2.imshow(f"anh loc {i}", img_mean1)


hist = cv2.calcHist([img_mean], [0], None, [256], [0, 256])
plt.plot(hist, color="r")
plt.hist(img_mean.ravel(), 256, [0, 256])
plt.title("Image Histogram For Red Channel")
plt.show()
img_equalization = cv2.equalizeHist(img_mean)
cv2.imshow("anh can bang hist", img_equalization)


gamma = 1.8
img_constr = np.power(img_mean, gamma)
max_val = np.max(img_constr.ravel())
img_constr = img_constr / max_val * 255
img_constr = img_constr.astype(np.uint8)
cv2.imshow(f"anh loc constr", img_constr)


cv2.waitKey(0)
cv2.destroyAllWindows()
