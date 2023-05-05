import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("Images/628548.jpg")
ims = cv2.resize(img, [640, 480])

h, w, c = ims.shape

print(h / w)

cv2.waitKey(0)
cv2.destroyAllWindows()
