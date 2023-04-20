import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("Images/628548.jpg")
img = cv2.resize(img, [640, 480])

hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)

h, s, v = cv2.split(hsv)

x = 20
y = 10
print(s[x - 2 : x + 3, y - 2 : y + 3])

for i in range(x - 2, x + 3):
    print(i)


cv2.waitKey(0)
cv2.destroyAllWindows()
