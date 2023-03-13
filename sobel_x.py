import cv2 as cv 
import numpy as np
img = cv.imread("Images/friends.jpg")
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
sobel_x_dir = cv.Sobel(gray_img, cv.CV_64F, 1, 0)
cv.imshow("SOBEL X DIRECTION", sobel_x_dir)
cv.waitKey(0)