import cv2 as cv
img = cv.imread('Images/friends.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('ORIGINAL IMAGE', img)
cv.imshow('GRAY OUTPUT', gray) 
cv.waitKey(0)
