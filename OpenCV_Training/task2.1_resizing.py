import cv2
import sys
import numpy as np

img = cv2.imread('starry_night.jpeg')
cv2.imshow("Display window", img)
k = cv2.waitKey(0)
res = cv2.resize(img,None,fx=2, fy=2, interpolation = cv2.INTER_CUBIC)
cv2.imshow("Display window2", res)
k2 = cv2.waitKey(0)