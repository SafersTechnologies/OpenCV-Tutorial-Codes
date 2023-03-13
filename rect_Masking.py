import cv2 as cv
import numpy as np
img = cv.imread("Images/friends.jpg")
cv.imshow("Original Image", img)
blank = np.zeros(img.shape[:2], dtype = "uint8")
rectangular_mask = cv.rectangle(blank.copy(), (30, 30), (100, 200), 255, -1)
cv.imshow("RECTANGULAR MASK", rectangular_mask)
masked = cv.bitwise_and(img, img, mask=rectangular_mask)
cv.imshow("MASKED IMAGE", masked)
cv.waitKey(0)
