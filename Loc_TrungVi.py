import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("Images/Lena.jpg", 0)
# ims = cv2.resize(img, (800, 540))
cv2.imshow("anh goc", img)

img_med = cv2.medianBlur(img, 9)
cv2.imshow("anh loc", img_med)

s = [3, 5, 7]
for i, k in enumerate(s):
    img_med1 = cv2.medianBlur(img, k)
    cv2.imshow(f"anh loc {i}", img_med1)


hist = cv2.calcHist([img_med], [0], None, [256], [0, 256])
plt.plot(hist, color="r")
plt.hist(img_med.ravel(), 256, [0, 256])
plt.title("Image Histogram For Blue Channel")
plt.show()
img_equalization = cv2.equalizeHist(img_med)
cv2.imshow("anh can bang hist", img_equalization)

gamma = 1.8
img_constr = np.power(img_med, gamma)
max_val = np.max(img_constr.ravel())
img_constr = img_constr / max_val * 255
img_constr = img_constr.astype(np.uint8)
cv2.imshow(f"anh loc constr", img_constr)

cv2.waitKey(0)
cv2.destroyAllWindows()
