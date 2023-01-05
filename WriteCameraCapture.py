import cv2

vid_capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)
frame_width = int(vid_capture.get(3))
frame_height = int(vid_capture.get(4))
frame_size = (frame_width, frame_height)
fps = 24

output = cv2.VideoWriter(
    "Videos\\output_video_from_file.avi",
    cv2.VideoWriter_fourcc("M", "J", "P", "G"),
    fps,
    frame_size,
)


while vid_capture.isOpened():
    ret, frame = vid_capture.read()
    cv2.imshow("video from camera pc", frame)
    if ret is True:
        output.write(frame)
    else:
        print("Stream disconnected")
        break
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

vid_capture.release()
cv2.destroyAllWindows()
