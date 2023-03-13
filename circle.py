import cv2 as cv
import numpy as np
blank = np.zeros((500, 400, 3), dtype ='uint8')
cv.circle(blank, (200,250), 80, (0, 0, 255), thickness = cv.FILLED)
cv.imshow("Red Circle", blank)
cv.waitKey(0)