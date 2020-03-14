import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):
    ret, frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    ORANGE_MIN = np.array([5,50,50])
    ORANGE_MAX = np.array([15,255,255])

    abcd = cv2.inRange(hsv, ORANGE_MIN, ORANGE_MAX)

    output = cv2.bitwise_and(frame, frame, mask = abcd)

    cv2.imshow('video_feed', frame)
    cv2.imshow('mask', abcd)
    cv2.imshow('final_frame', output)

    cv2.waitKey(1)

cv2.destroyAllWindows()
