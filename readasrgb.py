import cv2 as cv
img = cv.imread('Images/friends.jpg')
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow("Original Image", img)
cv.imshow("RGB", rgb)
cv.waitKey(0)
