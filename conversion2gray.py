import cv2 as cv
img = cv.imread('Images/seun.jpg')
gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
cv.imshow('Original Image', img)
cv.imshow('GRAY', gray)
cv.waitKey(0)