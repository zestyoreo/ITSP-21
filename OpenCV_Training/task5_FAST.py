import numpy as np
import cv2 as cv

img = cv.imread('bolt.jpeg')

# Initiate FAST object with default values
fast = cv.FastFeatureDetector_create(threshold = 50000)

# find and draw the keypoints
kp = fast.detect(img,None)
img2 = cv.drawKeypoints(img, kp, None, color=(255,0,0))

# Print all default params
print( "Threshold: {}".format(fast.getThreshold()) )
print( "nonmaxSuppression:{}".format(fast.getNonmaxSuppression()) )
print( "neighborhood: {}".format(fast.getType()) )
print( "Total Keypoints with nonmaxSuppression: {}".format(len(kp)) )

# Disable nonmaxSuppression
fast.setNonmaxSuppression(0)
kp = fast.detect(img,None)

print( "Total Keypoints without nonmaxSuppression: {}".format(len(kp)) )
img3 = cv.drawKeypoints(img, kp, None, color=(255,0,0))

cv.imshow('FAST with suppression', img2)
cv.waitKey(0)
cv.destroyAllWindows()

cv.imshow('FAST no suppression', img3)
cv.waitKey(0)
cv.destroyAllWindows()