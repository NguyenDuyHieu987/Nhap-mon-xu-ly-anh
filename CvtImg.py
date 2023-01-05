import cv2

img = cv2.imread("Images\\628548.jpg")
ims = cv2.resize(img, (680, 480))

# for h in range(ims.shape[0]):
#     for w in range(ims.shape[1]):
#         if ims[h, w] > 150:
#             ims[h, w] = 0
#         else:
#             ims[h, w] = 1
img2 = cv2.cvtColor(ims, cv2.COLOR_RGB2GRAY)
img3 = cv2.cvtColor(ims, cv2.COLOR_RGB2HLS)

ret, bw = cv2.threshold(img2, 127, 255, cv2.THRESH_BINARY)
img_and = cv2.bitwise_and(bw, img3, mask=None)

cv2.imshow("anh goc", bw)
cv2.waitKey(0)
cv2.destroyWindows()
