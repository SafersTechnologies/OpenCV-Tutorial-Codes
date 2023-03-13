import cv2 as cv
import numpy as np
img= cv.imread("Images/friends.jpg")
cv.imshow("Original Image", img)
blank = np.zeros(img.shape[:2], dtype = "uint8")
elliptical_mask = cv.ellipse(blank.copy(), (60, 60), (60, 120), 120, 0, 360, 255, -1)
rectangular_mask = cv.rectangle(blank.copy(), (60, 60), (250, 250), 255, -1)
combined_mask = cv.bitwise_and(elliptical_mask, rectangular_mask)
cv.imshow("COMBINED MASK", combined_mask)
masked = cv.bitwise_and(img, img, mask=combined_mask)
cv.imshow("MASKED IMAGE", masked)
cv.waitKey(0)
