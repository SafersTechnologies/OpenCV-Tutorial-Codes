import cv2 as cv
img = cv.imread("Images/seun.jpg")
bilateral = cv.bilateralFilter(img, 5, 15, 20)
cv.imshow("Original Image", img)
cv.imshow("BILATERAL FILTERED IMAGE", bilateral)
cv.waitKey(0)

