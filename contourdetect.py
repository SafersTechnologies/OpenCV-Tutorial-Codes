import cv2 as cv
img = cv.imread('Images/seun.jpg')
gray=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
canny = cv.Canny(gray, 125, 175)
contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print ("There are {} contours in this image".format(len(contours)))