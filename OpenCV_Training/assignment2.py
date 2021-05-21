#DATA AUGMENTATION
        #Make 10 alternate images from the image given below such
        # that all image contains “T”. Use 4 translation,4 rotation and 2 blurrings at least.
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('t.png')

#Original Image
plt.imshow(img), plt.title('Original Image')
plt.show()

#Translations
rows,cols,channels = img.shape  #channels needed to process colour images
                                #greyscale images need only rows,cols
M = np.float32([[1, 0, 100],[0, 1, 50]])
dst = cv2.warpAffine(img, M, (cols, rows))

plt.imshow(dst),plt.title('Translation 1')
plt.show()

M = np.float32([[1, 0, -100],[0, 1, -50]])
dst = cv2.warpAffine(img, M, (cols, rows))

plt.imshow(dst),plt.title('Translation 2')
plt.show()

#Rotation
M = cv2.getRotationMatrix2D((cols/2, rows/2), 90, 1)
dst = cv2.warpAffine(img, M, (cols, rows))

plt.imshow(dst),plt.title('Rotation 1')
plt.show()

M = cv2.getRotationMatrix2D((cols/2,rows/2),135,1)
dst = cv2.warpAffine(img,M,(cols,rows))

plt.imshow(dst),plt.title('Rotation 2')
plt.show()

#Rotation+Translation
M = cv2.getRotationMatrix2D((cols/2,rows/2),90,1)
dst = cv2.warpAffine(img,M,(cols,rows))

M = np.float32([[1,0,100],[0,1,50]])
dst = cv2.warpAffine(dst,M,(cols,rows))

plt.imshow(dst),plt.title('Rotation+Translation 1')
plt.show()

M = cv2.getRotationMatrix2D((cols/2,rows/2),-45,1)
dst = cv2.warpAffine(img,M,(cols,rows))

M = np.float32([[1,0,100],[0,1,50]])
dst = cv2.warpAffine(dst,M,(cols,rows))

plt.imshow(dst),plt.title('Rotation+Translation 2')
plt.show()

#Averaging
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
median = cv2.medianBlur(img,5)

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(median),plt.title('Median Filtered')
plt.xticks([]), plt.yticks([])
plt.show()

#Bilateral Filtering
blur = cv2.bilateralFilter(img,9,75,75)

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Bilateral Filter')
plt.xticks([]), plt.yticks([])
plt.show()