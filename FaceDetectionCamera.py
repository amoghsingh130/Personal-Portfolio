import cv2
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os
import numpy as np

class FaceDetectionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Face Detection & Capture")

        self.capture_button = ttk.Button(root, text="Capture", command=self.capture_image)
        self.capture_button.pack()

        self.record_button = ttk.Button(root, text="Start Recording", command=self.toggle_record)
        self.record_button.pack()

        self.video_source = cv2.VideoCapture(0)
        self.video_source.set(3, 640)
        self.video_source.set(4, 480) 

        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

        self.video_display = tk.Label(root)
        self.video_display.pack()

        self.recording = False
        self.video_writer = None
        self.image_count = 0
        self.video_count = 0

        self.update()
        self.root.mainloop()

    def capture_image(self):
        _, frame = self.video_source.read()
        if frame is not None:
            image_filename = os.path.join("C://Users//amogh//OneDrive//Documents//His exellency Amogh Singh//my world//Pictures For AI", f"pic{self.image_count}.jpg")
            self.image_count += 1

            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            cv2.imwrite(image_filename, frame)
            print(f"Image captured as '{image_filename}'.")

    def toggle_record(self):
        if not self.recording:
            self.recording = True
            self.record_button.config(text="Stop Recording")
            video_filename = os.path.join("C://Users//amogh//OneDrive//Documents//His exellency Amogh Singh//my world//Pictures For AI", f"vid{self.video_count}.avi")
            self.video_count += 1
            frame_width = int(self.video_source.get(3))
            frame_height = int(self.video_source.get(4))
            self.video_writer = cv2.VideoWriter(video_filename, cv2.VideoWriter_fourcc('X', 'V', 'I', 'D'), 20, (frame_width, frame_height))
        else:
            self.recording = False
            self.record_button.config(text="Start Recording")
            self.video_writer.release()
            print(f"Video saved as 'vid{self.video_count - 1}.avi.")



    def detect_faces(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        return frame

    def update(self):
        _, frame = self.video_source.read()
        if frame is not None:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = self.detect_faces(frame)
            self.photo = ImageTk.PhotoImage(image=Image.fromarray(frame))
            self.video_display.configure(image=self.photo)
            self.video_display.image = self.photo

            if self.recording:
                self.video_writer.write(frame)

        self.root.after(10, self.update)

if __name__ == "__main__":
    root = tk.Tk()
    app = FaceDetectionApp(root)
