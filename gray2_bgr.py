import cv2 as cv
img = cv.imread('Images/friends.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
bgr = cv.cvtColor(gray, cv.COLOR_GRAY2BGR)
cv.imshow('GRAY OUTPUT', gray) 
cv.imshow("BGR", bgr)
cv.waitKey(0)