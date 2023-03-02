import cv2
import numpy as np

img = cv2.imread("Images\\628548.jpg")
ims = cv2.resize(img, [640, 480])

gamma = 0.5
img_constr = np.power(ims, gamma)
max_val = np.max(img_constr.ravel())
img_constr = img_constr/max_val * 255
img_constr = img_constr.astype(np.uint8)

cv2.imwrite("Images\\628548_TangDoTuongPhan.jpg", img_constr)
cv2.imshow("img", ims)
cv2.imshow("Tang do tuong phan", img_constr)

cv2.waitKey(0)
cv2.destroyAllWindows()