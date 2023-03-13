import cv2 as cv
import numpy as np
blank = np.zeros((500, 400, 3), dtype ='uint8')
cv.circle(blank, (200,250), 120, (0, 0, 255), thickness = 2)
cv.imshow("Red Lined Circle", blank)
cv.waitKey(0)