#Change the colour of everything in your image from a red colour to blue colour.
import cv2
import matplotlib.pyplot as plt

#OpenCV reads images in BGR
img = cv2.imread('nemo0.jpeg')
plt.imshow(img)
plt.show()