import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("Images/628548.jpg")

ims = cv2.resize(img, (640, 480))
ims_copy = ims.copy()

cv2.imshow("anh goc", ims)

img_hsv = cv2.cvtColor(ims, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(img_hsv)

cv2.imshow("kenh v anh hsv", v)
print("Muc sang lon nhat cua kenh v: ", v.max())

img_blur = cv2.medianBlur(s, 5)
cv2.imshow("anh loc ", img_blur)

print(img_blur)
inverted_image = cv2.bitwise_not(img_blur)
print("\n anh nghich dao", inverted_image)
cv2.imshow("anh nghich dao ", inverted_image)

ret, Ib = cv2.threshold(inverted_image, 0, 255, cv2.THRESH_OTSU)

cv2.imshow("anh otsu", Ib)


contours, hierarchy = cv2.findContours(Ib, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
area_cnt = [cv2.contourArea(cnt) for cnt in contours]
max_area = np.argmax(area_cnt)

cv2.drawContours(ims_copy, contours[max_area], -1, (0, 255, 255), 3)
cv2.putText(
    ims_copy, str(max_area), (270, 320), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255)
)
cv2.imshow("anh otsu contours", ims_copy)

# c = 255 / np.log(1 + np.max(v))
# img_log = c * (np.log(v + 1))
# img_log = np.array(img_log, dtype="uint8")

c = 255 / np.log(1 + np.max(v))
img_log = c * np.log(v + 1)
img_log = np.array(img_log, dtype="uint8")

img_hsv1 = cv2.merge((h, s, img_log))

img_rgb = cv2.cvtColor(img_hsv1, cv2.COLOR_HSV2RGB)


cv2.imshow("anh RGB", img_rgb)


cv2.waitKey(0)
cv2.destroyAllWindows()
