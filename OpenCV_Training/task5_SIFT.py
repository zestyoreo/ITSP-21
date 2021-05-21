import numpy as np
import cv2 as cv

img = cv.imread('rash.jpeg')
gray= cv.cvtColor(img,cv.COLOR_BGR2GRAY)

sift = cv.xfeatures2d.SIFT_create()
kp, des = sift.detectAndCompute(gray,None)
# Draw without orientations
#img=cv.drawKeypoints(gray,kp,img)

img=cv.drawKeypoints(gray,kp,img,flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv.imshow('SIFT', img)

cv.waitKey(0)
cv.destroyAllWindows()