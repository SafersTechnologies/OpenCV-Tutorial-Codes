import cv2 as cv
img = cv.imread('Images/friends.jpg')
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('ORIGINAL IMAGE', img)
cv.imshow('LAB OUTPUT', lab) 
cv.waitKey(0)
