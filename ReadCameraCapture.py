import cv2

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
try:
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
except AttributeError:
    print("shape not found")

cap.release()
cv2.destroyAllWindows()
