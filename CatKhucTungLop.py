import cv2
import numpy as np

img = cv2.imread("Images\\628548.jpg")
ims = cv2.resize(img, [640, 480])

A = 50
B = 150
h, w, c = ims.shape
img_gls = np.array(ims.copy())

img_gls1 = np.where(((img_gls> A) & ( img_gls < B)), 255, 0)
img_gls1 = img_gls1.astype(np.uint8)
            
cv2.imshow('Khong nen',img_gls1)
cv2.imshow("img", ims)

img_gls2 = np.where(((img_gls> A) & ( img_gls < B)), 255, 100)
img_gls2 = img_gls2.astype(np.uint8)

cv2.imshow('Nen',img_gls2)

# cv2.imwrite("Images\\628548_CatKhucTungLop.jpg", img_gls)

cv2.waitKey(0)
cv2.destroyAllWindows()