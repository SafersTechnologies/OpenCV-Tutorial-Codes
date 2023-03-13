import cv2 as cv
img = cv.imread("Images/seun.jpg")
average = cv.blur(img, (3,3))
cv.imshow("ORIGINAL IMAGE", img)
cv.imshow("AVERAGE BLURRED IMAGE", average)
cv.waitKey(0)