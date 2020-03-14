import cv2
import numpy as np

img = cv2.imread('roadster.jpg')

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


cv2.imshow('frame',gray)

cv2.waitKey(0)

cv2.destroyedAllWindows()
