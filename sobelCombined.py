import cv2 as cv 
import numpy as np
img = cv.imread("Images/friends.jpg")
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
sobel_x = cv.Sobel(gray_img, cv.CV_64F, 1, 0)
sobel_y = cv.Sobel(gray_img, cv.CV_64F, 0, 1)
sobelcombo = cv.bitwise_or(sobel_x, sobel_y)
cv.imshow("SOBEL COMBINED", sobelcombo)
cv.waitKey(0)