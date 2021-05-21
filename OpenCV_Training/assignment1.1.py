# Import your image and convert to black and white and in greyscale.
import cv2 as cv
import sys
img = cv.imread("nemo0.jpeg")
if img is None:
    sys.exit("Could not read the image.")
greyImage = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Display window", greyImage)
k = cv.waitKey(0)
(thresh, bwimg) = cv.threshold(greyImage, 127, 255, cv.THRESH_BINARY)
cv.imshow("Display window", bwimg)
k = cv.waitKey(0)
