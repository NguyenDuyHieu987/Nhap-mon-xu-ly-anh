import cv2

img = cv2.imread("Images\\628548.jpg")
ims = cv2.resize(img, (680, 480))
print(f"height: {img.shape[0]}, width: {img.shape[1]}")
print(f"px: {ims[20, 30]}")
print(f"row: {ims[1,:]}")
print(f"column: {ims[:,1]}")
for i in range(100):
    # print(ims[0:30, i])
    ims[0:30, i] = (0, 0, 255)
img2 = cv2.transpose(ims)
img2 = cv2.cvtColor(ims, cv2.COLOR_RGB2HSV)
cv2.imshow("anh goc", img2)
cv2.waitKey(0)
cv2.destroyWindows()
