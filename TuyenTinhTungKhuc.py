import cv2
import numpy as np

def changePixelVal(img, r1, s1, r2, s2, r3, s3):
    if (0 <= img and img <= r1):
        return (s1 / r1)*img
    elif (r1 < img and img <= r2):
        return ((s2 - s1)/(r2 - r1)) * (img - r1) + s1
    elif (r1 < img and img <= r2 and img <= r3):
        return ((s3 - s2)/(r3 - r2)) * (img - r2) + s2
    else:
        return ((255 - s3)/(255 - r3)) * (img - r3) + s3
    
img = cv2.imread('Images\\628548.jpg')
ims = cv2.resize(img, [640, 480])

r1, s1, r2, s2, r3, s3 = 70, 0, 140, 127, 210, 255
vec = np.vectorize(changePixelVal)
img1 = vec(ims, r1, s1, r2, s2, r3, s3)

cv2.imwrite("Images\\628548_TuyenTinhTungKhuc.jpg", img1)
cv2.imshow('Anh bien doi tung khuc', img1)

cv2.waitKey(0)
cv2.destroyAllWindows()