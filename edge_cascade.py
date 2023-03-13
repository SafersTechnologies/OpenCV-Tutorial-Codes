import cv2 as cv
img = cv.imread('Images/seun.jpg')
edges = cv.Canny (img, 125, 175)
cv.imshow("Original Image", img)
cv.imshow("Edge Cascade", edges)
cv.waitKey(0)






