# import cv2

# img1 = cv2.imread("Images\\628548.jpg")
# img2 = cv2.imread("Images\\wallpaperflare.com_wallpaper (3).jpg")

# ims1 = cv2.resize(img1, (680, 480))
# ims2 = cv2.resize(img2, (680, 480))


# # cv2.imwrite("Images\\CvtImg.jpg", ims)

# # ims1 = cv2.cvtColor(ims1, cv2.COLOR_RGB2GRAY)
# # ims2 = cv2.cvtColor(ims2, cv2.COLOR_RGB2HSV)

# # ret, bw = cv2.threshold(ims, 127, 255, cv2.THRESH_BINARY)
# img_and = cv2.bitwise_and(ims1, ims2, mask=None)
# img_or = cv2.bitwise_or(ims1, ims2, mask=None)

# cv2.imshow("anh goc", img_and)

# cv2.waitKey(0)
# cv2.destroyWindows()


import numpy as np
import cv2


# draw a rectangle
rectangle = np.zeros((300, 300), dtype="uint8")
cv2.rectangle(rectangle, (100, 100), (200, 200), 255, -1)

# draw a circle
circle = np.zeros((300, 300), dtype="uint8")
cv2.circle(circle, (150, 150), 60, 255, -1)

bitwiseAnd = cv2.bitwise_and(rectangle, circle)
bitwiseOr = cv2.bitwise_or(rectangle, circle)

cv2.imshow("AND", bitwiseAnd)
cv2.imshow("OR", bitwiseOr)


cv2.waitKey(0)
cv2.destroyAllWindows()
