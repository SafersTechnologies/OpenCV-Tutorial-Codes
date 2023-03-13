import cv2 as cv
img = cv.imread("Images/friends.jpg")
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
adaptivegauss = cv.adaptiveThreshold(gray_img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 3)
cv.imshow("ADAPTIVE THRESHOLDED IMAGE", adaptivegauss)
cv.waitKey(0)