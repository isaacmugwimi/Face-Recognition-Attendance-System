import cv2

video_capture = cv2.VideoCapture(0)

while True:
    ret, frame = video_capture.read()
    if not ret:
        print("⚠️ Error: Unable to access the camera.")
        break
    
    cv2.imshow("Camera Test", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to exit
        break

video_capture.release()
cv2.destroyAllWindows()
