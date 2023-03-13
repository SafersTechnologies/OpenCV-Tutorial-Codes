import cv2 as cv
img = cv.imread('Images/friends.jpg')
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('ORIGINAL IMAGE', img)
cv.imshow('HSV OUTPUT', hsv) 
cv.waitKey(0)
