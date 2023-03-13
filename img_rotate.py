import cv2 as cv
img = cv.imread("Images/seun.jpg")
rotated_image = cv.rotate(img, cv.ROTATE_180)
cv.imshow("Original Image", img)
cv.imshow("Rotated Image", rotated_image)
cv.waitKey(0)
