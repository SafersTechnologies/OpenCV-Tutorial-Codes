import cv2 as cv
import numpy as np
blank = np.zeros((500, 400, 3), dtype ='uint8')
cv.rectangle(blank, (0,0), (200, 250), (0, 225, 255), thickness = cv.FILLED)
cv.imshow("Yellow Rectangle", blank)
cv.waitKey(0)