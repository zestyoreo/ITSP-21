#Given the image distinguish between different shapes.
#Like your model should be able to detect the centre and
# classify these shapes in the image automatically.
import cv2
from matplotlib import pyplot as plt

img= cv2.imread('shapes.png')
imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,0)

contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
img = cv2.drawContours(img, contours, -1, (0,255,0), 3)

for i in range(len(contours)):
    cnt=contours[i]
    M = cv2.moments(cnt)
    cx = int(M['m10'] / M['m00'])
    cy = int(M['m01'] / M['m00'])
    cv2.circle(img, (cx, cy), 7, (0,0,0), -1)

plt.imshow(img)
plt.xticks([]), plt.yticks([])
plt.show()