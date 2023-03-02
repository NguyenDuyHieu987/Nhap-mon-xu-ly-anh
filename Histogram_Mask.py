import matplotlib.pyplot as plt
import cv2
import numpy as np

img = cv2.imread("Images\\628548.jpg")
ims = cv2.resize(img, [640, 480])

# print(ims.shape[0:2])

mask = np.zeros(ims.shape[:2], np.uint8)
mask[100:300, 100:400] = 255


masked_img = cv2.bitwise_and(ims, ims, mask=mask)
hist_full = cv2.calcHist([ims], [0], None, [256], [0, 256])
hist_mask = cv2.calcHist([ims], [0], mask, [256], [0, 256])
plt.subplot(221), plt.imshow(img, "gray")
plt.subplot(222), plt.imshow(mask, "gray")
plt.subplot(223), plt.imshow(masked_img, "gray")
plt.subplot(224), plt.plot(hist_full), plt.plot(hist_mask)
plt.title("Image Histogram")
plt.show()
