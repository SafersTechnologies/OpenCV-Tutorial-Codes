import cv2 as cv
img = cv.imread("Images/friends.jpg")
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
threshold, thresh = cv.threshold(gray_img, 125, 255, cv.THRESH_BINARY)
cv.imshow("SIMPLE THRESHOLDED IMAGE", thresh)
cv.waitKey(0)