import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("Images/Lena.jpg")


smooth_image_f2D_5_5 = cv2.blur(img, (5, 5))

cv2.imshow("Image", smooth_image_f2D_5_5)

cv2.waitKey(0)
cv2.destroyAllWindows()
