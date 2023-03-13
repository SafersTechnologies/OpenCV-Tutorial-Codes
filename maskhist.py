import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
img = cv.imread("Images/friends.jpg")
blank = np.zeros(img.shape[:2], dtype = "uint8")
rectangular_mask = cv.rectangle(blank.copy(), (30, 30), (100, 200), 255, -1)
cv.imshow("RECTANGULAR MASK", rectangular_mask)
masked = cv.bitwise_and(img, img, mask=rectangular_mask)
colors= ('b', 'g', 'r')
plt.figure
plt.xlabel("bins")
plt.ylabel(" No of Pixels")
plt.title("Histogram of the colour format of the masked image")


for i, col in enumerate(colors):
    hist = cv.calcHist([img], [i], rectangular_mask, [256], [0, 255])
    plt.plot(hist, color=col) 
    plt.xlim([0, 255])
    
plt.show()
    
cv.waitKey(0)