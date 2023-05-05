import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("Images/628548.jpg")
ims = cv2.resize(img, [640, 480])

img_gray = cv2.cvtColor(ims, cv2.COLOR_BGR2GRAY)
thresh, ims1 = cv2.threshold(img_gray, 0, 255, cv2.THRESH_OTSU)
Icoppy = ims.copy()
ims2 = ims.copy()
ims3 = ims.copy()

contours, hierarchy = cv2.findContours(ims1, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

if len(contours) != 0:
    cv2.drawContours(ims, contours, -1, 255, 3)

    cnt = contours[0]
    areas = [cv2.contourArea(c) for c in contours]
    max_index = np.argmax(areas)

    cnt = contours[max_index]
    perimeter = cv2.arcLength(cnt, True)

    cv2.drawContours(ims2, contours[max_index], -1, (0, 255, 255), 3)
    # cv2.drawContours(ims3, contours[min_index], -1, (0, 255, 255), 3)

    cv2.putText(
        ims2,
        str(max_index),
        (470, 290),
        cv2.FONT_HERSHEY_COMPLEX,
        0.8,
        (255, 0, 0),
    )

    cv2.imshow("contours max", ims2)

cv2.waitKey(0)
cv2.destroyAllWindows()
