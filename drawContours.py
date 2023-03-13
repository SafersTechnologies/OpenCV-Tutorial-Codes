import cv2 as cv
import numpy as np
img = cv.imread('Images/seun.jpg')
gray=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
canny = cv.Canny(gray, 125, 175)
contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
blank = np.zeros(img.shape, dtype = 'uint8')
cv.drawContours(blank, contours, -1, (0, 0, 225), 1)
cv.imshow('Canny edges', canny)
cv.imshow("Contours Drawn.", blank)
cv.waitKey(0)