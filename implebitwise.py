import cv2 as cv
import numpy as np
blank = np.zeros((500, 500), dtype ="uint8")
rectangle = cv.rectangle(blank.copy(), (50,50), (350, 350), 255, -1)
circle = cv.circle(blank.copy(), (200, 200), 200, 255, -1)
cv.imshow("RECTANGLE", rectangle)
cv.imshow("CIRCLE", circle)
cv.waitKey(0)