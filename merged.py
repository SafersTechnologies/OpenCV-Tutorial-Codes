import cv2 as cv
img = cv.imread('Images/friends.jpg')
b, g, r = cv.split(img)
merged = cv.merge([b, g, r])
cv.imshow("MERGED IMAGE", merged)
cv.waitKey(0)