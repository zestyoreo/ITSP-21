#As for one-dimensional signals, images also can be filtered with various (LPF),(HPF), etc.
# A LPF helps in removing noise, or blurring the image.
# A HPF filters helps in finding edges in an image.

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('logo1.jpeg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
kernel = np.ones((5,5),np.float32)/25
dst = cv2.filter2D(img,-1,kernel)

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(dst),plt.title('Averaging')
plt.xticks([]), plt.yticks([])
plt.show()