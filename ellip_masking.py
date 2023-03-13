import cv2 as cv
import numpy as np
img = cv.imread("Images/friends.jpg")
cv.imshow("Original Image", img)
blank = np.zeros(img.shape[:2], dtype = "uint8")
elliptical_mask = cv.ellipse(blank.copy(), (100, 100), (60, 120), 120, 0, 360, 255, -1)
cv.imshow("ELLIPTICAL MASK", elliptical_mask)
masked = cv.bitwise_and(img, img, mask=elliptical_mask)
cv.imshow("MASKED IMAGE", masked)
cv.waitKey(0)
