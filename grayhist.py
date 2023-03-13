import cv2 as cv
import matplotlib.pyplot as plt
img = cv.imread("Images/friends.jpg")
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
hist = cv.calcHist([gray_img], [0], None, [255], [0, 255]) 
plt.plot(hist)
plt.xlabel("bins")
plt.ylabel(" No of Pixels")
plt.title("Histogram of the grayscale format of friends.jpg")
plt.xlim([0, 255])
plt.show()
cv.waitKey(0)
