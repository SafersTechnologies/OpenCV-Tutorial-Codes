import cv2 as cv
img = cv.imread('Images/seun.jpg')
blur = cv.GaussianBlur(img, (5,5), cv.BORDER_DEFAULT)
cv.imshow("Original Image", img)
cv.imshow("Blur Image", blur)
cv.waitKey(0)
