import cv2 as cv
import numpy as np
blank = np.zeros((400, 300), dtype ='uint8')
blank[:] = 0, 255, 0
cv.imshow("blank image", blank)
cv.waitKey(0)

