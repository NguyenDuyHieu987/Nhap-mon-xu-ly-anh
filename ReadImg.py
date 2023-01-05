import cv2

img = cv2.imread("Images\\628548.jpg")
ims = cv2.resize(img, (800, 540))
cv2.imshow("anh goc", ims)
cv2.waitKey(0)
cv2.destroyWindows()
