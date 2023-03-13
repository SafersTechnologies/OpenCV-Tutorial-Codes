import cv2 as cv
import numpy as np
blank = np.zeros((500, 500, 3), dtype ='uint8')
cv.ellipse(blank, (200, 200), (160, 80), 0, 0, 360, (0, 255, 0), -1)
cv.imshow("Yellow filled Triangle", blank)
cv.waitKey(0)