import cv2 as cv
import numpy as np
blank = np.zeros((500, 500, 3), dtype ='uint8')
pts = [ (350, 130), ( 250, 300), (160, 130)]
cv.fillPoly(blank, np.array([pts]),  (0, 225, 255))
cv.imshow("Yellow filled Triangle", blank)
cv.waitKey(0)