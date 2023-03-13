import cv2 as cv
img = cv.imread(0)
flipped_image = cv.flip(img, -1)
cv.imshow("Original Image", img)
cv.imshow("Flipped Image", flipped_image)
cv.waitKey(0)