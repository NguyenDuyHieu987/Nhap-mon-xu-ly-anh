import cv2
import numpy as np
import matplotlib.pyplot as plt
import math

img = cv2.imread("Images/628548.jpg")
ims = cv2.resize(img, [640, 480])

img_gray = cv2.cvtColor(ims, cv2.COLOR_BGR2GRAY)
print("min:", img_gray.min())
print("max:", img_gray.max())
print("avg:", img_gray.mean())


cv2.waitKey(0)
cv2.destroyAllWindows()
