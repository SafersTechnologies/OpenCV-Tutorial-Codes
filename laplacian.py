import cv2 as cv 
import numpy as np
img = cv.imread("Images/friends.jpg")
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
lap_edge = cv.Laplacian(gray_img, cv.CV_64F)
lap_edge = np.uint8(np.absolute(lap_edge))
cv.imshow("LAPLACIAN", lap_edge)
cv.waitKey(0)

