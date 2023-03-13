import cv2 as cv
img = cv.imread('Images/seun.jpg')
cropped_image= img [50:100, 100:350]
cv.imshow("Original Image", img)
cv.imshow("cropped image", cropped_image)
cv.waitKey(0)