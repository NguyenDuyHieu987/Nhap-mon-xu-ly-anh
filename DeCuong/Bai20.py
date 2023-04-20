import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("Images/628548.jpg")

height = 256
width = int(img.shape[1] * height / img.shape[0])

resized_img = cv2.resize(img, (width, height))
# resized_img = np.reshape(resized_img, (height, width, -1))

cv2.imshow("Image", resized_img)


cv2.waitKey(0)
cv2.destroyAllWindows()
