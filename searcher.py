import cv2
def draw_found_faces(detected, image, color: tuple):
    for (x, y, width, height) in detected:
        cv2.rectangle(
            image,
            (x, y),
            (x + width, y + height),
            color,
            thickness=2
        )
video_capture = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
while True:
    _, frame = video_capture.read()
    grayscale_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    detected_faces = face_cascade.detectMultiScale(image=grayscale_image, scaleFactor=1.3, minNeighbors=4)
    draw_found_faces(detected_faces, frame, (0, 0, 255))
    cv2.imshow('Face', frame)

    if cv2.waitKey(1) == 27:
        break
video_capture.release()
cv2.destroyAllWindows()
