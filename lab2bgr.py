import cv2 as cv
img = cv.imread('Images/friends.jpg')
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB OUTPUT', lab) 
bgr = cv.cvtColor(lab, cv.COLOR_LAB2BGR)
cv.imshow('BGR', bgr)
cv.waitKey(0)