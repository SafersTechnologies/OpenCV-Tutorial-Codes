import cv2 as cv
img = cv.imread("Images/seun.jpg")
median= cv.medianBlur(img, 3)
cv.imshow("ORIGINAL IMAGE", img)
cv.imshow("MEDIAN BLUR", median)
cv.waitKey(0)