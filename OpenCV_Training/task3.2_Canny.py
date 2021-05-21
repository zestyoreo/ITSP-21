#Pencil Edge Figure
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('nemo4.jpeg',0)
edges = cv2.Canny(img,100,200)

plt.subplot(131),plt.imshow(img)
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(132),plt.imshow(edges)
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
plt.subplot(133),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Grey Image'), plt.xticks([]), plt.yticks([])
plt.show()
