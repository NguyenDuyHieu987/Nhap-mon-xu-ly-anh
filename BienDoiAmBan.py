import cv2

img = cv2.imread("Images\\628548.jpg")
ims = cv2.resize(img, [640, 480])

img_gray = cv2.cvtColor(ims, cv2.COLOR_RGB2GRAY)

L = 25
img_neg = 255 - img_gray - L

b, g, r = cv2.split(ims)

b_neg = 255 - b - L
g_neg = 255 - g - L
r_neg = 255 - r - L

img_merge1 = cv2.merge([b_neg, g_neg, r_neg])
img_merge2 = cv2.merge([g_neg, b_neg, r_neg])
img_merge3 = cv2.merge([r_neg, g_neg, b_neg])

cv2.imwrite("Images\\628548_amban.jpg", img_neg)
cv2.imshow("anh am ban", img_neg)
cv2.imshow("img merge1", img_merge1)
cv2.imshow("img merge2", img_merge2)
cv2.imshow("img merge3", img_merge3)
cv2.imshow("img", ims)

cv2.waitKey(0)
cv2.destroyAllWindows()