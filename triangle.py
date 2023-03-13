import cv2 as cv
import numpy as np
blank = np.zeros((500, 500, 3), dtype ='uint8')
pts = [(200, 200), (300, 300), ( 250, 350) ]
cv.polylines(blank, np.array([pts]),  True, (0, 225, 255), 5)
cv.imshow("Yellow  Lined Triangle", blank)
cv.waitKey(0)
