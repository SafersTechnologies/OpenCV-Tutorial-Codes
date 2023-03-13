import cv2 as cv
img = cv.imread('Images/seun.jpg')
edges = cv.Canny(img, 125,175)
Dilated = cv.dilate(edges, (3, 3), iterations = 1)
cv.imshow("Original edges", edges)
cv.imshow("Dilated Image", Dilated)
cv.waitKey(0)
