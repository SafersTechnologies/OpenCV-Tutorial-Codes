import cv2 as cv
import numpy as np
img = cv.imread('Images/friends.jpg')
blank = np.zeros(img.shape[:2] , dtype="uint8")
b, g, r = cv.split(img)
blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

cv.imshow("BLUE", blue)
cv.imshow("GREEN", green)
cv.imshow("RED", red)
cv.waitKey(0)