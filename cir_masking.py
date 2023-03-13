import cv2 as cv
import numpy as np
img = cv.imread("Images/friends.jpg")
cv.imshow("Original Image", img)
blank = np.zeros(img.shape[:2], dtype = "uint8")
circular_mask = cv.circle(blank.copy(), (img.shape[1]//2, img.shape[0]//2), 70, 255, -1)
cv.imshow("CIRCULAR MASK", circular_mask)
masked = cv.bitwise_and(img, img, mask=circular_mask)
cv.imshow("MASKED IMAGE", masked)
cv.waitKey(0)
