import cv2
import tkinter as tk
from PIL import Image, ImageTk

class FaceDetectionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Face Detection & Eye Tracking")

        self.video_source = cv2.VideoCapture(0)
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        self.eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")

        self.video_display = tk.Label(root)
        self.video_display.pack()

        self.update()
        self.root.mainloop()

    def update(self):
        _, frame = self.video_source.read()
        if frame is not None:
            frame_with_face_eyes = self.detect_face_eyes(frame)
            self.photo = ImageTk.PhotoImage(image=Image.fromarray(cv2.cvtColor(frame_with_face_eyes, cv2.COLOR_BGR2RGB)))
            self.video_display.configure(image=self.photo)
            self.video_display.image = self.photo

        self.root.after(10, self.update)

    def detect_face_eyes(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = frame[y:y + h, x:x + w]

            eyes = self.eye_cascade.detectMultiScale(roi_gray)
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 0, 255), 2)

        return frame

if __name__ == "__main__":
    root = tk.Tk()
    app = FaceDetectionApp(root)
