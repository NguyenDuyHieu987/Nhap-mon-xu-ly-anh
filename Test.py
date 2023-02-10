import cv2
import numpy as np

img = cv2.imread("Images\\628548.jpg")
ims = cv2.resize(img, [640, 480])

print("Width:", ims.shape[1])
print("Height:", ims.shape[0])
print("chanels:", ims.shape[2])

img_gray = cv2.cvtColor(ims, cv2.COLOR_RGB2GRAY)
ret, bw = cv2.threshold(img_gray, 100, 255, cv2.THRESH_OTSU)
img_hsv = cv2.cvtColor(ims, cv2.COLOR_RGB2HSV)

b, g, r = cv2.split(ims)
cv2.imshow("Blue Image", b)
cv2.imshow("Green Image", g)
cv2.imshow("Red Image", r)

h, s, v = cv2.split(img_hsv)
cv2.imshow("h Image", h)
cv2.imshow("s Image", s)
cv2.imshow("v Image", v)

iHSV = np.zeros((480, 640), dtype="uint8")
iHSV[:, :] = 0.3*h + 0.5*s + 0.2*v
print(iHSV)
cv2.imshow("img iHSV", iHSV)

img_merge = cv2.merge([h*0.3, s*0.5, v*0.2])
cv2.imshow("img merge", img_merge)

# cv2.imshow("img", img_gray)
cv2.imshow("otsu", bw)
cv2.imshow("hsv", img_hsv)

cv2.waitKey(0)
cv2.destroyWindows()
