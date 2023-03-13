import cv2 as cv
img = cv.imread('Images/seun.jpg')
cropped_image= img [100:150, 0:350]
cv.imshow("Original Image", img)
cv.imshow("cropped image", cropped_image)
cv.waitKey(0)