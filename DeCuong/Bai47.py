import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("Images/628548.jpg")
ims = cv2.resize(img, [640, 480])

img_gray = cv2.cvtColor(ims, cv2.COLOR_BGR2GRAY)

thresh, I_bina = cv2.threshold(img_gray, 0, 255, cv2.THRESH_OTSU)
I_copy = ims.copy()
contours, hierarchy = cv2.findContours(I_bina, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
area_cnt = [cv2.contourArea(cnt) for cnt in contours]

# max = area_cnt[0]
# for i in range(len(area_cnt)):
#     if max < area_cnt[i]:
#         max = area_cnt[i]

max = np.argmax(area_cnt)

for contour in contours:
    if cv2.contourArea(contour) > (max / (5)):
        cv2.drawContours(I_copy, [contour], -1, (0, 255, 255), 3)


cv2.imshow("contours", I_copy)


cv2.waitKey(0)
cv2.destroyAllWindows()
