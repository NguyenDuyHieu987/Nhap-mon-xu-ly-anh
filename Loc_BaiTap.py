import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("Images/a-Lena-Gaussian-noise-b-Filtered-image.png", 0)
ims = cv2.resize(img, (800, 540))
cv2.imshow("anh goc", ims)

img_mean = cv2.blur(ims, (9, 9))
cv2.imshow("anh loc mean", img_mean)

img_gauss = cv2.GaussianBlur(ims, (9, 9), 0)
cv2.imshow("anh loc gauss", img_gauss)

img_med = cv2.medianBlur(ims, 9)
cv2.imshow("anh loc med", img_med)


hist = cv2.calcHist([img_mean], [0], None, [256], [0, 256])
plt.plot(hist, color="r")

hist2 = cv2.calcHist([img_gauss], [0], None, [256], [0, 256])
plt.plot(hist2, color="g")

hist3 = cv2.calcHist([img_med], [0], None, [256], [0, 256])
plt.plot(hist3, color="b")

plt.show()

img_equalization = cv2.equalizeHist(img_mean)
cv2.imshow("anh can bang hist", img_equalization)

gamma = 1.8
img_constr = np.power(img_mean, gamma)
max_val = np.max(img_constr.ravel())
img_constr = img_constr / max_val * 255
img_constr = img_constr.astype(np.uint8)
cv2.imshow(f"anh loc mean", img_constr)

gamma = 1.8
img_constr = np.power(img_mean, gamma)
max_val = np.max(img_constr.ravel())
img_constr = img_constr / max_val * 255
img_constr = img_constr.astype(np.uint8)
cv2.imshow(f"anh loc gauss", img_constr)

gamma = 1.8
img_constr = np.power(img_mean, gamma)
max_val = np.max(img_constr.ravel())
img_constr = img_constr / max_val * 255
img_constr = img_constr.astype(np.uint8)
cv2.imshow(f"anh loc med", img_constr)

cv2.waitKey(0)
cv2.destroyAllWindows()
