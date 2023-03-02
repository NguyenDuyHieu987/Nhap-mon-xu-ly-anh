import cv2
import numpy as np

img = cv2.imread("Images\\628548.jpg")
ims = cv2.resize(img, [640, 480])

ims = np.array(ims)
img_gray = cv2.cvtColor(ims, cv2.COLOR_RGB2GRAY)

for k in range(7):
    plane = np.full((img_gray.shape[0], img_gray.shape[1]), 2 ** k, np.uint8)
    res = cv2.bitwise_and(plane, img_gray)
    img_bit_slice = (res * 255).astype(np.uint8)
    
    cv2.imshow(f'Anh bien doi bit plan slicing {k}', img_bit_slice)


cv2.imshow('Nen',ims)

# cv2.imwrite("Images\\628548_CatKhucTungLop.jpg", img_gls)

cv2.waitKey(0)
cv2.destroyAllWindows()