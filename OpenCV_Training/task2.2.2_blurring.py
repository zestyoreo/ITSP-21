#Averaging
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('logo2.png')

blur = cv2.blur(img,(5,5))

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Average Blurred')
plt.xticks([]), plt.yticks([])
plt.show()

#Gaussian Filter
blur = cv2.GaussianBlur(img,(5,5),0)

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Gaussian Filtered')
plt.xticks([]), plt.yticks([])
plt.show()

#Median Filtering
#good for removing salt and pepper noise
img = cv2.imread('ae.jpg')

median = cv2.medianBlur(img,5)

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(median),plt.title('Median Filtered')
plt.xticks([]), plt.yticks([])
plt.show()

#Bilateral Filtering
#As we noted, the filters we presented earlier tend to blur edges.
# This is not the case for the bilateral filter, which was defined for,
# and is highly effective at noise removal while preserving edges.
img = cv2.imread('logo2.png')
blur = cv2.bilateralFilter(img,9,75,75)

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Bilateral Filter')
plt.xticks([]), plt.yticks([])
plt.show()