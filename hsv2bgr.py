import cv2 as cv
img = cv.imread('Images/friends.jpg')
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV OUTPUT', hsv) 
bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('BGR Output', bgr) 
cv.waitKey(0)
