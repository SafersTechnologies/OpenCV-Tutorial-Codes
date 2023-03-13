import cv2 as cv
img = cv.imread('Images/seun.jpg')
edges = cv.Canny(img, 125,175)
Dilated = cv.dilate(edges, (3, 3), iterations = 3)
Eroded = cv.erode(Dilated, (3, 3), iterations = 3)
cv.imshow("Eroded Image", Eroded)
cv.imshow("Dilated Image", Dilated)
cv.waitKey(0)