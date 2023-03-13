import cv2 as cv
img = cv.imread('Images/seun.jpg')
blur = cv.GaussianBlur(img, (5,5), cv.BORDER_DEFAULT)
more_blur = cv.Canny(blur, 125, 175)
cv.imshow("Original Image", img)
cv.imshow("Blur Image", blur)
cv.imshow("more blur", more_blur)
cv.waitKey(0)