#Make the pencil sketch of an image that you imported for assignment 1
import cv2
from matplotlib import pyplot as plt
import sys

img = cv2.imread("nemo0.jpeg")
if img is None:
    sys.exit("Could not read the image.")
grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(grey,100,200)
ret,pencil = cv2.threshold(edges,127,255,cv2.THRESH_BINARY_INV)
plt.imshow(pencil,cmap = 'gray')
plt.title('Edge Grey Image'), plt.xticks([]), plt.yticks([])
plt.show()

