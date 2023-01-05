import cv2

cap = cv2.VideoCapture("Videos\\bandicam 2022-10-27 11-23-09-365.mp4")

while True:
    ret, frame = cap.read()
    tshape = frame.shape
    t1 = frame.shape[0]
    t2 = frame.shape[2]
    print("shape: ", tshape)
    print(f"shape(0): {t1} , shape(2): {t2}")
    cv2.imshow("video from camera pc", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
