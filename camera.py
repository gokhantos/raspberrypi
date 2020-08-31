import cv2

vcap = cv2.VideoCapture("rtsp://192.168.1.1/MJPG?W=720&H=400&Q=50&BR=5000000/")

while(1):

    ret, frame = vcap.read()
    cv2.imshow('VIDEO', frame)
    cv2.waitKey(1)
