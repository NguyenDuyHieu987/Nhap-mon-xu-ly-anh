import cv2

img = cv2.imread("Images\\628548.jpg")
ims = cv2.resize(img, (680, 480))

for h in range(ims.shape[0]):
    for w in range(ims.shape[1]):
        if ims[h, w][0] > 150 and ims[h, w][1] > 150 and ims[h, w][2] > 150:
            ims[h, w] = [255, 255, 255]
        else:
            ims[h, w] = [0, 0, 0]


cv2.imshow("anh goc", ims)
cv2.waitKey(0)
cv2.destroyWindows()
