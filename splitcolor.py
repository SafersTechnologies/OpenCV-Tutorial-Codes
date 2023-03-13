import cv2 as cv
img = cv.imread('Images/friends.jpg')
b, g, r = cv.split(img)
print("The shape of the original image is {}". format(img.shape))
print("The shape of the blue colour component is {}". format(b.shape))
print("The shape of the green colour is {}". format(img.shape))
print("The shape of the original image is {}". format(img.shape))

cv.waitKey(0)