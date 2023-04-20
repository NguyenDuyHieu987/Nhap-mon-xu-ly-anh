import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("Images/628548.jpg")

resized_img = cv2.resize(img, (256, 256))
# resized_img = np.reshape(img, (256, 256, -1))

cv2.imshow("Image", resized_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
