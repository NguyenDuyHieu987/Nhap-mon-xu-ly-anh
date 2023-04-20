import cv2
import numpy as np

img = cv2.imread("Images/628548.jpg")

print(img.shape[0] / img.shape[1])
cv2.imshow("ims", img)

h, s, v = cv2.split(img)
cv2.imshow("s", s)

print(np.argmax(img))


cv2.waitKey(0)
cv2.destroyAllWindows()
