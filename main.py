# A Face Detection Program made by Techno Studio
# Developer of This code is, Areno Dev.

# Links - 
# Techno Studio's Website - https://techno-studio-tech.github.io/techno-studio/
# Areno Dev's Website - https://areno-dev.github.io/areno/

import cv2
import time
import datetime

__name__ = "Face Detection Program"
__author__ = "Areno Dev"


cap = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
body_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_fullbody.xml")


while True:
    _, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 1)

    for (x, y, width, height) in faces:
        cv2.cv2.rectangle(frame, (x, y), (x + width, y + height), (255, 0, 0), 3)

    cv2.imshow("Webcam", frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()