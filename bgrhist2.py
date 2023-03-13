import cv2 as cv
import matplotlib.pyplot as plt
img = cv.imread("Images/friends.jpg")
colors= ('b', 'g', 'r')
plt.figure
plt.xlabel("bins")
plt.ylabel(" No of Pixels")
plt.title("Histogram of the colour format of friends.jpg")


for i, col in enumerate(colors):
    hist = cv.calcHist([img], [i], None, [256], [0, 255])
    plt.plot(hist, color=col) 
    plt.xlim([0, 255])
    
plt.show()
    
cv.waitKey(0)