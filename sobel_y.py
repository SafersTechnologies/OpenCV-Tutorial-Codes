import cv2 as cv 
import numpy as np
img = cv.imread("Images/friends.jpg")
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
sobel_y_dir = cv.Sobel(gray_img, cv.CV_64F, 0, 1)
cv.imshow("SOBEL Y DIRECTION", sobel_y_dir)
cv.waitKey(0)