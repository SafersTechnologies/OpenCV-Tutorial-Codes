import cv2 as cv
img = cv.imread('Images/friends.jpg')
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
bgr = cv.cvtColor(rgb, cv.COLOR_RGB2BGR)
cv.imshow("RGB", rgb)
cv.imshow("BGR", img)
cv.waitKey(0)