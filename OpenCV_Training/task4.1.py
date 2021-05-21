import numpy as np
import cv2
from matplotlib import pyplot as plt

img= cv2.imread('nemo3.jpeg')
imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,0)
#If you pass cv2.CHAIN_APPROX_NONE, all the boundary points are stored.
#cv2.CHAIN_APPROX_SIMPLE removes all redundant points and compresses the contour, thereby saving memory.
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#shows all contours
#to draw all contours, pass -1) and remaining arguments are color, thickness etc.
img = cv2.drawContours(img, contours, -1, (0,255,0), 3)

#shows specific contours
'''cnt = contours[4]
img = cv2.drawContours(img, [cnt], 0, (0,255,0), 3)'''

plt.imshow(img)
plt.xticks([]), plt.yticks([])
plt.show()