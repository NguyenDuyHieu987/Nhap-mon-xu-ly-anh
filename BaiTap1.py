import cv2

img1 = cv2.imread("Images\\images.png")
img2 = cv2.imread("Images\\wallpaperflare.com_wallpaper (3).jpg")

ims1 = cv2.resize(img1, (100, 60))
ims2 = cv2.resize(img2, (680, 480))

ret, bw = cv2.threshold(ims1, 255, 255, cv2.THRESH_BINARY_INV)


ims2[0:60, 0:100] = bw

cv2.imshow("anh goc", ims2)


# img_and = cv2.bitwise_and(img1, ims2, mask=None)

cv2.waitKey(0)
cv2.destroyWindows()
