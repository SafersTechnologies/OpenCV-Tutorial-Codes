import cv2 as cv
import numpy as np
blank = np.zeros((500, 400, 3), dtype ='uint8')
blank[50:200,200:300] = 0, 0, 255
cv.imshow("Red", blank)
cv.waitKey(0)