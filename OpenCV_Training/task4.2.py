import cv2
import numpy as np
from matplotlib import pyplot as plt

imgo = cv2.imread('bolt.jpeg')
img = cv2.cvtColor(imgo, cv2.COLOR_BGR2GRAY)
plt.imshow(img)
plt.title("Original")
plt.xticks([]), plt.yticks([])
plt.show()

ret,thresh = cv2.threshold(img,127,255,0)
contours,hierarchy = cv2.findContours(thresh, 1, 2)

cnt = contours[0]
im = cv2.drawContours(img, cnt, -1, (0,255,0), 3)

plt.imshow(im)
plt.xticks([]), plt.yticks([])
plt.show()

#moments
M = cv2.moments(cnt)
print (M)
#centroid
cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])
print(cx,cy)
#contour area
area = cv2.contourArea(cnt)
print(area)
#perimeter
perimeter = cv2.arcLength(cnt,True)
print(perimeter)

#convex hull
hull = cv2.convexHull(cnt)

#bounding rectangle
x,y,w,h = cv2.boundingRect(cnt)
im = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
plt.imshow(im)
plt.xticks([]), plt.yticks([])
plt.show()

#bounding slanting rectangle
rect = cv2.minAreaRect(cnt)
box = cv2.boxPoints(rect)
box = np.int0(box)
im = cv2.drawContours(img,[box],0,(0,0,255),2)
plt.imshow(im)
plt.xticks([]), plt.yticks([])
plt.show()

#bounding circle
(x,y),radius = cv2.minEnclosingCircle(cnt)
center = (int(x),int(y))
radius = int(radius)
im = cv2.circle(img,center,radius,(0,255,0),2)
plt.imshow(im)
plt.xticks([]), plt.yticks([])
plt.show()

#bounding ellipse
ellipse = cv2.fitEllipse(cnt)
im = cv2.ellipse(img,ellipse,(0,255,0),2)
plt.imshow(im)
plt.xticks([]), plt.yticks([])
plt.show()

#line fitting
rows,cols = img.shape[:2]
[vx,vy,x,y] = cv2.fitLine(cnt, cv2.DIST_L2,0,0.01,0.01)
lefty = int((-x*vy/vx) + y)
righty = int(((cols-x)*vy/vx)+y)
im = cv2.line(img,(cols-1,righty),(0,lefty),(0,255,0),2)
plt.imshow(im)
plt.xticks([]), plt.yticks([])
plt.show()