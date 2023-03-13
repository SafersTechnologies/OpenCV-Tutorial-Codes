import cv2 as cv
img = cv.imread("Images/friends.jpg")
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
threshold, thresh_inv = cv.threshold(gray_img, 125, 255, cv.THRESH_BINARY_INV)
cv.imshow("INVERSE", thresh_inv)
cv.waitKey(0)