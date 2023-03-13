import cv2 as cv
img = cv.imread('Images/seun.jpg')
gray=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
retr, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print ("There are {} contours in this image".format(len(contours)))