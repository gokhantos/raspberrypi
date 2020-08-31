import cv2
import numpy as np

vcap = cv2.VideoCapture("rtsp://192.168.1.1/MJPG?W=720&H=400&Q=50&BR=5000000/")
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')


while(1):
    ret, frame = vcap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    cv2.imshow('VIDEO', frame)
    cv2.waitKey(1)
